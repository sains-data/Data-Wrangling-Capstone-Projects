# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1161 | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1161 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1161 | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1161 | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1161 | 2015 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1161 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2024 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1161 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1214 | 2010 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2011 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2012 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2013 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2014 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1214 | 2023 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1344 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1344 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2755 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2755 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi |
|---|---|---|---|
| var1161 | 11 | 50 | 509 |
| var1214 | 0 | 52 | 480 |
| var1344 | 4 | 32 | 306 |
| var2755 | 4 | 20 | 280 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1161 | 2011 | terisi |  |
| var1161 | 2012 | terisi |  |
| var1161 | 2013 | terisi |  |
| var1161 | 2014 | terisi |  |
| var1161 | 2015 | terisi |  |
| var1161 | 2016 | terisi |  |
| var1161 | 2017 | terisi |  |
| var1161 | 2018 | terisi |  |
| var1161 | 2019 | terisi |  |
| var1161 | 2020 | terisi |  |
| var1161 | 2021 | terisi |  |
| var1161 | 2022 | terisi |  |
| var1161 | 2023 | terisi |  |
| var1161 | 2024 | terisi |  |
| var1161 | 2025 | terisi |  |
| var1344 | 2015 | terisi |  |
| var1344 | 2016 | terisi |  |
| var1344 | 2017 | terisi |  |
| var1344 | 2018 | terisi |  |
| var1344 | 2019 | terisi |  |
| var1344 | 2020 | terisi |  |
| var1344 | 2021 | terisi |  |
| var1344 | 2022 | terisi |  |
| var1344 | 2023 | terisi |  |
| var1214 | 2010 | terisi |  |
| var1214 | 2011 | terisi |  |
| var1214 | 2012 | terisi |  |
| var1214 | 2013 | terisi |  |
| var1214 | 2014 | terisi |  |
| var1214 | 2015 | terisi |  |
| var1214 | 2016 | terisi |  |
| var1214 | 2017 | terisi |  |
| var1214 | 2018 | terisi |  |
| var1214 | 2019 | terisi |  |
| var1214 | 2020 | terisi |  |
| var1214 | 2021 | terisi |  |
| var1214 | 2022 | terisi |  |
| var1214 | 2023 | terisi |  |
| var2755 | 2018 | terisi |  |
| var2755 | 2019 | terisi |  |
| var2755 | 2020 | terisi |  |
| var2755 | 2021 | terisi |  |
| var2755 | 2022 | terisi |  |
| var2755 | 2023 | terisi |  |
| var2755 | 2024 | terisi |  |
| var2755 | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1161 | nasional | 2011 | 2025 | 15 |
| var1161 | provinsi | 2011 | 2025 | 15 |
| var1214 | nasional | 2010 | 2023 | 14 |
| var1214 | provinsi | 2010 | 2023 | 14 |
| var1344 | nasional | 2015 | 2023 | 9 |
| var1344 | provinsi | 2015 | 2023 | 9 |
| var2755 | nasional | 2018 | 2025 | 8 |
| var2755 | provinsi | 2018 | 2025 | 8 |

Provinsi yang belum ada pada sebagian periode panel: Kalimantan Utara, Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
