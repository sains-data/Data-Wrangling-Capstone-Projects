# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | HWF_0001 | selisih | 1 | 1 | 1 | -21.10 | 50.12 | definisi berbeda (1) |
| P2 | HWF_0006 | selisih | 1 | 1 | 1 | 79.10 | 25.61 | definisi berbeda (1) |
| P3 | UHC_INDEX_REPORTED | konteks | 11 | 9 | 0 |  |  | definisi berbeda (11) |
| P4 | FINPROTECTION_CATA_TOT_10_POP | konteks | 4 | 0 | 0 |  |  | definisi berbeda (4) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 37.86% (2 baris); semua pasangan termasuk antarpembanding: 37.86% (2 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P1 12, P2 12, P3 15, P4 20.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Dokter: BPS dokter umum (per 100.000) vs WHO semua dokter (per 10.000)

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (WHO termasuk dokter spesialis) setelah satuan diseragamkan (BPS x 0,1).

Rincian: BPS profesi=dokter_umum; dokter gigi tidak termasuk 'medical doctors'.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| HWF_0001 | 2018 | 21.00 | 42.10 | -21.10 | -50.12 | keduanya | definisi berbeda | pembanding dikali 10 (per_10000_penduduk → per_100000_penduduk) |

### P2: Perawat dan bidan: BPS (dua rincian dijumlahkan di Gold) vs WHO HWF_0006

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi (aktif vs terdaftar) setelah perawat + bidan dijumlahkan dan satuan diseragamkan.

Rincian: WHO menggabungkan perawat dan bidan; BPS memisahkan; penjumlahan sah karena penyebutnya sama (penduduk).

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| HWF_0006 | 2018 | 388.00 | 308.90 | 79.10 | 25.61 | keduanya | definisi berbeda | pembanding dikali 10 (per_10000_penduduk → per_100000_penduduk) |

### P3: Unmet need pelayanan (BPS) vs indeks cakupan UHC (WHO): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: persentase penduduk tidak berobat vs indeks 14 indikator layanan.

Rincian: tanpa rincian.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| UHC_INDEX_REPORTED | 2015 | 4.66 | 59.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2016 | 4.33 | 60.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2017 | 5.26 | 63.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2018 | 4.91 | 63.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2019 | 5.18 | 65.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2020 | 5.44 | 66.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2021 | 5.03 | 66.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2022 | 6.09 | 68.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2023 | 5.22 | 67.00 |  |  | keduanya | definisi berbeda | pasangan konteks: selisih tidak dihitung |
| UHC_INDEX_REPORTED | 2024 | 5.18 |  |  |  | hanya_utama | definisi berbeda |  |
| UHC_INDEX_REPORTED | 2025 | 5.32 |  |  |  | hanya_utama | definisi berbeda |  |

### P4: Kepemilikan JKN (BPS) vs pengeluaran kesehatan katastrofik (WHO): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Definisi berbeda: kepemilikan jaminan vs beban pengeluaran rumah tangga.

Rincian: WHO rincian total.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| FINPROTECTION_CATA_TOT_10_POP | 2022 | 67.01 |  |  |  | hanya_utama | definisi berbeda |  |
| FINPROTECTION_CATA_TOT_10_POP | 2023 | 69.88 |  |  |  | hanya_utama | definisi berbeda |  |
| FINPROTECTION_CATA_TOT_10_POP | 2024 | 72.97 |  |  |  | hanya_utama | definisi berbeda |  |
| FINPROTECTION_CATA_TOT_10_POP | 2025 | 75.49 |  |  |  | hanya_utama | definisi berbeda |  |
