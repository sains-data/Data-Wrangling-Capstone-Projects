# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SE.TER.ENRR | selisih | 11 | 9 | 9 | -7.20 | 19.67 | definisi berbeda (9), tanpa pasangan (2) |
| P2 | var1429 | konteks | 16 | 11 | 0 |  |  | definisi berbeda (16) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 19.67% (9 baris); semua pasangan termasuk antarpembanding: 19.67% (9 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 44.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: APK perguruan tinggi: BPS (umur 19–23) vs WDI (umur resmi jenjang tersier)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (kelompok umur acuan penyebut) dan metode (Susenas vs data administrasi UNESCO).

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SE.TER.ENRR | 2015 | 25.26 | 32.46 | -7.20 | -22.18 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2016 | 27.98 | 34.83 | -6.85 | -19.67 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2017 | 29.93 | 35.97 | -6.04 | -16.78 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2018 | 30.19 | 36.15 | -5.96 | -16.49 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2019 | 30.28 | 37.32 | -7.04 | -18.87 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2020 | 30.85 | 38.17 | -7.32 | -19.17 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2021 | 31.19 | 40.63 | -9.44 | -23.23 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2022 | 31.16 | 42.33 | -11.17 | -26.38 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2023 | 31.45 | 44.88 | -13.43 | -29.93 | keduanya | definisi berbeda |  |
| SE.TER.ENRR | 2024 | 32.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| SE.TER.ENRR | 2025 | 32.89 |  |  |  | hanya_utama | tanpa pasangan |  |

### P2: Lama sekolah (HLS, RLS): tanpa pembanding di paket

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Dua ukuran berbeda (harapan anak 7 tahun vs rata-rata penduduk 15+); variabel penjelas panel.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| var1429 | 2010 | 11.29 |  |  |  | hanya_utama | definisi berbeda |  |
| var1429 | 2011 | 11.44 |  |  |  | hanya_utama | definisi berbeda |  |
| var1429 | 2012 | 11.68 |  |  |  | hanya_utama | definisi berbeda |  |
| var1429 | 2013 | 12.10 |  |  |  | hanya_utama | definisi berbeda |  |
| var1429 | 2014 | 12.39 |  |  |  | hanya_utama | definisi berbeda |  |
| var1429 | 2015 | 12.55 | 8.32 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2016 | 12.72 | 8.42 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2017 | 12.85 | 8.50 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2018 | 12.91 | 8.58 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2019 | 12.95 | 8.75 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2020 | 12.98 | 8.90 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2021 | 13.08 | 8.97 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2022 | 13.10 | 9.08 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2023 | 13.15 | 9.13 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2024 | 13.21 | 9.22 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var1429 | 2025 | 13.30 | 9.41 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
