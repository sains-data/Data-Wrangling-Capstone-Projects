# Laporan tim — Kunci, kasus 16 Ketimpangan dan layanan dasar

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai tiga seri provinsi BPS (di bawah 50% median pendapatan, akses layanan dasar, pendapatan pemerintah),
dua seri WDI, dan tiga seri ILOSTAT. Silver pertama berisi 1.137 baris dari 8 seri. Panelnya
pendek dan berlubang: provinsi ditekan karena RSE, satu layanan tanpa angka, dan pendapatan pemerintah hanya dua tahun.

## Data dan lineage

18 berkas mentah: BPS (3 JSON, 3 CSV, 1 catatan unduhan), WDI (1 data + 3 metadata), ILOSTAT (3 CSV
SDMX, 3 DSD, 1 daftar dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()` (2.003 baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Provinsi ditekan (RSE) | `var.note` var2011 | `tidak_diterbitkan` | 9 sel | K-005 |
| Layanan mobilitas kosong | label di turvar tanpa angka | tiga layanan saja | 0 | K-006 |
| Dua tahun saja | var1254 2015–2016 | tanpa imputasi | 0 | K-012 |
| Status ILO A/R/M | `OBS_STATUS` | disimpan, arti ditanyakan | — | K-007 |
| Proyeksi ILO | 2026 | `PROYEKSI` | 1 | K-010 |
| Satuan kosong | judul | persen | 275 | K-004 |
| Pemekaran wilayah | Papua 2024 | `belum_ada` 76, `batas_lama` 12, `patahan_wilayah` 0 | sel | K-001, K-011 |
| Calon anomali | IQR | 37 outlier | 58 | K-003 |

Tidak ada sel yang benar-benar missing di deret yang diprofilkan (0) dan tidak ada galat input
(0).

## Integrasi dan rekonsiliasi

- P1 di bawah 50% median BPS vs WDI: 6 tahun; pendapatan vs pendapatan atau konsumsi.
- P2 kemiskinan pekerja (ILO) vs penduduk (WDI): 26 tahun; populasi berbeda.
- P3 layanan dasar, pendapatan pemerintah, perlindungan sosial, porsi upah: konteks.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: tanpa imputasi, layanan dari kamus, status dan proyeksi ILO
terdaftar; peringatan bila BPS jauh dari WDI. Kelengkapan panel per seri di `reports/kelengkapan-panel.md`. Silver
dimuat ke DuckDB (1.137 baris). `python pipeline.py` berjalan ±2.2 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
