# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1186 | 2015→2016 | 34 | 0.06 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2016→2017 | 34 | 0.03 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2017→2018 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2018→2019 | 34 | 0.03 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2019→2020 | 34 | 0.21 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2020→2021 | 34 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2021→2022 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2022→2023 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2023→2024 | 34 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1186 | 2024→2025 | 38 | 0.00 | 0.08 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2658 | 2020→2021 | 34 | 0.03 | 0.41 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2658 | 2021→2022 | 34 | 0.15 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2658 | 2022→2023 | 34 | 0.00 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2658 | 2023→2024 | 32 | 0.62 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2658 | 2024→2025 | 34 | 0.12 | 0.44 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1186 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 27.98 | 26.93 |
| var1186 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 25.06 | 27.85 |
| var2658 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 2.20 | 2.51 |
| var2658 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 2.75 | 1.41 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (72)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1186 | Lampung | 2015 | 28.26 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Tengah | 2015 | 26.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Kalimantan Timur | 2016 | 27.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Tengah | 2016 | 18.99 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Tenggara | 2016 | 16.64 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Barat | 2016 | 26.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | DI Yogyakarta | 2017 | 11.13 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2017 | 9.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Kalimantan Timur | 2017 | 20.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Utara | 2017 | 29.78 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1186 | Kepulauan Riau | 2018 | 19.74 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | DI Yogyakarta | 2018 | 12.52 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2018 | 8.59 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Sulawesi Utara | 2018 | 29.73 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1186 | DKI Jakarta | 2019 | 15.41 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1186 | DI Yogyakarta | 2019 | 9.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2019 | 9.40 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Kalimantan Utara | 2019 | 21.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Utara | 2019 | 28.10 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1186 | DI Yogyakarta | 2020 | 12.71 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2020 | 14.90 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | DI Yogyakarta | 2021 | 9.89 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | DI Yogyakarta | 2022 | 10.70 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2022 | 11.32 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Kalimantan Tengah | 2022 | 26.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Sulawesi Utara | 2022 | 33.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | DI Yogyakarta | 2023 | 10.89 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Bali | 2023 | 10.03 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Maluku | 2023 | 35.38 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Papua | 2023 | 25.06 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Bali | 2024 | 7.26 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Nusa Tenggara Barat | 2024 | 15.44 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Maluku | 2024 | 29.43 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Papua | 2024 | 27.85 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1186 | Lampung | 2025 | 18.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Jawa Tengah | 2025 | 16.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Jawa Timur | 2025 | 16.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Bali | 2025 | 5.33 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1186 | Sulawesi Selatan | 2025 | 19.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var1186 | Papua Tengah | 2025 | 21.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var1186 | Papua Pegunungan | 2025 | 11.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Aceh | 2020 | 1.22 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Sumatera Utara | 2020 | 4.25 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Kepulauan Bangka Belitung | 2020 | 2.39 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Jawa Timur | 2020 | 1.77 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Sulawesi Tenggara | 2020 | 6.16 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2658 | Papua Barat | 2020 | 3.41 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Banten | 2021 | 0.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Kepulauan Riau | 2022 | 1.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Sulawesi Tenggara | 2022 | 2.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Gorontalo | 2022 | 4.53 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Kepulauan Riau | 2023 | 1.61 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Kalimantan Barat | 2023 | 1.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Kalimantan Utara | 2023 | 2.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Gorontalo | 2023 | 3.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Maluku | 2023 | 1.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Kepulauan Bangka Belitung | 2024 | 1.10 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Kepulauan Riau | 2024 | 1.15 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Jawa Barat | 2024 | 1.45 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Banten | 2024 | 1.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Bali | 2024 | 2.19 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Nusa Tenggara Barat | 2024 | 4.09 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Nusa Tenggara Timur | 2024 | 5.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Sulawesi Tenggara | 2024 | 5.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Gorontalo | 2024 | 3.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Maluku | 2024 | 3.82 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2658 | Maluku Utara | 2024 | 3.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Papua | 2024 | 1.41 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2658 | Nusa Tenggara Timur | 2025 | 4.74 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2658 | Sulawesi Tenggara | 2025 | 3.44 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Maluku | 2025 | 1.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var2658 | Papua Tengah | 2025 | 5.43 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1186 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var2658 | 212 | 212 | 212 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
