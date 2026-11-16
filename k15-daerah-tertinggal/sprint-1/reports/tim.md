# Laporan tim — Kunci, kasus 15 Kemiskinan dan daerah tertinggal

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai tiga seri provinsi BPS (persentase penduduk miskin menurut daerah dan semester, jumlah desa
mandiri, jumlah desa tertinggal) dan satu seri WDI. Silver pertama berisi 3.897 baris dari
4 seri. Pekerjaan utamanya memetakan periode semester, menemukan semester mana yang dipakai WDI, dan
membaca catatan Indeks Desa yang berganti sumber setiap tahun.

## Data dan lineage

11 berkas mentah: BPS snapshot 20 Oktober 2026 (3 JSON, 3 CSV, 1 catatan unduhan), WDI (1 data + 3
metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (7.804 baris mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Periode campuran tahun dan semester | `turtahun`: Tahunan, Semester 1 (Maret), Semester 2 (September) | `AAAA`, `AAAA-S1`, `AAAA-S2` | 3.869 | K-006 |
| September 2023 tidak terbit | 2023 hanya Maret | tidak diisi | 0 | K-008 |
| Kode SDG | P0 garis nasional; nama berkas c/d/f | 1.2.1, 10.1.1(c), 10.1.1(d) | 3.869 | K-007 |
| Jakarta tanpa desa | tidak ada di 3 tahun | `tidak_diterbitkan` | 6 sel | K-005 |
| Indeks Desa berganti sumber | `var.note` | patahan seri | 23 calon | K-012 |
| Pemekaran wilayah | catatan var192 | `belum_ada` 139, `batas_lama` 8, `patahan_wilayah` 3 | sel | K-001, K-010 |
| Calon anomali | IQR | 150 outlier, 12 provinsi struktural | 227 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0). P0 perkotaan
melebihi perdesaan di beberapa sel (peringatan), dibiarkan sebagai temuan.

## Integrasi dan rekonsiliasi

- P1 P0 Indonesia BPS Maret vs WDI: 19 tahun; WDI = P0 Maret dibulatkan.
- P2 desa tertinggal dan mandiri: konteks; agregat nasional dijumlahkan dari provinsi di Gold.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: jumlah desa sama dengan rinciannya, jumlah desa bilangan
bulat, jenis periode cocok dengan bentuk periode; peringatan untuk P0 kota melebihi desa. Silver dimuat ke DuckDB
(3.897 baris). `python pipeline.py` berjalan ±2.2 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
