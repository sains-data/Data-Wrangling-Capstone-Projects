# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1410 | SP.REG.BRTH.ZS [total] | selisih | 4 | 2016, 2017, 2018, 2021 | metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun) |
| P2 | var1311 | VC.IHR.PSRC.P5 [total] | konteks | 1 | 2022 | definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi) |
| P3 | var1410 | var1831 [total] | konteks | 9 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | kelompok umur berbeda; tetap dua seri |

## Rincian per pasangan

### P1: Akta kelahiran balita: BPS vs WDI (UNICEF)
- Seri utama: `var1410` (rincian `total`)
- Pembanding: `SP.REG.BRTH.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2016, 2017, 2018, 2021
- Dugaan kategori selisih (diuji di Sprint 2): metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun)

Pertanyaan keterbandingan dan jawabannya:

1. **Kelompok umur sama?** Ya: var.note var1410 'anak berusia kurang dari 5 tahun'; sourceNote WDI 'children under age 5'.
2. **Bagaimana var1831?** Umur 0–17; seri terpisah, tidak dipasangkan dengan WDI.

### P2: Korban kekerasan (BPS) vs pembunuhan per 100.000 (WDI): konteks
- Seri utama: `var1311` (rincian `total`)
- Pembanding: `VC.IHR.PSRC.P5` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2022
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi)

Pertanyaan keterbandingan dan jawabannya:

1. **Satuan?** Persen penduduk vs per 100.000 penduduk; konsep berbeda.

### P3: Akta kelahiran balita vs anak 0–17 (BPS dengan BPS)
- Seri utama: `var1410` (rincian `total`)
- Pembanding: `var1831` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): kelompok umur berbeda; tetap dua seri

Pertanyaan keterbandingan dan jawabannya:

1. **Boleh disatukan?** Tidak: < 5 tahun vs 0–17 tahun.
