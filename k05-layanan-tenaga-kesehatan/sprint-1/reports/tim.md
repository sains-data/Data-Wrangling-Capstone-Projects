# Laporan tim — Kunci, kasus 05 Layanan dan tenaga kesehatan

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini menyatukan tiga seri provinsi BPS (unmet need pelayanan kesehatan, kepemilikan JKN, kepadatan tenaga
kesehatan menurut profesi) dengan empat seri WHO. Tidak ada WDI. Silver pertama berisi 1.722 baris dari
7 seri. Tantangan utamanya ada di `var1477`: sepuluh profesi tanpa baris total, satuan yang hanya
tertulis di catatan, dan pembanding WHO dengan satuan dan definisi profesi yang berbeda.

## Data dan lineage

13 berkas mentah dari snapshot 20 Oktober 2026: BPS (3 CSV, 3 JSON, 1 catatan unduhan) dan WHO GHO
(4 CSV, 2 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (3.193 baris mentah di berkas
data). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Satuan `var1477` kosong | `var.note`: per 100.000 penduduk | `per_100000_penduduk`, diseragamkan di Gold | 926 | K-007 |
| Profesi di `turvar` | 10 label profesi | rincian `profesi=<kode>` | 24 nilai rincian | K-006 |
| Tidak ada total `var1477` | `turvar` tanpa "Jumlah" | profil dan grid untuk tiga profesi | — | K-004 |
| Kode SDG butir nasional | nama tabel `sdg3_3_8_1_a`, `sdg3_3_8_2_a`, `sdg3_3_c_1` | 3.8.1(a), 3.8.2(a), 3.c.1 | 545 | K-008 |
| JKN baru terbit 2022 | daftar tahun JSON | tidak diimputasi ke belakang | 0 | K-005 |
| Indonesia `var1477` hanya 2018 | baris 9999 | P1, P2 satu tahun | 1 tahun | K-011 |
| Lonjakan serentak | unmet need 2021→2022, bidan 2016→2017 | `patahan_seri`, nilai tidak diubah | 11 | K-012 |
| Wilayah induk mengecil | Papua, Papua Barat | `patahan_wilayah` | 4 | K-010 |
| Provinsi belum dibentuk / belum dipecah | provinsi Papua baru | `belum_ada` 72, `batas_lama` 4 | sel | K-001 |
| Calon anomali lain | IQR ke bawah, perubahan, ke samping | 47 outlier ditandai | 62 | K-004 |
| BPS dua format | nilai CSV = JSON | JSON sebagai sumber | 1.471 | K-002 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Disiapkan di Sprint 1, dihitung di Sprint 2 (`reports/pasangan-rekonsiliasi.md`):

- P1 dokter umum BPS vs dokter WHO: 1 tahun (2018); WHO termasuk spesialis.
- P2 perawat + bidan BPS vs WHO: 1 tahun; BPS dijumlahkan dulu di Gold.
- P3 unmet need vs indeks UHC: konteks.
- P4 JKN vs pengeluaran katastrofik: konteks, tanpa tahun bersama.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (11 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: profesi dari kamus, dua satuan kepadatan tidak tercampur,
tidak ada baris JKN sebelum 2022; satu peringatan bila dokter WHO lebih kecil dari dokter umum BPS setelah satuan
disamakan. Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB dengan kunci
primer dan CHECK (1.722 baris). `python pipeline.py` berjalan ±2.3 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
