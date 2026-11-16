# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1402 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1402 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1402 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |
| var1477 [profesi=bidan] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=bidan] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=bidan] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=dokter_umum] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=dokter_umum] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=dokter_umum] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=perawat] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=perawat] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1477 [profesi=perawat] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2279 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2279 | 2023 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2279 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var2279 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi |
|---|---|---|---|
| var1402 | 4 | 32 | 382 |
| var1477 [profesi=bidan] | 0 | 12 | 102 |
| var1477 [profesi=dokter_umum] | 0 | 12 | 102 |
| var1477 [profesi=perawat] | 0 | 12 | 102 |
| var2279 | 0 | 4 | 148 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1402 | 2015 | terisi |  |
| var1402 | 2016 | terisi |  |
| var1402 | 2017 | terisi |  |
| var1402 | 2018 | terisi |  |
| var1402 | 2019 | terisi |  |
| var1402 | 2020 | terisi |  |
| var1402 | 2021 | terisi |  |
| var1402 | 2022 | terisi |  |
| var1402 | 2023 | terisi |  |
| var1402 | 2024 | terisi |  |
| var1402 | 2025 | terisi |  |
| var2279 | 2022 | terisi |  |
| var2279 | 2023 | terisi |  |
| var2279 | 2024 | terisi |  |
| var2279 | 2025 | terisi |  |
| var1477 [profesi=dokter_umum] | 2016 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=dokter_umum] | 2017 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=dokter_umum] | 2018 | terisi |  |
| var1477 [profesi=perawat] | 2016 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=perawat] | 2017 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=perawat] | 2018 | terisi |  |
| var1477 [profesi=bidan] | 2016 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=bidan] | 2017 | missing | provinsi sudah ada dan penerbit tidak menyatakan angka itu tidak ada |
| var1477 [profesi=bidan] | 2018 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1402 | nasional | 2015 | 2025 | 11 |
| var1402 | provinsi | 2015 | 2025 | 11 |
| var1477 [profesi=bidan] | nasional | 2018 | 2018 | 1 |
| var1477 [profesi=bidan] | provinsi | 2016 | 2018 | 3 |
| var1477 [profesi=dokter_umum] | nasional | 2018 | 2018 | 1 |
| var1477 [profesi=dokter_umum] | provinsi | 2016 | 2018 | 3 |
| var1477 [profesi=perawat] | nasional | 2018 | 2018 | 1 |
| var1477 [profesi=perawat] | provinsi | 2016 | 2018 | 3 |
| var2279 | nasional | 2022 | 2025 | 4 |
| var2279 | provinsi | 2022 | 2025 | 4 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
