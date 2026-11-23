# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SDG_0861_SEX_RT | selisih | 11 | 9 | 9 | 0.71 | 3.16 | metode berbeda (9), tanpa pasangan (2) |
| P1 | SL.UEM.NEET.ZS | selisih | 11 | 9 | 9 | 0.71 | 3.16 | metode berbeda (9), tanpa pasangan (2) |
| P2 | SDG_A871_SEX_AGE_RT | selisih | 6 | 1 | 1 | -0.04 | 2.36 | tanpa pasangan (5), cakupan berbeda (1) |
| P3 |  | konteks | 3 | 0 | 0 |  |  | cakupan berbeda (3) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 3.16% (19 baris); semua pasangan termasuk antarpembanding: 3.16% (19 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 34, P2 2.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: NEET 15–24: BPS vs ILO vs WDI

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (olahan Sakernas yang sama); kelompok umur sama (15–24).

Rincian: total jenis kelamin.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0861_SEX_RT | 2015 | 24.77 | 22.92 | 1.85 | 8.08 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2016 | 23.19 | 22.48 | 0.71 | 3.16 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2017 | 21.41 | 21.45 | -0.04 | -0.18 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2018 | 22.15 | 21.74 | 0.41 | 1.90 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2019 | 21.77 | 20.55 | 1.22 | 5.95 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2020 | 24.28 | 21.80 | 2.48 | 11.38 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2021 | 22.40 | 22.45 | -0.05 | -0.24 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2022 | 23.22 | 22.34 | 0.88 | 3.96 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2023 | 22.25 | 21.57 | 0.68 | 3.16 | keduanya | metode berbeda | None |
| SDG_0861_SEX_RT | 2024 | 20.31 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0861_SEX_RT | 2025 | 19.44 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.NEET.ZS | 2015 | 24.77 | 22.92 | 1.85 | 8.08 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2016 | 23.19 | 22.48 | 0.71 | 3.16 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2017 | 21.41 | 21.45 | -0.04 | -0.18 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2018 | 22.15 | 21.74 | 0.41 | 1.90 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2019 | 21.77 | 20.55 | 1.22 | 5.95 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2020 | 24.28 | 21.80 | 2.48 | 11.38 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2021 | 22.40 | 22.45 | -0.05 | -0.24 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2022 | 23.22 | 22.34 | 0.88 | 3.96 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2023 | 22.25 | 21.57 | 0.68 | 3.16 | keduanya | metode berbeda | None |
| SL.UEM.NEET.ZS | 2024 | 20.31 |  |  |  | hanya_utama | tanpa pasangan | None |
| SL.UEM.NEET.ZS | 2025 | 19.44 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: Pekerja anak: BPS (5–17) vs ILO kegiatan ekonomi (15–17)

Jenis **selisih**; kategori pasangan: **cakupan berbeda**. Definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023.

Rincian: ILO umur CLDVERSION_Y15-17, total jenis kelamin.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_A871_SEX_AGE_RT | 2020 | 2.15 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_A871_SEX_AGE_RT | 2021 | 1.74 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_A871_SEX_AGE_RT | 2022 | 1.60 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_A871_SEX_AGE_RT | 2023 | 1.53 | 1.57 | -0.04 | -2.36 | keduanya | cakupan berbeda | None |
| SDG_A871_SEX_AGE_RT | 2024 | 1.93 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_A871_SEX_AGE_RT | 2025 | 1.64 |  |  |  | hanya_utama | tanpa pasangan | None |

### P3: Anak bekerja 7–14 (WDI): konteks

Jenis **konteks**; kategori pasangan: **cakupan berbeda**. Kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2000 | 8.93 |  |  |  | hanya_utama | cakupan berbeda | None |
|  | 2009 | 6.60 |  |  |  | hanya_utama | cakupan berbeda | None |
|  | 2010 | 3.70 |  |  |  | hanya_utama | cakupan berbeda | None |
