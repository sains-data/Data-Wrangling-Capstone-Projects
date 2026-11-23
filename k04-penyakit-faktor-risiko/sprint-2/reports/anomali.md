# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1393 | 2010→2011 | 32 | 0.09 | 0.62 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2011→2012 | 32 | 0.28 | 0.41 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2012→2013 | 31 | 0.13 | 0.61 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2013→2014 | 31 | 0.16 | 0.71 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2014→2015 | 31 | 0.13 | 0.48 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2015→2016 | 32 | 0.12 | 0.56 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2016→2017 | 33 | 0.24 | 0.52 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2017→2018 | 33 | 0.24 | 0.58 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2018→2019 | 33 | 0.15 | 0.55 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2019→2020 | 32 | 0.25 | 0.34 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1393 | 2020→2021 | 33 | 0.24 | 0.52 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1480 | 2007→2013 | 33 | 0.00 | 0.52 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1480 | 2013→2018 | 33 | 0.64 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2017→2018 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2023→2024 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1435 | 2024→2025 | 38 | 0.05 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1393 | Kalimantan Timur | 6400 | 2014 | Kalimantan Utara | 0.47 | 0.32 |
| var1480 | Kalimantan Timur | 6400 | 2018 | Kalimantan Utara | 29.60 | 39.30 |
| var1435 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 25.30 | 25.90 |
| var1435 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 22.30 | 22.11 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (154)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1393 | Sumatera Barat | 2010 | 0.38 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Riau | 2010 | 1.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sumatera Selatan | 2010 | 1.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Kepulauan Bangka Belitung | 2010 | 7.77 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Kepulauan Riau | 2010 | 6.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Jawa Barat | 2010 | 0.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Jawa Tengah | 2010 | 0.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Jawa Timur | 2010 | 0.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Bali | 2010 | 0.03 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Barat | 2010 | 2.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2010 | 31.72 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Barat | 2010 | 6.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Kalimantan Timur | 2010 | 1.92 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Utara | 2010 | 6.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Tengah | 2010 | 5.69 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Selatan | 2010 | 0.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku Utara | 2010 | 12.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2010 | 61.18 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2010 | 54.94 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Nusa Tenggara Timur | 2011 | 22.09 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Barat | 2011 | 2.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Kalimantan Timur | 2011 | 1.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Utara | 2011 | 3.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Selatan | 2011 | 0.38 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Tenggara | 2011 | 1.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Barat | 2011 | 2.22 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2011 | 8.34 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2011 | 4.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2011 | 73.21 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2011 | 52.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2012 | 5.32 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Kepulauan Riau | 2012 | 2.47 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | DI Yogyakarta | 2012 | 0.06 | ke samping | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2012 | 19.41 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku | 2012 | 7.42 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua Barat | 2012 | 52.27 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2012 | 60.56 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2013 | 3.89 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2013 | 16.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku | 2013 | 8.25 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2013 | 4.51 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2013 | 38.44 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2013 | 42.65 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2014 | 2.17 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| var1393 | Nusa Tenggara Timur | 2014 | 12.81 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku | 2014 | 6.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2014 | 3.32 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| var1393 | Papua Barat | 2014 | 20.85 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2014 | 29.57 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2015 | 2.03 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2015 | 7.04 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Tengah | 2015 | 0.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Kalimantan Selatan | 2015 | 0.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2015 | 5.81 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2015 | 2.77 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2015 | 31.29 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2015 | 31.93 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2016 | 1.45 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Kepulauan Bangka Belitung | 2016 | 0.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2016 | 5.41 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku | 2016 | 3.95 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2016 | 2.44 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2016 | 6.79 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2016 | 45.85 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2017 | 0.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2017 | 5.76 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku | 2017 | 2.30 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2017 | 0.79 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2017 | 14.97 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2017 | 59.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Bengkulu | 2018 | 0.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Barat | 2018 | 0.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2018 | 3.42 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Timur | 2018 | 0.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2018 | 1.16 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2018 | 0.39 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2018 | 8.49 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2018 | 52.99 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Lampung | 2019 | 0.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2019 | 2.37 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Tengah | 2019 | 0.07 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Kalimantan Timur | 2019 | 0.55 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2019 | 0.72 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua Barat | 2019 | 7.38 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2019 | 64.03 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Riau | 2020 | 0.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Lampung | 2020 | 0.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Barat | 2020 | 0.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2020 | 2.76 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Timur | 2020 | 0.62 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Utara | 2020 | 0.36 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Sulawesi Tenggara | 2020 | 0.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2020 | 0.42 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Maluku Utara | 2020 | 0.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Papua Barat | 2020 | 10.15 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2020 | 63.12 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Sumatera Utara | 2021 | 0.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1393 | Nusa Tenggara Timur | 2021 | 1.69 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Kalimantan Timur | 2021 | 0.61 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1393 | Maluku | 2021 | 0.45 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua Barat | 2021 | 7.56 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1393 | Papua | 2021 | 80.05 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1435 | Aceh | 2015 | 29.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jawa Barat | 2015 | 33.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Banten | 2015 | 32.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Barat | 2016 | 26.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | DKI Jakarta | 2017 | 24.72 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Bali | 2017 | 22.22 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1435 | Nusa Tenggara Timur | 2017 | 27.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Gorontalo | 2017 | 34.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Papua | 2017 | 27.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Aceh | 2018 | 31.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Sumatera Utara | 2018 | 31.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Sumatera Barat | 2018 | 35.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Riau | 2018 | 32.72 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jambi | 2018 | 28.21 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Bengkulu | 2018 | 35.53 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Lampung | 2018 | 35.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Kepulauan Bangka Belitung | 2018 | 32.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Kepulauan Riau | 2018 | 29.67 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | DKI Jakarta | 2018 | 30.77 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jawa Barat | 2018 | 35.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jawa Tengah | 2018 | 30.79 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jawa Timur | 2018 | 30.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Banten | 2018 | 34.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Nusa Tenggara Timur | 2018 | 31.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Kalimantan Barat | 2018 | 30.92 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Kalimantan Tengah | 2018 | 32.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Kalimantan Timur | 2018 | 29.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Sulawesi Utara | 2018 | 32.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Sulawesi Selatan | 2018 | 29.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Sulawesi Barat | 2018 | 29.41 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Maluku | 2018 | 32.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Maluku Utara | 2018 | 35.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Barat | 2018 | 32.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Jambi | 2019 | 28.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Bali | 2019 | 20.96 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Barat | 2020 | 25.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | DKI Jakarta | 2021 | 24.44 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | DI Yogyakarta | 2021 | 24.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Bali | 2021 | 19.58 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1435 | Nusa Tenggara Barat | 2021 | 32.71 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Kalimantan Utara | 2021 | 27.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Maluku | 2021 | 27.90 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Papua | 2021 | 24.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Kepulauan Riau | 2023 | 25.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Banten | 2023 | 29.34 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1435 | Bali | 2023 | 18.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1435 | DKI Jakarta | 2025 | 25.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Barat | 2025 | 27.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Tengah | 2025 | 23.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var1435 | Papua Pegunungan | 2025 | 26.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var1480 | Papua Barat | 2007 | 20.10 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1480 | Kalimantan Selatan | 2018 | 44.10 | ke bawah | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1393 | 416 | 416 | 416 | 0 | 0 | 0 | (kosong) |
| var1435 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var1480 | 104 | 104 | 104 | 0 | 0 | 0 | (kosong) |

## Kunci Silver kembar: 0
