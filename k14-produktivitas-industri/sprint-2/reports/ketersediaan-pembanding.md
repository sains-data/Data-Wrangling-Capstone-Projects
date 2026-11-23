# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| NV.IND.MANF.ZS | wdi | total | persen | 43 | 1983 | 2025 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | tidak |
| SDG_0821_NOC_RT | ilostat | total | persen_per_tahun | 28 | 2000 | 2027 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | tidak |
| SDG_0922_NOC_RT | ilostat | total | persen | 24 | 2000 | 2023 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |
| SDG_B821_NOC_RT | ilostat | total | persen_per_tahun | 28 | 2000 | 2027 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | tidak |
| SL.GDP.PCAP.EM.KD | wdi | total | usd_ppp_2021 | 35 | 1991 | 2025 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| NV.IND.MANF.ZS | 66 | 43 |
| SL.GDP.PCAP.EM.KD | 66 | 35 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NV.IND.MANF.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SDG_0821_NOC_RT | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SDG_0922_NOC_RT | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| SDG_B821_NOC_RT | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SL.GDP.PCAP.EM.KD | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1161 | SDG_0821_NOC_RT (total), SDG_B821_NOC_RT (total) | tanpa rincian |
| P2 | var1161 | SL.GDP.PCAP.EM.KD (total) | tanpa rincian |
| P3 | var1214 | NV.IND.MANF.ZS (total) | tanpa rincian |
| P4 | var2755 | SDG_0922_NOC_RT (total) | tanpa rincian |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
