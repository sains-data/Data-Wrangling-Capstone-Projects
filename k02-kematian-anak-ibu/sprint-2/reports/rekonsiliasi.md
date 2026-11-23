# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | MDG_0000000007 | selisih | 6 | 2 | 2 | 7.83 | 27.65 | tanpa pasangan (4), metode berbeda (2) |
| P1 | SH.DYN.MORT | selisih | 6 | 2 | 2 | 9.15 | 34.12 | tanpa pasangan (4), metode berbeda (2) |
| P2 |  | konteks | 2 | 0 | 0 |  |  | definisi berbeda (2) |
| P3 | SH.STA.BRTC.ZS | konteks | 5 | 4 | 0 |  |  | definisi berbeda (5) |
| P4 | SH.DYN.MORT | selisih | 73 | 64 | 64 | 0.58 | 0.84 | vintage berbeda (64), tanpa pasangan (9) |
| P5 | SH.STA.MMRT | selisih | 39 | 39 | 39 | 0.19 | 0.09 | vintage berbeda (39) |
| P1J | MDG_0000000007 | selisih | 2 | 2 | 2 | 4.18 | 13.01 | metode berbeda (2) |
| P1J | SH.DYN.MORT | selisih | 2 | 2 | 2 | 5.24 | 17.02 | metode berbeda (2) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 21.63% (8 baris); semua pasangan termasuk antarpembanding: 0.25% (111 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 126, P3 17, P4 1.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Kematian balita: titik survei BPS vs estimasi tahunan WHO dan WDI

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode dan definisi periode (survei dengan rujukan 5 tahun vs estimasi model tahunan).

Rincian: WHO rincian total (jenis kelamin dan kuintil TOTAL); BPS baris Indonesia.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| MDG_0000000007 | 2012 | 40.00 | 30.96 | 9.04 | 29.20 | keduanya | metode berbeda |  |
| MDG_0000000007 | 2013 |  | 29.73 |  |  | hanya_pembanding | tanpa pasangan |  |
| MDG_0000000007 | 2014 |  | 28.56 |  |  | hanya_pembanding | tanpa pasangan |  |
| MDG_0000000007 | 2015 |  | 27.44 |  |  | hanya_pembanding | tanpa pasangan |  |
| MDG_0000000007 | 2016 |  | 26.37 |  |  | hanya_pembanding | tanpa pasangan |  |
| MDG_0000000007 | 2017 | 32.00 | 25.38 | 6.62 | 26.10 | keduanya | metode berbeda |  |
| SH.DYN.MORT | 2012 | 40.00 | 29.90 | 10.10 | 33.78 | keduanya | metode berbeda |  |
| SH.DYN.MORT | 2013 |  | 28.60 |  |  | hanya_pembanding | tanpa pasangan |  |
| SH.DYN.MORT | 2014 |  | 27.30 |  |  | hanya_pembanding | tanpa pasangan |  |
| SH.DYN.MORT | 2015 |  | 26.10 |  |  | hanya_pembanding | tanpa pasangan |  |
| SH.DYN.MORT | 2016 |  | 25.00 |  |  | hanya_pembanding | tanpa pasangan |  |
| SH.DYN.MORT | 2017 | 32.00 | 23.80 | 8.20 | 34.45 | keduanya | metode berbeda |  |

### P2: Kematian bayi BPS dan pembanding yang tersedia

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: tidak ada seri kematian bayi (0–11 bulan) di paket pembanding.

Rincian: WHOSIS_000003 = neonatal 0–27 hari, MDG_0000000007 = balita; keduanya bukan bayi.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2012 | 32.00 |  |  |  | hanya_utama | definisi berbeda |  |
|  | 2017 | 24.00 |  |  |  | hanya_utama | definisi berbeda |  |

### P3: Persalinan: di fasilitas (BPS, 40% terbawah) vs ditolong tenaga kesehatan (WDI, semua)

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi dan cakupan berbeda; tidak dihitung sebagai selisih.

Rincian: tidak ada rincian yang menyamakan keduanya di paket.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.STA.BRTC.ZS | 2015 | 70.25 |  |  |  | hanya_utama | definisi berbeda |  |
| SH.STA.BRTC.ZS | 2016 | 73.05 | 92.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| SH.STA.BRTC.ZS | 2017 | 74.89 | 90.90 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| SH.STA.BRTC.ZS | 2018 | 76.82 | 93.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| SH.STA.BRTC.ZS | 2019 | 81.02 | 94.70 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |

### P4: Kematian balita: WHO vs WDI (dua rilis estimasi yang sama)

Jenis **selisih**; kategori pasangan: **vintage berbeda**. Vintage (rilis estimasi UN IGME berbeda).

Rincian: rincian total keduanya.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.DYN.MORT | 1951 | 292.12 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1952 | 283.58 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1953 | 275.27 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1954 | 267.32 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1955 | 259.33 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1956 | 251.62 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1957 | 244.11 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1958 | 236.98 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1959 | 230.19 |  |  |  | hanya_utama | tanpa pasangan |  |
| SH.DYN.MORT | 1960 | 223.80 | 224.50 | -0.70 | -0.31 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1961 | 217.72 | 218.20 | -0.48 | -0.22 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1962 | 211.84 | 212.30 | -0.46 | -0.22 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1963 | 206.03 | 206.40 | -0.37 | -0.18 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1964 | 200.32 | 200.70 | -0.38 | -0.19 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1965 | 229.05 | 229.90 | -0.85 | -0.37 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1966 | 188.85 | 189.10 | -0.25 | -0.13 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1967 | 183.08 | 183.30 | -0.22 | -0.12 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1968 | 177.31 | 177.50 | -0.19 | -0.11 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1969 | 171.61 | 171.80 | -0.19 | -0.11 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1970 | 166.03 | 166.30 | -0.27 | -0.16 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1971 | 160.68 | 160.90 | -0.22 | -0.14 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1972 | 155.40 | 155.60 | -0.20 | -0.13 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1973 | 150.36 | 150.50 | -0.14 | -0.09 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1974 | 145.54 | 145.60 | -0.06 | -0.04 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1975 | 140.92 | 140.90 | 0.02 | 0.02 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1976 | 136.54 | 136.40 | 0.14 | 0.11 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1977 | 132.35 | 132.20 | 0.15 | 0.12 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1978 | 128.37 | 128.10 | 0.27 | 0.21 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1979 | 124.51 | 124.20 | 0.31 | 0.25 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1980 | 120.74 | 120.40 | 0.34 | 0.28 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1981 | 117.00 | 116.60 | 0.40 | 0.35 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1982 | 113.33 | 112.80 | 0.53 | 0.47 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1983 | 109.70 | 109.10 | 0.60 | 0.55 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1984 | 106.08 | 105.40 | 0.68 | 0.65 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1985 | 102.45 | 101.80 | 0.65 | 0.63 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1986 | 98.78 | 98.10 | 0.68 | 0.70 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1987 | 95.12 | 94.40 | 0.72 | 0.76 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1988 | 91.39 | 90.70 | 0.69 | 0.77 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1989 | 87.65 | 86.90 | 0.75 | 0.86 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1990 | 83.87 | 83.20 | 0.67 | 0.80 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1991 | 80.10 | 79.40 | 0.70 | 0.89 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1992 | 76.40 | 75.80 | 0.60 | 0.79 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1993 | 72.82 | 72.20 | 0.62 | 0.85 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1994 | 69.37 | 68.80 | 0.57 | 0.82 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1995 | 66.07 | 65.50 | 0.57 | 0.86 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1996 | 62.93 | 62.40 | 0.53 | 0.86 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1997 | 59.94 | 59.40 | 0.54 | 0.92 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1998 | 57.11 | 56.60 | 0.51 | 0.91 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 1999 | 54.45 | 53.90 | 0.55 | 1.01 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2000 | 51.93 | 51.40 | 0.53 | 1.03 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2001 | 49.56 | 49.00 | 0.56 | 1.14 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2002 | 47.32 | 46.70 | 0.62 | 1.32 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2003 | 45.20 | 44.60 | 0.60 | 1.34 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2004 | 49.13 | 48.60 | 0.53 | 1.09 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2005 | 41.35 | 40.70 | 0.65 | 1.60 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2006 | 39.60 | 38.90 | 0.70 | 1.79 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2007 | 37.95 | 37.20 | 0.75 | 2.02 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2008 | 36.42 | 35.60 | 0.82 | 2.31 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2009 | 34.97 | 34.10 | 0.87 | 2.55 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2010 | 33.57 | 32.60 | 0.97 | 2.98 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2011 | 32.24 | 31.20 | 1.04 | 3.34 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2012 | 30.96 | 29.90 | 1.06 | 3.54 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2013 | 29.73 | 28.60 | 1.13 | 3.95 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2014 | 28.56 | 27.30 | 1.26 | 4.60 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2015 | 27.44 | 26.10 | 1.34 | 5.12 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2016 | 26.37 | 25.00 | 1.37 | 5.49 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2017 | 25.38 | 23.80 | 1.58 | 6.62 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2018 | 24.46 | 22.80 | 1.66 | 7.27 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2019 | 23.61 | 21.80 | 1.81 | 8.31 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2020 | 22.79 | 20.80 | 1.99 | 9.56 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2021 | 22.02 | 19.90 | 2.12 | 10.65 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2022 | 21.29 | 19.10 | 2.19 | 11.48 | keduanya | vintage berbeda |  |
| SH.DYN.MORT | 2023 | 20.62 | 18.40 | 2.22 | 12.09 | keduanya | vintage berbeda |  |

### P5: Rasio kematian ibu: WHO vs WDI (konteks nasional)

Jenis **selisih**; kategori pasangan: **vintage berbeda**. Vintage; tidak ada padanan BPS di paket.

Rincian: rincian total keduanya.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.STA.MMRT | 1985 | 473.59 | 474.00 | -0.41 | -0.09 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1986 | 455.19 | 455.00 | 0.19 | 0.04 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1987 | 437.24 | 437.00 | 0.24 | 0.06 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1988 | 431.30 | 431.00 | 0.30 | 0.07 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1989 | 401.83 | 402.00 | -0.17 | -0.04 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1990 | 391.72 | 392.00 | -0.28 | -0.07 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1991 | 378.09 | 378.00 | 0.09 | 0.02 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1992 | 359.27 | 359.00 | 0.27 | 0.08 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1993 | 326.63 | 327.00 | -0.37 | -0.11 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1994 | 332.52 | 333.00 | -0.48 | -0.14 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1995 | 334.49 | 334.00 | 0.49 | 0.15 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1996 | 330.95 | 331.00 | -0.05 | -0.02 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1997 | 322.80 | 323.00 | -0.20 | -0.06 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1998 | 317.30 | 317.00 | 0.30 | 0.09 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 1999 | 320.56 | 321.00 | -0.44 | -0.14 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2000 | 311.24 | 311.00 | 0.24 | 0.08 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2001 | 300.20 | 300.00 | 0.20 | 0.07 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2002 | 283.48 | 283.00 | 0.48 | 0.17 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2003 | 278.89 | 279.00 | -0.11 | -0.04 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2004 | 283.31 | 283.00 | 0.31 | 0.11 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2005 | 268.07 | 268.00 | 0.07 | 0.03 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2006 | 264.15 | 264.00 | 0.15 | 0.06 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2007 | 256.65 | 257.00 | -0.35 | -0.13 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2008 | 250.90 | 251.00 | -0.10 | -0.04 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2009 | 245.57 | 246.00 | -0.43 | -0.18 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2010 | 241.86 | 242.00 | -0.14 | -0.06 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2011 | 230.46 | 230.00 | 0.46 | 0.20 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2012 | 220.28 | 220.00 | 0.28 | 0.13 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2013 | 208.47 | 208.00 | 0.47 | 0.23 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2014 | 198.42 | 198.00 | 0.42 | 0.21 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2015 | 190.19 | 190.00 | 0.19 | 0.10 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2016 | 181.75 | 182.00 | -0.25 | -0.14 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2017 | 173.12 | 173.00 | 0.12 | 0.07 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2018 | 168.11 | 168.00 | 0.11 | 0.06 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2019 | 161.19 | 161.00 | 0.19 | 0.12 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2020 | 184.44 | 184.00 | 0.44 | 0.24 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2021 | 226.46 | 226.00 | 0.46 | 0.20 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2022 | 148.24 | 148.00 | 0.24 | 0.16 | keduanya | vintage berbeda |  |
| SH.STA.MMRT | 2023 | 140.50 | 140.00 | 0.50 | 0.36 | keduanya | vintage berbeda |  |

### P1J: Kematian balita: BPS vs rata-rata WHO/WDI pada jendela rujukan 5 tahun

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (survei SDKI vs estimasi model UN IGME); periode rujukan sudah disamakan dengan merata-ratakan pembanding pada 5 tahun sebelum survei.

Rincian: WHO rincian total (jenis kelamin dan kuintil TOTAL); BPS baris Indonesia.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| MDG_0000000007 | 2012 | 40.00 | 35.03 | 4.97 | 14.18 | keduanya | metode berbeda | pembanding = rata-rata 2007–2011 (jendela rujukan survei) |
| MDG_0000000007 | 2017 | 32.00 | 28.61 | 3.39 | 11.84 | keduanya | metode berbeda | pembanding = rata-rata 2012–2016 (jendela rujukan survei) |
| SH.DYN.MORT | 2012 | 40.00 | 34.14 | 5.86 | 17.16 | keduanya | metode berbeda | pembanding = rata-rata 2007–2011 (jendela rujukan survei) |
| SH.DYN.MORT | 2017 | 32.00 | 27.38 | 4.62 | 16.87 | keduanya | metode berbeda | pembanding = rata-rata 2012–2016 (jendela rujukan survei) |
