# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| var1373 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1373 | 2017 | 38 | 0 | 0 | 0.00 |  |
| var1541 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1541 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1541 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1541 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1541 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var1584 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var1584 | 2017 | 38 | 0 | 0 | 0.00 |  |

## Jumlah sel per kategori (provinsi)

| seri_kode | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|
| var1373 | 9 | 33 | 34 |
| var1541 | 20 | 170 | 0 |
| var1584 | 9 | 33 | 34 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var1373 | 2012 | terisi |  |
| var1373 | 2017 | terisi |  |
| var1584 | 2012 | terisi |  |
| var1584 | 2017 | terisi |  |
| var1541 | 2015 | terisi |  |
| var1541 | 2016 | terisi |  |
| var1541 | 2017 | terisi |  |
| var1541 | 2018 | terisi |  |
| var1541 | 2019 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| var1373 | nasional | 2012 | 2017 | 2 |
| var1373 | provinsi | 2012 | 2012 | 1 |
| var1541 | nasional | 2015 | 2019 | 5 |
| var1541 | provinsi | 2015 | 2019 | 5 |
| var1584 | nasional | 2012 | 2017 | 2 |
| var1584 | provinsi | 2012 | 2012 | 1 |

Provinsi yang belum ada pada sebagian periode panel: Kalimantan Utara, Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
