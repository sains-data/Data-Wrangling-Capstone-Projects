# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| kejadian [jumlah] | 2010→2011 | 36 | 0.31 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2011→2012 | 36 | 0.44 | 0.28 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2012→2013 | 38 | 0.42 | 0.26 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2013→2014 | 37 | 0.22 | 0.46 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2014→2015 | 37 | 0.38 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2015→2016 | 38 | 0.58 | 0.21 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2016→2017 | 37 | 0.57 | 0.27 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2017→2018 | 38 | 0.45 | 0.26 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2018→2019 | 38 | 0.42 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2019→2020 | 38 | 0.55 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2020→2021 | 38 | 0.55 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2021→2022 | 37 | 0.08 | 0.68 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2022→2023 | 38 | 0.63 | 0.13 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2023→2024 | 38 | 0.34 | 0.58 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| kejadian [jumlah] | 2024→2025 | 38 | 0.63 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_meninggal [jumlah] | 2021→2022 | 34 | 0.32 | 0.53 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_meninggal [jumlah] | 2022→2024 | 33 | 0.55 | 0.39 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_meninggal [jumlah] | 2024→2025 | 34 | 0.65 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_hilang [jumlah] | 2021→2022 | 18 | 0.44 | 0.56 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_hilang [jumlah] | 2022→2024 | 21 | 0.52 | 0.48 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_hilang [jumlah] | 2024→2025 | 25 | 0.60 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_luka_sakit [jumlah] | 2021→2022 | 34 | 0.26 | 0.62 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_luka_sakit [jumlah] | 2022→2024 | 34 | 0.44 | 0.44 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_luka_sakit [jumlah] | 2024→2025 | 34 | 0.47 | 0.35 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| korban_mengungsi [jumlah] | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| korban_terdampak [jumlah] | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| korban_terdampak_mengungsi [jumlah] | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| korban_mengungsi_per_100rb [jumlah] | — | 0 |  |  | tidak dapat diuji | hanya 1 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| korban_meninggal_hilang_per_100rb [jumlah] | — | 0 |  |  | tidak dapat diuji | hanya 1 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| jumlah_penduduk | — | 0 |  |  | tidak dapat diuji | hanya 1 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 6

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| korban_meninggal [jumlah] | Papua Barat | 9100 | 2024 | Papua Barat Daya | 3.00 | 4.00 |
| korban_meninggal [jumlah] | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 8.00 | 2.00 |
| korban_hilang [jumlah] | Papua Barat | 9100 | 2024 | Papua Barat Daya | 0.00 | 0.00 |
| korban_hilang [jumlah] | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 0.00 | 0.00 |
| korban_luka_sakit [jumlah] | Papua Barat | 9100 | 2024 | Papua Barat Daya | 10.00 | 1.00 |
| korban_luka_sakit [jumlah] | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 17.00 | 0.00 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (119)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| kejadian [jumlah] | Kepulauan Bangka Belitung | 2010 | 0.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Riau | 2011 | 4.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Tengah | 2011 | 467.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Timur | 2011 | 278.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Utara | 2011 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Sulawesi Tenggara | 2011 | 13.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2011 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Pegunungan | 2011 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Bangka Belitung | 2012 | 0.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Sulawesi Tenggara | 2012 | 99.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Bangka Belitung | 2013 | 15.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Sulawesi Tenggara | 2013 | 29.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Barat Daya | 2013 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Selatan | 2014 | 13.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Riau | 2015 | 5.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Bali | 2015 | 6.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | DKI Jakarta | 2016 | 43.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Barat | 2016 | 306.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Tengah | 2016 | 600.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Timur | 2016 | 406.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Maluku | 2016 | 5.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua | 2016 | 1.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2016 | 0.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Lampung | 2017 | 9.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Tengah | 2017 | 1,071.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Utara | 2017 | 2.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2017 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Kepulauan Bangka Belitung | 2018 | 117.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Nusa Tenggara Timur | 2018 | 185.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Tengah | 2018 | 0.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Bangka Belitung | 2019 | 22.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | DKI Jakarta | 2019 | 6.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Barat | 2019 | 699.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Tengah | 2019 | 926.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Timur | 2019 | 622.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Nusa Tenggara Timur | 2019 | 38.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Utara | 2019 | 21.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Barat Daya | 2019 | 1.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2019 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Pegunungan | 2019 | 5.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Pegunungan | 2020 | 0.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Barat | 2021 | 1,358.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Barat Daya | 2021 | 0.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2021 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Tengah | 2021 | 4.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Pegunungan | 2021 | 3.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jambi | 2022 | 9.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kepulauan Riau | 2022 | 11.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Jawa Barat | 2022 | 825.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Barat Daya | 2022 | 8.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2022 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Tengah | 2022 | 0.00 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Pegunungan | 2022 | 1.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2023 | 2.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Tengah | 2023 | 1.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Pegunungan | 2023 | 2.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Sumatera Selatan | 2024 | 271.00 | ke samping | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Selatan | 2024 | 26.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Riau | 2025 | 396.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Kalimantan Selatan | 2025 | 276.00 | perubahan | outlier | tandai, nilai tidak diubah |
| kejadian [jumlah] | Papua Selatan | 2025 | 1.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| kejadian [jumlah] | Papua Tengah | 2025 | 4.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sumatera Utara | 2021 | 5.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Kepulauan Riau | 2021 | 6.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Jawa Timur | 2021 | 11.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Nusa Tenggara Timur | 2021 | 47.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sulawesi Barat | 2021 | 7.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sumatera Barat | 2022 | 3.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Kepulauan Riau | 2022 | 0.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Jawa Barat | 2022 | 12.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | DI Yogyakarta | 2022 | 2.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Jawa Timur | 2022 | 0.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Banten | 2022 | 2.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Nusa Tenggara Timur | 2022 | 2.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sulawesi Selatan | 2022 | 6.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sumatera Barat | 2024 | 21.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Jawa Barat | 2024 | 9.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Gorontalo | 2024 | 16.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Aceh | 2025 | 30.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Sumatera Utara | 2025 | 42.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Sumatera Barat | 2025 | 70.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_hilang [jumlah] | Gorontalo | 2025 | 0.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_hilang [jumlah] | Papua Pegunungan | 2025 | 15.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Sulawesi Barat | 2021 | 11,126.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Sumatera Barat | 2022 | 465.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Jawa Barat | 2022 | 7,913.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_luka_sakit [jumlah] | Sulawesi Barat | 2022 | 37.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Jawa Barat | 2024 | 10,645.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_luka_sakit [jumlah] | Gorontalo | 2024 | 235.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Aceh | 2025 | 5,419.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Jawa Barat | 2025 | 148.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| korban_luka_sakit [jumlah] | Gorontalo | 2025 | 1.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_luka_sakit [jumlah] | Papua Pegunungan | 2025 | 222.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_mengungsi [jumlah] | Kepulauan Bangka Belitung | 2025 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_mengungsi [jumlah] | Papua Selatan | 2025 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_mengungsi [jumlah] | Papua Tengah | 2025 | 0.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_mengungsi_per_100rb [jumlah] | Aceh | 2025 | 16,839.66 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Nusa Tenggara Timur | 2021 | 190.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Jawa Barat | 2022 | 645.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Nusa Tenggara Timur | 2022 | 5.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Sulawesi Barat | 2022 | 3.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Jawa Barat | 2024 | 51.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Kalimantan Selatan | 2024 | 0.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Gorontalo | 2024 | 29.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Aceh | 2025 | 566.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Sumatera Utara | 2025 | 384.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal [jumlah] | Sumatera Barat | 2025 | 270.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal_hilang_per_100rb [jumlah] | Aceh | 2025 | 10.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal_hilang_per_100rb [jumlah] | Sumatera Utara | 2025 | 2.70 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal_hilang_per_100rb [jumlah] | Sumatera Barat | 2025 | 5.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal_hilang_per_100rb [jumlah] | Papua Barat | 2025 | 3.40 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_meninggal_hilang_per_100rb [jumlah] | Papua Pegunungan | 2025 | 1.89 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_terdampak [jumlah] | Bali | 2024 | 7.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_terdampak [jumlah] | Bali | 2025 | 33,540.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_terdampak [jumlah] | Papua Pegunungan | 2025 | 164,982.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_terdampak_mengungsi [jumlah] | Papua Barat | 2021 | 479.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| korban_terdampak_mengungsi [jumlah] | Bali | 2022 | 23,492.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_terdampak_mengungsi [jumlah] | Kalimantan Selatan | 2022 | 103,051.00 | perubahan | outlier | tandai, nilai tidak diubah |
| korban_terdampak_mengungsi [jumlah] | Papua Barat | 2022 | 7,674.00 | perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

Tidak ada seri BPS dua format.

## Kunci Silver kembar: 0
