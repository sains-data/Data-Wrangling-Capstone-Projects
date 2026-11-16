# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| SDG_0861_SEX_RT | ilostat | jenis_kelamin=FEMALE | persen | 24 | 2000 | 2023 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |
| SDG_0861_SEX_RT | ilostat | jenis_kelamin=MALE | persen | 24 | 2000 | 2023 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |
| SDG_0861_SEX_RT | ilostat | total | persen | 24 | 2000 | 2023 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |
| SDG_A871_SEX_AGE_RT | ilostat | jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | persen | 3 | 2009 | 2023 | 2019, 2023 | tidak |
| SDG_A871_SEX_AGE_RT | ilostat | jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | persen | 3 | 2009 | 2023 | 2019, 2023 | tidak |
| SDG_A871_SEX_AGE_RT | ilostat | umur=CLDVERSION_Y15-17 | persen | 3 | 2009 | 2023 | 2019, 2023 | tidak |
| SDG_B871_SEX_AGE_RT | ilostat | jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | persen | 1 | 2009 | 2009 | (tidak ada) | tidak |
| SDG_B871_SEX_AGE_RT | ilostat | jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | persen | 1 | 2009 | 2009 | (tidak ada) | tidak |
| SDG_B871_SEX_AGE_RT | ilostat | umur=CLDVERSION_Y15-17 | persen | 1 | 2009 | 2009 | (tidak ada) | tidak |
| SL.TLF.0714.ZS | wdi | total | persen | 3 | 2000 | 2010 | (tidak ada) | tidak |
| SL.UEM.NEET.ZS | wdi | total | persen | 28 | 1996 | 2023 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SL.TLF.0714.ZS | 66 | 3 |
| SL.UEM.NEET.ZS | 66 | 28 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 |
|---|---|---|---|---|---|---|---|---|---|---|
| SDG_0861_SEX_RT | jenis_kelamin=FEMALE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SDG_0861_SEX_RT | jenis_kelamin=MALE | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SDG_0861_SEX_RT | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| SDG_A871_SEX_AGE_RT | jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| SDG_A871_SEX_AGE_RT | jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| SDG_A871_SEX_AGE_RT | umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| SDG_B871_SEX_AGE_RT | jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SDG_B871_SEX_AGE_RT | jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SDG_B871_SEX_AGE_RT | umur=CLDVERSION_Y15-17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SL.TLF.0714.ZS | total | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SL.UEM.NEET.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1186 | SDG_0861_SEX_RT (total), SL.UEM.NEET.ZS (total) | total jenis kelamin |
| P2 | var2658 | SDG_A871_SEX_AGE_RT (umur=CLDVERSION_Y15-17) | ILO umur CLDVERSION_Y15-17, total jenis kelamin |
| P3 | SL.TLF.0714.ZS |  | tanpa rincian |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
