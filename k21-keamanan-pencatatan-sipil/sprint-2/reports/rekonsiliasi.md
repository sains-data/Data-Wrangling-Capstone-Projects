# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SP.REG.BRTH.ZS | selisih | 11 | 4 | 4 | 0.03 | 0.05 | tanpa pasangan (7), metode berbeda (4) |
| P2 | VC.IHR.PSRC.P5 | konteks | 10 | 1 | 0 |  |  | definisi berbeda (10) |
| P3 | var1831 | konteks | 11 | 9 | 0 |  |  | cakupan berbeda (11) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 0.05% (4 baris); semua pasangan termasuk antarpembanding: 0.05% (4 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 4, P2 5.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Akta kelahiran balita: BPS vs WDI (UNICEF)

Jenis **selisih**; kategori pasangan: **metode berbeda**. Metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SP.REG.BRTH.ZS | 2015 | 72.65 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2016 | 72.54 | 72.50 | 0.04 | 0.06 | keduanya | metode berbeda |  |
| SP.REG.BRTH.ZS | 2017 | 73.18 | 77.90 | -4.72 | -6.06 | keduanya | metode berbeda |  |
| SP.REG.BRTH.ZS | 2018 | 71.92 | 71.90 | 0.02 | 0.03 | keduanya | metode berbeda |  |
| SP.REG.BRTH.ZS | 2019 | 74.36 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2020 | 77.20 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2021 | 77.04 | 77.00 | 0.04 | 0.05 | keduanya | metode berbeda |  |
| SP.REG.BRTH.ZS | 2022 | 81.34 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2023 | 83.44 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2024 | 85.07 |  |  |  | hanya_utama | tanpa pasangan |  |
| SP.REG.BRTH.ZS | 2025 | 86.76 |  |  |  | hanya_utama | tanpa pasangan |  |

### P2: Korban kekerasan (BPS) vs pembunuhan per 100.000 (WDI): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| VC.IHR.PSRC.P5 | 2015 | 0.05 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2016 | 0.06 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2017 | 0.09 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2018 | 0.08 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2019 | 0.06 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2020 | 0.04 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2021 | 0.03 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2022 | 0.03 | 0.30 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| VC.IHR.PSRC.P5 | 2023 | 0.02 |  |  |  | hanya_utama | definisi berbeda |  |
| VC.IHR.PSRC.P5 | 2024 | 0.04 |  |  |  | hanya_utama | definisi berbeda |  |

### P3: Akta kelahiran balita vs anak 0–17 (BPS dengan BPS)

Jenis **konteks**; kategori pasangan: **cakupan berbeda**. Kelompok umur berbeda; tetap dua seri.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| var1831 | 2015 | 72.65 | 79.92 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2016 | 72.54 | 81.68 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2017 | 73.18 | 83.33 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2018 | 71.92 | 83.55 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2019 | 74.36 | 86.01 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2020 | 77.20 | 88.11 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2021 | 77.04 | 88.42 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2022 | 81.34 | 90.41 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2023 | 83.44 | 91.79 |  |  | keduanya | cakupan berbeda | pasangan konteks: selisih tidak dihitung |
| var1831 | 2024 | 85.07 |  |  |  | hanya_utama | cakupan berbeda |  |
| var1831 | 2025 | 86.76 |  |  |  | hanya_utama | cakupan berbeda |  |
