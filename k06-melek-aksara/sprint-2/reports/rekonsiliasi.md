# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | tabel:sdg4_amh_rinci | selisih | 12 | 12 | 12 | 0.00 | 0.00 | tidak berselisih (11), belum terjelaskan (1) |
| P2 | SE.ADT.LITR.ZS | selisih | 12 | 5 | 5 | -0.00 | 0.00 | tanpa pasangan (7), metode berbeda (4), tidak berselisih (1) |
| P3 | SE.ADT.LITR.ZS | selisih | 17 | 8 | 8 | -0.00 | 0.00 | tanpa pasangan (9), metode berbeda (7), tidak berselisih (1) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 0.00% (25 baris); semua pasangan termasuk antarpembanding: 0.00% (25 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 5, P2 8, P3 5.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Total tabel rinci vs tabel ringkas var1458 (BPS dengan BPS)

Jenis **selisih**; kategori pasangan: **belum terjelaskan**. Dua tabel penerbit yang sama; selisih (bila ada) dilaporkan, tidak disamakan paksa.

Rincian: rincian total = perkotaan+perdesaan dan laki-laki+perempuan.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| tabel:sdg4_amh_rinci | 2014 | 95.12 | 95.12 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2015 | 95.22 | 95.22 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2016 | 95.38 | 95.38 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2017 | 95.50 | 95.92 | -0.42 | -0.44 | keduanya | belum terjelaskan | None |
| tabel:sdg4_amh_rinci | 2018 | 95.66 | 95.66 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2019 | 95.90 | 95.90 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2020 | 96.00 | 96.00 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2021 | 96.04 | 96.04 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2022 | 96.35 | 96.35 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2023 | 96.53 | 96.53 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2024 | 96.67 | 96.67 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| tabel:sdg4_amh_rinci | 2025 | 97.10 | 97.10 | 0.00 | 0.00 | keduanya | tidak berselisih | None |

### P2: Melek aksara BPS (Indonesia) vs WDI (UNESCO)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (Susenas vs kompilasi UNESCO dari sensus/survei).

Rincian: keduanya penduduk 15+ tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.ADT.LITR.ZS | 2014 | 95.12 | 95.12 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2015 | 95.22 | 95.22 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2016 | 95.38 | 95.38 | 0.00 | 0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2017 | 95.50 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2018 | 95.66 | 95.66 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2019 | 95.90 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2020 | 96.00 | 96.00 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SE.ADT.LITR.ZS | 2021 | 96.04 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2022 | 96.35 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2023 | 96.53 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2024 | 96.67 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2025 | 97.10 |  |  |  | hanya_utama | tanpa pasangan | None |

### P3: Melek aksara tabel rinci (2009–2025) vs WDI

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode.

Rincian: rincian total.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.ADT.LITR.ZS | 2009 | 92.58 | 92.58 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2010 | 92.91 | 92.32 | 0.59 | 0.64 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2011 | 92.81 | 92.81 | 0.00 | 0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2012 | 93.25 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2013 | 93.92 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2014 | 95.12 | 95.12 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2015 | 95.22 | 95.22 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2016 | 95.38 | 95.38 | 0.00 | 0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2017 | 95.92 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2018 | 95.66 | 95.66 | -0.00 | -0.00 | keduanya | metode berbeda | None |
| SE.ADT.LITR.ZS | 2019 | 95.90 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2020 | 96.00 | 96.00 | 0.00 | 0.00 | keduanya | tidak berselisih | None |
| SE.ADT.LITR.ZS | 2021 | 96.04 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2022 | 96.35 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2023 | 96.53 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2024 | 96.67 |  |  |  | hanya_utama | tanpa pasangan | None |
| SE.ADT.LITR.ZS | 2025 | 97.10 |  |  |  | hanya_utama | tanpa pasangan | None |
