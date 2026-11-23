# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SDG_0821_NOC_RT | selisih | 15 | 15 | 15 | -0.10 | 36.30 | metode berbeda (15) |
| P1 | SDG_B821_NOC_RT | selisih | 15 | 15 | 15 | -0.10 | 36.30 | metode berbeda (15) |
| P2 | SL.GDP.PCAP.EM.KD (laju) | selisih | 15 | 15 | 15 | -0.10 | 36.50 | metode berbeda (15) |
| P3 | NV.IND.MANF.ZS | selisih | 14 | 14 | 14 | 0.80 | 3.96 | metode berbeda (14) |
| P4 | SDG_0922_NOC_RT | selisih | 8 | 6 | 6 | 0.25 | 1.73 | metode berbeda (6), tanpa pasangan (2) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 9.50% (65 baris); semua pasangan termasuk antarpembanding: 9.50% (65 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 26, P2 19, P3 29, P4 18.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Laju produktivitas: BPS vs ILO (dua basis harga)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (PDB riil BPS vs estimasi model ILO); proyeksi ILO dikeluarkan.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0821_NOC_RT | 2011 | 6.95 | 3.51 | 3.44 | 97.84 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2012 | 1.23 | 2.88 | -1.65 | -57.34 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2013 | 5.32 | 4.86 | 0.46 | 9.47 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2014 | 3.30 | 3.40 | -0.10 | -3.00 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2015 | 4.70 | 4.02 | 0.68 | 16.97 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2016 | 1.85 | 3.82 | -1.97 | -51.57 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2017 | 2.80 | 2.56 | 0.24 | 9.50 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2018 | 0.79 | 3.01 | -2.22 | -73.78 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2019 | 3.00 | 1.96 | 1.04 | 53.14 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2020 | -1.84 | -1.35 | -0.49 | 36.30 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2021 | 1.65 | 4.54 | -2.89 | -63.63 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2022 | 2.00 | 1.93 | 0.07 | 3.63 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2023 | 1.63 | 2.19 | -0.56 | -25.54 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2024 | 1.55 | 3.66 | -2.11 | -57.68 | keduanya | metode berbeda |  |
| SDG_0821_NOC_RT | 2025 | 3.75 | 3.43 | 0.32 | 9.20 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2011 | 6.95 | 3.51 | 3.44 | 97.84 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2012 | 1.23 | 2.88 | -1.65 | -57.34 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2013 | 5.32 | 4.86 | 0.46 | 9.47 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2014 | 3.30 | 3.40 | -0.10 | -3.00 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2015 | 4.70 | 4.02 | 0.68 | 16.97 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2016 | 1.85 | 3.82 | -1.97 | -51.57 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2017 | 2.80 | 2.56 | 0.24 | 9.50 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2018 | 0.79 | 3.01 | -2.22 | -73.78 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2019 | 3.00 | 1.96 | 1.04 | 53.14 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2020 | -1.84 | -1.35 | -0.49 | 36.30 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2021 | 1.65 | 4.54 | -2.89 | -63.63 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2022 | 2.00 | 1.93 | 0.07 | 3.63 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2023 | 1.63 | 2.19 | -0.56 | -25.54 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2024 | 1.55 | 3.66 | -2.11 | -57.68 | keduanya | metode berbeda |  |
| SDG_B821_NOC_RT | 2025 | 3.75 | 3.43 | 0.32 | 9.20 | keduanya | metode berbeda |  |

### P2: Laju produktivitas BPS vs WDI tingkat PDB per pekerja

Jenis **selisih**; kategori pasangan: **metode berbeda**. WDI tingkat (USD PPP 2021), bukan laju; laju WDI dihitung di Gold sebelum dibandingkan.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SL.GDP.PCAP.EM.KD (laju) | 2011 | 6.95 | 3.51 | 3.44 | 97.77 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2012 | 1.23 | 2.88 | -1.65 | -57.32 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2013 | 5.32 | 4.86 | 0.46 | 9.48 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2014 | 3.30 | 3.40 | -0.10 | -3.02 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2015 | 4.70 | 4.02 | 0.68 | 16.96 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2016 | 1.85 | 3.82 | -1.97 | -51.56 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2017 | 2.80 | 2.56 | 0.24 | 9.49 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2018 | 0.79 | 3.01 | -2.22 | -73.78 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2019 | 3.00 | 1.96 | 1.04 | 53.26 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2020 | -1.84 | -1.35 | -0.49 | 36.50 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2021 | 1.65 | 4.54 | -2.89 | -63.62 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2022 | 2.00 | 1.93 | 0.07 | 3.57 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2023 | 1.63 | 2.19 | -0.56 | -25.50 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2024 | 1.55 | 3.67 | -2.12 | -57.71 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |
| SL.GDP.PCAP.EM.KD (laju) | 2025 | 3.75 | 3.68 | 0.07 | 1.97 | keduanya | metode berbeda | pembanding = laju tahunan WDI dihitung dari tingkat |

### P3: Nilai tambah manufaktur terhadap PDB: BPS vs WDI

Jenis **selisih**; kategori pasangan: **metode berbeda**. Dasar harga belum diketahui di kedua sumber; dicek di Sprint 2.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| NV.IND.MANF.ZS | 2010 | 22.04 | 22.04 | 0.00 | 0.01 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2011 | 22.06 | 21.76 | 0.30 | 1.37 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2012 | 21.97 | 21.45 | 0.52 | 2.42 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2013 | 21.72 | 21.03 | 0.69 | 3.29 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2014 | 21.65 | 21.08 | 0.57 | 2.73 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2015 | 21.54 | 20.99 | 0.55 | 2.64 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2016 | 21.38 | 20.52 | 0.86 | 4.18 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2017 | 21.22 | 20.16 | 1.06 | 5.26 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2018 | 21.04 | 19.86 | 1.18 | 5.92 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2019 | 20.79 | 19.70 | 1.09 | 5.51 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2020 | 20.61 | 19.87 | 0.74 | 3.74 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2021 | 20.55 | 19.24 | 1.31 | 6.79 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2022 | 20.47 | 18.34 | 2.13 | 11.64 | keduanya | metode berbeda |  |
| NV.IND.MANF.ZS | 2023 | 20.39 | 18.67 | 1.72 | 9.23 | keduanya | metode berbeda |  |

### P4: Tenaga kerja manufaktur: BPS vs ILO

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (olahan Sakernas yang sama).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0922_NOC_RT | 2018 | 14.68 | 14.39 | 0.29 | 2.01 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2019 | 14.91 | 14.38 | 0.53 | 3.66 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2020 | 13.61 | 13.78 | -0.17 | -1.23 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2021 | 14.27 | 13.92 | 0.35 | 2.53 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2022 | 14.17 | 13.97 | 0.20 | 1.46 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2023 | 13.83 | 13.70 | 0.13 | 0.96 | keduanya | metode berbeda |  |
| SDG_0922_NOC_RT | 2024 | 13.83 |  |  |  | hanya_utama | tanpa pasangan |  |
| SDG_0922_NOC_RT | 2025 | 13.86 |  |  |  | hanya_utama | tanpa pasangan |  |
