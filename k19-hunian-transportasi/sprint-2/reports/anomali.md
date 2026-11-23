# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1241 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2018→2019 | 34 | 0.00 | 0.97 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2020→2021 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1241 | 2024→2025 | 38 | 0.05 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2012 | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| var2013 | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| var2753 [arus=bongkar] | 2021→2022 | 36 | 0.25 | 0.17 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=bongkar] | 2022→2023 | 36 | 0.22 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=bongkar] | 2023→2024 | 36 | 0.22 | 0.31 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=bongkar] | 2024→2025 | 36 | 0.25 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=muat] | 2021→2022 | 36 | 0.22 | 0.17 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=muat] | 2022→2023 | 36 | 0.36 | 0.25 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=muat] | 2023→2024 | 36 | 0.36 | 0.17 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2753 [arus=muat] | 2024→2025 | 36 | 0.33 | 0.14 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=bongkar] | 2021→2022 | 38 | 0.21 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=bongkar] | 2022→2023 | 38 | 0.18 | 0.21 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=bongkar] | 2023→2024 | 38 | 0.53 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=bongkar] | 2024→2025 | 38 | 0.24 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=muat] | 2021→2022 | 38 | 0.18 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=muat] | 2022→2023 | 38 | 0.21 | 0.13 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=muat] | 2023→2024 | 38 | 0.39 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2754 [arus=muat] | 2024→2025 | 38 | 0.29 | 0.11 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

