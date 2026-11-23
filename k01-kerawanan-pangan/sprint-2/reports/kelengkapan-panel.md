# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1473 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1473 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1473 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1474 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1474 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1474 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi |
|---|---|---|---|
| var1473 | 4 | 24 | 314 |
| var1474 | 4 | 24 | 314 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1473 | 2017 | terisi |  |
| var1473 | 2018 | terisi |  |
| var1473 | 2019 | terisi |  |
| var1473 | 2020 | terisi |  |
| var1473 | 2021 | terisi |  |
| var1473 | 2022 | terisi |  |
| var1473 | 2023 | terisi |  |
| var1473 | 2024 | terisi |  |
| var1473 | 2025 | terisi |  |
| var1474 | 2017 | terisi |  |
| var1474 | 2018 | terisi |  |
| var1474 | 2019 | terisi |  |
| var1474 | 2020 | terisi |  |
| var1474 | 2021 | terisi |  |
| var1474 | 2022 | terisi |  |
| var1474 | 2023 | terisi |  |
| var1474 | 2024 | terisi |  |
| var1474 | 2025 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1473 | nasional | 2017 | 2025 | 9 |
| var1473 | provinsi | 2017 | 2025 | 9 |
| var1474 | nasional | 2017 | 2025 | 9 |
| var1474 | provinsi | 2017 | 2025 | 9 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
