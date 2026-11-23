# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SI.DST.50MD | selisih | 6 | 6 | 6 | 2.17 | 23.45 | definisi berbeda (6) |
| P2 | SI.POV.DDAY | selisih | 26 | 26 | 26 | -1.15 | 4.78 | cakupan berbeda (26) |
| P3 |  | konteks | 5 | 0 | 0 |  |  | tanpa pasangan (5) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 23.45% (6 baris); semua pasangan termasuk antarpembanding: 4.95% (32 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 27, P2 7.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Di bawah 50% median: BPS vs WDI

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi dan metode: BPS menyebut pendapatan; WDI pendapatan atau konsumsi per kapita dengan median PPP.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SI.DST.50MD | 2018 | 12.63 | 10.30 | 2.33 | 22.62 | keduanya | definisi berbeda | None |
| SI.DST.50MD | 2019 | 11.93 | 9.70 | 2.23 | 22.99 | keduanya | definisi berbeda | None |
| SI.DST.50MD | 2020 | 11.99 | 9.60 | 2.39 | 24.90 | keduanya | definisi berbeda | None |
| SI.DST.50MD | 2021 | 11.61 | 9.50 | 2.11 | 22.21 | keduanya | definisi berbeda | None |
| SI.DST.50MD | 2022 | 10.16 | 8.20 | 1.96 | 23.90 | keduanya | definisi berbeda | None |
| SI.DST.50MD | 2023 | 9.44 | 7.50 | 1.94 | 25.87 | keduanya | definisi berbeda | None |

### P2: Kemiskinan pekerja (ILO) vs kemiskinan ekstrem penduduk (WDI)

Jenis **selisih**; kategori pasangan: **cakupan berbeda**. Populasi berbeda (pekerja vs seluruh penduduk); garis kemiskinan sama (US$3 PPP 2021).

Rincian: ILO total jenis kelamin dan umur 15+.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SI.POV.DDAY | 2000 | 63.86 | 65.70 | -1.84 | -2.81 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2001 | 60.13 | 62.30 | -2.16 | -3.48 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2002 | 45.93 | 46.80 | -0.87 | -1.85 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2003 | 43.59 | 45.50 | -1.91 | -4.21 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2004 | 43.36 | 45.40 | -2.04 | -4.49 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2005 | 39.05 | 41.10 | -2.05 | -4.99 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2006 | 44.52 | 46.80 | -2.28 | -4.88 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2007 | 39.08 | 41.10 | -2.02 | -4.91 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2008 | 36.19 | 38.00 | -1.81 | -4.76 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2009 | 36.08 | 37.90 | -1.82 | -4.80 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2010 | 32.55 | 34.10 | -1.55 | -4.56 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2011 | 29.77 | 31.20 | -1.43 | -4.59 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2012 | 24.27 | 26.60 | -2.33 | -8.74 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2013 | 25.98 | 27.20 | -1.22 | -4.50 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2014 | 24.62 | 25.70 | -1.08 | -4.21 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2015 | 20.89 | 21.60 | -0.71 | -3.27 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2016 | 17.82 | 18.00 | -0.18 | -1.01 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2017 | 15.02 | 14.80 | 0.22 | 1.51 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2018 | 13.14 | 12.50 | 0.64 | 5.10 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2019 | 11.81 | 10.90 | 0.91 | 8.39 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2020 | 11.00 | 9.80 | 1.20 | 12.20 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2021 | 9.88 | 8.60 | 1.28 | 14.87 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2022 | 9.22 | 7.90 | 1.32 | 16.77 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2023 | 7.89 | 6.70 | 1.19 | 17.75 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2024 | 6.39 | 5.40 | 0.99 | 18.30 | keduanya | cakupan berbeda | None |
| SI.POV.DDAY | 2025 | 5.64 | 3.70 | 1.94 | 52.49 | keduanya | cakupan berbeda | None |

### P3: Layanan dasar, pendapatan pemerintah (BPS) dan perlindungan sosial, porsi upah (ILO): konteks

Jenis **konteks**; kategori pasangan: **tanpa pasangan**. Tidak ada padanan langsung di paket.

Rincian: layanan air minum sebagai contoh.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2019 | 42.84 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2020 | 42.31 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2021 | 43.81 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2022 | 44.94 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2023 | 44.95 |  |  |  | hanya_utama | tanpa pasangan | None |
