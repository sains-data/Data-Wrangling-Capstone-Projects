# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1172 | 2015→2016 | 34 | 0.26 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2016→2017 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2019→2020 | 34 | 0.29 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2021→2022 | 34 | 0.00 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2022→2023 | 34 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1172 | 2024→2025 | 38 | 0.05 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2019→2020 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2023→2024 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2153 | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1172 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 25,695.00 | 28,214.00 |
| var1172 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 28,570.00 | 27,849.00 |
| var2153 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 58.55 | 62.87 |
| var2153 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 84.43 | 57.28 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (83)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1172 | Kepulauan Riau | 2015 | 18,863.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1172 | Banten | 2015 | 14,228.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1172 | Bali | 2015 | 11,038.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1172 | Kalimantan Timur | 2015 | 16,323.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2015 | 19,290.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2016 | 23,181.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Banten | 2016 | 21,033.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Sulawesi Tenggara | 2016 | 23,444.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Sulawesi Barat | 2016 | 11,730.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2016 | 22,961.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2017 | 23,826.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Banten | 2017 | 19,719.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Kalimantan Timur | 2017 | 21,864.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Kalimantan Utara | 2017 | 20,392.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Sulawesi Tenggara | 2017 | 16,604.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2017 | 25,657.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Kepulauan Riau | 2018 | 23,212.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | DKI Jakarta | 2018 | 25,238.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Papua | 2018 | 25,987.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2019 | 25,236.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Papua | 2019 | 24,984.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Kepulauan Bangka Belitung | 2020 | 15,763.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Maluku | 2020 | 26,198.00 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2020 | 32,138.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2021 | 30,662.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Kalimantan Utara | 2021 | 22,972.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Maluku | 2021 | 21,156.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua Barat | 2021 | 29,600.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2021 | 30,382.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2022 | 32,685.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Papua | 2022 | 24,097.00 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Kepulauan Riau | 2023 | 27,640.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | DKI Jakarta | 2023 | 42,354.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Maluku Utara | 2023 | 27,078.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua | 2023 | 28,570.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | DKI Jakarta | 2024 | 35,281.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Sulawesi Utara | 2024 | 23,831.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Maluku Utara | 2024 | 21,965.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Kepulauan Bangka Belitung | 2025 | 19,614.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | DKI Jakarta | 2025 | 39,018.92 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1172 | Sulawesi Utara | 2025 | 21,434.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Maluku Utara | 2025 | 26,731.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua Tengah | 2025 | 34,165.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var1172 | Papua Pegunungan | 2025 | 31,388.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var2153 | Kepulauan Riau | 2018 | 31.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | DKI Jakarta | 2018 | 30.15 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Jawa Barat | 2018 | 48.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kalimantan Utara | 2018 | 42.95 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kepulauan Bangka Belitung | 2019 | 46.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kepulauan Riau | 2019 | 29.57 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | DKI Jakarta | 2019 | 31.35 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Jawa Barat | 2019 | 50.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kalimantan Utara | 2019 | 46.69 | perubahan | outlier | tandai, nilai tidak diubah |
| var2153 | Gorontalo | 2019 | 58.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Papua | 2019 | 79.29 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Kepulauan Bangka Belitung | 2020 | 52.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kepulauan Riau | 2020 | 35.41 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | DKI Jakarta | 2020 | 38.22 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Jawa Tengah | 2020 | 62.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | DI Yogyakarta | 2020 | 57.41 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Sulawesi Tenggara | 2020 | 64.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Sulawesi Barat | 2020 | 72.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var2153 | Papua | 2020 | 79.92 | perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Kepulauan Riau | 2021 | 35.20 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | DKI Jakarta | 2021 | 38.26 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua | 2021 | 80.47 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Gorontalo | 2022 | 64.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Sulawesi Barat | 2022 | 77.25 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Papua | 2022 | 84.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Kepulauan Riau | 2023 | 33.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua | 2023 | 84.43 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Kepulauan Riau | 2024 | 31.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua Barat | 2024 | 62.87 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2153 | Papua | 2024 | 57.28 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var2153 | Papua Tengah | 2024 | 87.02 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua Pegunungan | 2024 | 95.76 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Aceh | 2025 | 63.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var2153 | Lampung | 2025 | 64.72 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Kepulauan Riau | 2025 | 34.25 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Nusa Tenggara Timur | 2025 | 68.44 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2153 | Papua | 2025 | 52.88 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua Tengah | 2025 | 84.72 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2153 | Papua Pegunungan | 2025 | 95.30 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1172 | 393 | 393 | 393 | 0 | 0 | 0 | Rupiah/Jam |
| var2153 | 288 | 288 | 288 | 0 | 0 | 0 | (kosong) |

## Kunci Silver kembar: 0
