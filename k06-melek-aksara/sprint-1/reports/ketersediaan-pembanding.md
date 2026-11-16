# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| SE.ADT.LITR.ZS | wdi | total | persen | 13 | 1980 | 2020 | 2009, 2010, 2011, 2014, 2015, 2016, 2018, 2020 | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SE.ADT.LITR.ZS | 66 | 13 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2009 | 2010 | 2011 | 2014 | 2015 | 2016 | 2018 | 2020 |
|---|---|---|---|---|---|---|---|---|---|
| SE.ADT.LITR.ZS | total | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1458 | tabel:sdg4_amh_rinci (total) | rincian total = perkotaan+perdesaan dan laki-laki+perempuan |
| P2 | var1458 | SE.ADT.LITR.ZS (total) | keduanya penduduk 15+ tanpa rincian |
| P3 | tabel:sdg4_amh_rinci | SE.ADT.LITR.ZS (total) | rincian total |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
