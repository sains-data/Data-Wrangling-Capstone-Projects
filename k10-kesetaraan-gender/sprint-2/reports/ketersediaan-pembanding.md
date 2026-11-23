# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| SDG_0552_NOC_RT | ilostat | total | persen | 5 | 2007 | 2023 | 2023 | tidak |
| SDG_T552_NOC_RT | ilostat | total | persen | 15 | 2007 | 2023 | 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023 | tidak |
| SG.GEN.PARL.ZS | wdi | total | persen | 28 | 1997 | 2025 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | tidak |
| SP.M18.2024.FE.ZS | wdi | total | persen | 8 | 1987 | 2017 | 2017 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SG.GEN.PARL.ZS | 66 | 28 |
| SP.M18.2024.FE.ZS | 66 | 8 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SDG_0552_NOC_RT | total | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| SDG_T552_NOC_RT | total | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| SG.GEN.PARL.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SP.M18.2024.FE.ZS | total | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var2003 | SDG_T552_NOC_RT (total) | tanpa rincian |
| P2 | var2003 | SDG_0552_NOC_RT (total) | tanpa rincian |
| P3 | var1360 | SP.M18.2024.FE.ZS (total) | keduanya perempuan 20–24, sebelum 18 |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
