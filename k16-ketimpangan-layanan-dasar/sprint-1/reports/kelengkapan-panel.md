# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1254 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1254 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2011 | 2023 | 38 | 29 | 29 | 76.30 | 100.00 |
| var2016 [layanan=air_minum] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=air_minum] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=air_minum] | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=air_minum] | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=air_minum] | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=kesehatan] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=kesehatan] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=kesehatan] | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=kesehatan] | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=kesehatan] | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=sanitasi] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=sanitasi] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=sanitasi] | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=sanitasi] | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var2016 [layanan=sanitasi] | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| var1254 | 0 | 8 | 68 | 0 |
| var2011 | 0 | 20 | 199 | 9 |
| var2016 [layanan=air_minum] | 4 | 16 | 170 | 0 |
| var2016 [layanan=kesehatan] | 4 | 16 | 170 | 0 |
| var2016 [layanan=sanitasi] | 4 | 16 | 170 | 0 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var2011 | 2018 | terisi |  |
| var2011 | 2019 | terisi |  |
| var2011 | 2020 | terisi |  |
| var2011 | 2021 | terisi |  |
| var2011 | 2022 | terisi |  |
| var2011 | 2023 | terisi |  |
| var2016 [layanan=air_minum] | 2019 | terisi |  |
| var2016 [layanan=air_minum] | 2020 | terisi |  |
| var2016 [layanan=air_minum] | 2021 | terisi |  |
| var2016 [layanan=air_minum] | 2022 | terisi |  |
| var2016 [layanan=air_minum] | 2023 | terisi |  |
| var2016 [layanan=sanitasi] | 2019 | terisi |  |
| var2016 [layanan=sanitasi] | 2020 | terisi |  |
| var2016 [layanan=sanitasi] | 2021 | terisi |  |
| var2016 [layanan=sanitasi] | 2022 | terisi |  |
| var2016 [layanan=sanitasi] | 2023 | terisi |  |
| var2016 [layanan=kesehatan] | 2019 | terisi |  |
| var2016 [layanan=kesehatan] | 2020 | terisi |  |
| var2016 [layanan=kesehatan] | 2021 | terisi |  |
| var2016 [layanan=kesehatan] | 2022 | terisi |  |
| var2016 [layanan=kesehatan] | 2023 | terisi |  |
| var1254 | 2015 | terisi |  |
| var1254 | 2016 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1254 | nasional | 2015 | 2016 | 2 |
| var1254 | provinsi | 2015 | 2016 | 2 |
| var2011 | nasional | 2018 | 2023 | 6 |
| var2011 | provinsi | 2018 | 2023 | 6 |
| var2016 [layanan=air_minum] | nasional | 2019 | 2023 | 5 |
| var2016 [layanan=air_minum] | provinsi | 2019 | 2023 | 5 |
| var2016 [layanan=kesehatan] | nasional | 2019 | 2023 | 5 |
| var2016 [layanan=kesehatan] | provinsi | 2019 | 2023 | 5 |
| var2016 [layanan=sanitasi] | nasional | 2019 | 2023 | 5 |
| var2016 [layanan=sanitasi] | provinsi | 2019 | 2023 | 5 |

Provinsi yang belum ada pada sebagian periode panel: Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
