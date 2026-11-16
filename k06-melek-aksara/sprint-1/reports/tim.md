# Laporan tim — Kunci, kasus 06 Melek aksara

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai dua tabel BPS untuk angka melek aksara penduduk 15 tahun ke atas: tabel dinamis ringkas
(`var1458`, 2014–2025) dan tabel statis rinci menurut daerah dan jenis kelamin (2009–2025), ditambah satu seri WDI.
Silver pertama berisi 5.762 baris dari 3 seri. Pekerjaan utamanya membaca tabel statis
berbentuk HTML dan memutuskan angka total mana yang kanonik.

## Data dan lineage

9 berkas mentah: BPS snapshot 17 Oktober 2026 (1 JSON dinamis, 1 JSON tabel statis, 2 CSV,
1 catatan unduhan), WDI snapshot 20 Oktober 2026 (1 data + 3 metadata). Semua berkas tertangani oleh
`ekstraksi.jalankan()` (12.860 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw`
dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tabel statis berupa HTML | JSON `data.table`: tabel Excel di-*escape*, 3 blok | dibaca dari HTML, diuji silang dengan CSV | 0 beda | K-002 |
| Nama wilayah tanpa kode | `KEP. RIAU`, `Kepulauan Bangka Belitung` | kamus nama → kode | — | K-001 |
| Sel kosong tabel rinci | nilai kosong | tidak masuk Silver | 645 | K-003 |
| Dua angka total | tabel ringkas vs rinci | `var1458` kanonik | — | K-005 |
| Total berbeda 2017 | semua provinsi, sampai 0,21 poin | dilaporkan, tidak disamakan | 12 tahun dibandingkan | K-006 |
| Jakarta tanpa perdesaan | 6 rincian | aturan konsistensi per provinsi | 0 | K-007 |
| WDI = BPS, derau float32 | 95.120002746582 | disimpan apa adanya | 5 tahun | K-010, K-012 |
| Pemekaran wilayah | Kalimantan Utara, Papua 2024 | `belum_ada` 96, `batas_lama` 11, `patahan_wilayah` 6 | sel | K-001, K-011 |
| Calon anomali | IQR | 88 outlier, 4 provinsi struktural | 133 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

- P1 total rinci vs `var1458`: 12 tahun; beda hanya 2017.
- P2 `var1458` vs WDI: 5 tahun; WDI meneruskan angka Susenas.
- P3 tabel rinci vs WDI: 8 tahun (mulai 2009).

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: satu total kanonik per provinsi × tahun, susunan rincian
konsisten, total di antara perkotaan dan perdesaan; peringatan untuk selisih total rinci dan ringkas. Setiap aturan
diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB (5.762 baris).
`python pipeline.py` berjalan ±2.4 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
