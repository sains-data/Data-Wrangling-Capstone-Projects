# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SE.PRM.CMPT.ZS | selisih | 9 | 9 | 9 | -7.38 | 7.17 | definisi berbeda (9) |
| P2 | SE.ENR.PRSC.FM.ZS | konteks | 6 | 0 | 0 |  |  | definisi berbeda (6) |
| P3 |  | konteks | 6 | 0 | 0 |  |  | tanpa pasangan (6) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 7.17% (9 baris); semua pasangan termasuk antarpembanding: 7.17% (9 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 38, P2 42.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Penyelesaian SD: BPS (kohort umur) vs WDI (rasio masuk kasar kelas terakhir)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi berbeda: umur 3–5 tahun di atas umur lulus (BPS) vs siswa baru kelas terakhir tanpa memandang umur (WDI).

Rincian: BPS jenjang=sd.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.PRM.CMPT.ZS | 2015 | 91.44 | 108.90 | -17.46 | -16.03 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2016 | 93.88 | 107.21 | -13.33 | -12.44 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2017 | 95.25 | 104.77 | -9.52 | -9.09 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2018 | 94.68 | 102.63 | -7.95 | -7.74 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2019 | 95.48 | 102.86 | -7.38 | -7.17 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2020 | 96.00 | 102.12 | -6.12 | -5.99 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2021 | 97.37 | 103.37 | -6.00 | -5.80 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2022 | 97.82 | 102.07 | -4.25 | -4.16 | keduanya | definisi berbeda | None |
| SE.PRM.CMPT.ZS | 2023 | 97.83 | 99.95 | -2.12 | -2.12 | keduanya | definisi berbeda | None |

### P2: Paritas: BPS APK PT perempuan/laki-laki vs WDI GPI SD+menengah

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: jenjang berbeda (PT vs SD dan menengah); skala BPS x100, WDI x1.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.ENR.PRSC.FM.ZS | 2020 | 109.01 |  |  |  | hanya_utama | definisi berbeda | None |
| SE.ENR.PRSC.FM.ZS | 2021 | 115.26 |  |  |  | hanya_utama | definisi berbeda | None |
| SE.ENR.PRSC.FM.ZS | 2022 | 116.04 |  |  |  | hanya_utama | definisi berbeda | None |
| SE.ENR.PRSC.FM.ZS | 2023 | 116.31 |  |  |  | hanya_utama | definisi berbeda | None |
| SE.ENR.PRSC.FM.ZS | 2024 | 121.96 |  |  |  | hanya_utama | definisi berbeda | None |
| SE.ENR.PRSC.FM.ZS | 2025 | 120.39 |  |  |  | hanya_utama | definisi berbeda | None |

### P3: Paritas kuintil APK SMA (BPS): tanpa pembanding di paket

Jenis **konteks**; kategori pasangan: **tanpa pasangan**. Tidak ada seri paritas kuintil di paket pembanding.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
|  | 2020 | 76.75 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2021 | 75.67 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2022 | 77.98 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2023 | 78.01 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2024 | 76.47 |  |  |  | hanya_utama | tanpa pasangan | None |
|  | 2025 | 89.31 |  |  |  | hanya_utama | tanpa pasangan | None |
