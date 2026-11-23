# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1360 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1360 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1360 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2003 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2003 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2003 | 2025 | 38 | 36 | 38 | 94.70 | 94.70 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | missing | terisi |
|---|---|---|---|---|
| var1360 | 4 | 32 | 0 | 382 |
| var2003 | 4 | 32 | 2 | 380 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1360 | 2015 | terisi |  |
| var1360 | 2016 | terisi |  |
| var1360 | 2017 | terisi |  |
| var1360 | 2018 | terisi |  |
| var1360 | 2019 | terisi |  |
| var1360 | 2020 | terisi |  |
| var1360 | 2021 | terisi |  |
| var1360 | 2022 | terisi |  |
| var1360 | 2023 | terisi |  |
| var1360 | 2024 | terisi |  |
| var1360 | 2025 | terisi |  |
| var2003 | 2015 | terisi |  |
| var2003 | 2016 | terisi |  |
| var2003 | 2017 | terisi |  |
| var2003 | 2018 | terisi |  |
| var2003 | 2019 | terisi |  |
| var2003 | 2020 | terisi |  |
| var2003 | 2021 | terisi |  |
| var2003 | 2022 | terisi |  |
| var2003 | 2023 | terisi |  |
| var2003 | 2024 | terisi |  |
| var2003 | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1360 | nasional | 2015 | 2025 | 11 |
| var1360 | provinsi | 2015 | 2025 | 11 |
| var2003 | nasional | 2015 | 2025 | 11 |
| var2003 | provinsi | 2015 | 2025 | 11 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
