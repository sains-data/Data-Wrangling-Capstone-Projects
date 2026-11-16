# Laporan tim — Kunci, kasus 19 Hunian dan transportasi

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai lima seri provinsi BPS (hunian layak, akses transportasi umum, pengguna kendaraan umum, bongkar
muat kapal, bongkar muat pesawat) dan satu seri WDI. Silver pertama berisi 1.305 baris dari
6 seri. Temuan terpenting adalah patahan definisi hunian layak 2019, yang terlihat seperti
penurunan besar di hampir semua provinsi.

## Data dan lineage

22 berkas mentah: BPS snapshot 17 dan 20 Oktober 2026 (tiga seri ada di keduanya), WDI (1 data + 3
metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (4.958 baris mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Hunian layak turun serentak 2019 | `var.note`; 97% provinsi turun > 20% | patahan definisi, nilai tidak diubah | 3 calon | K-012 |
| Moda tidak ada di katalog | judul JSON | kapal / pesawat; rincian bongkar/muat | 3 nilai rincian | K-003 |
| Kapal tidak mencakup semua provinsi | DIY, Papua Pegunungan | `tidak_diterbitkan` | 16 sel | K-005 |
| Tiga seri di dua snapshot | 17 dan 20 Oktober | snapshot terbaru; 0 beda | 3 seri | K-004 |
| Satuan dan kode SDG | judul, nama berkas | persen; butir (a)/(b) | 533 | K-007, K-008 |
| Pemekaran wilayah | Papua 2024 | `belum_ada` 52, `batas_lama` 4, `patahan_wilayah` 2 | sel | K-001, K-011 |
| Calon anomali | IQR | 103 outlier, 12 provinsi struktural | 202 | K-006 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0). Jumlah provinsi
bongkar muat sama dengan baris Indonesia (selisih ≤ 1%).

## Integrasi dan rekonsiliasi

- P1 hunian layak vs penduduk kumuh perkotaan: konteks, arah perubahan.
- P2 bongkar muat kapal vs pesawat: konteks; rekonsiliasi internal jumlah provinsi vs Indonesia.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: bongkar muat ≥ 0 dan berkilogram, rincian hanya bongkar/muat,
satu snapshot per seri; peringatan bila jumlah provinsi berbeda dari Indonesia. Silver dimuat ke DuckDB
(1.305 baris). `python pipeline.py` berjalan ±2.5 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
