# Laporan tim — Kunci, kasus 23 Kerusakan dan kerugian bencana

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai sebelas seri provinsi BNPB (kejadian; rumah rusak, rumah terendam, fasilitas kesehatan, satuan
pendidikan, jembatan, kantor, rumah ibadat, kios/toko, pabrik; nilai kerusakan dan kerugian), dua seri luas yang
hanya terbit nasional, dan satu seri WDI. Silver pertama berisi 18.187 baris dari 15 seri.
Tantangannya bentuk data (tanpa kode seri, tujuh tata letak, sel tergabung, kab/kota yang dijumlahkan) dan sifat
tabel nilai: daftar usulan rehabilitasi-rekonstruksi, bukan penilaian kerusakan semua kejadian.

## Data dan lineage

58 berkas mentah: katalog CKAN (1), DataStore JSON BNPB (38), XLSX unduhan tangan (15), WDI (1 data
+ 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (90.269 baris mentah di berkas data,
90.203 sel BNPB). Angka provinsi hasil jumlah kab/kota dapat ditelusuri lewat `reports/bnpb-agregasi.csv`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tanpa kode seri, tujuh tata letak | judul resource katalog CKAN, kepala kolom | satu bentuk sel + kamus ukuran | 90.203 sel | K-002 |
| Sel Provinsi tergabung | rekap 2021/2022 XLSX | sel diisi sebelum dibaca | 7.574 angka jumlahan | K-003 |
| Rumah rusak dengan dan tanpa tingkat | rekap vs tabel per jenis | satu seri, rincian `tingkat_kerusakan` | — | K-006 |
| Usulan beberapa tahun kejadian | "2013 - 2015" | tidak dipakai | 168 sel | K-012 |
| Usulan berulang per kab/kota | Donggala, Kota Palu 2018 | dijumlah, didaftar | 10 kasus | K-012 |
| Luas kebakaran 2012 mustahil | 44 juta ha | dibuang (`GALAT_INPUT`) | 1 | K-014 |
| Luas hanya nasional, satuan tidak dinyatakan | Keterangan | tingkat nasional, hektar (dugaan) | 2 seri | K-013 |
| Kab/kota vs provinsi | aturan hitung Keterangan | kejadian boleh lebih besar; DKI -> Jawa Barat 2024 peringatan | 2 unit rusak | K-009 |
| Observasi sama di beberapa berkas | `reports/bnpb-lintas-berkas.csv` | semua disimpan; deret memilih satu | 172 kelompok berbeda | K-007 |
| Tahun tanpa tabel provinsi, provinsi tanpa usulan | katalog CKAN | `tidak_diterbitkan` | 3.158 sel | K-011 |
| Lompatan serentak 2021 -> 2022 | fasilitas kesehatan, rumah ibadat | `patahan_seri`, cari catatan metode | 10 calon | K-015 |
| Pemekaran Papua | rekap 2022 34 provinsi | `patahan_wilayah` | 16 | K-016 |
| Kerusakan dan rupiah menceng | profil | IQR pada log(1 + nilai) | 158 calon (130 outlier) | K-004 |

## Integrasi dan rekonsiliasi

Panel Gold memuat 12 indikator provinsi (1.688 sel terisi, 3.556 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 33 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 0.0%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Rumah rusak banjir: baris INDONESIA vs jumlah 38 provinsi | 0.0% | tidak berselisih (angka sama) | seharusnya sama: satu rumah tidak dihitung di dua provinsi (berbeda dengan kejadian) |
| P2 | Rumah rusak 2025: tabel per jenis vs rekap nasional (berat + sedang + ringan) | 0.0% | tidak berselisih (angka sama) | seharusnya sama: dua tabel 2025 dari kompilasi yang sama |
| P3 | Penduduk terdampak kekeringan, banjir, suhu ekstrem (WDI): konteks | — | definisi berbeda | periode dan konsep berbeda: WDI persen penduduk terdampak 1990–2009, BNPB unit rusak |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P1: baris INDONESIA dibandingkan dengan jumlah baris provinsi di berkas yang sama (GOLD_AGREGAT); P2: rumah rusak berat + sedang + ringan di rekap nasional dijumlahkan dulu sebelum dibandingkan dengan tabel per jenis.

## Validasi dan reproduksibilitas

24 aturan berjalan setiap `python pipeline.py` (20 lolos, 4
peringatan; `reports/validasi.md`). Aturan khas kasus: cacah bilangan bulat, jumlah jenis = Total, tingkat kerusakan
= tabel per jenis; peringatan untuk kab/kota vs provinsi, baris Indonesia antarberkas, dan rekap nilai vs tabel per
tahun. Silver dimuat ke DuckDB (18.187 baris). `python pipeline.py` berjalan ±8.7 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (5.305 baris).
