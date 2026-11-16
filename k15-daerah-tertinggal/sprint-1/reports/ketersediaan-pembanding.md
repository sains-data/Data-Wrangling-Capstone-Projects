# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2007, 2008, 2009, 2010, 2011, 2012-S1, 2012-S2, 2013-S1, 2013-S2, 2014-S1, 2014-S2, 2015-S1, 2015-S2, 2016-S1, 2016-S2, 2017-S1, 2017-S2, 2018-S1, 2018-S2, 2019, 2019-S1, 2019-S2, 2020, 2020-S1, 2020-S2, 2021, 2021-S1, 2021-S2, 2022-S1, 2022-S2, 2023-S1, 2024-S1, 2024-S2, 2025-S1, 2025-S2, 2026-S1.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| SI.POV.NAHC | wdi | total | persen | 28 | 1996 | 2025 | 2007, 2008, 2009, 2010, 2011, 2019, 2020, 2021 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SI.POV.NAHC | 66 | 28 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2007 | 2008 | 2009 | 2010 | 2011 | 2019 | 2020 | 2021 |
|---|---|---|---|---|---|---|---|---|---|
| SI.POV.NAHC | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var192 | SI.POV.NAHC (total) | rincian jumlah (perkotaan + perdesaan); semester Maret |
| P2 | var2191 | var2190 (total) | rincian jumlah |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
