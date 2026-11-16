# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1186 | SDG_0861_SEX_RT [total], SL.UEM.NEET.ZS [total] | selisih | 9 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | metode (olahan Sakernas yang sama); kelompok umur sama (15–24) |
| P2 | var2658 | SDG_A871_SEX_AGE_RT [umur=CLDVERSION_Y15-17] | selisih | 1 | 2023 | definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023 |
| P3 | SL.TLF.0714.ZS | — | konteks | 0 | — | kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025) |

## Rincian per pasangan

### P1: NEET 15–24: BPS vs ILO vs WDI
- Seri utama: `var1186` (rincian `total`)
- Pembanding: `SDG_0861_SEX_RT` (rincian `total`), `SL.UEM.NEET.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): metode (olahan Sakernas yang sama); kelompok umur sama (15–24)

Pertanyaan keterbandingan dan jawabannya:

1. **Kelompok umur?** 15–24 di ketiganya (judul BPS, nama DSD ILO, sourceNote WDI).
2. **Sumber WDI?** ILO Labour Force Statistics (sourceOrganization).

### P2: Pekerja anak: BPS (5–17) vs ILO kegiatan ekonomi (15–17)
- Seri utama: `var2658` (rincian `total`)
- Pembanding: `SDG_A871_SEX_AGE_RT` (rincian `umur=CLDVERSION_Y15-17`)
- Jenis: **selisih**; tahun beririsan: 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023

Pertanyaan keterbandingan dan jawabannya:

1. **Kelompok umur ILO?** Hanya 15–17 di berkas, walaupun definisi DSD mencakup 5–17.
2. **Beda A871 dan B871?** B871 menambah pekerjaan rumah tangga >= 21 jam untuk umur 5–14; untuk 15–17 sama, sehingga B871 2009 = A871 2009.

### P3: Anak bekerja 7–14 (WDI): konteks
- Seri utama: `SL.TLF.0714.ZS` (rincian `total`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025)

Pertanyaan keterbandingan dan jawabannya:

1. **Tahun bersama dengan BPS?** Tidak ada; bukan missing, serinya tidak tumpang tindih.
