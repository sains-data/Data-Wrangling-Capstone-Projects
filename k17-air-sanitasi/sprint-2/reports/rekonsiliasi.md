# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | WSH_WATER_SAFELY_MANAGED | selisih | 6 | 3 | 3 | 13.82 | 46.08 | definisi berbeda (3), tanpa pasangan (3) |
| P1 | SH.H2O.SMDW.ZS | selisih | 6 | 5 | 5 | 13.76 | 45.78 | definisi berbeda (5), tanpa pasangan (1) |
| P2 | SH.H2O.BASW.ZS | selisih | 33 | 15 | 15 | -31.01 | 39.39 | tanpa pasangan (18), definisi berbeda (15) |
| P3 | WSH_HYGIENE_BASIC | selisih | 10 | 7 | 7 | -0.32 | 0.99 | definisi berbeda (7), tanpa pasangan (3) |
| P4 | SH.H2O.SMDW.ZS | selisih | 23 | 23 | 23 | -0.02 | 0.10 | vintage berbeda (23) |
| P5 |  | konteks | 14 | 0 | 0 |  |  | definisi berbeda (14) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 40.18% (30 baris); semua pasangan termasuk antarpembanding: 0.99% (53 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 40, P3 10, P4 2.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Air minum aman: BPS (rumah tangga) vs WHO dan WDI (penduduk)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (satuan analisis rumah tangga vs penduduk) dan metode (JMP memodelkan dari banyak survei).

Rincian: WHO rincian total daerah.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| WSH_WATER_SAFELY_MANAGED | 2020 | 42.31 | 29.71 | 12.60 | 42.39 | keduanya | definisi berbeda | None |
| WSH_WATER_SAFELY_MANAGED | 2021 | 43.81 | 29.99 | 13.82 | 46.08 | keduanya | definisi berbeda | None |
| WSH_WATER_SAFELY_MANAGED | 2022 | 44.94 | 30.27 | 14.67 | 48.48 | keduanya | definisi berbeda | None |
| WSH_WATER_SAFELY_MANAGED | 2023 | 44.95 |  |  |  | hanya_utama | tanpa pasangan | None |
| WSH_WATER_SAFELY_MANAGED | 2024 | 44.19 |  |  |  | hanya_utama | tanpa pasangan | None |
| WSH_WATER_SAFELY_MANAGED | 2025 | 44.24 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.SMDW.ZS | 2020 | 42.31 | 29.77 | 12.54 | 42.12 | keduanya | definisi berbeda | None |
| SH.H2O.SMDW.ZS | 2021 | 43.81 | 30.05 | 13.76 | 45.78 | keduanya | definisi berbeda | None |
| SH.H2O.SMDW.ZS | 2022 | 44.94 | 30.33 | 14.61 | 48.17 | keduanya | definisi berbeda | None |
| SH.H2O.SMDW.ZS | 2023 | 44.95 | 30.40 | 14.55 | 47.88 | keduanya | definisi berbeda | None |
| SH.H2O.SMDW.ZS | 2024 | 44.19 | 30.46 | 13.73 | 45.07 | keduanya | definisi berbeda | None |
| SH.H2O.SMDW.ZS | 2025 | 44.24 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: Air minum layak (BPS) vs setidaknya dasar (WDI)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (layak vs basic: syarat waktu ambil air ≤ 30 menit di WDI; rumus BPS berganti 2011).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.H2O.BASW.ZS | 1993 | 37.73 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1994 | 37.74 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1995 | 38.03 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1996 | 41.18 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1997 | 42.76 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1998 | 41.95 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 1999 | 42.18 |  |  |  | hanya_utama | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2000 | 37.51 | 75.78 | -38.27 | -50.50 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2001 | 48.68 | 76.78 | -28.10 | -36.59 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2002 | 48.33 | 77.76 | -29.43 | -37.85 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2003 | 47.73 | 78.74 | -31.01 | -39.39 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2004 | 48.81 | 79.71 | -30.90 | -38.77 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2005 | 47.62 | 80.67 | -33.05 | -40.97 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2006 | 47.79 | 81.62 | -33.83 | -41.45 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2007 | 48.31 | 82.56 | -34.25 | -41.49 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2008 | 46.45 | 83.49 | -37.04 | -44.36 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2009 | 47.71 | 84.39 | -36.68 | -43.47 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2010 | 44.19 | 85.17 | -40.98 | -48.11 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2011 |  | 85.64 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2012 |  | 86.07 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2013 |  | 86.50 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2014 |  | 86.91 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2015 |  | 87.30 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2016 |  | 87.68 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2017 |  | 88.05 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2018 |  | 88.41 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2019 |  | 88.75 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2020 |  | 89.09 |  |  | hanya_pembanding | tanpa pasangan | None |
| SH.H2O.BASW.ZS | 2021 | 90.78 | 89.40 | 1.38 | 1.54 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2022 | 91.05 | 89.71 | 1.34 | 1.49 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2023 | 91.72 | 89.36 | 2.36 | 2.64 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2024 | 92.64 | 89.01 | 3.63 | 4.08 | keduanya | definisi berbeda | None |
| SH.H2O.BASW.ZS | 2025 | 93.22 |  |  |  | hanya_utama | tanpa pasangan | None |

### P3: Cuci tangan dengan sabun dan air: BPS vs WHO

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (rumah tangga vs penduduk); 2016 dari Susenas MKP.

Rincian: WHO rincian total daerah.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| WSH_HYGIENE_BASIC | 2016 | 66.28 | 77.69 | -11.41 | -14.69 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2017 | 68.16 | 77.95 | -9.79 | -12.56 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2018 | 78.87 | 78.19 | 0.68 | 0.87 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2019 | 76.07 | 78.42 | -2.35 | -2.99 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2020 | 78.30 | 78.62 | -0.32 | -0.41 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2021 | 79.59 | 78.81 | 0.78 | 0.99 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2022 | 79.33 | 78.99 | 0.34 | 0.44 | keduanya | definisi berbeda | None |
| WSH_HYGIENE_BASIC | 2023 | 80.15 |  |  |  | hanya_utama | tanpa pasangan | None |
| WSH_HYGIENE_BASIC | 2024 | 80.85 |  |  |  | hanya_utama | tanpa pasangan | None |
| WSH_HYGIENE_BASIC | 2025 | 81.60 |  |  |  | hanya_utama | tanpa pasangan | None |

### P4: Air minum aman: WHO vs WDI (keduanya JMP)

Jenis **selisih**; kategori pasangan: **vintage berbeda**. Vintage.

Rincian: rincian total.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SH.H2O.SMDW.ZS | 2000 | 23.54 | 23.51 | 0.03 | 0.12 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2001 | 23.88 | 23.85 | 0.02 | 0.10 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2002 | 24.21 | 24.19 | 0.02 | 0.08 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2003 | 24.54 | 24.53 | 0.01 | 0.06 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2004 | 24.87 | 24.86 | 0.01 | 0.04 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2005 | 25.20 | 25.20 | 0.00 | 0.02 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2006 | 25.53 | 25.53 | -0.00 | -0.00 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2007 | 25.85 | 25.86 | -0.00 | -0.02 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2008 | 26.17 | 26.18 | -0.01 | -0.03 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2009 | 26.49 | 26.51 | -0.01 | -0.05 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2010 | 26.81 | 26.82 | -0.02 | -0.07 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2011 | 27.11 | 27.13 | -0.02 | -0.08 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2012 | 27.41 | 27.43 | -0.03 | -0.09 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2013 | 27.70 | 27.73 | -0.03 | -0.11 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2014 | 28.00 | 28.03 | -0.03 | -0.12 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2015 | 28.29 | 28.33 | -0.04 | -0.13 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2016 | 28.58 | 28.62 | -0.04 | -0.15 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2017 | 28.87 | 28.91 | -0.05 | -0.16 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2018 | 29.15 | 29.20 | -0.05 | -0.17 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2019 | 29.43 | 29.49 | -0.05 | -0.18 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2020 | 29.71 | 29.77 | -0.06 | -0.19 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2021 | 29.99 | 30.05 | -0.06 | -0.20 | keduanya | vintage berbeda | None |
| SH.H2O.SMDW.ZS | 2022 | 30.27 | 30.33 | -0.06 | -0.21 | keduanya | vintage berbeda | None |

### P5: Bantuan pembangunan air dan sanitasi (WHO): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: uang, bukan cakupan layanan.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2010 | 263.21 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2011 | 266.04 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2012 | 211.60 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2013 | 181.92 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2014 | 125.43 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2015 | 121.56 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2016 | 118.42 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2017 | 104.91 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2018 | 115.26 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2019 | 119.93 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2020 | 161.94 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2021 | 178.60 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2022 | 178.10 |  |  |  | hanya_utama | definisi berbeda | None |
|  | 2023 | 266.22 |  |  |  | hanya_utama | definisi berbeda | None |
