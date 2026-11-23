# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1360 | 2015→2016 | 34 | 0.09 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2016→2017 | 34 | 0.18 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2017→2018 | 34 | 0.06 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2018→2019 | 34 | 0.09 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2019→2020 | 34 | 0.09 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2020→2021 | 34 | 0.06 | 0.26 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2021→2022 | 34 | 0.03 | 0.35 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2022→2023 | 34 | 0.06 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2023→2024 | 34 | 0.03 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1360 | 2024→2025 | 38 | 0.11 | 0.42 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2015→2016 | 34 | 0.32 | 0.26 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2016→2017 | 34 | 0.32 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2017→2018 | 34 | 0.38 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2018→2019 | 34 | 0.15 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2019→2020 | 34 | 0.35 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2020→2021 | 34 | 0.15 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2021→2022 | 34 | 0.15 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2022→2023 | 34 | 0.21 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2023→2024 | 34 | 0.18 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2003 | 2024→2025 | 36 | 0.19 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1360 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 7.86 | 4.90 |
| var1360 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 11.19 | 2.70 |
| var2003 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 34.86 | 31.74 |
| var2003 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 45.39 | 35.76 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (49)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1360 | Sulawesi Barat | 2016 | 15.67 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Maluku Utara | 2017 | 17.21 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | DI Yogyakarta | 2018 | 6.20 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kalimantan Selatan | 2018 | 17.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kepulauan Bangka Belitung | 2020 | 18.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kepulauan Riau | 2020 | 7.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kalimantan Selatan | 2020 | 16.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kepulauan Bangka Belitung | 2022 | 7.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Sulawesi Barat | 2022 | 11.70 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Maluku Utara | 2023 | 7.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Sumatera Selatan | 2024 | 8.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Kepulauan Riau | 2024 | 2.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Gorontalo | 2024 | 7.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Papua Barat | 2024 | 4.90 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1360 | Papua | 2024 | 2.70 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var1360 | Sumatera Selatan | 2025 | 8.09 | ke samping | outlier | tandai, nilai tidak diubah |
| var1360 | Nusa Tenggara Barat | 2025 | 11.31 | ke samping | outlier | tandai, nilai tidak diubah |
| var1360 | Gorontalo | 2025 | 6.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var1360 | Papua Barat | 2025 | 12.25 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Papua Barat Daya | 2025 | 6.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var1360 | Papua | 2025 | 1.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var1360 | Papua Tengah | 2025 | 2.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Tenggara | 2015 | 37.60 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Gorontalo | 2015 | 43.28 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Barat | 2015 | 21.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Selatan | 2016 | 10.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Kalimantan Barat | 2017 | 18.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Gorontalo | 2019 | 45.82 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Maluku Utara | 2019 | 20.62 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Utara | 2020 | 47.93 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Gorontalo | 2020 | 50.43 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | DI Yogyakarta | 2021 | 25.84 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Utara | 2021 | 42.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Gorontalo | 2021 | 39.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Maluku | 2021 | 37.72 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Jambi | 2022 | 45.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Kepulauan Riau | 2022 | 38.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Sumatera Barat | 2023 | 27.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Sumatera Selatan | 2024 | 37.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Kepulauan Bangka Belitung | 2024 | 41.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Utara | 2024 | 49.42 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Maluku | 2024 | 50.26 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Papua Pegunungan | 2024 | 13.74 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Sumatera Barat | 2025 | 45.89 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Kepulauan Bangka Belitung | 2025 | 26.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var2003 | Kalimantan Barat | 2025 | 34.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Utara | 2025 | 51.72 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2003 | Sulawesi Barat | 2025 | 41.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var2003 | Maluku Utara | 2025 | 45.01 | ke samping | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1360 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var2003 | 391 | 391 | 391 | 0 | 0 | 0 | (kosong) |

## Kunci Silver kembar: 0
