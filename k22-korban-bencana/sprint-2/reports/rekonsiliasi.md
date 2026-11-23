# Tabel rekonsiliasi seri utama vs pembanding nasional

Dihasilkan `python pipeline.py` (`src/gold/rekonsiliasi.py`) dari `data/gold/nasional.parquet`. Selisih = nilai utama − nilai pembanding; selisih relatif dalam persen terhadap pembanding. Periode tanpa pasangan tetap ditampilkan. Selisih tidak dihapus dan tidak dipaksa sama.

## Ringkasan per pasangan

| pasangan_id | seri_pembanding | jenis | periode | berpasangan | selisih_dihitung | median_selisih | median_selisih_relatif | kategori |
|---|---|---|---|---|---|---|---|---|
| P1 | korban_mengungsi / jumlah_penduduk x 100.000 | selisih | 1 | 1 | 1 | 0.00 | 0.00 | tidak berselisih (1) |
| P2 | (korban_meninggal + korban_hilang) / jumlah_penduduk x 100.000 | selisih | 1 | 1 | 1 | 0.00 | 0.00 | tidak berselisih (1) |
| P3 | kejadian (agregat provinsi) | selisih | 16 | 2 | 2 | -4.00 | 0.28 | tanpa pasangan (14), definisi berbeda (1), tidak berselisih (1) |
| P4 | korban_terdampak | konteks | 1 | 0 | 0 |  |  | definisi berbeda (1) |

Median selisih relatif mutlak, pasangan yang seri utamanya seri provinsi (BPS/BNPB): 0.00% (4 baris); semua pasangan termasuk antarpembanding: 0.00% (4 baris).

Periode pembanding di luar rentang seri utama yang tidak ditulis: P4 16.

## Kategori

Kategori baku: *definisi berbeda*, *metode berbeda*, *vintage berbeda*, *cakupan berbeda*, *belum terjelaskan*, *tanpa pasangan*, *tidak berselisih*. Kategori pasangan ditetapkan dari bukti di pasangan rekonsiliasi Sprint 1 (`reports/pasangan-rekonsiliasi.md`); baris satu sisi menjadi *tanpa pasangan*, baris yang angkanya sama menjadi *tidak berselisih*.

## Rincian per pasangan

### P1: Mengungsi per 100.000: angka BNPB vs dihitung ulang dari pengungsi dan penduduk

Jenis **selisih**; kategori pasangan: **metode berbeda**. Pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah.

Rincian: banjir: jenis dengan pengungsi terbanyak 2025; jenis lain dihitung sama di Sprint 2.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| korban_mengungsi / jumlah_penduduk x 100.000 | 2025 | 392.09 | 392.09 | 0.00 | 0.00 | keduanya | tidak berselisih | pembanding = hitungan ulang dari pengungsi dan jumlah penduduk |

### P2: Meninggal dan hilang per 100.000: angka BNPB vs (meninggal + hilang) / penduduk

Jenis **selisih**; kategori pasangan: **metode berbeda**. Pembulatan; pembilang dari dua berkas terpisah.

Rincian: banjir, sama dengan P1.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| (korban_meninggal + korban_hilang) / jumlah_penduduk x 100.000 | 2025 | 0.54 | 0.54 | 0.00 | 0.00 | keduanya | tidak berselisih | pembanding = hitungan ulang dari meninggal + hilang dan jumlah penduduk |

### P3: Kejadian banjir: baris INDONESIA vs jumlah 38 provinsi

Jenis **selisih**; kategori pasangan: **definisi berbeda**. Definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional.

Rincian: baris INDONESIA di tabel per jenis dibandingkan dengan jumlah baris provinsi di berkas yang sama.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| kejadian (agregat provinsi) | 2010 | 1,060.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2011 | 573.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2012 | 584.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2013 | 725.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2014 | 596.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2015 | 525.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2016 | 824.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2017 | 979.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2018 | 871.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2019 | 784.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2020 | 1,518.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2021 | 1,794.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2022 | 1,531.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2023 | 1,255.00 |  |  |  | hanya_utama | tanpa pasangan |  |
| kejadian (agregat provinsi) | 2024 | 1,420.00 | 1,428.00 | -8.00 | -0.56 | keduanya | definisi berbeda | agregat provinsi (GOLD_AGREGAT) |
| kejadian (agregat provinsi) | 2025 | 2,009.00 | 2,009.00 | 0.00 | 0.00 | keduanya | tidak berselisih | agregat provinsi (GOLD_AGREGAT) |

### P4: Penduduk terdampak kekeringan, banjir, suhu ekstrem (WDI): konteks

Jenis **konteks**; kategori pasangan: **definisi berbeda**. Periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025.

Rincian: WDI tanpa rincian; BNPB banjir sebagai contoh jenis yang tercakup.

| seri_pembanding | periode | nilai_utama | nilai_pembanding | selisih | selisih_relatif | asal | kategori | catatan |
|---|---|---|---|---|---|---|---|---|
| korban_terdampak | 2009 | 0.16 |  |  |  | hanya_utama | definisi berbeda |  |
