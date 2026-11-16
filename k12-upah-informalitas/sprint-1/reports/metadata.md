# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1172 | Upah Rata - Rata Per Jam Pekerja Menurut Provinsi | Upah rata-rata per jam pekerja |
| var2153 | Proporsi Lapangan Kerja Informal Menurut Provinsi | Proporsi lapangan kerja informal |
| SDG_0851_SEX_OCU_NB | SDG indicator 8.5.1: Average hourly earnings of employees by sex and occupation | Average hourly earnings of employees by sex and occupation (IDR) |
| SDG_0831_SEX_ECO_RT | SDG indicator 8.3.1: Proportion of informal employment in total employment by sex and economic activity | Proportion of informal employment in total employment by sex and economic activity (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1172 | rupiah_per_jam | rupiah_per_jam | var.unit: 'Rupiah/Jam' | 8.5.1 | 8.5.1 |
| var2153 | tidak_ada | persen | judul 'Proporsi'; var.unit kosong; nilai 20–90 | 8.3.1 | 8.3.1 |
| SDG_0851_SEX_OCU_NB | — | rupiah_per_jam | UNIT_MEASURE LC (mata uang lokal); NOTE_INDICATOR 'IDR: Indonesian rupiah'; judul DSD 'hourly earnings' | 8.5.1 | 8.5.1 |
| SDG_0831_SEX_ECO_RT | — | persen | UNIT_MEASURE PT | 8.3.1 | 8.3.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var2153 | satuan tidak_ada -> persen |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2153 | Sumber: Sakernas, BPS |
| 1172 | Sumber: Sakernas, BPS Tahun 2015-2019 angka revisi karena perubahan penimbang |

## Metadata WDI yang muncul di lebih dari satu berkas

Tidak ada.

## Judul dengan spasi di awal/akhir

Tidak ada.
