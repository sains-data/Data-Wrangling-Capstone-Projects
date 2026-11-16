# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2014→2015 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2015→2016 | 33 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2016→2017 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2017→2018 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2018→2019 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2019→2020 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2020→2021 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 2022→2023 | 34 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2014→2015 | 33 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2015→2016 | 33 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2016→2017 | 33 | 0.03 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2017→2018 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2018→2019 | 33 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2019→2020 | 33 | 0.27 | 0.24 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2020→2021 | 33 | 0.30 | 0.27 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1304 | 2014→2015 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1304 | 2015→2016 | 33 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1304 | 2016→2017 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1304 | 2017→2018 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1304 | 2018→2023 | 33 | 0.00 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var588 | 2006→2011 | 31 | 0.39 | 0.42 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var588 | 2011→2013 | 32 | 0.34 | 0.34 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var588 | 2013→2018 | 33 | 0.24 | 0.55 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iku] | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iku] | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iku] | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iku] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iku] | 2023→2024 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=ika] | 2019→2020 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=ika] | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=ika] | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=ika] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=ika] | 2023→2024 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iktl] | 2019→2020 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iktl] | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iktl] | 2021→2022 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iktl] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2532 [komponen=iktl] | 2023→2024 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 18

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 6400 | 2021 | Kalimantan Utara | 19,504.80 | 12,734.90 |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua Barat | 9100 | 2023 | Papua Barat Daya | 9,803.80 | 5,942.00 |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 30,956.60 | 8,155.50 |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Timur | 6400 | 2021 | Kalimantan Utara | 63.00 | 60.90 |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Papua Barat | 9100 | 2023 | Papua Barat Daya | 93.10 | 93.50 |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 81.80 | 94.30 |
| var1304 | Kalimantan Timur | 6400 | 2023 | Kalimantan Utara | 19,504.80 | 12,576.50 |
| var1304 | Papua Barat | 9100 | 2023 | Papua Barat Daya | 9,624.90 | 5,942.00 |
| var1304 | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 31,076.90 | 8,155.50 |
| var588 | Riau | 1400 | 2011 | Kepulauan Riau | 2,415,015.00 | 840,658.00 |
| var588 | Kalimantan Timur | 6400 | 2013 | Kalimantan Utara | 318,836.00 | 910,820.00 |
| var2532 [komponen=iku] | Papua Barat | 9100 | 2023 | Papua Barat Daya | 95.79 | 96.22 |
| var2532 [komponen=iku] | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 95.32 | 95.87 |
| var2532 [komponen=ika] | Papua Barat | 9100 | 2023 | Papua Barat Daya | 62.00 | 59.52 |
| var2532 [komponen=ika] | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 55.07 | 54.73 |
| var2532 [komponen=iktl] | Kalimantan Timur | 6400 | 2020 | Kalimantan Utara | 87.94 | 80.85 |
| var2532 [komponen=iktl] | Papua Barat | 9100 | 2023 | Papua Barat Daya | 100.00 | 100.00 |
| var2532 [komponen=iktl] | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 100.00 | 100.00 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (313)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2014 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2014 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2014 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2014 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2015 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2015 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2015 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2015 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | DI Yogyakarta | 2016 | 3,194.00 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2016 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2016 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2016 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2016 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | DI Yogyakarta | 2017 | 319.40 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2017 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2017 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2017 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2017 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2018 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2018 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2018 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2018 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2019 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2019 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2019 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2019 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2020 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2020 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2020 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2020 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Sumatera Selatan | 2021 | 8,606.70 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2021 | 14,556.40 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2021 | 15,170.20 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2021 | 12,734.90 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua Barat | 2021 | 9,801.40 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2021 | 30,958.30 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Jambi | 2022 | 4,847.10 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Sumatera Selatan | 2022 | 8,606.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2022 | 14,555.30 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2022 | 15,169.70 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2022 | 12,660.70 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Sulawesi Selatan | 2022 | 4,457.50 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Maluku | 2022 | 4,629.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua Barat | 2022 | 9,803.80 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2022 | 30,956.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Aceh | 2023 | 5,659.30 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Jawa Tengah | 2023 | 3,463.70 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Bali | 2023 | 567.50 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Barat | 2023 | 14,572.10 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Tengah | 2023 | 15,192.90 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Timur | 2023 | 12,576.50 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Kalimantan Utara | 2023 | 6,959.20 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Sulawesi Tengah | 2023 | 6,089.30 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Sulawesi Selatan | 2023 | 4,433.70 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua Barat | 2023 | 5,942.00 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Papua | 2023 | 8,155.50 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Timur | 2014 | 26.40 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Tengah | 2014 | 51.50 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sumatera Selatan | 2015 | 13.90 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kepulauan Riau | 2015 | 30.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Tengah | 2015 | 29.50 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Barat | 2015 | 40.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Timur | 2015 | 41.70 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Tengah | 2015 | 51.50 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Timur | 2015 | 66.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Tengah | 2015 | 64.80 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Aceh | 2016 | 57.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Tengah | 2016 | 22.80 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Barat | 2016 | 46.50 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Timur | 2016 | 37.30 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Gorontalo | 2016 | 57.80 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Maluku Utara | 2016 | 62.20 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Riau | 2017 | 25.90 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sumatera Selatan | 2017 | 13.30 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Tengah | 2017 | 29.50 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | DI Yogyakarta | 2017 | 10.80 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Barat | 2017 | 40.10 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Timur | 2017 | 41.90 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Maluku Utara | 2017 | 64.50 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Tenggara | 2018 | 51.10 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sumatera Selatan | 2019 | 16.80 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Barat | 2019 | 21.60 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Tengah | 2019 | 19.20 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Timur | 2019 | 25.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Barat | 2019 | 44.40 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Timur | 2019 | 36.40 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Gorontalo | 2019 | 59.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Bengkulu | 2020 | 11.60 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Lampung | 2020 | 33.20 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | DKI Jakarta | 2020 | 16.30 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Barat | 2020 | 1.40 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | DI Yogyakarta | 2020 | 18.40 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jawa Timur | 2020 | 6.40 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Banten | 2020 | 24.70 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Bali | 2020 | 38.80 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Nusa Tenggara Barat | 2020 | 25.50 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Barat | 2020 | 68.10 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Tengah | 2020 | 38.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Selatan | 2020 | 61.00 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Utara | 2020 | 52.40 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Tengah | 2020 | 49.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Tenggara | 2020 | 17.20 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Gorontalo | 2020 | 43.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Sulawesi Barat | 2020 | 36.50 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Papua Barat | 2020 | 81.70 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Papua | 2020 | 93.20 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kepulauan Riau | 2022 | 39.70 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | DI Yogyakarta | 2022 | 7.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kalimantan Timur | 2022 | 62.40 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Jambi | 2023 | 30.60 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kepulauan Bangka Belitung | 2023 | 14.30 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Kepulauan Riau | 2023 | 40.60 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | Papua | 2023 | 94.30 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1304 | Kalimantan Barat | 2014 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2014 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Timur | 2014 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Papua | 2014 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Barat | 2015 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2015 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Timur | 2015 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Papua | 2015 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | DI Yogyakarta | 2016 | 3,194.00 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Kalimantan Barat | 2016 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2016 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Timur | 2016 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Papua | 2016 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | DI Yogyakarta | 2017 | 319.40 | perubahan | outlier | tandai, nilai tidak diubah |
| var1304 | Kalimantan Barat | 2017 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2017 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Timur | 2017 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Papua | 2017 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Barat | 2018 | 14,572.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2018 | 15,266.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Timur | 2018 | 19,504.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Papua | 2018 | 31,076.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Aceh | 2023 | 5,659.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sumatera Utara | 2023 | 7,076.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sumatera Barat | 2023 | 4,159.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Riau | 2023 | 8,851.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Jambi | 2023 | 4,855.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sumatera Selatan | 2023 | 8,616.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Bengkulu | 2023 | 2,012.40 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Lampung | 2023 | 3,364.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Kepulauan Bangka Belitung | 2023 | 1,668.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Kepulauan Riau | 2023 | 812.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | DKI Jakarta | 2023 | 66.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Jawa Barat | 2023 | 3,723.40 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Jawa Tengah | 2023 | 3,463.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Jawa Timur | 2023 | 4,873.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Banten | 2023 | 945.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Bali | 2023 | 567.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Nusa Tenggara Barat | 2023 | 2,003.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Nusa Tenggara Timur | 2023 | 4,735.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Kalimantan Barat | 2023 | 14,572.10 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Tengah | 2023 | 15,192.90 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1304 | Kalimantan Selatan | 2023 | 3,689.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Kalimantan Timur | 2023 | 12,576.50 | ke bawah + perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1304 | Sulawesi Utara | 2023 | 1,443.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sulawesi Tengah | 2023 | 6,089.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sulawesi Selatan | 2023 | 4,433.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sulawesi Tenggara | 2023 | 3,627.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Gorontalo | 2023 | 1,196.40 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Sulawesi Barat | 2023 | 1,656.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Maluku | 2023 | 4,633.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Maluku Utara | 2023 | 3,142.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1304 | Papua Barat | 2023 | 5,942.00 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1304 | Papua | 2023 | 8,155.50 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2532 [komponen=ika] | DI Yogyakarta | 2019 | 35.37 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Banten | 2019 | 43.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Papua | 2019 | 47.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Kepulauan Bangka Belitung | 2020 | 65.63 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Kepulauan Riau | 2020 | 50.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DKI Jakarta | 2020 | 42.73 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Jawa Barat | 2020 | 41.50 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DI Yogyakarta | 2020 | 50.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Bali | 2020 | 64.33 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Nusa Tenggara Barat | 2020 | 50.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Kalimantan Selatan | 2020 | 51.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Sulawesi Selatan | 2020 | 52.38 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Sulawesi Barat | 2020 | 52.44 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Aceh | 2021 | 57.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DKI Jakarta | 2021 | 44.19 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Jawa Barat | 2021 | 43.09 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DI Yogyakarta | 2021 | 45.73 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Nusa Tenggara Barat | 2021 | 45.10 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Kepulauan Riau | 2022 | 56.79 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DKI Jakarta | 2022 | 41.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | DI Yogyakarta | 2022 | 39.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Nusa Tenggara Barat | 2022 | 43.39 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Maluku | 2022 | 52.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DKI Jakarta | 2023 | 40.76 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | DI Yogyakarta | 2023 | 40.28 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Sulawesi Barat | 2023 | 58.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Aceh | 2024 | 63.25 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Jambi | 2024 | 55.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | Lampung | 2024 | 62.97 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=ika] | DKI Jakarta | 2024 | 41.22 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | DI Yogyakarta | 2024 | 42.94 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=ika] | Sulawesi Utara | 2024 | 58.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Sumatera Utara | 2019 | 52.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Riau | 2019 | 48.15 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jambi | 2019 | 60.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Sumatera Selatan | 2019 | 39.84 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Barat | 2019 | 38.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Nusa Tenggara Timur | 2019 | 63.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Tengah | 2019 | 76.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Selatan | 2019 | 46.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Timur | 2019 | 87.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Sulawesi Selatan | 2019 | 58.06 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Papua | 2019 | 99.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Sumatera Utara | 2020 | 47.69 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jambi | 2020 | 55.93 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Sumatera Selatan | 2020 | 42.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Barat | 2020 | 42.77 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Tengah | 2020 | 41.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Nusa Tenggara Timur | 2020 | 58.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Tengah | 2020 | 75.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Selatan | 2020 | 50.13 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kalimantan Timur | 2020 | 80.85 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2532 [komponen=iktl] | Maluku Utara | 2020 | 86.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jambi | 2021 | 52.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Lampung | 2021 | 33.56 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Barat | 2021 | 40.78 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | DI Yogyakarta | 2021 | 29.66 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Aceh | 2022 | 76.33 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Lampung | 2022 | 35.22 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kepulauan Riau | 2022 | 59.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | DKI Jakarta | 2022 | 27.07 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Barat | 2022 | 41.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Tengah | 2022 | 42.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | DI Yogyakarta | 2022 | 46.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Banten | 2022 | 38.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Bali | 2022 | 43.36 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Gorontalo | 2022 | 85.45 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kepulauan Riau | 2023 | 66.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Tengah | 2023 | 46.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Banten | 2023 | 43.13 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Gorontalo | 2023 | 80.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jambi | 2024 | 53.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Kepulauan Bangka Belitung | 2024 | 40.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Jawa Tengah | 2024 | 48.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | DI Yogyakarta | 2024 | 51.13 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Bali | 2024 | 46.87 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iktl] | Papua Selatan | 2024 | 92.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Sumatera Utara | 2019 | 86.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Sumatera Barat | 2019 | 89.45 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | DKI Jakarta | 2019 | 67.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2019 | 75.10 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | DI Yogyakarta | 2019 | 85.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Banten | 2019 | 74.98 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Gorontalo | 2019 | 86.88 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Papua Barat | 2019 | 92.64 | ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | DKI Jakarta | 2020 | 66.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2020 | 78.46 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Tengah | 2020 | 84.73 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Timur | 2020 | 84.06 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Banten | 2020 | 72.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Kalimantan Utara | 2020 | 94.23 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Gorontalo | 2020 | 93.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Papua Barat | 2020 | 94.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Papua | 2020 | 94.57 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | DKI Jakarta | 2021 | 66.52 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2021 | 79.34 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Tengah | 2021 | 84.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Timur | 2021 | 83.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Banten | 2021 | 74.14 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Papua Barat | 2021 | 95.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jambi | 2022 | 89.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Sumatera Selatan | 2022 | 89.10 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | DKI Jakarta | 2022 | 68.06 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2022 | 80.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Tengah | 2022 | 85.14 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Timur | 2022 | 84.28 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Banten | 2022 | 73.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Kalimantan Timur | 2022 | 87.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Papua Barat | 2022 | 95.79 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | DKI Jakarta | 2023 | 68.46 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2023 | 81.39 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Banten | 2023 | 66.67 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Kalimantan Selatan | 2023 | 92.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Aceh | 2024 | 92.81 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Sumatera Barat | 2024 | 92.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Kepulauan Riau | 2024 | 92.12 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | DKI Jakarta | 2024 | 72.59 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Barat | 2024 | 83.68 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Tengah | 2024 | 87.73 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Jawa Timur | 2024 | 88.09 | ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Banten | 2024 | 69.84 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2532 [komponen=iku] | Bali | 2024 | 92.12 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Nusa Tenggara Barat | 2024 | 93.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Sulawesi Selatan | 2024 | 93.36 | ke samping | outlier | tandai, nilai tidak diubah |
| var2532 [komponen=iku] | Papua Pegunungan | 2024 | 93.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Nusa Tenggara Timur | 2006 | 3,219,811.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Tengah | 2006 | 3,206,887.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Papua | 2006 | 2,970,400.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Riau | 2011 | 840,658.00 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var588 | Sumatera Selatan | 2011 | 3,886,062.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Nusa Tenggara Timur | 2011 | 1,041,688.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Barat | 2011 | 3,169,491.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Tengah | 2011 | 4,636,890.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Papua | 2011 | 1,076,699.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Riau | 2013 | 1,889,622.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Jambi | 2013 | 779,774.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Sumatera Selatan | 2013 | 312,864.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Jawa Timur | 2013 | 1,221,919.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Barat | 2013 | 859,575.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Tengah | 2013 | 5,144,704.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Kalimantan Timur | 2013 | 910,820.00 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var588 | Papua | 2013 | 2,239,229.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Sumatera Utara | 2018 | 1,338,810.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var588 | Riau | 2018 | 710,873.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var588 | Kalimantan Tengah | 2018 | 861,240.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var588 | Papua | 2018 | 538,523.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1304 | 627 | 627 | 627 | 0 | 0 | 0 | Ribu Hektar |
| var2532 | 1179 | 1179 | 1179 | 0 | 0 | 0 | (kosong) |
| var588 | 399 | 399 | 399 | 0 | 0 | 0 | Hektar |

## Kunci Silver kembar: 0
