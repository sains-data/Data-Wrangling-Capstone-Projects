# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| IT.NET.USER.ZS | wdi | total | persen | 32 | 1990 | 2024 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | tidak |
| SE.PRE.ENRR | wdi | total | persen_apk | 49 | 1970 | 2018 | 2015, 2016, 2017, 2018 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| IT.NET.USER.ZS | 66 | 32 |
| SE.PRE.ENRR | 66 | 49 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IT.NET.USER.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SE.PRE.ENRR | total | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1439 | SE.PRE.ENRR (total) | tanpa rincian |
| P2 | var1221 | IT.NET.USER.ZS (total) | tanpa rincian |
| P3 | var1451 | var1447 (total) | tanpa rincian |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
