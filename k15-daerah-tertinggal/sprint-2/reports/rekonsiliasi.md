# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | SI.POV.NAHC | selisih | 20 | 19 | 19 | -0.01 | 0.33 | metode berbeda (19), tanpa pasangan (1) |
| P2 | var2190 | konteks | 3 | 3 | 0 |  |  | definisi berbeda (3) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 0.33% (19 baris); semua pasangan termasuk antarpembanding: 0.33% (19 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 9.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: P0 Indonesia: BPS Maret (Semester 1) vs WDI tahunan

Jenis **selisih**; kategori pasangan: **metode berbeda**. Pembulatan: WDI = P0 Maret BPS dibulatkan satu desimal; tahun 2007–2011 BPS tahunan.

Rincian: rincian jumlah (perkotaan + perdesaan); semester Maret.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| SI.POV.NAHC | 2007 | 16.58 | 16.60 | -0.02 | -0.12 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2008 | 15.42 | 15.40 | 0.02 | 0.13 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2009 | 14.15 | 14.20 | -0.05 | -0.35 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2010 | 13.33 | 13.30 | 0.03 | 0.23 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2011 | 12.49 | 12.50 | -0.01 | -0.08 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2012 | 11.96 | 12.00 | -0.04 | -0.33 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2013 | 11.37 | 11.40 | -0.03 | -0.26 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2014 | 11.25 | 11.30 | -0.05 | -0.44 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2015 | 11.22 | 11.20 | 0.02 | 0.18 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2016 | 10.86 | 10.90 | -0.04 | -0.37 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2017 | 10.64 | 10.60 | 0.04 | 0.38 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2018 | 9.82 | 9.80 | 0.02 | 0.20 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2019 | 9.41 | 9.40 | 0.01 | 0.11 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2020 | 9.78 | 9.80 | -0.02 | -0.20 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2021 | 10.14 | 10.10 | 0.04 | 0.40 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2022 | 9.54 | 9.50 | 0.04 | 0.42 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2023 | 9.36 | 9.40 | -0.04 | -0.43 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2024 | 9.03 | 9.00 | 0.03 | 0.33 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2025 | 8.47 | 8.50 | -0.03 | -0.35 | keduanya | metode berbeda |  |
| SI.POV.NAHC | 2026 | 8.07 |  |  |  | hanya_utama | tanpa pasangan |  |

### P2: Desa tertinggal dan mandiri: tanpa pembanding nasional di paket

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Tidak ada baris Indonesia; agregat nasional dijumlahkan dari 34 provinsi di Gold.

Rincian: rincian jumlah.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| var2190 | 2019 | 19,152.00 | 1,444.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2190 | 2020 | 15,246.00 | 2,310.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| var2190 | 2021 | 13,215.00 | 2,906.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
