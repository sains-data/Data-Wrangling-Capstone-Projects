# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| EN.POP.SLUM.UR.ZS | wdi | total | persen | 12 | 2000 | 2022 | 2016, 2018, 2020, 2022 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| EN.POP.SLUM.UR.ZS | 66 | 12 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2016 | 2018 | 2020 | 2022 |
|---|---|---|---|---|---|
| EN.POP.SLUM.UR.ZS | total | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1241 | EN.POP.SLUM.UR.ZS (total) | tanpa rincian |
| P2 | var2753 | var2754 (arus=bongkar) | arus bongkar; muat diperlakukan sama |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
