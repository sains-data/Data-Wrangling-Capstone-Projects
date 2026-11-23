# Laporan tim — Kunci, kasus 10 Kesetaraan gender

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
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

Panel Gold memuat 2 indikator provinsi (762 sel terisi, 74 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 33 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 3.0%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Perempuan manajer: BPS vs ILO seluruh manajemen (T552) | 2.3% | metode berbeda | metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen) |
| P2 | Perempuan manajer: BPS vs ILO senior dan menengah (0552) | 40.7% | definisi berbeda | definisi (0552 tanpa manajer junior) |
| P3 | Perkawinan anak: BPS vs WDI (UNICEF) | 29.2% | metode berbeda | tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017) |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: status ILO terdaftar, dua definisi ILO terpisah, 0552 tidak
melebihi T552; peringatan bila ILO jauh dari BPS. Silver dimuat ke DuckDB (840 baris).
`python pipeline.py` berjalan ±2.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (947 baris).
