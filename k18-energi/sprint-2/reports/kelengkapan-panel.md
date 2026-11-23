# Kelengkapan panel provinsi dan kategori sel kosong

Dihasilkan `python pipeline.py` (`src/silver/grid.py`). Grid = 38 provinsi susunan 2025 x periode yang diterbitkan seri itu. Persen dari 38 menghitung semua sel; persen dari seharusnya hanya menghitung sel yang provinsinya sudah ada dan tidak dinyatakan tidak terbit oleh penerbit.

## Persen sel terisi per seri per periode

| seri_kode | periode | sel | terisi | seharusnya_ada | persen_dari_38 | persen_dari_seharusnya |
|---|---|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2001 | 38 | 27 | 29 | 71.10 | 93.10 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2001 | 38 | 27 | 29 | 71.10 | 93.10 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2001 | 38 | 27 | 29 | 71.10 | 93.10 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2021 | 38 | 33 | 34 | 86.80 | 97.10 |
| var87 | 1993 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1994 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1995 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1996 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1997 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1998 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 1999 | 38 | 26 | 26 | 68.40 | 100.00 |
| var87 | 2000 | 38 | 24 | 24 | 63.20 | 100.00 |
| var87 | 2001 | 38 | 29 | 29 | 76.30 | 100.00 |
| var87 | 2002 | 38 | 30 | 30 | 78.90 | 100.00 |
| var87 | 2003 | 38 | 30 | 30 | 78.90 | 100.00 |
| var87 | 2004 | 38 | 30 | 30 | 78.90 | 100.00 |
| var87 | 2006 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2007 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2008 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2009 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2010 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2011 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2012 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2013 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2014 | 38 | 33 | 33 | 86.80 | 100.00 |
| var87 | 2015 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2016 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2017 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2018 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2019 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2020 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2021 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2022 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2023 | 38 | 34 | 34 | 89.50 | 100.00 |
| var87 | 2024 | 38 | 38 | 38 | 100.00 | 100.00 |
| var87 | 2025 | 38 | 38 | 38 | 100.00 | 100.00 |

## Jumlah sel per kategori (provinsi)

| seri_kode | batas_lama | belum_ada | missing | terisi | tidak_diterbitkan |
|---|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2 | 74 | 2 | 529 | 1 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2 | 74 | 2 | 529 | 1 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2 | 74 | 3 | 528 | 1 |
| var87 | 9 | 199 | 0 | 1004 | 4 |

## Baris Indonesia

| seri_kode | periode | kategori | bukti |
|---|---|---|---|
| var87 | 1993 | terisi |  |
| var87 | 1994 | terisi |  |
| var87 | 1995 | terisi |  |
| var87 | 1996 | terisi |  |
| var87 | 1997 | terisi |  |
| var87 | 1998 | terisi |  |
| var87 | 1999 | terisi |  |
| var87 | 2000 | terisi |  |
| var87 | 2001 | terisi |  |
| var87 | 2002 | terisi |  |
| var87 | 2003 | terisi |  |
| var87 | 2004 | terisi |  |
| var87 | 2006 | terisi |  |
| var87 | 2007 | terisi |  |
| var87 | 2008 | terisi |  |
| var87 | 2009 | terisi |  |
| var87 | 2010 | terisi |  |
| var87 | 2011 | terisi |  |
| var87 | 2012 | terisi |  |
| var87 | 2013 | terisi |  |
| var87 | 2014 | terisi |  |
| var87 | 2015 | terisi |  |
| var87 | 2016 | terisi |  |
| var87 | 2017 | terisi |  |
| var87 | 2018 | terisi |  |
| var87 | 2019 | terisi |  |
| var87 | 2020 | terisi |  |
| var87 | 2021 | terisi |  |
| var87 | 2022 | terisi |  |
| var87 | 2023 | terisi |  |
| var87 | 2024 | terisi |  |
| var87 | 2025 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2001 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2007 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2008 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2009 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2010 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2011 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2012 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2013 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2014 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2015 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2016 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2017 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2018 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2019 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2020 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2021 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2001 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2007 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2008 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2009 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2010 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2011 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2012 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2013 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2014 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2015 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2016 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2017 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2018 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2019 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2020 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2021 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2001 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2007 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2008 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2009 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2010 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2011 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2012 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2013 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2014 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2015 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2016 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2017 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2018 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2019 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2020 | terisi |  |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2021 | terisi |  |

## Batas pemakaian panel

| seri_kode | tingkat | periode_pertama | periode_terakhir | jumlah_periode |
|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | nasional | 2001 | 2021 | 16 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | provinsi | 2001 | 2021 | 16 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | nasional | 2001 | 2021 | 16 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | provinsi | 2001 | 2021 | 16 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | nasional | 2001 | 2021 | 16 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | provinsi | 2001 | 2021 | 16 |
| var87 | nasional | 1993 | 2025 | 32 |
| var87 | provinsi | 1993 | 2025 | 32 |

Provinsi yang belum ada pada sebagian periode panel: Banten, Gorontalo, Kalimantan Utara, Kepulauan Bangka Belitung, Kepulauan Riau, Maluku Utara, Papua Barat, Papua Barat Daya, Papua Pegunungan, Papua Selatan, Papua Tengah, Sulawesi Barat.

Tahun sesudah periode terakhir di luar jangkauan panel; panel tidak menggambarkan keadaan tahun itu. Tahun di antara dua periode survei tidak termasuk grid dan tidak diisi di Silver.

Daftar semua sel kosong beserta buktinya: `reports/grid-sel-kosong.csv`.
