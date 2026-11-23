# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1311 | 2015→2016 | 34 | 0.56 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2016→2017 | 34 | 0.68 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2017→2018 | 34 | 0.26 | 0.44 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2018→2019 | 34 | 0.15 | 0.62 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2019→2020 | 27 | 0.30 | 0.56 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2020→2021 | 19 | 0.05 | 0.79 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2021→2022 | 18 | 0.28 | 0.22 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2022→2023 | 15 | 0.27 | 0.60 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1311 | 2023→2024 | 14 | 0.71 | 0.21 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1312 | 2014→2017 | 33 | 0.00 | 0.76 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1312 | 2017→2020 | 34 | 0.44 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1312 | 2020→2025 | 34 | 0.85 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var2738 | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| var2740 | 2020→2021 | 20 | 0.40 | 0.25 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2740 | 2021→2022 | 15 | 0.40 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2740 | 2022→2023 | 16 | 0.56 | 0.31 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2740 | 2023→2024 | 22 | 0.27 | 0.45 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2017→2018 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2018→2019 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2021→2022 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1410 | 2024→2025 | 38 | 0.05 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2018→2019 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1831 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

- `var1311` mulai 2017: var.note: mulai angka 2017 (Susenas 2018) rujukan kejadian 1 Januari–31 Desember tahun itu; periode berarti tahun kejadian, bukan tahun survei

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 11

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1311 | Papua | 9400 | 2024 | Papua Pegunungan | 0.18 | 0.18 |
| var1312 | Kalimantan Timur | 6400 | 2017 | Kalimantan Utara | 76.86 | 55.42 |
| var1312 | Papua Barat | 9100 | 2025 | Papua Barat Daya | 58.40 | 82.13 |
| var1312 | Papua | 9400 | 2025 | Papua Selatan, Papua Tengah, Papua Pegunungan | 69.31 | 82.58 |
| var2738 | Kalimantan Timur | 6400 | 2020 | Kalimantan Utara | 51.24 | 51.03 |
| var2740 | Papua Barat | 9100 | 2023 | Papua Barat Daya | 41.17 | 22.55 |
| var2740 | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah | 73.04 | 53.10 |
| var1410 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 60.35 | 64.18 |
| var1410 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 47.60 | 68.71 |
| var1831 | Papua Barat | 9100 | 2020 | Papua Barat Daya | 75.05 | 77.36 |
| var1831 | Papua | 9400 | 2020 | Papua Selatan, Papua Tengah, Papua Pegunungan | 45.88 | 50.40 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (115)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1311 | Papua Barat | 2015 | 0.18 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Sumatera Utara | 2016 | 0.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Kepulauan Bangka Belitung | 2016 | 0.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Kepulauan Riau | 2016 | 0.19 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1311 | Gorontalo | 2016 | 0.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Papua Barat | 2016 | 0.21 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Papua | 2016 | 0.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Kepulauan Riau | 2017 | 0.10 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Jawa Barat | 2017 | 0.09 | ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | DI Yogyakarta | 2017 | 0.18 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Nusa Tenggara Barat | 2017 | 0.20 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Sulawesi Tengah | 2017 | 0.23 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Sulawesi Tenggara | 2017 | 0.25 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Gorontalo | 2017 | 0.13 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Maluku Utara | 2017 | 0.19 | perubahan + ke samping | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Papua Barat | 2017 | 0.27 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Papua | 2017 | 0.30 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var1311 | Riau | 2018 | 0.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var1311 | Sulawesi Tenggara | 2018 | 0.07 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Maluku Utara | 2018 | 0.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Papua Barat | 2018 | 0.25 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Papua | 2018 | 0.23 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Papua Barat | 2019 | 0.29 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Maluku | 2020 | 0.17 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Papua Barat | 2020 | 0.25 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Maluku | 2021 | 0.06 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1311 | Papua Barat | 2021 | 0.12 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Papua Barat | 2022 | 0.07 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Bengkulu | 2023 | 0.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Maluku | 2023 | 0.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var1311 | Papua | 2023 | 0.18 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1311 | Papua | 2024 | 0.18 | ke bawah | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1312 | Kepulauan Riau | 2017 | 71.43 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1312 | Bali | 2017 | 73.43 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1312 | Papua | 2017 | 58.69 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1312 | DKI Jakarta | 2020 | 40.17 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1312 | DKI Jakarta | 2025 | 81.52 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1312 | Bali | 2025 | 86.74 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1312 | Gorontalo | 2025 | 69.02 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var1312 | Papua Barat Daya | 2025 | 69.15 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var1312 | Papua Tengah | 2025 | 53.50 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var1410 | Nusa Tenggara Timur | 2016 | 30.71 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Aceh | 2017 | 78.10 | perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Kepulauan Riau | 2017 | 86.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2017 | 31.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Nusa Tenggara Timur | 2018 | 32.89 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua | 2018 | 29.53 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2019 | 34.12 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Maluku | 2019 | 51.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Papua | 2019 | 40.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2020 | 36.77 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Sulawesi Tengah | 2020 | 66.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Papua | 2020 | 42.02 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2021 | 39.34 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Maluku | 2021 | 53.08 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua Barat | 2021 | 54.49 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua | 2021 | 36.79 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2022 | 46.36 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua Barat | 2022 | 60.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua | 2022 | 50.26 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2023 | 51.10 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Maluku | 2023 | 66.32 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua Barat | 2023 | 60.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua | 2023 | 47.60 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Nusa Tenggara Timur | 2024 | 57.29 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua | 2024 | 68.71 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1410 | Papua Selatan | 2024 | 47.27 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua Pegunungan | 2024 | 17.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Nusa Tenggara Timur | 2025 | 55.24 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua | 2025 | 70.61 | ke samping | outlier | tandai, nilai tidak diubah |
| var1410 | Papua Selatan | 2025 | 57.77 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1410 | Papua Tengah | 2025 | 62.03 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1410 | Papua Pegunungan | 2025 | 28.19 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | DI Yogyakarta | 2015 | 95.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var1831 | Papua | 2015 | 38.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Bengkulu | 2016 | 86.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var1831 | Nusa Tenggara Barat | 2016 | 73.25 | perubahan | outlier | tandai, nilai tidak diubah |
| var1831 | Nusa Tenggara Timur | 2016 | 53.66 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2016 | 40.54 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2017 | 56.65 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2017 | 44.50 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Sumatera Barat | 2018 | 85.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var1831 | Kepulauan Riau | 2018 | 92.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var1831 | Nusa Tenggara Barat | 2018 | 79.65 | perubahan | outlier | tandai, nilai tidak diubah |
| var1831 | Papua | 2018 | 36.32 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2019 | 61.08 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2019 | 45.88 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2020 | 63.33 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Sulawesi Tengah | 2020 | 83.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var1831 | Papua Barat Daya | 2020 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2020 | 50.40 | ke bawah | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1831 | Papua Selatan | 2020 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Tengah | 2020 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Pegunungan | 2020 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2021 | 65.66 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Barat Daya | 2021 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2021 | 45.19 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Selatan | 2021 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Tengah | 2021 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Pegunungan | 2021 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2022 | 69.47 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Kalimantan Timur | 2022 | 95.24 | ke samping | outlier | tandai, nilai tidak diubah |
| var1831 | Papua Barat Daya | 2022 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2022 | 53.77 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Selatan | 2022 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Tengah | 2022 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Pegunungan | 2022 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Nusa Tenggara Timur | 2023 | 73.94 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Kalimantan Timur | 2023 | 96.38 | ke samping | outlier | tandai, nilai tidak diubah |
| var1831 | Papua Barat Daya | 2023 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua | 2023 | 50.85 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Selatan | 2023 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Tengah | 2023 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1831 | Papua Pegunungan | 2023 | 0.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2738 | Nusa Tenggara Timur | 2020 | 81.66 | ke bawah | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1311 | 285 | 285 | 285 | 0 | 0 | 0 | Persen |
| var1312 | 143 | 143 | 143 | 0 | 0 | 0 | Persen |
| var1410 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var1831 | 331 | 331 | 331 | 0 | 0 | 0 | Persen |
| var2738 | 69 | 69 | 69 | 0 | 0 | 0 | Persen |
| var2740 | 135 | 135 | 135 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
