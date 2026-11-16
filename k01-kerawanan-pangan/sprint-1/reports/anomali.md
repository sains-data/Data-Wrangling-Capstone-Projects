# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1473 | 2017→2018 | 34 | 0.15 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2018→2019 | 34 | 0.12 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2019→2020 | 34 | 0.26 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2020→2021 | 34 | 0.21 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2021→2022 | 34 | 0.59 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2022→2023 | 34 | 0.00 | 0.35 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2023→2024 | 34 | 0.09 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1473 | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2017→2018 | 34 | 0.03 | 0.44 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2018→2019 | 34 | 0.00 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2019→2020 | 34 | 0.03 | 0.35 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2020→2021 | 34 | 0.18 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2021→2022 | 34 | 0.06 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2022→2023 | 34 | 0.03 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2023→2024 | 34 | 0.00 | 0.47 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1474 | 2024→2025 | 38 | 0.24 | 0.16 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1473 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 24.00 | 21.91 |
| var1473 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 35.63 | 26.03 |
| var1474 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 9.97 | 7.58 |
| var1474 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 8.58 | 9.71 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (114)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1473 | Bengkulu | 2017 | 12.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Nusa Tenggara Barat | 2017 | 8.71 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Sulawesi Tengah | 2017 | 4.60 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2017 | 26.57 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2017 | 34.05 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2017 | 27.22 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2017 | 34.27 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Nusa Tenggara Barat | 2018 | 5.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2018 | 34.17 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2018 | 30.75 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2018 | 21.18 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2018 | 38.35 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Kalimantan Barat | 2019 | 19.11 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2019 | 34.12 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2019 | 35.81 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2019 | 19.22 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2019 | 38.21 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Kalimantan Barat | 2020 | 19.92 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1473 | Sulawesi Selatan | 2020 | 10.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2020 | 35.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2020 | 35.48 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2020 | 23.09 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2020 | 31.49 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Aceh | 2021 | 6.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Bali | 2021 | 7.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2021 | 29.62 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2021 | 28.86 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2021 | 24.59 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2021 | 37.37 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Aceh | 2022 | 10.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Riau | 2022 | 15.12 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Kepulauan Bangka Belitung | 2022 | 15.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | DI Yogyakarta | 2022 | 13.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Jawa Timur | 2022 | 10.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Bali | 2022 | 7.72 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Kalimantan Tengah | 2022 | 12.83 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Kalimantan Utara | 2022 | 23.01 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Sulawesi Selatan | 2022 | 10.79 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Sulawesi Tenggara | 2022 | 17.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2022 | 31.68 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2022 | 30.71 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2022 | 29.38 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2022 | 36.18 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Kepulauan Bangka Belitung | 2023 | 13.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2023 | 30.27 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2023 | 29.56 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Barat | 2023 | 24.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2023 | 35.63 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku | 2024 | 31.66 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2024 | 28.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2024 | 26.03 | ke bawah + perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1473 | Papua Selatan | 2024 | 29.26 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Tengah | 2024 | 37.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Pegunungan | 2024 | 27.26 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Kalimantan Timur | 2025 | 8.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var1473 | Maluku | 2025 | 30.54 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Maluku Utara | 2025 | 27.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua | 2025 | 26.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Selatan | 2025 | 27.51 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Tengah | 2025 | 32.30 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1473 | Papua Pegunungan | 2025 | 28.72 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Aceh | 2017 | 11.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Sumatera Utara | 2017 | 9.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Sumatera Barat | 2017 | 11.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Jawa Barat | 2017 | 9.52 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Jawa Tengah | 2017 | 5.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | DI Yogyakarta | 2017 | 4.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Jawa Timur | 2017 | 5.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Banten | 2017 | 8.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2017 | 27.54 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Kalimantan Tengah | 2017 | 7.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Kalimantan Selatan | 2017 | 5.96 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Sulawesi Selatan | 2017 | 7.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Gorontalo | 2017 | 19.36 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Banten | 2018 | 7.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2018 | 21.32 | ke bawah + perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Sulawesi Selatan | 2018 | 6.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Gorontalo | 2018 | 10.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Papua | 2018 | 15.12 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2019 | 10.59 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Kalimantan Utara | 2019 | 3.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku Utara | 2019 | 14.99 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1474 | Papua | 2019 | 10.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | DI Yogyakarta | 2020 | 2.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2020 | 15.46 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Maluku Utara | 2020 | 12.55 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1474 | Kepulauan Riau | 2021 | 7.55 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Bali | 2021 | 4.51 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2021 | 15.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Gorontalo | 2021 | 9.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku Utara | 2021 | 10.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Kepulauan Riau | 2022 | 4.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2022 | 14.48 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Kalimantan Utara | 2022 | 6.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Gorontalo | 2022 | 5.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku | 2022 | 11.18 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1474 | Papua Barat | 2022 | 10.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Bali | 2023 | 2.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2023 | 14.68 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Kalimantan Utara | 2023 | 3.65 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku | 2023 | 10.26 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku Utara | 2023 | 12.18 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Papua Barat | 2023 | 9.97 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1474 | Papua | 2023 | 8.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Nusa Tenggara Timur | 2024 | 14.48 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Maluku | 2024 | 12.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Papua Selatan | 2024 | 18.13 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Nusa Tenggara Timur | 2025 | 13.69 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Kalimantan Selatan | 2025 | 1.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku | 2025 | 9.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Maluku Utara | 2025 | 7.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Papua Barat | 2025 | 11.29 | perubahan | outlier | tandai, nilai tidak diubah |
| var1474 | Papua Selatan | 2025 | 11.97 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1474 | Papua Pegunungan | 2025 | 6.72 | perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1473 | 323 | 323 | 323 | 0 | 0 | 0 | Persen |
| var1474 | 323 | 323 | 323 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
