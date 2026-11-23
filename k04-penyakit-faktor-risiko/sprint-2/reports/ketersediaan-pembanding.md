# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| MALARIA_EST_INCIDENCE | who_gho | total | per_1000_penduduk_berisiko | 24 | 2000 | 2023 | 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | ada |
| M_Est_tob_curr_std | who_gho | jenis_kelamin=FEMALE | persen | 10 | 2000 | 2030 | 2007, 2010, 2015, 2020, 2021, 2022, 2025 | ada |
| M_Est_tob_curr_std | who_gho | jenis_kelamin=MALE | persen | 10 | 2000 | 2030 | 2007, 2010, 2015, 2020, 2021, 2022, 2025 | ada |
| M_Est_tob_curr_std | who_gho | total | persen | 10 | 2000 | 2030 | 2007, 2010, 2015, 2020, 2021, 2022, 2025 | ada |
| NCDMORT3070 | who_gho | jenis_kelamin=FEMALE | persen | 22 | 2000 | 2021 | 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 | ada |
| NCDMORT3070 | who_gho | jenis_kelamin=MALE | persen | 22 | 2000 | 2021 | 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 | ada |
| NCDMORT3070 | who_gho | total | persen | 22 | 2000 | 2021 | 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 | ada |
| SH.MLR.INCD.P3 | wdi | total | per_1000_penduduk_berisiko | 25 | 2000 | 2024 | 2007, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SH.MLR.INCD.P3 | 66 | 25 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2007 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MALARIA_EST_INCIDENCE | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| M_Est_tob_curr_std | jenis_kelamin=FEMALE | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| M_Est_tob_curr_std | jenis_kelamin=MALE | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| M_Est_tob_curr_std | total | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| NCDMORT3070 | jenis_kelamin=FEMALE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| NCDMORT3070 | jenis_kelamin=MALE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| NCDMORT3070 | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| SH.MLR.INCD.P3 | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1393 | MALARIA_EST_INCIDENCE (total), SH.MLR.INCD.P3 (total) | tanpa rincian di ketiganya |
| P2 | var1435 | M_Est_tob_curr_std (total) | WHO rincian total jenis kelamin |
| P3 | var1480 | NCDMORT3070 (total) | WHO rincian total jenis kelamin |
| P4 | MALARIA_EST_INCIDENCE | SH.MLR.INCD.P3 (total) | tanpa rincian |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
