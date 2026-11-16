# Laporan tim — Kunci, kasus 22 Korban bencana

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai sembilan seri provinsi BNPB (kejadian, korban meninggal, hilang, luka/sakit, mengungsi,
terdampak, terdampak-mengungsi, dua angka per 100.000) beserta penyebutnya (jumlah penduduk), dan satu seri WDI.
Silver pertama berisi 14.193 baris dari 11 seri. Tantangannya bentuk data: tidak ada kode
seri, enam tata letak dalam dua format, sel tergabung, angka provinsi yang sebagian harus dibentuk dari kab/kota,
dan observasi yang sama terbit di beberapa berkas.

## Data dan lineage

44 berkas mentah: katalog CKAN (1), DataStore JSON BNPB (26), XLSX unduhan tangan (13), WDI (1 data
+ 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (77.522 baris mentah di berkas data,
77.456 sel BNPB). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`; angka provinsi hasil jumlah
kab/kota dapat ditelusuri ke baris kab/kotanya lewat `reports/bnpb-agregasi.csv`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tanpa kode seri, enam tata letak | judul resource katalog CKAN, kepala kolom | satu bentuk sel + kamus ukuran | 77.456 sel | K-002 |
| Sel Provinsi tergabung | rekap 2021/2022 XLSX | sel diisi sebelum dibaca | 4.494 angka jumlahan | K-003 |
| Kode Kemendagri ≠ BPS untuk Papua | lembar Keterangan | dipetakan, kode dan nama harus sepakat | — | K-001 |
| Kab/kota dijumlahkan | tabel kab/kota | jumlah + banyak kab/kota dicatat | 46.330 baris kab/kota | K-008 |
| Kab/kota vs provinsi | aturan hitung Keterangan | kejadian boleh lebih besar (164); DKI -> Jawa Barat 2024 peringatan | 6 korban | K-009 |
| Observasi sama di beberapa berkas | `reports/bnpb-lintas-berkas.csv` | semua disimpan; deret memilih satu | 172 kelompok berbeda | K-007 |
| INDONESIA tanah longsor 2024 = 27 | tiga tabel lain dan jumlah provinsi = 207 | peringatan, tidak diubah | 1 | K-014 |
| Galat titik mengambang Excel | `11.000000000000002` | dibulatkan | 33 | K-010 |
| Tahun tanpa tabel provinsi | katalog CKAN | `tidak_diterbitkan` | 1.772 sel | K-011 |
| Pemekaran Papua | rekap 2022 34 provinsi | `patahan_wilayah` | 6 | K-013 |
| Jumlah korban menceng | profil | IQR pada log(1 + nilai) | 119 calon (101 outlier) | K-004 |

Tidak ada galat input menurut rentang satuan (0).

## Integrasi dan rekonsiliasi

- P1, P2 angka per 100.000: dihitung ulang dari pembilang dan Jumlah Penduduk; selisih 0 di semua sel (aturan keras
  `per_100rb_dihitung_ulang`), jadi angka terbit memang turunan langsung dari dua tabel lain.
- P3 kejadian banjir INDONESIA vs jumlah 38 provinsi: 16 tahun; jumlah provinsi boleh lebih besar.
- P4 WDI kekeringan, banjir, suhu ekstrem: konteks (rata-rata 1990–2009).

## Validasi dan reproduksibilitas

13 aturan berjalan setiap `python pipeline.py` (10 lolos, 3
peringatan; `reports/validasi.md`). Aturan khas kasus: cacah bilangan bulat, jumlah jenis = Total, angka per 100.000
dapat dihitung ulang; peringatan untuk kab/kota vs provinsi dan baris Indonesia yang berbeda antarberkas. Silver
dimuat ke DuckDB (14.193 baris). `python pipeline.py` berjalan ±5.4 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
