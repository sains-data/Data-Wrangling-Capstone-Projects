# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | EN.POP.SLUM.UR.ZS | konteks | 11 | 4 | 0 |  |  | definisi berbeda (11) |
| P2 | var2754 | konteks | 5 | 5 | 0 |  |  | definisi berbeda (5) |

Tidak ada baris yang selisihnya dapat dihitung.

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 8.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Hunian layak (BPS, rumah tangga) vs penduduk kumuh perkotaan (WDI): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: arah berlawanan dan populasi berbeda; dibandingkan arah perubahannya.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| EN.POP.SLUM.UR.ZS | 2015 | 92.85 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2016 | 94.00 | 21.89 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| EN.POP.SLUM.UR.ZS | 2017 | 95.05 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2018 | 95.70 | 20.24 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| EN.POP.SLUM.UR.ZS | 2019 | 56.51 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2020 | 59.54 | 19.41 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| EN.POP.SLUM.UR.ZS | 2021 | 60.90 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2022 | 60.66 | 19.41 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| EN.POP.SLUM.UR.ZS | 2023 | 63.15 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2024 | 65.25 |  |  |  | hanya_utama | definisi berbeda |  |
| EN.POP.SLUM.UR.ZS | 2025 | 68.40 |  |  |  | hanya_utama | definisi berbeda |  |

### P2: Bongkar muat kapal vs pesawat (BPS): jumlah provinsi vs Indonesia

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Moda berbeda; rekonsiliasi internal: jumlah provinsi vs baris Indonesia di Gold.

Rincian: arus bongkar; muat diperlakukan sama.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| var2754 | 2021 | 399,000,000.00 | 622,000,000.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2754 | 2022 | 393,000,000.00 | 577,000,000.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2754 | 2023 | 358,000,000.00 | 580,939,961.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2754 | 2024 | 396,000,000.00 | 689,000,000.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2754 | 2025 | 452,000,000.00 | 675,000,000.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
