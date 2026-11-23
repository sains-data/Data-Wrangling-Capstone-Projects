# Laporan tim — Kunci, kasus 04 Penyakit dan faktor risiko

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
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

Panel Gold memuat 3 indikator provinsi (886 sel terisi, 140 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 71 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 71.5%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Malaria: kasus dilaporkan per 1.000 penduduk (BPS) vs estimasi per 1.000 penduduk berisiko (WHO, WDI) | 75.8% | definisi berbeda | definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi) |
| P2 | Merokok (BPS, kasar, rokok) vs penggunaan tembakau (WHO, distandarkan umur) | 23.8% | definisi berbeda | definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan |
| P3 | Hipertensi (BPS) vs kematian PTM 30–70 (WHO): konteks | — | definisi berbeda | definisi berbeda: prevalensi faktor risiko vs probabilitas kematian |
| P4 | Malaria WHO vs WDI (estimasi yang sama, rilis berbeda) | 0.1% | vintage berbeda | vintage |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P1: selisih tetap dihitung walau penyebut berbeda (seluruh penduduk vs penduduk di daerah penularan); kategori definisi berbeda.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: tidak ada tahun BPS di luar tahun terbit, setiap tahun
sesudah 2026 terdaftar sebagai proyeksi, satuan malaria BPS dan WHO/WDI tetap dibedakan; satu peringatan untuk
lonjakan malaria lebih dari sepuluh kali lipat. Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`).
Silver dimuat ke DuckDB dengan kunci primer dan CHECK (1.058 baris). `python pipeline.py` berjalan
±3.1 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (1.205 baris).
