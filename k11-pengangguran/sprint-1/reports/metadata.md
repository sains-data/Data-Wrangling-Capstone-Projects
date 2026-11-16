# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var543 | Tingkat Pengangguran Terbuka Menurut Provinsi | Tingkat Pengangguran Terbuka (TPT) |
| SL.UEM.TOTL.ZS | Unemployment, total (% of total labor force) (modeled ILO estimate) | Unemployment, total (% of total labor force) (modeled ILO estimate) |
| SL.UEM.TOTL.NE.ZS | Unemployment, total (% of total labor force) (national estimate) | Unemployment, total (% of total labor force) (national estimate) |
| SDG_0852_SEX_AGE_RT | SDG indicator 8.5.2: Unemployment rate by sex and age | Unemployment rate by sex and age (%) |
| SDG_0852_SEX_DSB_RT | SDG indicator 8.5.2: Unemployment rate by sex and disability status | Unemployment rate by sex and disability status (%) |
| UNE_DEAP_SEX_AGE_RT | Unemployment rate by sex and age | Unemployment rate by sex and age, ILO modelled/harmonized (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var543 | persen | persen | var.unit: 'Persen' | 8.5.2 | 8.5.2 |
| SL.UEM.TOTL.ZS | — | persen | name: '(% of total labor force)' | — | 8.5.2 |
| SL.UEM.TOTL.NE.ZS | — | persen | name: '(% of total labor force)' | — | 8.5.2 |
| SDG_0852_SEX_AGE_RT | — | persen | UNIT_MEASURE PT | 8.5.2 | 8.5.2 |
| SDG_0852_SEX_DSB_RT | — | persen | UNIT_MEASURE PT | 8.5.2 | 8.5.2 |
| UNE_DEAP_SEX_AGE_RT | — | persen | UNIT_MEASURE PT | 8.5.2 | 8.5.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| SL.UEM.TOTL.ZS | kode SDG kosong -> 8.5.2 |
| SL.UEM.TOTL.NE.ZS | kode SDG kosong -> 8.5.2 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 543 | Data 2011-2013 menggunakan Backcast dari Penimbang Proyeksi Komponen Data 2018-2020 menggunakan Backcast dari Penimbang berbasis SUPAS 2015 1986-1998, penghitungan tanpa data Provinsi Timor Timor Pada tahun 1995, Sakernas tidak dilaksanakan Pada tahun 2000, tanpa Maluku Sumber: Survei Angkatan Kerja Nasional (Sakernas) |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SL.UEM.TOTL.NE.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SL.UEM.TOTL.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
