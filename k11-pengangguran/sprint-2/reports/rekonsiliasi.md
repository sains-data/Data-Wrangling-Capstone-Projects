# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SDG_0852_SEX_AGE_RT | selisih | 39 | 24 | 24 | 1.86 | 37.19 | definisi berbeda (24), tanpa pasangan (15) |
| P2 | SL.UEM.TOTL.ZS | selisih | 43 | 32 | 32 | 0.00 | 0.00 | tidak berselisih (31), tanpa pasangan (11), metode berbeda (1) |
| P3 |  | konteks | 9 | 0 | 0 |  |  | tanpa pasangan (9) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 37.19% (24 baris); semua pasangan termasuk antarpembanding: 0.00% (56 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P2 2.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: TPT BPS Agustus vs ILO SDG 8.5.2 (total, rujukan Agustus)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan.

Rincian: ILO total jenis kelamin dan umur 15+; BPS Agustus karena NOTE_SOURCE ILO 'Data reference period: August'.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0852_SEX_AGE_RT | 1986 | 2.70 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1987 | 2.62 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1988 | 2.85 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1989 | 2.81 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1990 | 2.55 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1991 | 2.62 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1992 | 2.74 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1993 | 2.79 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1994 | 4.36 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1996 | 4.87 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1997 | 4.69 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1998 | 5.46 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 1999 | 6.36 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 2000 | 6.08 | 6.08 | 0.00 | 0.03 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2001 | 8.10 | 6.08 | 2.02 | 33.18 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2002 | 9.06 | 6.60 | 2.46 | 37.19 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2003 | 9.67 | 6.66 | 3.01 | 45.24 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2004 | 9.86 | 7.30 | 2.56 | 35.01 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2005 | 11.24 | 7.95 | 3.29 | 41.47 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2006 | 10.28 | 7.55 | 2.73 | 36.14 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2007 | 9.11 | 8.06 | 1.05 | 13.03 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2008 | 8.39 | 7.21 | 1.18 | 16.38 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2009 | 7.87 | 6.11 | 1.76 | 28.89 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2010 | 7.14 | 5.61 | 1.53 | 27.18 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2011 | 7.48 | 5.15 | 2.33 | 45.16 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2012 | 6.13 | 4.47 | 1.66 | 37.20 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2013 | 6.17 | 4.34 | 1.83 | 42.30 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2014 | 5.94 | 4.05 | 1.89 | 46.70 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2015 | 6.18 | 4.51 | 1.67 | 36.91 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2016 | 5.61 | 4.30 | 1.31 | 30.43 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2017 | 5.50 | 3.78 | 1.72 | 45.39 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2018 | 5.30 | 4.39 | 0.91 | 20.81 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2019 | 5.23 | 3.59 | 1.64 | 45.68 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2020 | 7.07 | 4.25 | 2.82 | 66.16 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2021 | 6.49 | 3.83 | 2.66 | 69.58 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2022 | 5.86 | 3.46 | 2.40 | 69.27 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2023 | 5.32 | 3.42 | 1.90 | 55.37 | keduanya | definisi berbeda | None |
| SDG_0852_SEX_AGE_RT | 2024 | 4.91 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0852_SEX_AGE_RT | 2025 | 4.85 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: WDI estimasi nasional vs estimasi model ILO

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SL.UEM.TOTL.ZS | 1976 | 1.92 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1977 | 1.29 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1978 | 2.48 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1980 | 1.66 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1982 | 2.85 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1985 | 2.10 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1986 | 2.59 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1987 | 2.55 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1988 | 2.74 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1990 | 2.54 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1991 | 2.62 | 2.62 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1992 | 2.73 | 2.73 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1993 | 2.78 | 2.78 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1994 | 4.37 | 4.37 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1995 |  | 4.61 |  |  | hanya_pembanding | tanpa pasangan | None |
| SL.UEM.TOTL.ZS | 1996 | 4.86 | 4.86 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1997 | 4.68 | 4.68 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1998 | 5.46 | 5.46 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 1999 | 6.36 | 6.36 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2000 | 6.08 | 6.08 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2001 | 6.08 | 6.08 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2002 | 6.60 | 6.60 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2003 | 6.66 | 6.66 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2004 | 7.30 | 7.30 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2005 | 7.95 | 7.95 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2006 | 7.55 | 7.55 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2007 | 8.06 | 8.06 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2008 | 7.21 | 7.21 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2009 | 6.11 | 6.11 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2010 | 5.61 | 5.61 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2011 | 5.15 | 5.15 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2012 | 4.47 | 4.47 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2013 | 4.34 | 4.34 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2014 | 4.05 | 4.05 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2015 | 4.51 | 4.51 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2016 | 4.30 | 4.30 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2017 | 3.78 | 3.78 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2018 | 4.39 | 4.39 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2019 | 3.59 | 3.59 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2020 | 4.25 | 4.25 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2021 | 3.83 | 3.83 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2022 | 3.46 | 3.46 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SL.UEM.TOTL.ZS | 2023 | 3.42 | 3.31 | 0.12 | 3.51 | keduanya | metode berbeda | None |

### P3: Pengangguran menurut disabilitas (ILO): konteks

Jenis **konteks**; kategori pasangan: **tanpa pasangan**. Tidak ada padanan BPS di paket.

Rincian: disabilitas.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2010 | 2.50 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2016 | 1.63 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2017 | 1.53 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2018 | 2.37 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2019 | 1.80 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2020 | 2.18 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2021 | 1.60 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2022 | 1.46 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2023 | 3.35 |  |  |  | hanya_utama | tanpa pasangan | None |
