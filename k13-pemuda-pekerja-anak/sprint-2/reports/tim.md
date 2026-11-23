# Laporan tim — Kunci, kasus 13 Pemuda dan pekerja anak

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai dua seri provinsi BPS (NEET 15–24, pekerja anak 5–17), dua seri WDI, dan tiga seri ILOSTAT.
Silver pertama berisi 720 baris dari 7 seri. Kesulitannya kelompok umur: NEET sama di semua
sumber, tetapi pekerja anak berbeda (BPS 5–17, ILO 15–17, WDI 7–14), dan seri pekerja anak sangat pendek.

## Data dan lineage

16 berkas mentah: BPS (2 JSON, 2 CSV, 1 catatan unduhan), WDI (1 data + 3 metadata), ILOSTAT (3 CSV
SDMX, 3 DSD, 1 daftar dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()` (1.426 baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Kelompok umur pekerja anak | judul, kolom AGE, name WDI | dicatat per seri; P2 definisi | — | K-003 |
| Dua definisi ILO 8.7.1 | DSD A871, B871 | dua seri; B871 ≥ A871 | 0 | K-006 |
| WDI tidak tumpang tindih | 2000–2010 vs 2020–2025 | konteks, bukan missing | 0 | K-011 |
| Provinsi hilang 2024–2025 | tanpa catatan | `missing` | 6 sel | K-013 |
| Status ILO B | `OBS_STATUS` | `status_obs` | 9 | K-005 |
| Pemekaran wilayah | Papua 2024 | `belum_ada` 44, `batas_lama` 8, `patahan_wilayah` 4 | sel | K-001, K-009 |
| Calon anomali | IQR | 55 outlier | 72 | K-004 |

Tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 2 indikator provinsi (588 sel terisi, 58 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 31 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 3.2%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | NEET 15–24: BPS vs ILO vs WDI | 3.2% | metode berbeda | metode (olahan Sakernas yang sama); kelompok umur sama (15–24) |
| P2 | Pekerja anak: BPS (5–17) vs ILO kegiatan ekonomi (15–17) | 2.4% | cakupan berbeda | definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023 |
| P3 | Anak bekerja 7–14 (WDI): konteks | — | cakupan berbeda | kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025) |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: umur ILO dari kamus, B871 ≥ A871, status ILO terdaftar;
peringatan bila NEET BPS jauh dari ILO. Silver dimuat ke DuckDB (720 baris). `python pipeline.py`
berjalan ±3.1 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (752 baris).
