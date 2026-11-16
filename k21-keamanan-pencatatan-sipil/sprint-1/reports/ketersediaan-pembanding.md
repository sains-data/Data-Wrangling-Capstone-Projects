# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| SP.REG.BRTH.ZS | wdi | total | persen | 8 | 2002 | 2021 | 2016, 2017, 2018, 2021 | tidak |
| VC.IHR.PSRC.P5 | wdi | total | per_100000_penduduk | 6 | 1998 | 2022 | 2022 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SP.REG.BRTH.ZS | 66 | 8 |
| VC.IHR.PSRC.P5 | 66 | 6 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2016 | 2017 | 2018 | 2021 | 2022 |
|---|---|---|---|---|---|---|
| SP.REG.BRTH.ZS | total | 1 | 1 | 1 | 1 | 0 |
| VC.IHR.PSRC.P5 | total | 0 | 0 | 0 | 0 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1410 | SP.REG.BRTH.ZS (total) | tanpa rincian |
| P2 | var1311 | VC.IHR.PSRC.P5 (total) | tanpa rincian |
| P3 | var1410 | var1831 (total) | tanpa rincian |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
