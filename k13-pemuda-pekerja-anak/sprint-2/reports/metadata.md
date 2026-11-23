# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1186 | Persentase Usia Muda (15-24 Tahun) Yang Sedang Tidak Sekolah, Bekerja Atau Mengikuti Pelatihan | Persentase usia muda (15–24 tahun) yang tidak sekolah, bekerja, atau mengikuti pelatihan (NEET) |
| var2658 | 8.7.1* Persentase dan Jumlah Pekerja Anak Usia 5-17 tahun Sesuai dengan Metadata SDGs Global Menurut Provinsi | Persentase pekerja anak usia 5–17 tahun sesuai metadata SDGs global |
| SL.UEM.NEET.ZS | Share of youth not in education, employment or training, total (% of youth population) | Share of youth not in education, employment or training, total (% of youth population) |
| SL.TLF.0714.ZS | Children in employment, total (% of children ages 7-14) | Children in employment, total (% of children ages 7-14) |
| SDG_0861_SEX_RT | SDG indicator 8.6.1: Proportion of youth aged 15 to 24 years not in education, employment or training by sex | Proportion of youth aged 15 to 24 years not in education, employment or training (%) |
| SDG_A871_SEX_AGE_RT | SDG indicator 8.7.1: Proportion of children engaged in economic activity by sex and age | Proportion of children engaged in economic activity (%) |
| SDG_B871_SEX_AGE_RT | SDG indicator 8.7.1: Proportion of children engaged in economic activity and household chores by sex and age | Proportion of children engaged in economic activity and household chores (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1186 | persen | persen | var.unit: 'Persen' | 8.6.1 | 8.6.1 |
| var2658 | persen | persen | var.unit: 'Persen' (judul menyebut 'Persentase dan Jumlah', berkas hanya persentase) | 8.7.1 | 8.7.1 |
| SL.UEM.NEET.ZS | — | persen | name: '(% of youth population)' | — | 8.6.1 |
| SL.TLF.0714.ZS | — | persen | name: '(% of children ages 7-14)' | — | 8.7.1 |
| SDG_0861_SEX_RT | — | persen | UNIT_MEASURE PT | 8.6.1 | 8.6.1 |
| SDG_A871_SEX_AGE_RT | — | persen | UNIT_MEASURE PT | 8.7.1 | 8.7.1 |
| SDG_B871_SEX_AGE_RT | — | persen | UNIT_MEASURE PT | 8.7.1 | 8.7.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| SL.UEM.NEET.ZS | kode SDG kosong -> 8.6.1 |
| SL.TLF.0714.ZS | kode SDG kosong -> 8.7.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2658 | Sumber: Badan Pusat Statistik |
| 1186 | Sumber: Sakernas, BPS |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SL.TLF.0714.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SL.UEM.NEET.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
