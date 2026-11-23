# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SDG_0851_SEX_OCU_NB | selisih | 11 | 8 | 8 | 1,331.91 | 9.34 | metode berbeda (8), tanpa pasangan (3) |
| P2 | SDG_0831_SEX_ECO_RT | selisih | 8 | 4 | 4 | -23.15 | 28.71 | definisi berbeda (4), tanpa pasangan (4) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 13.88% (12 baris); semua pasangan termasuk antarpembanding: 13.88% (12 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 7, P2 2.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Upah per jam: BPS (pekerja) vs ILO (rata-rata penghasilan per jam pekerja)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (pengolahan Sakernas; nominal keduanya, rupiah per jam).

Rincian: ILO total jenis kelamin dan tingkat keahlian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0851_SEX_OCU_NB | 2015 | 11,434.00 | 10,338.45 | 1,095.55 | 10.60 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2016 | 14,068.00 | 12,125.98 | 1,942.02 | 16.02 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2017 | 14,731.00 | 13,924.58 | 806.42 | 5.79 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2018 | 15,275.00 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0851_SEX_OCU_NB | 2019 | 15,823.00 | 14,964.70 | 858.30 | 5.74 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2020 | 17,696.00 | 15,835.27 | 1,860.73 | 11.75 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2021 | 18,089.00 | 16,734.73 | 1,354.27 | 8.09 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2022 | 17,542.00 | 16,232.45 | 1,309.55 | 8.07 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2023 | 19,027.00 | 16,316.96 | 2,710.04 | 16.61 | keduanya | metode berbeda | None |
| SDG_0851_SEX_OCU_NB | 2024 | 19,009.00 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0851_SEX_OCU_NB | 2025 | 20,030.36 |  |  |  | hanya_utama | tanpa pasangan | None |

### P2: Informalitas: BPS vs ILO

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda).

Rincian: ILO total sektor (termasuk pertanian).

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SDG_0831_SEX_ECO_RT | 2018 | 56.98 | 82.26 | -25.28 | -30.73 | keduanya | definisi berbeda | None |
| SDG_0831_SEX_ECO_RT | 2019 | 55.88 | 80.34 | -24.46 | -30.45 | keduanya | definisi berbeda | None |
| SDG_0831_SEX_ECO_RT | 2020 | 60.47 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0831_SEX_ECO_RT | 2021 | 59.45 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0831_SEX_ECO_RT | 2022 | 59.31 | 80.16 | -20.85 | -26.01 | keduanya | definisi berbeda | None |
| SDG_0831_SEX_ECO_RT | 2023 | 59.11 | 80.94 | -21.83 | -26.97 | keduanya | definisi berbeda | None |
| SDG_0831_SEX_ECO_RT | 2024 | 57.95 |  |  |  | hanya_utama | tanpa pasangan | None |
| SDG_0831_SEX_ECO_RT | 2025 | 57.80 |  |  |  | hanya_utama | tanpa pasangan | None |
