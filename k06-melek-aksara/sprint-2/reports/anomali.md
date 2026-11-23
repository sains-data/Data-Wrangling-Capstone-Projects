# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1458 | 2014→2015 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2023→2024 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1458 | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2009→2010 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2010→2011 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2011→2012 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2012→2013 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2013→2014 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2014→2015 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2023→2024 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg4_amh_rinci | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 6

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1458 | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 98.59 | 98.69 |
| var1458 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 97.84 | 97.89 |
| var1458 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 84.22 | 98.37 |
| tabel:sdg4_amh_rinci | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 98.59 | 98.69 |
| tabel:sdg4_amh_rinci | Papua Barat | 9100 | 2024 | Papua Barat Daya | 97.84 | 97.89 |
| tabel:sdg4_amh_rinci | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 84.22 | 98.37 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (133)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| tabel:sdg4_amh_rinci | Sumatera Selatan | 2009 | 94.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Kepulauan Riau | 2009 | 95.51 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | DI Yogyakarta | 2009 | 87.80 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Banten | 2009 | 89.46 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Tengah | 2009 | 87.02 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Tenggara | 2009 | 87.59 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2009 | 70.29 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | DI Yogyakarta | 2010 | 90.84 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Jawa Timur | 2010 | 88.34 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Banten | 2010 | 96.20 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Tengah | 2010 | 96.08 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Selatan | 2010 | 87.75 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Tenggara | 2010 | 91.85 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2010 | 88.48 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2010 | 68.27 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Jambi | 2011 | 95.52 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2011 | 83.24 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Selatan | 2011 | 88.07 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2011 | 87.61 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua Barat | 2011 | 92.41 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2011 | 64.08 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Sulawesi Selatan | 2012 | 88.73 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2012 | 88.79 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua Barat | 2012 | 94.74 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2012 | 65.69 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2013 | 90.79 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2013 | 67.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2014 | 86.96 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2014 | 70.78 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Timur | 2015 | 91.45 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Tengah | 2015 | 97.34 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Gorontalo | 2015 | 98.24 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2015 | 92.64 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2015 | 70.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua | 2016 | 71.02 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua | 2017 | 75.80 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua | 2018 | 76.79 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Bali | 2019 | 94.53 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2019 | 87.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Timur | 2019 | 93.24 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Kalimantan Utara | 2019 | 96.39 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2019 | 78.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Banten | 2020 | 97.88 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Bali | 2020 | 94.80 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2020 | 87.60 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Kalimantan Utara | 2020 | 96.66 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2020 | 93.17 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua Barat | 2020 | 97.52 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2020 | 77.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2021 | 87.39 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Timur | 2021 | 93.85 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua Barat | 2021 | 97.91 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2021 | 78.89 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2022 | 88.97 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2022 | 81.19 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | DI Yogyakarta | 2023 | 95.59 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2023 | 89.11 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Nusa Tenggara Timur | 2023 | 95.11 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Kalimantan Barat | 2023 | 94.79 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Selatan | 2023 | 93.83 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2023 | 94.33 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2023 | 84.22 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2024 | 89.83 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Kalimantan Utara | 2024 | 97.37 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Barat | 2024 | 95.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2024 | 98.37 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| tabel:sdg4_amh_rinci | Papua Tengah | 2024 | 84.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua Pegunungan | 2024 | 70.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Nusa Tenggara Barat | 2025 | 91.07 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Sulawesi Selatan | 2025 | 95.05 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg4_amh_rinci | Papua | 2025 | 98.39 | ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua Tengah | 2025 | 85.82 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg4_amh_rinci | Papua Pegunungan | 2025 | 68.32 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Riau | 2014 | 98.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Sumatera Selatan | 2014 | 98.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Bengkulu | 2014 | 97.52 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | DKI Jakarta | 2014 | 99.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Kalimantan Timur | 2014 | 98.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Utara | 2014 | 99.60 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Gorontalo | 2014 | 97.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Maluku Utara | 2014 | 98.36 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2014 | 70.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Timur | 2015 | 91.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Kalimantan Timur | 2015 | 98.69 | ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1458 | Sulawesi Utara | 2015 | 99.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Tengah | 2015 | 97.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Gorontalo | 2015 | 98.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Barat | 2015 | 92.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Maluku Utara | 2015 | 98.49 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2015 | 70.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua | 2016 | 71.02 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua | 2017 | 73.89 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Sulawesi Utara | 2018 | 99.87 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2018 | 76.79 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Bali | 2019 | 94.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Nusa Tenggara Barat | 2019 | 87.59 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Timur | 2019 | 93.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Kalimantan Utara | 2019 | 96.39 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2019 | 78.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Banten | 2020 | 97.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Bali | 2020 | 94.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Nusa Tenggara Barat | 2020 | 87.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Kalimantan Utara | 2020 | 96.66 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Barat | 2020 | 93.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua Barat | 2020 | 97.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2020 | 77.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Barat | 2021 | 87.39 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Timur | 2021 | 93.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua Barat | 2021 | 97.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2021 | 78.89 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Barat | 2022 | 88.97 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua | 2022 | 81.19 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | DI Yogyakarta | 2023 | 95.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Nusa Tenggara Barat | 2023 | 89.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Timur | 2023 | 95.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Kalimantan Barat | 2023 | 94.79 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Selatan | 2023 | 93.83 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Barat | 2023 | 94.33 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2023 | 84.22 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Nusa Tenggara Barat | 2024 | 89.83 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Kalimantan Utara | 2024 | 97.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Sulawesi Barat | 2024 | 95.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2024 | 98.37 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1458 | Papua Tengah | 2024 | 84.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua Pegunungan | 2024 | 70.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Aceh | 2025 | 98.92 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Jambi | 2025 | 97.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Kepulauan Riau | 2025 | 99.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Nusa Tenggara Barat | 2025 | 91.07 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Kalimantan Selatan | 2025 | 97.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var1458 | Papua | 2025 | 98.39 | ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua Tengah | 2025 | 85.82 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1458 | Papua Pegunungan | 2025 | 68.32 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1458 | 427 | 427 | 427 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
