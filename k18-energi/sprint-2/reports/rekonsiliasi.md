# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | EG.ELC.ACCS.ZS | selisih | 33 | 31 | 31 | -2.82 | 3.13 | definisi berbeda (31), tanpa pasangan (2) |
| P2 | EG.CFT.ACCS.ZS | selisih | 21 | 16 | 16 | -0.86 | 1.51 | definisi berbeda (16), tanpa pasangan (5) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 2.74% (47 baris); semua pasangan termasuk antarpembanding: 2.74% (47 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 2, P2 4.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Listrik: BPS (rumah tangga, PLN saja) vs WDI (penduduk, semua sumber)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (PLN saja vs semua sumber listrik; rumah tangga vs penduduk).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| EG.ELC.ACCS.ZS | 1993 | 51.83 | 55.43 | -3.60 | -6.49 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1994 | 57.51 | 62.80 | -5.29 | -8.42 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1995 | 63.10 | 66.86 | -3.76 | -5.62 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1996 | 68.66 | 72.39 | -3.73 | -5.15 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1997 | 73.77 | 80.30 | -6.53 | -8.13 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1998 | 78.13 | 80.94 | -2.81 | -3.47 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 1999 | 81.70 | 83.73 | -2.03 | -2.42 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2000 | 83.97 | 86.30 | -2.33 | -2.70 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2001 | 83.48 | 86.30 | -2.82 | -3.27 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2002 | 85.38 | 87.60 | -2.22 | -2.53 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2003 | 85.02 | 87.90 | -2.88 | -3.28 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2004 | 86.56 | 89.00 | -2.44 | -2.74 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2005 |  | 84.80 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.ELC.ACCS.ZS | 2006 | 87.76 | 90.60 | -2.84 | -3.13 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2007 | 88.37 | 91.10 | -2.73 | -3.00 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2008 | 89.46 | 92.70 | -3.24 | -3.50 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2009 | 89.29 | 93.60 | -4.31 | -4.60 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2010 | 89.47 | 94.20 | -4.73 | -5.02 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2011 | 90.51 | 94.80 | -4.29 | -4.53 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2012 | 92.13 | 96.00 | -3.87 | -4.03 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2013 | 93.17 | 96.50 | -3.33 | -3.45 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2014 | 93.97 | 97.00 | -3.03 | -3.12 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2015 | 94.44 | 97.50 | -3.06 | -3.14 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2016 | 94.93 | 97.60 | -2.67 | -2.74 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2017 | 95.99 | 98.10 | -2.11 | -2.15 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2018 | 96.52 | 98.50 | -1.98 | -2.01 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2019 | 96.73 | 98.80 | -2.07 | -2.10 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2020 | 96.95 | 97.00 | -0.05 | -0.05 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2021 | 97.26 | 99.20 | -1.94 | -1.96 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2022 | 97.73 | 100.00 | -2.27 | -2.27 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2023 | 97.93 | 99.40 | -1.47 | -1.48 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2024 | 98.24 | 99.90 | -1.66 | -1.66 | keduanya | definisi berbeda | None |
| EG.ELC.ACCS.ZS | 2025 | 98.46 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: Bahan bakar bersih: BPS (gas/elpiji + listrik, dijumlahkan di Gold) vs WDI

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (kategori bersih; rumah tangga vs penduduk); BPS berakhir 2021.

Rincian: kategori bersih = listrik + gas/elpiji (KATEGORI_BAHAN_BAKAR); minyak tanah tidak bersih.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| EG.CFT.ACCS.ZS | 2001 | 8.22 | 6.00 | 2.22 | 37.00 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2002 |  | 7.00 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.CFT.ACCS.ZS | 2003 |  | 8.00 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.CFT.ACCS.ZS | 2004 |  | 10.00 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.CFT.ACCS.ZS | 2005 |  | 13.00 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.CFT.ACCS.ZS | 2006 |  | 17.00 |  |  | hanya_pembanding | tanpa pasangan | None |
| EG.CFT.ACCS.ZS | 2007 | 10.57 | 22.00 | -11.43 | -51.95 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2008 | 18.68 | 28.00 | -9.32 | -33.29 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2009 | 35.54 | 35.00 | 0.54 | 1.54 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2010 | 41.51 | 42.00 | -0.49 | -1.17 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2011 | 47.40 | 48.00 | -0.60 | -1.25 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2012 | 54.54 | 54.00 | 0.54 | 1.00 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2013 | 58.42 | 60.00 | -1.58 | -2.63 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2014 | 61.88 | 64.00 | -2.12 | -3.31 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2015 | 68.78 | 69.00 | -0.22 | -0.32 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2016 | 72.38 | 73.00 | -0.62 | -0.85 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2017 | 76.14 | 76.00 | 0.14 | 0.18 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2018 | 77.83 | 79.00 | -1.17 | -1.48 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2019 | 79.90 | 81.00 | -1.10 | -1.36 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2020 | 81.98 | 84.00 | -2.02 | -2.40 | keduanya | definisi berbeda | None |
| EG.CFT.ACCS.ZS | 2021 | 83.36 | 86.00 | -2.64 | -3.07 | keduanya | definisi berbeda | None |
