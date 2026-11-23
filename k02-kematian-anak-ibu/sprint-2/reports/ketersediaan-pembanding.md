# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2012, 2015, 2016, 2017, 2018, 2019.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| MDG_0000000007 | who_gho | jenis_kelamin=FEMALE | per_1000_kh | 72 | 1952 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | jenis_kelamin=MALE | per_1000_kh | 72 | 1952 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | kuintil=WQ1 | per_1000_kh | 34 | 1990 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | kuintil=WQ2 | per_1000_kh | 34 | 1990 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | kuintil=WQ3 | per_1000_kh | 34 | 1990 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | kuintil=WQ4 | per_1000_kh | 34 | 1990 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | kuintil=WQ5 | per_1000_kh | 34 | 1990 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000007 | who_gho | total | per_1000_kh | 73 | 1951 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| MDG_0000000026 | who_gho | total | per_100000_kh | 39 | 1985 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |
| SH.DYN.MORT | wdi | total | per_1000_kh | 65 | 1960 | 2024 | 2012, 2015, 2016, 2017, 2018, 2019 | tidak |
| SH.STA.BRTC.ZS | wdi | total | persen | 21 | 1987 | 2019 | 2012, 2016, 2017, 2018, 2019 | tidak |
| SH.STA.MMRT | wdi | total | per_100000_kh | 39 | 1985 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | tidak |
| WHOSIS_000003 | who_gho | total | per_1000_kh | 71 | 1953 | 2023 | 2012, 2015, 2016, 2017, 2018, 2019 | ada |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| SH.DYN.MORT | 66 | 65 |
| SH.STA.BRTC.ZS | 66 | 21 |
| SH.STA.MMRT | 66 | 39 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

| seri_kode | rincian | 2012 | 2015 | 2016 | 2017 | 2018 | 2019 |
|---|---|---|---|---|---|---|---|
| MDG_0000000007 | jenis_kelamin=FEMALE | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | jenis_kelamin=MALE | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | kuintil=WQ1 | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | kuintil=WQ2 | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | kuintil=WQ3 | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | kuintil=WQ4 | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | kuintil=WQ5 | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000007 | total | 1 | 1 | 1 | 1 | 1 | 1 |
| MDG_0000000026 | total | 1 | 1 | 1 | 1 | 1 | 1 |
| SH.DYN.MORT | total | 1 | 1 | 1 | 1 | 1 | 1 |
| SH.STA.BRTC.ZS | total | 1 | 0 | 1 | 1 | 1 | 1 |
| SH.STA.MMRT | total | 1 | 1 | 1 | 1 | 1 | 1 |
| WHOSIS_000003 | total | 1 | 1 | 1 | 1 | 1 | 1 |

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | var1373 | MDG_0000000007 (total), SH.DYN.MORT (total) | WHO rincian total (jenis kelamin dan kuintil TOTAL); BPS baris Indonesia |
| P2 | var1584 |  | WHOSIS_000003 = neonatal 0–27 hari, MDG_0000000007 = balita; keduanya bukan bayi |
| P3 | var1541 | SH.STA.BRTC.ZS (total) | tidak ada rincian yang menyamakan keduanya di paket |
| P4 | MDG_0000000007 | SH.DYN.MORT (total) | rincian total keduanya |
| P5 | MDG_0000000026 | SH.STA.MMRT (total) | rincian total keduanya |
| P1J | var1373 | MDG_0000000007 (total), SH.DYN.MORT (total) | WHO rincian total (jenis kelamin dan kuintil TOTAL); BPS baris Indonesia |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
