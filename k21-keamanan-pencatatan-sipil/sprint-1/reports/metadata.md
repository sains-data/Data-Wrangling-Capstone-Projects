# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1311 | 16.1.3 (a) Proporsi Penduduk Yang Menjadi Korban Kejahatan Kekerasan Dalam 12 Bulan Terakhir Menurut Provinsi | Proporsi penduduk yang menjadi korban kejahatan kekerasan dalam 12 bulan terakhir |
| var1312 | 16.1.4* Proporsi penduduk yang merasa aman berjalan sendirian di area tempat tinggalnya berdasarkan provinsi | Proporsi penduduk yang merasa aman berjalan sendirian di area tempat tinggalnya |
| var2738 | 16.2.1 (a) Proporsi rumah tangga yang memiliki anak umur 1-17 tahun yang mengalami hukuman fisik dan/atau agresi psikologis dari pengasuh dalam setahun terakhir berdasarkan provinsi | Proporsi rumah tangga dengan anak 1–17 tahun yang mengalami hukuman fisik dan/atau agresi psikologis dari pengasuh |
| var2740 | 16.3.1.(a) Proporsi korban kekerasan dalam 12 bulan terakhir yang melaporkan kepada polisi berdasarkan provinsi | Proporsi korban kekerasan dalam 12 bulan terakhir yang melaporkan kepada polisi |
| var1410 | Proporsi anak umur di bawah 5 tahun yang kelahirannya dicatat oleh lembaga pencatatan sipil Menurut Provinsi | Proporsi anak umur di bawah 5 tahun yang kelahirannya dicatat lembaga pencatatan sipil |
| var1831 | Persentase Anak Berumur 0-17 Tahun yang Memiliki Akta Kelahiran Menurut Provinsi | Persentase anak berumur 0–17 tahun yang memiliki akta kelahiran |
| SP.REG.BRTH.ZS | Completeness of birth registration (%) | Completeness of birth registration (%) |
| VC.IHR.PSRC.P5 | Intentional homicides (per 100,000 people) | Intentional homicides (per 100,000 people) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1311 | persen | persen | var.unit: 'Persen' | 16.1.3 | 16.1.3(a) |
| var1312 | persen | persen | var.unit: 'Persen' | 16.1.4 | 16.1.4 |
| var2738 | persen | persen | var.unit: 'Persen' | 16.2.1 | 16.2.1(a) |
| var2740 | persen | persen | var.unit: 'Persen' | 16.3.1 | 16.3.1(a) |
| var1410 | persen | persen | var.unit: 'Persen' | 16.9.1 | 16.9.1 |
| var1831 | persen | persen | var.unit: 'Persen' | 16.9.1 | 16.9.1(b) |
| SP.REG.BRTH.ZS | — | persen | name: '(%)' | — | 16.9.1 |
| VC.IHR.PSRC.P5 | — | per_100000_penduduk | name: '(per 100,000 people)' | — | 16.1.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1311 | kode SDG 16.1.3 -> 16.1.3(a) |
| var2738 | kode SDG 16.2.1 -> 16.2.1(a) |
| var2740 | kode SDG 16.3.1 -> 16.3.1(a) |
| var1831 | kode SDG 16.9.1 -> 16.9.1(b) |
| SP.REG.BRTH.ZS | kode SDG kosong -> 16.9.1 |
| VC.IHR.PSRC.P5 | kode SDG kosong -> 16.1.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1311 | Sumber: Susenas. Untuk Susenas 2018 pertanyaan kejahatan ditanyakan untuk time reference 1 Januari - 31 Desember 2017, sehingga indikator kejahatan merupakan kondisi tahun 2017. Sebelum 2018 Susenas pertanyaan melaporkan kepada Polisi belum dipisah per jenis kejahatan, sehingga nilai indikator 2015 dan 2016 merupakan pelaporan kejahatan untuk semua jenis kejahatan. Namun untuk tahun 2017 yang bersumber dari Susenas 2018 indikatornya mencakup kejahatan kekerasan saja. |
| 1312 | Sumber: Susenas Modul Hansos |
| 2738 | Sumber: Badan Pusat Statistik |
| 2740 | Sumber: Badan Pusat Statistik |
| 1831 | Persentase Anak Berumur 0-17 Tahun yang Memiliki Akta Kelahiran Menurut Provinsi (Persen), 2023 |
| 1410 | Sumber : Susenas BPS Definisi : Bagian dari populasi anak berusia kurang dari 5 tahun yang kelahirannya dicatat oleh lembaga pencatatan sipil dan dibuktikan dengan penerbitan akta kelahiran |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SP.REG.BRTH.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| VC.IHR.PSRC.P5 | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
