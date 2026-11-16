# Laporan tim — Kunci, kasus 04 Penyakit dan faktor risiko

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini menyatukan tiga seri provinsi BPS (kejadian malaria, prevalensi hipertensi, merokok) dengan satu seri
WDI dan tiga seri WHO. Silver pertama berisi 1.058 baris dari 7 seri. Ketiga seri BPS
berbeda bentuk: malaria tahunan dari laporan Kemenkes, hipertensi dari empat putaran survei yang berganti sumber,
merokok tahunan dari Susenas. Masalah utamanya penyebut yang berbeda (malaria), kode SDG yang ternyata butir
nasional (hipertensi), dan tahun proyeksi di seri WHO.

## Data dan lineage

16 berkas mentah dari snapshot 20 Oktober 2026: BPS (3 CSV, 3 JSON berhalaman, 1 catatan unduhan),
WDI (1 berkas data, 3 metadata), WHO GHO (3 CSV, 2 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()`
(2.012 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Satuan malaria dan hipertensi kosong | `var.label` ("Per 1000 Orang", "Prevalensi") | `per_1000_penduduk`, `persen` | 520 | K-007, K-008 |
| Penyebut malaria berbeda | WHO Denominator: penduduk di daerah penularan | satuan dibedakan; P1 selisih definisi | 12 tahun | K-007, K-014 |
| Hipertensi bukan indikator global 3.4.1 | nama tabel `sdg3_3_4_1_b` | 3.4.1(b) | 104 | K-008 |
| Hipertensi 2016 hanya Indonesia | JSON 2016: 0 dari 34 provinsi | `tidak_diterbitkan` | 34 sel | K-005 |
| Tahun proyeksi WHO | 2025, 2030 | terdaftar `PROYEKSI`, tidak ikut rekonsiliasi | 6 | K-010 |
| Beban malaria tinggi di timur | IQR antarprovinsi berulang | perbedaan struktural, tidak di-*winsorize* | 4 provinsi | K-004 |
| Malaria turun serentak 2013→2014 | > 70% provinsi turun > 20% | `patahan_seri`, nilai tidak diubah | 2 | K-012 |
| Wilayah induk mengecil | Kalimantan Timur, Papua, Papua Barat | `patahan_wilayah` | 4 | K-013 |
| Provinsi belum dibentuk / belum dipecah | Kalimantan Utara, provinsi Papua baru | `belum_ada` 100, `batas_lama` 6 | sel | K-001 |
| Calon anomali lain | IQR ke bawah, perubahan, ke samping | 105 outlier ditandai | 154 | K-004 |
| BPS dua format, JSON berhalaman | nilai CSV = JSON; 2–4 halaman per seri | JSON, semua halaman | 913 | K-002 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0). Lonjakan
lebih dari sepuluh kali lipat di provinsi Jawa dan Bali 2010–2012 terjadi pada angka yang sangat kecil dan
dilaporkan sebagai peringatan, bukan diperbaiki.

## Integrasi dan rekonsiliasi

Disiapkan di Sprint 1, dihitung di Sprint 2 (`reports/pasangan-rekonsiliasi.md`):

- P1 malaria BPS vs WHO dan WDI: 12 tahun; penyebut dan metode berbeda.
- P2 merokok BPS vs WHO tembakau: 4 tahun estimasi (proyeksi dikeluarkan); definisi berbeda.
- P3 hipertensi vs kematian PTM: konteks.
- P4 malaria WHO vs WDI: 24 tahun; vintage.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: tidak ada tahun BPS di luar tahun terbit, setiap tahun
sesudah 2026 terdaftar sebagai proyeksi, satuan malaria BPS dan WHO/WDI tetap dibedakan; satu peringatan untuk
lonjakan malaria lebih dari sepuluh kali lipat. Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`).
Silver dimuat ke DuckDB dengan kunci primer dan CHECK (1.058 baris). `python pipeline.py` berjalan
±2.1 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
