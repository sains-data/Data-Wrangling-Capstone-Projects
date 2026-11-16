# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1311 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1311 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1311 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1311 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1311 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1311 | 2020 | 38 | 27 | 34 | 71.10 | 79.40 |
| var1311 | 2021 | 38 | 20 | 34 | 52.60 | 58.80 |
| var1311 | 2022 | 38 | 22 | 34 | 57.90 | 64.70 |
| var1311 | 2023 | 38 | 16 | 35 | 42.10 | 45.70 |
| var1311 | 2024 | 38 | 20 | 37 | 52.60 | 54.10 |
| var1312 | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1312 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1312 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1312 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1410 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1410 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1410 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1831 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1831 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1831 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1831 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1831 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1831 | 2020 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1831 | 2021 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1831 | 2022 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1831 | 2023 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2738 | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| var2738 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2740 | 2020 | 38 | 31 | 33 | 81.60 | 93.90 |
| var2740 | 2021 | 38 | 22 | 34 | 57.90 | 64.70 |
| var2740 | 2022 | 38 | 22 | 34 | 57.90 | 64.70 |
| var2740 | 2023 | 38 | 26 | 38 | 68.40 | 68.40 |
| var2740 | 2024 | 38 | 29 | 38 | 76.30 | 76.30 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | missing | terisi |
|---|---|---|---|---|
| var1311 | 4 | 32 | 69 | 275 |
| var1312 | 1 | 12 | 0 | 139 |
| var1410 | 4 | 32 | 0 | 382 |
| var1831 | 0 | 20 | 0 | 322 |
| var2738 | 1 | 8 | 0 | 67 |
| var2740 | 1 | 12 | 47 | 130 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1311 | 2015 | terisi |  |
| var1311 | 2016 | terisi |  |
| var1311 | 2017 | terisi |  |
| var1311 | 2018 | terisi |  |
| var1311 | 2019 | terisi |  |
| var1311 | 2020 | terisi |  |
| var1311 | 2021 | terisi |  |
| var1311 | 2022 | terisi |  |
| var1311 | 2023 | terisi |  |
| var1311 | 2024 | terisi |  |
| var1312 | 2014 | terisi |  |
| var1312 | 2017 | terisi |  |
| var1312 | 2020 | terisi |  |
| var1312 | 2025 | terisi |  |
| var2738 | 2014 | terisi |  |
| var2738 | 2020 | terisi |  |
| var2740 | 2020 | terisi |  |
| var2740 | 2021 | terisi |  |
| var2740 | 2022 | terisi |  |
| var2740 | 2023 | terisi |  |
| var2740 | 2024 | terisi |  |
| var1410 | 2015 | terisi |  |
| var1410 | 2016 | terisi |  |
| var1410 | 2017 | terisi |  |
| var1410 | 2018 | terisi |  |
| var1410 | 2019 | terisi |  |
| var1410 | 2020 | terisi |  |
| var1410 | 2021 | terisi |  |
| var1410 | 2022 | terisi |  |
| var1410 | 2023 | terisi |  |
| var1410 | 2024 | terisi |  |
| var1410 | 2025 | terisi |  |
| var1831 | 2015 | terisi |  |
| var1831 | 2016 | terisi |  |
| var1831 | 2017 | terisi |  |
| var1831 | 2018 | terisi |  |
| var1831 | 2019 | terisi |  |
| var1831 | 2020 | terisi |  |
| var1831 | 2021 | terisi |  |
| var1831 | 2022 | terisi |  |
| var1831 | 2023 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1311 | nasional | 2015 | 2024 | 10 |
| var1311 | provinsi | 2015 | 2024 | 10 |
| var1312 | nasional | 2014 | 2025 | 4 |
| var1312 | provinsi | 2014 | 2025 | 4 |
| var1410 | nasional | 2015 | 2025 | 11 |
| var1410 | provinsi | 2015 | 2025 | 11 |
| var1831 | nasional | 2015 | 2023 | 9 |
| var1831 | provinsi | 2015 | 2023 | 9 |
| var2738 | nasional | 2014 | 2020 | 2 |
| var2738 | provinsi | 2014 | 2020 | 2 |
| var2740 | nasional | 2020 | 2024 | 5 |
| var2740 | provinsi | 2020 | 2024 | 5 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
