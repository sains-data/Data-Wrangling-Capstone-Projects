# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var192 | Persentase Penduduk Miskin (P0) Menurut Provinsi dan Daerah | Persentase penduduk miskin (P0) menurut daerah |
| var2190 | Jumlah Desa Mandiri Menurut Provinsi | Jumlah desa mandiri |
| var2191 | Jumlah Desa Tertinggal menurut Provinsi | Jumlah desa tertinggal dan sangat tertinggal |
| SI.POV.NAHC | Poverty headcount ratio at national poverty lines (% of population) | Poverty headcount ratio at national poverty lines (% of population) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var192 | persen | persen | var.unit: 'Persen' | 10.1.1 | 1.2.1 |
| var2190 | desa | desa | var.unit: 'Desa' | 10.1.1 | 10.1.1(d) |
| var2191 | desa | desa | var.unit: 'Desa' | 10.1.1 | 10.1.1(c) |
| SI.POV.NAHC | — | persen | name: '(% of population)' | — | 1.2.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var192 | kode SDG 10.1.1 -> 1.2.1 (berkas dipakai BPS sebagai butir 10.1.1(f)) |
| var2190 | kode SDG 10.1.1 -> 10.1.1(d) |
| var2191 | kode SDG 10.1.1 -> 10.1.1(c) |
| SI.POV.NAHC | kode SDG kosong -> 1.2.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2191 | Keterangan: Mulai tahun 2019, menggunakan sumber Indeks Desa. Sebelumnya menggunakan Indeks Pembangunan Desa (tahun 2018). Terdapat perbedaan kategori di antara keduanya sehingga tidak bisa dibandingkan Indeks Desa 2019 dihitung berdasarkan data hasil pendataan Podes 2018 dan Updating Podes 2019 serta menggunakan daftar desa Kepmnedagri No 414 Tahun 2019 Indeks Desa 2020 dihitung berdasarkan data hasil Updating Podes 2020 dan menggunakan daftar desa Kepmendagri No 146 Tahun 2020 Indeks Desa 2021 dihitung berdasarkan data hasil Pendataan Podes 2021 dan menggunakan daftar desa Kepmendagri No 146 Tahun 2020 |
| 2190 | Keterangan: Mulai tahun 2019, menggunakan sumber Indeks Desa. Sebelumnya menggunakan Indeks Pembangunan Desa (tahun 2018). Terdapat perbedaan kategori di antara keduanya sehingga tidak bisa dibandingkan Indeks Desa 2019 dihitung berdasarkan data hasil pendataan Podes 2018 dan Updating Podes 2019 serta menggunakan daftar desa Kepmnedagri No 414 Tahun 2019 Indeks Desa 2020 dihitung berdasarkan data hasil Updating Podes 2020 dan menggunakan daftar desa Kepmendagri No 146 Tahun 2020 Indeks Desa 2021 dihitung berdasarkan data hasil Pendataan Podes 2021 dan menggunakan daftar desa Kepmendagri No 146 Tahun 2020 |
| 192 | Data Provinsi Kalimantan Utara pada tahun 2013 dan 2014 masih bergabung dengan Provinsi Kalimantan Timur Angka Provinsi Papua Barat dan Papua sebelum tahun 2024 merupakan angka provinsi sebelum mengalami pemekaran Daerah Otonom Baru (DOB) |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SI.POV.NAHC | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
