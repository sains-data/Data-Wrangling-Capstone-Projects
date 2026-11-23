# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1458 | Angka Melek Aksara Penduduk 15 Tahun ke Atas Menurut Provinsi | Angka melek aksara penduduk 15 tahun ke atas |
| tabel:sdg4_amh_rinci | Angka Melek Aksara Penduduk Umur 15 Tahun ke Atas Menurut Provinsi, Klasifikasi Desa, dan Jenis Kelamin, 2009-2025 | Angka melek aksara penduduk 15 tahun ke atas menurut klasifikasi desa dan jenis kelamin |
| SE.ADT.LITR.ZS | Literacy rate, adult total (% of people ages 15 and above) | Literacy rate, adult total (% of people ages 15 and above) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1458 | persen | persen | var.unit: 'Persen' | 4.6.1 | 4.6.1 |
| tabel:sdg4_amh_rinci | persen | persen | judul tabel statis (angka melek aksara, persen) | 4.6.1 | 4.6.1 |
| SE.ADT.LITR.ZS | — | persen | name: '(% of people ages 15 and above)' | — | 4.6.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| SE.ADT.LITR.ZS | kode SDG kosong -> 4.6.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1458 | Sumber: BPS, Susenas |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SE.ADT.LITR.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
