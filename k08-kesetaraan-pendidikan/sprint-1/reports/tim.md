# Laporan tim — Kunci, kasus 08 Kesetaraan pendidikan

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai lima seri provinsi BPS (APM per jenjang, dua rasio paritas APK, tingkat penyelesaian per
jenjang, APS per kelompok umur) dan dua seri WDI. Silver pertama berisi 5.418 baris dari 7
seri. Masalah utamanya identitas seri yang hanya terbaca dari judul, satuan yang kosong di katalog, dan rasio BPS
yang ditulis dikali 100.

## Data dan lineage

15 berkas mentah: BPS snapshot 17 Oktober 2026 (5 JSON berhalaman, 5 CSV, 1 catatan unduhan), WDI
snapshot 20 Oktober 2026 (1 data + 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()`
(10.790 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tiga seri berkode 4.5.1 | judul JSON | var2595 kuintil, var2600 jenis kelamin, var304 → 4.1 | 2.376 | K-003 |
| Satuan kosong | judul, besaran nilai | `persen`, `rasio_x100` | 5.329 | K-007 |
| Rasio BPS x100 | nilai 32–260 vs GPI 0,77–1,02 | `rasio_x100`, diseragamkan di Gold | — | K-007 |
| Catatan APS salah tempel | `var.note`: definisi disabilitas | tidak dipakai | 0 | K-009 |
| APM berganti definisi 2007 | `var.note` | `PATAHAN_DEFINISI` | — | K-012 |
| Aceh 2005 tidak ada | tanpa catatan | `missing`, tidak diisi | 3 sel | K-005 |
| Pemekaran wilayah | sejak 2003 | `belum_ada` 527, `batas_lama` 69, `patahan_wilayah` 30 | sel | K-001, K-011 |
| Calon anomali | IQR | 342 outlier, 8 provinsi struktural | 551 | K-004 |

Tidak ada galat input (0). Penyelesaian SMA tidak pernah melebihi SD.

## Integrasi dan rekonsiliasi

- P1 penyelesaian SD BPS vs WDI: 9 tahun; definisi berbeda (kohort umur vs rasio masuk kasar).
- P2 paritas jenis kelamin BPS (PT) vs WDI (SD + menengah): konteks; tanpa tahun bersama.
- P3 paritas kuintil APK SMA: tanpa pembanding di paket.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: rasio paritas masuk akal setelah skala disamakan, satuan
per jenis ukuran, tanpa total buatan; peringatan bila penyelesaian SMA melebihi SD. Setiap aturan diuji dengan
baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB (5.418 baris). `python pipeline.py`
berjalan ±4.0 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
