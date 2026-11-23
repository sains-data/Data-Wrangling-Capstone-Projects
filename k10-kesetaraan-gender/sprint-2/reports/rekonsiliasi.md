# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SDG_T552_NOC_RT | selisih | 11 | 8 | 8 | 0.26 | 2.30 | metode berbeda (8), tanpa pasangan (3) |
| P2 | SDG_0552_NOC_RT | selisih | 11 | 1 | 1 | 10.13 | 40.67 | tanpa pasangan (10), definisi berbeda (1) |
| P3 | SP.M18.2024.FE.ZS | selisih | 11 | 1 | 1 | -4.76 | 29.20 | tanpa pasangan (10), metode berbeda (1) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 2.99% (10 baris); semua pasangan termasuk antarpembanding: 2.99% (10 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 7, P2 4, P3 7.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Perempuan manajer: BPS vs ILO seluruh manajemen (T552)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_T552_NOC_RT | 2015 | 22.32 | 22.38 | -0.06 | -0.26 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2016 | 23.60 | 44.78 | -21.18 | -47.30 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2017 | 26.56 | 27.46 | -0.90 | -3.27 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2018 | 28.75 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_T552_NOC_RT | 2019 | 30.37 | 29.57 | 0.80 | 2.72 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2020 | 33.08 | 32.61 | 0.47 | 1.43 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2021 | 32.50 | 32.44 | 0.06 | 0.19 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2022 | 32.26 | 31.66 | 0.59 | 1.88 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2023 | 35.02 | 33.13 | 1.89 | 5.70 | keduanya | metode berbeda | None |
| SDG_T552_NOC_RT | 2024 | 35.49 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_T552_NOC_RT | 2025 | 36.68 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: Perempuan manajer: BPS vs ILO senior dan menengah (0552)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (0552 tanpa manajer junior).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0552_NOC_RT | 2015 | 22.32 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2016 | 23.60 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2017 | 26.56 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2018 | 28.75 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2019 | 30.37 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2020 | 33.08 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2021 | 32.50 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2022 | 32.26 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2023 | 35.02 | 24.89 | 10.13 | 40.67 | keduanya | definisi berbeda | None |
| SDG_0552_NOC_RT | 2024 | 35.49 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0552_NOC_RT | 2025 | 36.68 |  |  |  | hanya_utama | tanpa pasangan | None |

### P3: Perkawinan anak: BPS vs WDI (UNICEF)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017).

Rincian: keduanya perempuan 20–24, sebelum 18.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SP.M18.2024.FE.ZS | 2015 | 12.14 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2016 | 11.11 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2017 | 11.54 | 16.30 | -4.76 | -29.20 | keduanya | metode berbeda | None |
| SP.M18.2024.FE.ZS | 2018 | 11.21 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2019 | 10.82 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2020 | 10.35 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2021 | 9.23 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2022 | 8.06 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2023 | 6.92 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2024 | 5.90 |  |  |  | hanya_utama | tanpa pasangan | None |
| SP.M18.2024.FE.ZS | 2025 | 4.56 |  |  |  | hanya_utama | tanpa pasangan | None |
