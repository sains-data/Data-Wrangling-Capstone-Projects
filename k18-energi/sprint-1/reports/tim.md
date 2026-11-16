# Laporan tim — Kunci, kasus 18 Energi: listrik dan bahan bakar memasak

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai seri BPS listrik PLN (1993–2025) dan tabel statis bahan bakar memasak (2001, 2007–2021), ditambah
dua seri WDI. Silver pertama berisi 4.889 baris dari 4 seri. Pekerjaan utamanya membaca
tabel statis HTML (dengan dua pemisah desimal), menetapkan kategori bahan bakar bersih, dan menangani catatan
pencacahan Susenas tahun 2000–2002.

## Data dan lineage

9 berkas mentah: BPS snapshot 17 Oktober 2026 (1 JSON dinamis, 1 JSON tabel statis, 2 CSV, 1
catatan unduhan), WDI (1 data + 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (10.041
baris mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tabel statis HTML | JSON `data.table` | dibaca dari HTML, uji silang CSV | 0 beda | K-002 |
| Koma desimal campuran | `77,94` vs `74.41` | koma tanpa titik = desimal | 385 sel | K-003 |
| Tanda catatan kaki di header | `Gas/Elpiji 1`, `Lainnya 2` | dibuang saat dikodekan | — | K-006 |
| Jumlah 100,01 | pembulatan | batas atas 100,05 | — | K-009 |
| Provinsi tidak dicacah | `var.def` | `tidak_diterbitkan` | 7 sel | K-005 |
| Hanya ibu kota 2002 | `var.def` | `cakupan_parsial` | 3 calon | K-012 |
| Sel "-" | tabel bahan bakar | tidak diisi nol; `missing` | 7 sel | K-013 |
| Gas/elpiji melonjak 2007–2008 | > 70% provinsi naik | `patahan_seri` | 7 calon | K-014 |
| Pemekaran wilayah | sejak 1999 | `belum_ada` 421, `batas_lama` 15, `patahan_wilayah` 22 | sel | K-001, K-011 |
| Calon anomali | IQR | 307 outlier | 337 | K-004 |

Tidak ada galat input (0).

## Integrasi dan rekonsiliasi

- P1 listrik PLN vs akses listrik WDI: 31 tahun; PLN saja dan rumah tangga vs semua sumber dan penduduk.
- P2 bahan bakar bersih vs WDI: 16 tahun; kategori bersih dijumlahkan di Gold.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: jumlah jenis bahan bakar 99–101%, setiap jenis punya satu
kategori, baris jumlah = 100; peringatan bila PLN melebihi akses listrik WDI. Silver dimuat ke DuckDB
(4.889 baris). `python pipeline.py` berjalan ±2.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
