# Laporan tim — Kunci, kasus 21 Keamanan dan pencatatan sipil

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai enam seri provinsi BPS (korban kejahatan kekerasan, rasa aman, hukuman fisik pada anak, pelaporan
ke polisi, akta kelahiran balita, akta kelahiran anak 0–17) dan dua seri WDI. Silver pertama berisi
1.370 baris dari 8 seri. Tantangannya ketersediaan: seri berbeda tahun dan jumlah
provinsinya, empat seri ada di dua snapshot, dan dua seri kehilangan banyak provinsi sejak 2020 tanpa catatan.

## Data dan lineage

26 berkas mentah: BPS snapshot 17 dan 20 Oktober 2026 (empat seri ada di keduanya), WDI (1 data + 3
metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (4.108 baris mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Empat seri di dua snapshot | 17 dan 20 Oktober | snapshot terbaru; 0 beda | 4 seri | K-003 |
| Provinsi hilang sejak 2020 | var1311, var2740 | `missing`, tidak diisi | 116 sel | K-005 |
| Periode = tahun kejadian | `var.note` var1311 | disimpan apa adanya; 2017 pergantian | — | K-012 |
| Dua seri akta | balita vs 0–17 | terpisah | 0 | K-006 |
| Kode SDG butir nasional | judul, nama berkas | (a), (b) | 820 | K-007 |
| Lompatan serentak | korban 2020–2024, rasa aman 2014–2025 | `patahan_seri` | 19 calon | K-004 |
| Pemekaran wilayah | Kalimantan Utara, Papua 2024 | `belum_ada` 116, `batas_lama` 11, `patahan_wilayah` 11 | sel | K-001, K-011 |
| Calon anomali | IQR | 38 outlier, 7 provinsi struktural | 115 | K-004 |

Tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 6 indikator provinsi (1.315 sel terisi, 243 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 32 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 0.1%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Akta kelahiran balita: BPS vs WDI (UNICEF) | 0.1% | metode berbeda | metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun) |
| P2 | Korban kekerasan (BPS) vs pembunuhan per 100.000 (WDI): konteks | — | definisi berbeda | definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi) |
| P3 | Akta kelahiran balita vs anak 0–17 (BPS dengan BPS) | — | cakupan berbeda | kelompok umur berbeda; tetap dua seri |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (21 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: satu nilai per kunci, satu snapshot per seri, dua seri akta
tidak tertukar; peringatan bila akta 0–17 lebih rendah dari balita. Silver dimuat ke DuckDB (1.370 baris).
`python pipeline.py` berjalan ±3.4 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (1.645 baris).
