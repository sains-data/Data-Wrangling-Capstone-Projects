# Laporan tim — Kunci, kasus 20 Hutan, lahan, dan lingkungan

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai tabel statis tutupan hutan (luas dan persen), tiga seri BPS (penutupan lahan menurut kawasan,
lahan kritis, komponen IKLH), dan tiga seri WDI. Silver pertama berisi 4.045 baris dari 8
seri. Temuan terpenting adalah galat di sumber: kolom 2020 tabel tutupan hutan tergeser terhadap nama provinsi.

## Data dan lineage

13 berkas mentah: BPS snapshot 17 Oktober 2026 (3 JSON dinamis, 1 JSON tabel statis, 4 CSV, 1 catatan
unduhan), WDI (1 data + 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (8.113 baris
mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tabel statis HTML, dua satuan | header luas dan % | dua seri; uji silang CSV | 0 beda | K-002, K-006 |
| Kolom 2020 tergeser | 2020 menyimpang > 50%; kolom `cek` CSV | disimpan, peringatan, tidak dipakai di Gold | — | K-013 |
| Jumlah ≠ rincian | DIY 2016 di dua tabel | dilaporkan | 1 | K-012 |
| Kode SDG keliru | judul `var1304`, berkas `sdg15_iklh` | 15.1.1, 15 | 1.806 | K-007 |
| Tiga satuan luas | ribu ha, ha, km2 | disimpan apa adanya | — | K-008 |
| Kalimantan Utara digabung | keterangan tabel | `batas_lama` | 21 sel | K-001 |
| Jakarta tanpa lahan kritis | tidak ada di 4 review | `tidak_diterbitkan` | 4 sel | K-005 |
| Calon anomali | IQR | 194 outlier, 11 provinsi struktural | 313 | K-004 |

Tidak ada sel yang benar-benar missing (0). Galat input tidak ditemukan oleh aturan rentang; galat
kolom 2020 ditemukan oleh aturan konsistensi, bukan rentang.

## Integrasi dan rekonsiliasi

- P1 luas hutan BPS vs WDI: 10 tahun; konversi ribu ha → km2 di Gold.
- P2 persen hutan: penyebut berbeda.
- P3 indeks kualitas udara vs PM2.5: konteks, arah berlawanan.
- P4 dua tabel KLHK: 6 tahun; jumlah luas seharusnya sama.

## Validasi dan reproduksibilitas

12 aturan berjalan setiap `python pipeline.py` (9 lolos, 3
peringatan; `reports/validasi.md`). Aturan khas kasus: luas ≥ 0 dengan satu satuan per seri, komponen IKLH dari
kamus; peringatan untuk jumlah ≠ rincian, kolom 2020 tergeser, dan hutan + non hutan ≠ jumlah. Silver dimuat ke
DuckDB (4.045 baris). `python pipeline.py` berjalan ±2.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
