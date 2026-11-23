# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SE.PRE.ENRR | selisih | 11 | 4 | 4 | -25.84 | 41.61 | tanpa pasangan (7), definisi berbeda (4) |
| P2 | IT.NET.USER.ZS | konteks | 11 | 10 | 0 |  |  | definisi berbeda (11) |
| P3 | var1447 | konteks | 11 | 11 | 0 |  |  | cakupan berbeda (11) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 41.61% (4 baris); semua pasangan termasuk antarpembanding: 41.61% (4 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 45, P2 22.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: APK PAUD: BPS (3–6 tahun) vs WDI prasekolah (umur resmi)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (kelompok umur acuan dan jenis layanan PAUD vs pendidikan prasekolah).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.PRE.ENRR | 2015 | 35.18 | 47.35 | -12.17 | -25.70 | keduanya | definisi berbeda |  |
| SE.PRE.ENRR | 2016 | 34.62 | 61.88 | -27.26 | -44.05 | keduanya | definisi berbeda |  |
| SE.PRE.ENRR | 2017 | 33.84 | 63.19 | -29.35 | -46.45 | keduanya | definisi berbeda |  |
| SE.PRE.ENRR | 2018 | 37.92 | 62.34 | -24.42 | -39.18 | keduanya | definisi berbeda |  |
| SE.PRE.ENRR | 2019 | 36.93 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2020 | 37.52 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2021 | 35.59 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2022 | 35.28 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2023 | 36.36 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2024 | 36.03 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.PRE.ENRR | 2025 | 36.19 |  |  |  | hanya_utama | tanpa pasangan |  |

### P2: Telepon genggam (BPS) vs pengguna internet (WDI): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Konsep berbeda: kepemilikan perangkat vs penggunaan internet.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| IT.NET.USER.ZS | 2015 | 56.92 | 22.06 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2016 | 58.30 | 25.45 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2017 | 59.59 | 32.34 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2018 | 62.41 | 39.90 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2019 | 63.53 | 47.69 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2020 | 62.84 | 53.73 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2021 | 65.87 | 62.10 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2022 | 67.88 | 66.48 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2023 | 67.29 | 69.21 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2024 | 68.65 | 72.78 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| IT.NET.USER.ZS | 2025 | 70.75 |  |  |  | hanya_utama | definisi berbeda |  |

### P3: Keterampilan TIK 15–24 vs 15–59 (BPS dengan BPS)

Jenis **konteks**; kategori pasangan: **cakupan berbeda**. Kelompok umur berbeda; tidak dijumlah atau dirata-rata.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| var1447 | 2015 | 51.83 | 27.04 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2016 | 58.21 | 31.83 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2017 | 68.93 | 40.48 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2018 | 77.05 | 49.73 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2019 | 83.58 | 58.22 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2020 | 87.17 | 64.26 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2021 | 91.83 | 70.17 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2022 | 93.21 | 75.16 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2023 | 94.31 | 79.03 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2024 | 95.51 | 82.75 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1447 | 2025 | 96.50 | 87.14 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
