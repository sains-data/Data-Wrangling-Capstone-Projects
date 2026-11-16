# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1393 | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1393 | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1393 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1393 | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1393 | 2014 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1393 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1435 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1435 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1480 | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1480 | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1480 | 2016 | 38 | 0 | 0 | 0.00 |  |
| var1480 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| var1393 | 1 | 51 | 404 | 0 |
| var1435 | 4 | 32 | 382 | 0 |
| var1480 | 1 | 17 | 100 | 34 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1393 | 2010 | terisi |  |
| var1393 | 2011 | terisi |  |
| var1393 | 2012 | terisi |  |
| var1393 | 2013 | terisi |  |
| var1393 | 2014 | terisi |  |
| var1393 | 2015 | terisi |  |
| var1393 | 2016 | terisi |  |
| var1393 | 2017 | terisi |  |
| var1393 | 2018 | terisi |  |
| var1393 | 2019 | terisi |  |
| var1393 | 2020 | terisi |  |
| var1393 | 2021 | terisi |  |
| var1480 | 2007 | terisi |  |
| var1480 | 2013 | terisi |  |
| var1480 | 2016 | terisi |  |
| var1480 | 2018 | terisi |  |
| var1435 | 2015 | terisi |  |
| var1435 | 2016 | terisi |  |
| var1435 | 2017 | terisi |  |
| var1435 | 2018 | terisi |  |
| var1435 | 2019 | terisi |  |
| var1435 | 2020 | terisi |  |
| var1435 | 2021 | terisi |  |
| var1435 | 2022 | terisi |  |
| var1435 | 2023 | terisi |  |
| var1435 | 2024 | terisi |  |
| var1435 | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1393 | nasional | 2010 | 2021 | 12 |
| var1393 | provinsi | 2010 | 2021 | 12 |
| var1435 | nasional | 2015 | 2025 | 11 |
| var1435 | provinsi | 2015 | 2025 | 11 |
| var1480 | nasional | 2007 | 2018 | 4 |
| var1480 | provinsi | 2007 | 2018 | 3 |

Provinsi yang belum ada pada sebagian periode panel: Kalimantan Utara, Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
