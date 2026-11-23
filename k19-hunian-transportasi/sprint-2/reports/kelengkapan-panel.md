# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1241 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1241 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1241 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2012 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2012 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2013 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2013 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2753 [arus=bongkar] | 2021 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=bongkar] | 2022 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=bongkar] | 2023 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=bongkar] | 2024 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=bongkar] | 2025 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=muat] | 2021 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=muat] | 2022 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=muat] | 2023 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=muat] | 2024 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2753 [arus=muat] | 2025 | 38 | 36 | 36 | 94.70 | 100.00 |
| var2754 [arus=bongkar] | 2021 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=bongkar] | 2022 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=bongkar] | 2023 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=bongkar] | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=bongkar] | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=muat] | 2021 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=muat] | 2022 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=muat] | 2023 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=muat] | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2754 [arus=muat] | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| var1241 | 4 | 32 | 382 | 0 |
| var2012 | 0 | 8 | 68 | 0 |
| var2013 | 0 | 8 | 68 | 0 |
| var2753 [arus=bongkar] | 0 | 2 | 180 | 8 |
| var2753 [arus=muat] | 0 | 2 | 180 | 8 |
| var2754 [arus=bongkar] | 0 | 0 | 190 | 0 |
| var2754 [arus=muat] | 0 | 0 | 190 | 0 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1241 | 2015 | terisi |  |
| var1241 | 2016 | terisi |  |
| var1241 | 2017 | terisi |  |
| var1241 | 2018 | terisi |  |
| var1241 | 2019 | terisi |  |
| var1241 | 2020 | terisi |  |
| var1241 | 2021 | terisi |  |
| var1241 | 2022 | terisi |  |
| var1241 | 2023 | terisi |  |
| var1241 | 2024 | terisi |  |
| var1241 | 2025 | terisi |  |
| var2012 | 2017 | terisi |  |
| var2012 | 2020 | terisi |  |
| var2013 | 2017 | terisi |  |
| var2013 | 2020 | terisi |  |
| var2753 [arus=bongkar] | 2021 | terisi |  |
| var2753 [arus=bongkar] | 2022 | terisi |  |
| var2753 [arus=bongkar] | 2023 | terisi |  |
| var2753 [arus=bongkar] | 2024 | terisi |  |
| var2753 [arus=bongkar] | 2025 | terisi |  |
| var2753 [arus=muat] | 2021 | terisi |  |
| var2753 [arus=muat] | 2022 | terisi |  |
| var2753 [arus=muat] | 2023 | terisi |  |
| var2753 [arus=muat] | 2024 | terisi |  |
| var2753 [arus=muat] | 2025 | terisi |  |
| var2754 [arus=bongkar] | 2021 | terisi |  |
| var2754 [arus=bongkar] | 2022 | terisi |  |
| var2754 [arus=bongkar] | 2023 | terisi |  |
| var2754 [arus=bongkar] | 2024 | terisi |  |
| var2754 [arus=bongkar] | 2025 | terisi |  |
| var2754 [arus=muat] | 2021 | terisi |  |
| var2754 [arus=muat] | 2022 | terisi |  |
| var2754 [arus=muat] | 2023 | terisi |  |
| var2754 [arus=muat] | 2024 | terisi |  |
| var2754 [arus=muat] | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1241 | nasional | 2015 | 2025 | 11 |
| var1241 | provinsi | 2015 | 2025 | 11 |
| var2012 | nasional | 2017 | 2020 | 2 |
| var2012 | provinsi | 2017 | 2020 | 2 |
| var2013 | nasional | 2017 | 2020 | 2 |
| var2013 | provinsi | 2017 | 2020 | 2 |
| var2753 [arus=bongkar] | nasional | 2021 | 2025 | 5 |
| var2753 [arus=bongkar] | provinsi | 2021 | 2025 | 5 |
| var2753 [arus=muat] | nasional | 2021 | 2025 | 5 |
| var2753 [arus=muat] | provinsi | 2021 | 2025 | 5 |
| var2754 [arus=bongkar] | nasional | 2021 | 2025 | 5 |
| var2754 [arus=bongkar] | provinsi | 2021 | 2025 | 5 |
| var2754 [arus=muat] | nasional | 2021 | 2025 | 5 |
| var2754 [arus=muat] | provinsi | 2021 | 2025 | 5 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
