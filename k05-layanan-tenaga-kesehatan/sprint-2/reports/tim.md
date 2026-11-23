# Laporan tim — Kunci, kasus 05 Layanan dan tenaga kesehatan

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
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

Panel Gold memuat 5 indikator provinsi (836 sel terisi, 76 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 17 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 37.9%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Dokter: BPS dokter umum (per 100.000) vs WHO semua dokter (per 10.000) | 50.1% | definisi berbeda | definisi (WHO termasuk dokter spesialis) setelah satuan diseragamkan (BPS x 0,1) |
| P2 | Perawat dan bidan: BPS (dua rincian dijumlahkan di Gold) vs WHO HWF_0006 | 25.6% | definisi berbeda | definisi (aktif vs terdaftar) setelah perawat + bidan dijumlahkan dan satuan diseragamkan |
| P3 | Unmet need pelayanan (BPS) vs indeks cakupan UHC (WHO): konteks | — | definisi berbeda | definisi berbeda: persentase penduduk tidak berobat vs indeks 14 indikator layanan |
| P4 | Kepemilikan JKN (BPS) vs pengeluaran kesehatan katastrofik (WHO): konteks | — | definisi berbeda | definisi berbeda: kepemilikan jaminan vs beban pengeluaran rumah tangga |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P1: WHO per 10.000 penduduk, BPS per 100.000 (var.note): pembanding dikali 10 sebelum selisih dihitung; P2: kepadatan BPS perawat + bidan dijumlahkan karena WHO menggabungkan keduanya; penyebut sama (penduduk).

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (21 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: profesi dari kamus, dua satuan kepadatan tidak tercampur,
tidak ada baris JKN sebelum 2022; satu peringatan bila dokter WHO lebih kecil dari dokter umum BPS setelah satuan
disamakan. Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB dengan kunci
primer dan CHECK (1.722 baris). `python pipeline.py` berjalan ±3.5 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (1.017 baris).
