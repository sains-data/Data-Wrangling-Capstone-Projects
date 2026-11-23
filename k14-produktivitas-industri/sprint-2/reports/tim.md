# Laporan tim — Kunci, kasus 14 Produktivitas dan industri

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
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

Panel Gold memuat 4 indikator provinsi (1.575 sel terisi, 173 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 67 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 9.5%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Laju produktivitas: BPS vs ILO (dua basis harga) | 36.3% | metode berbeda | metode (PDB riil BPS vs estimasi model ILO); proyeksi ILO dikeluarkan |
| P2 | Laju produktivitas BPS vs WDI tingkat PDB per pekerja | 36.5% | metode berbeda | WDI tingkat (USD PPP 2021), bukan laju; laju WDI dihitung di Gold sebelum dibandingkan |
| P3 | Nilai tambah manufaktur terhadap PDB: BPS vs WDI | 4.0% | metode berbeda | dasar harga belum diketahui di kedua sumber; dicek di Sprint 2 |
| P4 | Tenaga kerja manufaktur: BPS vs ILO | 1.7% | metode berbeda | metode (olahan Sakernas yang sama) |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P2: laju tahunan WDI dihitung di Gold dari tingkat output per pekerja ((t/t-1 - 1) x 100) sebelum dibandingkan dengan laju BPS.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (21 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: satu satuan per seri dan rincian, tahun depan terdaftar
proyeksi, satu snapshot per seri; peringatan bila median laju provinsi jauh dari Indonesia. Silver dimuat ke DuckDB
(1.779 baris). `python pipeline.py` berjalan ±3.7 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (2.019 baris).
