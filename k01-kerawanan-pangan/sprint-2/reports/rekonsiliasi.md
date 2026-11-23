# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SN.ITK.DEFC.ZS | selisih | 9 | 8 | 8 | 1.94 | 31.25 | metode berbeda (8), tanpa pasangan (1) |
| P2 | SN.ITK.MSFI.ZS | selisih | 9 | 8 | 8 | -0.06 | 2.72 | metode berbeda (7), tidak berselisih (1), tanpa pasangan (1) |
| P3 | NUTOVERWEIGHTPREV | konteks | 25 | 25 | 0 |  |  | definisi berbeda (25) |
| P3 | NUTRITION_WH_2 | konteks | 25 | 11 | 0 |  |  | definisi berbeda (25) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 16.58% (16 baris); semua pasangan termasuk antarpembanding: 16.58% (16 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 16, P2 2, P3 1.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Ketidakcukupan konsumsi pangan: BPS (Susenas) vs WDI (FAO)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket.

Rincian: keduanya seluruh penduduk tanpa rincian; BPS baris Indonesia.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SN.ITK.DEFC.ZS | 2017 | 8.23 | 6.00 | 2.23 | 37.17 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2018 | 7.92 | 6.00 | 1.92 | 32.00 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2019 | 7.63 | 6.40 | 1.23 | 19.22 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2020 | 8.34 | 6.60 | 1.74 | 26.36 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2021 | 8.49 | 6.70 | 1.79 | 26.72 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2022 | 10.21 | 6.60 | 3.61 | 54.70 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2023 | 8.53 | 6.50 | 2.03 | 31.23 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2024 | 8.27 | 6.30 | 1.97 | 31.27 | keduanya | metode berbeda |  |
| SN.ITK.DEFC.ZS | 2025 | 7.89 |  |  |  | hanya_utama | tanpa pasangan |  |

### P2: Kerawanan pangan sedang atau berat (FIES): BPS vs WDI (FAO)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Sumber data dan cara estimasi berbeda; definisi FIES sama.

Rincian: keduanya seluruh penduduk tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SN.ITK.MSFI.ZS | 2017 | 8.66 | 7.60 | 1.06 | 13.95 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2018 | 6.86 | 7.00 | -0.14 | -2.00 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2019 | 5.42 | 5.80 | -0.38 | -6.55 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2020 | 5.12 | 5.10 | 0.02 | 0.39 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2021 | 4.79 | 4.90 | -0.11 | -2.24 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2022 | 4.85 | 4.70 | 0.15 | 3.19 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2023 | 4.50 | 4.50 | 0.00 | 0.00 | keduanya | tidak berselisih |  |
| SN.ITK.MSFI.ZS | 2024 | 4.02 | 4.20 | -0.18 | -4.29 | keduanya | metode berbeda |  |
| SN.ITK.MSFI.ZS | 2025 | 4.00 |  |  |  | hanya_utama | tanpa pasangan |  |

### P3: Gizi balita WHO (stunting, overweight, wasting): konteks, bukan pasangan BPS

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk.

Rincian: rincian total (jenis kelamin, umur, daerah TOTAL atau kosong).

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| NUTOVERWEIGHTPREV | 2000 | 39.80 | 3.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2001 | 39.60 | 3.40 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2002 | 39.60 | 3.80 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2003 | 39.60 | 4.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2004 | 39.60 | 4.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2005 | 39.60 | 5.10 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2006 | 39.60 | 5.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2007 | 39.30 | 6.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2008 | 38.70 | 6.70 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2009 | 38.00 | 7.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2010 | 37.00 | 7.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2011 | 35.80 | 8.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2012 | 34.60 | 8.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2013 | 33.50 | 8.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2014 | 32.20 | 8.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2015 | 31.00 | 8.40 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2016 | 29.80 | 8.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2017 | 28.50 | 7.70 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2018 | 27.30 | 7.20 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2019 | 26.10 | 6.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2020 | 25.10 | 5.70 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2021 | 24.30 | 4.90 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2022 | 23.70 | 4.10 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2023 | 23.10 | 3.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTOVERWEIGHTPREV | 2024 | 22.60 | 2.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2000 | 39.80 | 5.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2001 | 39.60 | 5.40 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2002 | 39.60 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2003 | 39.60 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2004 | 39.60 | 14.40 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2005 | 39.60 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2006 | 39.60 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2007 | 39.30 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2008 | 38.70 | 14.80 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2009 | 38.00 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2010 | 37.00 | 12.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2011 | 35.80 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2012 | 34.60 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2013 | 33.50 | 13.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2014 | 32.20 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2015 | 31.00 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2016 | 29.80 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2017 | 28.50 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2018 | 27.30 | 10.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2019 | 26.10 | 8.60 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2020 | 25.10 |  |  |  | hanya_utama | definisi berbeda |  |
| NUTRITION_WH_2 | 2021 | 24.30 | 7.10 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2022 | 23.70 | 7.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2023 | 23.10 | 8.40 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| NUTRITION_WH_2 | 2024 | 22.60 |  |  |  | hanya_utama | definisi berbeda |  |
