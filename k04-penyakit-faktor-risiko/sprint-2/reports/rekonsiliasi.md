# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | MALARIA_EST_INCIDENCE | selisih | 12 | 12 | 12 | -3.17 | 75.83 | definisi berbeda (12) |
| P1 | SH.MLR.INCD.P3 | selisih | 12 | 12 | 12 | -3.18 | 75.83 | definisi berbeda (12) |
| P2 | M_Est_tob_curr_std | selisih | 11 | 5 | 4 | -9.02 | 23.84 | tanpa pasangan (7), definisi berbeda (4) |
| P3 | NCDMORT3070 | konteks | 12 | 4 | 0 |  |  | definisi berbeda (12) |
| P4 | SH.MLR.INCD.P3 | selisih | 24 | 24 | 24 | 0.00 | 0.07 | vintage berbeda (24) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 71.52% (28 baris); semua pasangan termasuk antarpembanding: 48.17% (52 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 25, P2 5, P3 10, P4 1.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Malaria: kasus dilaporkan per 1.000 penduduk (BPS) vs estimasi per 1.000 penduduk berisiko (WHO, WDI)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi).

Rincian: tanpa rincian di ketiganya.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| MALARIA_EST_INCIDENCE | 2010 | 1.96 | 8.09 | -6.13 | -75.76 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2011 | 1.75 | 7.26 | -5.51 | -75.90 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2012 | 1.69 | 7.11 | -5.42 | -76.24 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2013 | 1.38 | 5.98 | -4.60 | -76.92 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2014 | 0.99 | 4.49 | -3.50 | -77.96 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2015 | 0.85 | 3.97 | -3.12 | -78.59 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2016 | 0.88 | 4.11 | -3.23 | -78.58 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2017 | 0.99 | 2.78 | -1.79 | -64.44 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2018 | 0.84 | 2.45 | -1.61 | -65.77 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2019 | 0.93 | 2.84 | -1.91 | -67.27 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2020 | 0.94 | 2.80 | -1.86 | -66.42 | keduanya | definisi berbeda |  |
| MALARIA_EST_INCIDENCE | 2021 | 1.12 | 2.93 | -1.81 | -61.81 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2010 | 1.96 | 8.09 | -6.13 | -75.77 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2011 | 1.75 | 7.26 | -5.51 | -75.90 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2012 | 1.69 | 7.11 | -5.42 | -76.23 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2013 | 1.38 | 5.98 | -4.60 | -76.92 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2014 | 0.99 | 4.49 | -3.50 | -77.95 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2015 | 0.85 | 3.97 | -3.12 | -78.59 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2016 | 0.88 | 4.11 | -3.23 | -78.59 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2017 | 0.99 | 2.78 | -1.79 | -64.39 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2018 | 0.84 | 2.45 | -1.61 | -65.71 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2019 | 0.93 | 1.96 | -1.03 | -52.55 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2020 | 0.94 | 1.93 | -0.99 | -51.30 | keduanya | definisi berbeda |  |
| SH.MLR.INCD.P3 | 2021 | 1.12 | 1.56 | -0.44 | -28.21 | keduanya | definisi berbeda |  |

### P2: Merokok (BPS, kasar, rokok) vs penggunaan tembakau (WHO, distandarkan umur)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan.

Rincian: WHO rincian total jenis kelamin.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| M_Est_tob_curr_std | 2015 | 30.08 | 37.10 | -7.02 | -18.92 | keduanya | definisi berbeda |  |
| M_Est_tob_curr_std | 2016 | 28.97 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2017 | 29.25 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2018 | 32.20 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2019 | 29.03 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2020 | 28.69 | 37.80 | -9.11 | -24.10 | keduanya | definisi berbeda |  |
| M_Est_tob_curr_std | 2021 | 28.96 | 37.90 | -8.94 | -23.59 | keduanya | definisi berbeda |  |
| M_Est_tob_curr_std | 2022 | 28.26 | 38.20 | -9.94 | -26.02 | keduanya | definisi berbeda |  |
| M_Est_tob_curr_std | 2023 | 28.62 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2024 | 28.99 |  |  |  | hanya_utama | tanpa pasangan |  |
| M_Est_tob_curr_std | 2025 | 28.68 | 38.70 |  |  | keduanya | tanpa pasangan | tahun proyeksi, tidak dibandingkan |

### P3: Hipertensi (BPS) vs kematian PTM 30–70 (WHO): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: prevalensi faktor risiko vs probabilitas kematian.

Rincian: WHO rincian total jenis kelamin.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| NCDMORT3070 | 2007 | 31.70 | 26.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NCDMORT3070 | 2008 |  | 26.20 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2009 |  | 26.10 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2010 |  | 26.00 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2011 |  | 25.70 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2012 |  | 25.50 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2013 | 25.80 | 25.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NCDMORT3070 | 2014 |  | 25.10 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2015 |  | 25.00 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2016 | 30.90 | 24.70 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NCDMORT3070 | 2017 |  | 24.50 |  |  | hanya_pembanding | definisi berbeda |  |
| NCDMORT3070 | 2018 | 34.10 | 24.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |

### P4: Malaria WHO vs WDI (estimasi yang sama, rilis berbeda)

Jenis **selisih**; kategori pasangan: **vintage berbeda**. Vintage.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.MLR.INCD.P3 | 2000 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2001 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2002 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2003 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2004 | 4.77 | 4.77 | -0.00 | -0.00 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2005 | 5.14 | 5.14 | 0.00 | 0.05 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2006 | 5.92 | 5.92 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2007 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2008 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2009 | 5.28 | 5.28 | 0.00 | 0.07 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2010 | 8.09 | 8.09 | -0.00 | -0.06 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2011 | 7.26 | 7.26 | 0.00 | 0.02 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2012 | 7.11 | 7.11 | 0.00 | 0.02 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2013 | 5.98 | 5.98 | -0.00 | -0.03 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2014 | 4.49 | 4.49 | 0.00 | 0.06 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2015 | 3.97 | 3.97 | 0.00 | 0.00 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2016 | 4.11 | 4.11 | -0.00 | -0.02 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2017 | 2.78 | 2.78 | 0.00 | 0.14 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2018 | 2.45 | 2.45 | 0.00 | 0.17 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2019 | 2.84 | 1.96 | 0.88 | 44.99 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2020 | 2.80 | 1.93 | 0.87 | 45.04 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2021 | 2.93 | 1.56 | 1.37 | 87.99 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2022 | 4.14 | 1.99 | 2.15 | 108.25 | keduanya | vintage berbeda |  |
| SH.MLR.INCD.P3 | 2023 | 3.88 | 1.81 | 2.07 | 114.12 | keduanya | vintage berbeda |  |
