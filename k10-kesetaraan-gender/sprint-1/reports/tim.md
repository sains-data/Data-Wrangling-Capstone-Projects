# Laporan tim — Kunci, kasus 10 Kesetaraan gender

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai dua seri provinsi BPS (perkawinan anak, perempuan di posisi manajerial), dua seri WDI, dan dua seri
ILOSTAT. Silver pertama berisi 840 baris dari 6 seri. Pekerjaan utamanya membaca format
SDMX ILOSTAT, membedakan dua definisi manajerial ILO, dan menyimpan status pengamatan sebagai penanda patahan.

## Data dan lineage

15 berkas mentah: BPS (2 JSON, 2 CSV, 1 catatan unduhan), WDI (2 data + 3 metadata), ILOSTAT (2 CSV
SDMX, 2 DSD, 1 daftar dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()` (1.720 baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Dua definisi ILO 5.5.2 | deskripsi DSD | dua seri; T552 pembanding utama | — | K-003, K-011 |
| Status pengamatan ILO | `OBS_STATUS` B + `NOTE_INDICATOR` | kolom `status_obs` | 4 baris B | K-005 |
| ILO T552 2016 janggal | 44,78 vs ±22–27 | peringatan, tidak direkonsiliasi | 1 | K-012 |
| Satuan `var2003` kosong | judul, ILO PT | persen | 391 | K-007 |
| Provinsi baru hilang 2025 | Papua Tengah, Pegunungan | `missing` | 2 sel | K-013 |
| Pemekaran wilayah | Papua 2024 | `belum_ada` 64, `batas_lama` 8, `patahan_wilayah` 4 | sel | K-001, K-010 |
| Calon anomali | IQR | 47 outlier | 49 | K-004 |

Tidak ada galat input (0).

## Integrasi dan rekonsiliasi

- P1 perempuan manajer BPS vs ILO T552: 8 tahun; definisi sama, angka berdekatan kecuali ILO 2016.
- P2 BPS vs ILO 0552: 1 tahun; definisi berbeda.
- P3 perkawinan anak BPS vs WDI: 1 tahun.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: status ILO terdaftar, dua definisi ILO terpisah, 0552 tidak
melebihi T552; peringatan bila ILO jauh dari BPS. Silver dimuat ke DuckDB (840 baris).
`python pipeline.py` berjalan ±1.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