- `var1241` mulai 2019: var.note: sejak 2019 hunian layak memakai empat kriteria (luas per kapita >= 7,2 m2, air minum layak, sanitasi layak, ketahanan bangunan)

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 2

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1241 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 56.92 | 58.22 |
| var1241 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 29.01 | 62.15 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (202)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1241 | Nusa Tenggara Timur | 2015 | 56.40 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2015 | 49.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Nusa Tenggara Timur | 2016 | 59.67 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | Papua Barat | 2016 | 88.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2016 | 49.33 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Nusa Tenggara Timur | 2017 | 66.25 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Sulawesi Barat | 2017 | 88.77 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Maluku Utara | 2017 | 91.36 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2017 | 55.21 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Nusa Tenggara Timur | 2018 | 72.06 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2018 | 58.23 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2019 | 26.16 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1241 | DKI Jakarta | 2019 | 34.25 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1241 | Papua | 2019 | 26.19 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1241 | Kepulauan Bangka Belitung | 2020 | 30.64 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | DKI Jakarta | 2020 | 33.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2020 | 28.56 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2021 | 27.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | DKI Jakarta | 2021 | 40.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | DI Yogyakarta | 2021 | 85.15 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | Nusa Tenggara Timur | 2021 | 40.41 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2021 | 28.92 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2022 | 30.79 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | DKI Jakarta | 2022 | 36.23 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2022 | 27.28 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2023 | 32.57 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Riau | 2023 | 54.21 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2023 | 29.01 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2024 | 30.72 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kalimantan Utara | 2024 | 69.65 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2024 | 62.15 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1241 | Papua Tengah | 2024 | 26.79 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Papua Pegunungan | 2024 | 4.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Kepulauan Bangka Belitung | 2025 | 33.13 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Nusa Tenggara Timur | 2025 | 62.27 | perubahan | outlier | tandai, nilai tidak diubah |
| var1241 | Papua | 2025 | 58.41 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Papua Tengah | 2025 | 30.95 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1241 | Papua Pegunungan | 2025 | 9.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2012 | DKI Jakarta | 2020 | 74.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var2012 | Jawa Barat | 2020 | 63.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var2012 | Nusa Tenggara Timur | 2020 | 65.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var2012 | Kalimantan Tengah | 2020 | 48.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var2012 | Sulawesi Barat | 2020 | 61.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var2013 | DKI Jakarta | 2017 | 11.67 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2013 | Maluku | 2017 | 13.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2013 | Papua Barat | 2017 | 10.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2013 | Sulawesi Utara | 2020 | 13.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var2013 | Gorontalo | 2020 | 5.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var2013 | Maluku | 2020 | 15.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2013 | Papua | 2020 | 8.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Tengah | 2021 | 33,675,509.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Timur | 2021 | 34,487,630.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Banten | 2021 | 76,360,233.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Kalimantan Selatan | 2021 | 61,289,467.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jambi | 2022 | 7,181,376.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Lampung | 2022 | 11,002,519.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Kepulauan Riau | 2022 | 10,066,895.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | DKI Jakarta | 2022 | 14,859,079.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Tengah | 2022 | 20,710,203.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Timur | 2022 | 36,404,570.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Banten | 2022 | 66,775,592.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Nusa Tenggara Timur | 2022 | 2,649,232.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Kalimantan Selatan | 2022 | 67,835,734.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | DKI Jakarta | 2023 | 35,956,909.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Timur | 2023 | 44,458,445.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Banten | 2023 | 50,868,767.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Bali | 2023 | 14,560,403.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Kalimantan Selatan | 2023 | 11,878,759.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Riau | 2024 | 24,606,522.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jambi | 2024 | 3,525,914.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | DKI Jakarta | 2024 | 33,472,879.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Tengah | 2024 | 29,931,389.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Timur | 2024 | 33,849,628.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Banten | 2024 | 64,474,307.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Kalimantan Tengah | 2024 | 931,782.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Kalimantan Timur | 2024 | 31,965,124.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Sulawesi Utara | 2024 | 3,390,366.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Sulawesi Tengah | 2024 | 31,395,451.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Maluku Utara | 2024 | 9,024,289.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Lampung | 2025 | 14,476,599.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Jawa Timur | 2025 | 40,069,895.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Banten | 2025 | 64,726,193.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=bongkar] | Kalimantan Barat | 2025 | 17,696,542.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=bongkar] | Kalimantan Timur | 2025 | 48,400,770.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Jawa Timur | 2021 | 24,447,572.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Selatan | 2021 | 111,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Timur | 2021 | 63,246,049.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Riau | 2022 | 12,763,338.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Lampung | 2022 | 21,511,579.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Kepulauan Bangka Belitung | 2022 | 5,535,011.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Jawa Timur | 2022 | 21,798,505.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Banten | 2022 | 11,103,514.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Kalimantan Selatan | 2022 | 117,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Timur | 2022 | 63,289,363.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Sulawesi Tengah | 2022 | 13,259,869.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Maluku | 2022 | 1,303,260.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Papua Barat | 2022 | 8,920,653.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Lampung | 2023 | 12,794,521.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Kepulauan Riau | 2023 | 5,604,099.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Jawa Timur | 2023 | 33,413,566.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Barat | 2023 | 8,410,202.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Kalimantan Tengah | 2023 | 4,272,910.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Kalimantan Selatan | 2023 | 84,681,909.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Timur | 2023 | 81,116,607.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Utara | 2023 | 15,518,137.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Maluku Utara | 2023 | 14,040,627.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Papua Barat | 2023 | 393,560.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Lampung | 2024 | 9,413,173.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Jawa Timur | 2024 | 36,456,303.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Selatan | 2024 | 91,390,301.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Timur | 2024 | 105,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Sulawesi Tengah | 2024 | 18,945,166.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Lampung | 2025 | 13,321,003.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Jawa Timur | 2025 | 36,746,907.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Selatan | 2025 | 116,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Kalimantan Timur | 2025 | 111,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2753 [arus=muat] | Sulawesi Tengah | 2025 | 30,618,464.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Sulawesi Selatan | 2025 | 10,082,137.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Sulawesi Tenggara | 2025 | 25,997,481.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2753 [arus=muat] | Maluku Utara | 2025 | 34,809,308.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Sumatera Utara | 2021 | 42,234,410.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Banten | 2021 | 119,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Kalimantan Timur | 2021 | 36,240,286.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Selatan | 2021 | 50,803,801.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Papua Pegunungan | 2021 | 124,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sumatera Utara | 2022 | 35,923,629.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | DKI Jakarta | 2022 | 2,311,572.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Banten | 2022 | 114,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Kalimantan Timur | 2022 | 35,005,771.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Selatan | 2022 | 52,742,332.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Papua | 2022 | 16,747,053.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Papua Tengah | 2022 | 6,268,029.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Papua Pegunungan | 2022 | 84,213,686.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sumatera Utara | 2023 | 32,497,265.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Kepulauan Riau | 2023 | 25,460,342.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | DKI Jakarta | 2023 | 5,603,127.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Banten | 2023 | 100,199,541.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Bali | 2023 | 14,111,061.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Kalimantan Barat | 2023 | 19,108,362.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Kalimantan Timur | 2023 | 35,164,727.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Selatan | 2023 | 48,571,017.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Tenggara | 2023 | 3,311,696.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Papua | 2023 | 9,920,100.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Papua Tengah | 2023 | 11,358,194.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=bongkar] | Papua Pegunungan | 2023 | 123,130,032.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sumatera Utara | 2024 | 40,514,777.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Banten | 2024 | 117,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Kalimantan Timur | 2024 | 42,773,503.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Selatan | 2024 | 58,902,442.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Papua Pegunungan | 2024 | 129,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sumatera Utara | 2025 | 40,489,641.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Banten | 2025 | 114,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Kalimantan Timur | 2025 | 42,770,003.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Sulawesi Selatan | 2025 | 63,474,391.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=bongkar] | Papua Pegunungan | 2025 | 89,783,504.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | DKI Jakarta | 2021 | 67,980,973.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Jawa Timur | 2021 | 41,408,580.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Banten | 2021 | 181,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua | 2021 | 103,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Kepulauan Riau | 2022 | 13,220,162.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DKI Jakarta | 2022 | 19,509,830.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Jawa Barat | 2022 | 8,682,563.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Timur | 2022 | 42,565,385.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Banten | 2022 | 259,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Bali | 2022 | 12,388,676.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Kalimantan Timur | 2022 | 11,337,301.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Sulawesi Tengah | 2022 | 4,205,977.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Sulawesi Selatan | 2022 | 31,328,206.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua | 2022 | 126,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua Tengah | 2022 | 8,088,651.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Papua Pegunungan | 2022 | 10,697,755.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Kepulauan Riau | 2023 | 11,003,058.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DKI Jakarta | 2023 | 39,627,175.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Jawa Barat | 2023 | 4,403,760.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Tengah | 2023 | 11,234,132.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DI Yogyakarta | 2023 | 9,390,606.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Timur | 2023 | 40,921,248.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Banten | 2023 | 200,936,111.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Bali | 2023 | 9,647,668.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Nusa Tenggara Barat | 2023 | 3,570,293.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Kalimantan Timur | 2023 | 14,467,789.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Sulawesi Selatan | 2023 | 30,877,260.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua | 2023 | 121,462,646.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua Tengah | 2023 | 11,655,915.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DKI Jakarta | 2024 | 45,701,903.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Jawa Tengah | 2024 | 17,517,659.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DI Yogyakarta | 2024 | 13,688,249.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Timur | 2024 | 47,540,633.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Banten | 2024 | 236,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Sulawesi Selatan | 2024 | 37,950,976.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua | 2024 | 115,000,000.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua Tengah | 2024 | 19,680,538.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Kepulauan Riau | 2025 | 14,311,489.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | DKI Jakarta | 2025 | 50,015,794.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Jawa Barat | 2025 | 135,732.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Tengah | 2025 | 21,033,224.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Jawa Timur | 2025 | 50,493,528.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Banten | 2025 | 236,000,000.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Sulawesi Selatan | 2025 | 40,552,229.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua | 2025 | 88,960,996.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2754 [arus=muat] | Papua Selatan | 2025 | 2,789,626.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2754 [arus=muat] | Papua Tengah | 2025 | 24,497,976.00 | perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1241 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var2012 | 70 | 70 | 70 | 0 | 0 | 0 | (kosong) |
| var2013 | 70 | 70 | 70 | 0 | 0 | 0 | (kosong) |
| var2753 | 370 | 370 | 370 | 0 | 0 | 0 | KG |
| var2754 | 390 | 390 | 390 | 0 | 0 | 0 | KG |

## Kunci Silver kembar: 0
