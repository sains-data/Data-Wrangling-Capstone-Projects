# Laporan tim — Kunci, kasus 07 Partisipasi dan lama sekolah

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai lima seri provinsi BPS (APK per jenjang, APK perguruan tinggi, partisipasi pendidikan dan
pelatihan, harapan lama sekolah, rata-rata lama sekolah) dan satu seri WDI. Silver pertama berisi 4.216
baris dari 6 seri. Masalah utamanya identitas seri (dua seri APK berkode sama), satuan APK yang bisa
melebihi 100, dan berkas HLS yang memuat kabupaten/kota.

## Data dan lineage

15 berkas mentah: BPS snapshot 17 Oktober 2026 (5 JSON berhalaman, 5 CSV, 1 catatan unduhan), WDI
snapshot 20 Oktober 2026 (1 data + 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()`
(24.726 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Dua APK berkode 4.3.1 | `turvar` var303: SD, SMP, SM | var303 → 4.1 | 2.376 | K-003 |
| APK > 100, satuan kosong | judul APK; nilai sampai > 120 | `persen_apk` (0–250) | 3.162 | K-007 |
| Kabupaten/kota di HLS | kode tidak berakhiran 00 | dikeluarkan | 8.167 | K-005 |
| Kelompok umur tumpang tindih | var2685: 15–64 mencakup yang lain | tanpa total buatan | 8 nilai rincian | K-006 |
| APK berganti definisi 2007 | `var.note` | `PATAHAN_DEFINISI` | — | K-012 |
| Aceh 2005 tidak ada | tanpa catatan | `missing`, tidak diisi | 3 sel | K-013 |
| Pemekaran wilayah | sejak 2003 | `belum_ada` 402, `batas_lama` 49, `patahan_wilayah` 27 | sel | K-001, K-011 |
| Calon anomali | IQR | 262 outlier, 4 provinsi struktural | 367 | K-004 |

Tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 7 indikator provinsi (3.726 sel terisi, 454 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 27 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 19.7%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | APK perguruan tinggi: BPS (umur 19–23) vs WDI (umur resmi jenjang tersier) | 19.7% | definisi berbeda | definisi (kelompok umur acuan penyebut) dan metode (Susenas vs data administrasi UNESCO) |
| P2 | Lama sekolah (HLS, RLS): tanpa pembanding di paket | — | definisi berbeda | dua ukuran berbeda (harapan anak 7 tahun vs rata-rata penduduk 15+); variabel penjelas panel |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

22 aturan berjalan setiap `python pipeline.py` (22 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: HLS dan RLS dalam rentang tahun masuk akal, var303 tanpa
jenjang PT, var2685 tanpa total, tidak ada kabupaten/kota; peringatan bila RLS melebihi HLS. Setiap aturan diuji
dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB (4.216 baris). `python pipeline.py`
berjalan ±4.7 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (4.298 baris).
