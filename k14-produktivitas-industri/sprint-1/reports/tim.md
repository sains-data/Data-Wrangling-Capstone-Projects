# Laporan tim — Kunci, kasus 14 Produktivitas dan industri

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai empat seri provinsi BPS (laju produktivitas, nilai tambah pertanian per tenaga kerja, porsi nilai
tambah manufaktur, porsi tenaga kerja manufaktur), dua seri WDI, dan tiga seri ILOSTAT. Silver pertama berisi
1.779 baris dari 9 seri. Pekerjaan utamanya menangani kunci JSON yang rusak, satuan laju yang
bisa negatif, tahun proyeksi ILO, dan perbedaan tingkat vs laju.

## Data dan lineage

24 berkas mentah: BPS snapshot 17 dan 20 Oktober 2026 (`var2755` di keduanya), WDI (3 data + 3
metadata), ILOSTAT (3 CSV SDMX, 3 DSD, 1 daftar dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()`
(4.030 baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Kunci JSON rusak | 2 kunci 10 karakter, wilayah tidak dikenal | dilaporkan, tidak masuk Silver | 2 | K-003 |
| Laju bisa negatif | judul "Laju Pertumbuhan" | `persen_per_tahun` (-100..100) | 1.018 | K-007 |
| Dua basis ILO sama | 0821 = B821 | dua seri, dicatat | 0 | K-006 |
| Proyeksi ILO | 2026–2027 | `PROYEKSI` | 4 | K-010 |
| Provinsi baru 2024 | `var.note` | `batas_lama` | 19 sel | K-005 |
| Snapshot ganda | `var2755` | terbaru; 0 beda | 1 seri | K-004 |
| Kode SDG butir | nama berkas `sdg2_2_3_1_a` | 2.3.1(a) | 315 | K-008 |
| Calon anomali | IQR | 165 outlier, 8 provinsi struktural | 240 | K-011 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

- P1 laju produktivitas BPS vs ILO: 15 tahun (proyeksi dikeluarkan).
- P2 laju BPS vs tingkat WDI: laju WDI dihitung di Gold.
- P3 porsi manufaktur BPS vs WDI: 14 tahun; dasar harga belum diketahui.
- P4 tenaga kerja manufaktur BPS vs ILO: 6 tahun.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: satu satuan per seri dan rincian, tahun depan terdaftar
proyeksi, satu snapshot per seri; peringatan bila median laju provinsi jauh dari Indonesia. Silver dimuat ke DuckDB
(1.779 baris). `python pipeline.py` berjalan ±2.4 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
