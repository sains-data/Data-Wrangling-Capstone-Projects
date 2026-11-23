# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1402 | 2015→2016 | 34 | 0.00 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2016→2017 | 34 | 0.59 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2017→2018 | 34 | 0.09 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2018→2019 | 34 | 0.06 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2019→2020 | 34 | 0.09 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2020→2021 | 34 | 0.06 | 0.41 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2021→2022 | 34 | 0.71 | 0.09 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2022→2023 | 34 | 0.09 | 0.26 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2023→2024 | 34 | 0.03 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1402 | 2024→2025 | 38 | 0.11 | 0.13 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2279 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2279 | 2023→2024 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2279 | 2024→2025 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=dokter_umum] | 2016→2017 | 34 | 0.03 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=dokter_umum] | 2017→2018 | 34 | 0.38 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=perawat] | 2016→2017 | 34 | 0.68 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=perawat] | 2017→2018 | 34 | 0.35 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=bidan] | 2016→2017 | 34 | 0.79 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var1477 [profesi=bidan] | 2017→2018 | 34 | 0.47 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 4

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var1402 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 2.97 | 3.66 |
| var1402 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 2.66 | 3.02 |
| var2279 | Papua Barat | 9100 | 2023 | Papua Barat Daya | 70.09 | 70.98 |
| var2279 | Papua | 9400 | 2023 | Papua Selatan, Papua Tengah, Papua Pegunungan | 84.00 | 76.93 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (62)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1402 | Kalimantan Selatan | 2015 | 7.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Gorontalo | 2015 | 8.51 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Lampung | 2016 | 4.03 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Jawa Timur | 2016 | 4.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Gorontalo | 2016 | 6.23 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Kalimantan Utara | 2017 | 7.55 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Gorontalo | 2017 | 8.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Papua Barat | 2017 | 5.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Banten | 2018 | 5.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Kalimantan Utara | 2018 | 4.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Sulawesi Tengah | 2018 | 8.57 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Riau | 2019 | 4.86 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Gorontalo | 2020 | 6.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Riau | 2021 | 3.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Lampung | 2021 | 3.89 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Jawa Tengah | 2021 | 8.28 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | DI Yogyakarta | 2021 | 3.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Jawa Timur | 2021 | 6.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Sulawesi Utara | 2021 | 3.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Jambi | 2022 | 6.56 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Lampung | 2022 | 7.33 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Kepulauan Bangka Belitung | 2022 | 6.03 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | DKI Jakarta | 2022 | 1.56 | ke bawah + ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | DI Yogyakarta | 2022 | 7.48 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Kalimantan Timur | 2022 | 5.34 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Kalimantan Utara | 2022 | 8.90 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Sulawesi Selatan | 2022 | 7.15 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Sulawesi Tenggara | 2022 | 10.21 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Sulawesi Barat | 2022 | 8.50 | ke samping | patahan_seri | tandai; cari catatan metode |
| var1402 | Bali | 2023 | 2.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Nusa Tenggara Barat | 2023 | 9.04 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Kalimantan Barat | 2023 | 7.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var1402 | Gorontalo | 2023 | 8.72 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Papua | 2023 | 2.66 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Nusa Tenggara Barat | 2024 | 8.24 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Maluku | 2024 | 3.73 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Papua Tengah | 2024 | 1.39 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1402 | Bengkulu | 2025 | 4.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Kepulauan Riau | 2025 | 2.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var1402 | Papua | 2025 | 3.62 | ke samping | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=bidan] | Aceh | 2016 | 124.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1477 [profesi=bidan] | Bengkulu | 2016 | 133.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=bidan] | Aceh | 2017 | 233.00 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1477 [profesi=bidan] | Sulawesi Tenggara | 2017 | 139.00 | perubahan | patahan_seri | tandai; cari catatan metode |
| var1477 [profesi=bidan] | Aceh | 2018 | 213.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1477 [profesi=bidan] | Nusa Tenggara Barat | 2018 | 138.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=bidan] | Sulawesi Tengah | 2018 | 169.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Kepulauan Riau | 2017 | 17.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | DKI Jakarta | 2017 | 38.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | DI Yogyakarta | 2017 | 25.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Kalimantan Utara | 2017 | 37.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Sulawesi Tengah | 2017 | 11.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Maluku | 2017 | 11.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Papua Barat | 2017 | 15.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | DKI Jakarta | 2018 | 118.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | DI Yogyakarta | 2018 | 54.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=dokter_umum] | Nusa Tenggara Barat | 2018 | 51.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=perawat] | DKI Jakarta | 2017 | 223.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=perawat] | Kalimantan Utara | 2017 | 300.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=perawat] | Nusa Tenggara Barat | 2018 | 377.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var1477 [profesi=perawat] | Papua Barat | 2018 | 295.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2279 | Papua | 2023 | 76.93 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1402 | 393 | 393 | 393 | 0 | 0 | 0 | Persen |
| var1477 | 926 | 926 | 926 | 0 | 0 | 0 | (kosong) |
| var2279 | 152 | 152 | 152 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
