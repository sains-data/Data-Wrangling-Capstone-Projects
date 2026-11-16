# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var87 | Persentase Rumah Tangga menurut Provinsi dan Sumber Penerangan Utama dari Listrik PLN | Persentase rumah tangga dengan sumber penerangan utama listrik PLN |
| tabel:sdg7_bahan_bakar | Persentase Rumah Tangga Menurut Provinsi dan Bahan Bakar Utama untuk Memasak Tahun 2001, 2007-2021 | Persentase rumah tangga menurut bahan bakar utama untuk memasak |
| EG.ELC.ACCS.ZS | Access to electricity (% of population) | Access to electricity (% of population) |
| EG.CFT.ACCS.ZS | Access to clean fuels and technologies for cooking (% of population) | Access to clean fuels and technologies for cooking (% of population) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var87 | persen | persen | var.unit: 'Persen' | 7.1.1 | 7.1.1 |
| tabel:sdg7_bahan_bakar | persen | persen | judul tabel statis 'Persentase Rumah Tangga' | 7.1.2 | 7.1.2 |
| EG.ELC.ACCS.ZS | — | persen | name: '(% of population)' | — | 7.1.1 |
| EG.CFT.ACCS.ZS | — | persen | name: '(% of population)' | — | 7.1.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| EG.ELC.ACCS.ZS | kode SDG kosong -> 7.1.1 |
| EG.CFT.ACCS.ZS | kode SDG kosong -> 7.1.2 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 87 | Sumber: Susenas Maret |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| EG.CFT.ACCS.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| EG.ELC.ACCS.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
