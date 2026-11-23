# Laporan tim — Kunci, kasus 16 Ketimpangan dan layanan dasar

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
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

Panel Gold memuat 5 indikator provinsi (777 sel terisi, 97 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 37 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 23.4%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Di bawah 50% median: BPS vs WDI | 23.4% | definisi berbeda | definisi dan metode: BPS menyebut pendapatan; WDI pendapatan atau konsumsi per kapita dengan median PPP |
| P2 | Kemiskinan pekerja (ILO) vs kemiskinan ekstrem penduduk (WDI) | 4.8% | cakupan berbeda | populasi berbeda (pekerja vs seluruh penduduk); garis kemiskinan sama (US$3 PPP 2021) |
| P3 | Layanan dasar, pendapatan pemerintah (BPS) dan perlindungan sosial, porsi upah (ILO): konteks | — | tanpa pasangan | tidak ada padanan langsung di paket |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (21 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: tanpa imputasi, layanan dari kamus, status dan proyeksi ILO
terdaftar; peringatan bila BPS jauh dari WDI. Kelengkapan panel per seri di `reports/kelengkapan-panel.md`. Silver
dimuat ke DuckDB (1.137 baris). `python pipeline.py` berjalan ±3.4 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (1.041 baris).
