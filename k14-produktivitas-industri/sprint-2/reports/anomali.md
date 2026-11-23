# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1161 | — | 38 |  |  | tidak diuji | seri laju pertumbuhan: perubahan relatif laju tidak bermakna (bisa berganti tanda); patahan diuji pada seri tingkat |
| var1344 | 2015→2016 | 34 | 0.18 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2016→2017 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2017→2018 | 34 | 0.09 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2020→2021 | 34 | 0.09 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2021→2022 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1344 | 2022→2023 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2010→2011 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2011→2012 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2012→2013 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2013→2014 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2014→2015 | 34 | 0.03 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2015→2016 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2016→2017 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2017→2018 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2019→2020 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2020→2021 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2021→2022 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1214 | 2022→2023 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2018→2019 | 34 | 0.03 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2019→2020 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2020→2021 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2021→2022 | 34 | 0.03 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2022→2023 | 34 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2023→2024 | 34 | 0.09 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2755 | 2024→2025 | 38 | 0.05 | 0.05 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 7

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1161 | Kalimantan Timur | 6400 | 2016 | Kalimantan Utara | 16.39 | -10.21 |
| var1161 | Papua Barat | 9100 | 2025 | Papua Barat Daya | 9.22 | 7.11 |
| var1161 | Papua | 9400 | 2025 | Papua Selatan, Papua Tengah, Papua Pegunungan | 3.40 | 9.90 |
| var1214 | Papua Barat | 9100 | 2023 | Papua Barat Daya | 30.87 | 39.36 |
| var1214 | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 1.65 | 2.86 |
| var2755 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 4.44 | 5.04 |
| var2755 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 1.53 | 5.32 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (240)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1161 | Sumatera Utara | 2011 | 18.09 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Jambi | 2011 | 13.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Lampung | 2011 | 18.22 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kepulauan Bangka Belitung | 2011 | 12.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tenggara | 2011 | 15.58 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Sumatera Utara | 2012 | 0.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Lampung | 2012 | 1.95 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Aceh | 2013 | 0.70 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Riau | 2013 | -0.81 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Jambi | 2013 | 9.84 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | DKI Jakarta | 2013 | 9.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Timur | 2013 | -6.41 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Barat | 2013 | 12.15 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sumatera Utara | 2014 | 8.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Timur | 2014 | -2.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Barat | 2014 | -0.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Nusa Tenggara Barat | 2015 | 19.85 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Timur | 2015 | 16.39 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tengah | 2015 | 12.52 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku | 2015 | -3.12 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Kepulauan Bangka Belitung | 2016 | -5.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Nusa Tenggara Barat | 2016 | -4.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Timur | 2016 | -10.21 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1161 | DKI Jakarta | 2017 | 14.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Tengah | 2017 | 8.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Utara | 2017 | -7.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Utara | 2017 | 13.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Nusa Tenggara Timur | 2018 | -7.31 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Utara | 2018 | 4.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tengah | 2018 | 11.98 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku | 2018 | -8.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Nusa Tenggara Barat | 2019 | -6.51 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2019 | -15.34 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Bali | 2020 | -7.63 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Nusa Tenggara Barat | 2020 | -2.70 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Barat | 2020 | -2.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Selatan | 2020 | -3.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku Utara | 2020 | 5.25 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2020 | 8.47 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tengah | 2021 | 11.09 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku Utara | 2021 | 13.47 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua Barat | 2021 | -5.52 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2021 | 3.20 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tengah | 2022 | 10.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku Utara | 2022 | 19.52 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Riau | 2023 | 9.99 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kepulauan Riau | 2023 | 19.25 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Banten | 2023 | 12.87 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Kalimantan Barat | 2023 | -3.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Tengah | 2023 | 14.74 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua Barat | 2023 | -9.66 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2023 | -16.88 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Kepulauan Riau | 2024 | 2.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Banten | 2024 | -0.29 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku Utara | 2024 | 9.31 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Papua Barat | 2024 | 9.22 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2024 | 3.40 | perubahan | outlier | tandai, nilai tidak diubah |
| var1161 | Sulawesi Barat | 2025 | -0.29 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1161 | Maluku Utara | 2025 | 31.79 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1161 | Papua | 2025 | 9.90 | ke bawah | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1161 | Papua Tengah | 2025 | -22.96 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1214 | DI Yogyakarta | 2010 | 14.25 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Selatan | 2010 | 13.72 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Timur | 2010 | 24.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | DI Yogyakarta | 2011 | 14.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Tengah | 2011 | 14.57 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Timur | 2011 | 22.33 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Riau | 2012 | 25.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Lampung | 2012 | 17.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2012 | 43.34 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Jawa Tengah | 2012 | 34.94 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | DI Yogyakarta | 2012 | 13.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Banten | 2012 | 38.29 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Tengah | 2012 | 14.37 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Timur | 2012 | 20.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Aceh | 2013 | 7.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Riau | 2013 | 26.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2013 | 43.68 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Kalimantan Tengah | 2013 | 14.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Timur | 2013 | 19.66 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Riau | 2014 | 27.33 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Kepulauan Bangka Belitung | 2014 | 23.26 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2014 | 43.72 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Banten | 2014 | 37.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Kalimantan Tengah | 2014 | 15.25 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Barat | 2014 | 11.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Aceh | 2015 | 5.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Riau | 2015 | 28.26 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2015 | 43.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Kalimantan Timur | 2015 | 20.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2015 | 9.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2016 | 43.07 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Kalimantan Timur | 2016 | 21.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2016 | 12.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2017 | 43.07 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Maluku Utara | 2017 | 7.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Lampung | 2018 | 18.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2018 | 43.42 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Banten | 2018 | 34.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2018 | 21.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Selatan | 2018 | 13.19 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku Utara | 2018 | 7.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Nusa Tenggara Timur | 2019 | 1.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2019 | 23.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Riau | 2020 | 31.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Kepulauan Riau | 2020 | 40.77 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | DKI Jakarta | 2020 | 10.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2020 | 42.16 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Sulawesi Tengah | 2020 | 27.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku Utara | 2020 | 11.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Kepulauan Riau | 2021 | 41.96 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2021 | 42.36 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | Nusa Tenggara Timur | 2021 | 1.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2021 | 29.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku Utara | 2021 | 17.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | DI Yogyakarta | 2022 | 11.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Nusa Tenggara Timur | 2022 | 1.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2022 | 32.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tenggara | 2022 | 8.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Gorontalo | 2022 | 4.40 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku | 2022 | 6.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku Utara | 2022 | 25.66 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Papua | 2022 | 1.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Kepulauan Riau | 2023 | 40.66 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Jawa Barat | 2023 | 42.88 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1214 | DI Yogyakarta | 2023 | 11.33 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tengah | 2023 | 36.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var1214 | Sulawesi Tenggara | 2023 | 8.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku | 2023 | 6.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Maluku Utara | 2023 | 30.09 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1214 | Papua Barat | 2023 | 39.36 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1214 | Papua | 2023 | 2.86 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1344 | Riau | 2015 | 124,492,105.50 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Lampung | 2015 | 42,534,940.39 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | DKI Jakarta | 2015 | 34,746,299.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | Jawa Barat | 2015 | 42,002,733.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | Jawa Tengah | 2015 | 31,008,568.47 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | Jawa Timur | 2015 | 33,107,268.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | Nusa Tenggara Barat | 2015 | 24,410,637.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2015 | 112,811,919.40 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2015 | 123,346,018.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Riau | 2016 | 140,456,266.70 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kepulauan Riau | 2016 | 98,106,166.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | DKI Jakarta | 2016 | 120,232,473.70 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2016 | 127,408,296.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2016 | 138,693,395.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Sulawesi Utara | 2016 | 82,469,708.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Riau | 2017 | 145,498,341.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kepulauan Riau | 2017 | 109,922,192.38 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | DKI Jakarta | 2017 | 130,123,080.83 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2017 | 135,705,272.48 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2017 | 147,289,096.52 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Riau | 2018 | 149,541,382.22 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | DKI Jakarta | 2018 | 93,703,148.43 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Banten | 2018 | 64,305,740.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2018 | 157,265,983.66 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2018 | 135,364,238.41 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Sulawesi Utara | 2018 | 77,633,466.90 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Riau | 2019 | 154,991,100.84 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Timur | 2019 | 159,684,833.29 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2019 | 153,748,725.48 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Riau | 2020 | 165,160,425.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kepulauan Riau | 2020 | 88,571,947.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2020 | 154,191,705.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2020 | 160,272,315.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Riau | 2021 | 185,539,364.69 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kepulauan Bangka Belitung | 2021 | 90,148,456.06 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | DKI Jakarta | 2021 | 72,446,101.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2021 | 164,941,698.81 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2021 | 175,583,697.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Sulawesi Utara | 2021 | 106,417,957.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Riau | 2022 | 199,870,060.50 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kepulauan Riau | 2022 | 102,373,400.79 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | DKI Jakarta | 2022 | 99,345,461.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2022 | 185,990,703.48 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Kalimantan Utara | 2022 | 165,546,300.84 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Gorontalo | 2022 | 88,461,848.78 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Papua Barat | 2022 | 50,608,064.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Riau | 2023 | 235,350,879.04 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Jambi | 2023 | 114,799,868.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var1344 | Kalimantan Timur | 2023 | 190,742,066.74 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1344 | Sulawesi Tenggara | 2023 | 97,368,042.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Sumatera Selatan | 2018 | 7.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Kepulauan Riau | 2018 | 23.70 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | DKI Jakarta | 2018 | 13.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Jawa Barat | 2018 | 20.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2018 | 21.86 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2018 | 23.39 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Maluku | 2018 | 8.53 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Papua Barat | 2018 | 6.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Sumatera Selatan | 2019 | 6.22 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Lampung | 2019 | 11.23 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Kepulauan Riau | 2019 | 23.91 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Barat | 2019 | 21.07 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2019 | 22.40 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2019 | 23.68 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Gorontalo | 2019 | 7.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Papua Barat | 2019 | 3.90 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Kepulauan Riau | 2020 | 22.76 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Barat | 2020 | 18.56 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2020 | 20.64 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2020 | 20.32 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Maluku | 2020 | 11.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Kepulauan Riau | 2021 | 25.01 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2021 | 22.17 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2021 | 20.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Sulawesi Utara | 2021 | 10.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Maluku Utara | 2021 | 16.66 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Kepulauan Riau | 2022 | 25.77 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Barat | 2022 | 19.29 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2022 | 21.89 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2022 | 23.04 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Kalimantan Tengah | 2022 | 3.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Maluku Utara | 2022 | 19.84 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Kepulauan Riau | 2023 | 25.23 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2023 | 20.94 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | DI Yogyakarta | 2023 | 13.74 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Banten | 2023 | 21.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Maluku Utara | 2023 | 25.48 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Kepulauan Riau | 2024 | 23.65 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Barat | 2024 | 18.74 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2024 | 20.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | DI Yogyakarta | 2024 | 17.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Banten | 2024 | 21.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Nusa Tenggara Barat | 2024 | 10.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Sulawesi Utara | 2024 | 9.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Sulawesi Barat | 2024 | 8.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Maluku Utara | 2024 | 24.66 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Papua | 2024 | 5.32 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2755 | Sumatera Barat | 2025 | 7.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Kepulauan Riau | 2025 | 24.16 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Jawa Tengah | 2025 | 20.98 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Banten | 2025 | 22.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Sulawesi Utara | 2025 | 11.55 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Sulawesi Selatan | 2025 | 7.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Sulawesi Tenggara | 2025 | 8.41 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Maluku | 2025 | 13.07 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2755 | Maluku Utara | 2025 | 24.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2755 | Papua Barat | 2025 | 3.43 | perubahan | outlier | tandai, nilai tidak diubah |
| var2755 | Papua | 2025 | 4.79 | ke samping | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1161 | 524 | 524 | 524 | 0 | 0 | 0 | (kosong) |
| var1214 | 494 | 494 | 494 | 0 | 0 | 0 | (kosong) |
| var1344 | 315 | 315 | 315 | 0 | 0 | 0 | Rupiah/Tenaga Kerja |
| var2755 | 288 | 288 | 288 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
