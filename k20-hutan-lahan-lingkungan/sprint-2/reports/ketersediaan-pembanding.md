# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2006, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| AG.LND.FRST.K2 | wdi | total | km2 | 36 | 1990 | 2025 | 2006, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | tidak |
| AG.LND.FRST.ZS | wdi | total | persen | 35 | 1990 | 2024 | 2006, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | tidak |
| EN.ATM.PM25.MC.M3 | wdi | total | mikrogram_per_m3 | 34 | 1990 | 2023 | 2006, 2011, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| AG.LND.FRST.K2 | 66 | 36 |
| AG.LND.FRST.ZS | 66 | 35 |
| EN.ATM.PM25.MC.M3 | 66 | 34 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2006 | 2011 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AG.LND.FRST.K2 | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| AG.LND.FRST.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| EN.ATM.PM25.MC.M3 | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | tabel:sdg15_tutupan_hutan:luas_ribu_ha | AG.LND.FRST.K2 (total) | BPS tutupan=hutan |
| P2 | tabel:sdg15_tutupan_hutan:persen | AG.LND.FRST.ZS (total) | tutupan=hutan |
| P3 | var2532 | EN.ATM.PM25.MC.M3 (total) | komponen udara |
| P4 | var1304 | tabel:sdg15_tutupan_hutan:luas_ribu_ha (total) | rincian jumlah |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
