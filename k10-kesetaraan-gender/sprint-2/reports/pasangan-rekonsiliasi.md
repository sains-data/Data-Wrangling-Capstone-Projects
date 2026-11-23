# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var2003 | SDG_T552_NOC_RT [total] | selisih | 8 | 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023 | metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen) |
| P2 | var2003 | SDG_0552_NOC_RT [total] | selisih | 1 | 2023 | definisi (0552 tanpa manajer junior) |
| P3 | var1360 | SP.M18.2024.FE.ZS [total] | selisih | 1 | 2017 | tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017) |

## Rincian per pasangan

### P1: Perempuan manajer: BPS vs ILO seluruh manajemen (T552)
- Seri utama: `var2003` (rincian `total`)
- Pembanding: `SDG_T552_NOC_RT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen)

Pertanyaan keterbandingan dan jawabannya:

1. **ILO mana yang sebanding?** T552 = seluruh manajemen (ISCO 1); var.note BPS mencakup seluruh lapangan usaha. 0552 hanya manajer senior dan menengah.
2. **Apa yang janggal?** ILO T552 2016 = 44,78, sedangkan 2015 22,38, 2017 27,46, dan BPS 2016 23,6; tidak bertanda B.

### P2: Perempuan manajer: BPS vs ILO senior dan menengah (0552)
- Seri utama: `var2003` (rincian `total`)
- Pembanding: `SDG_0552_NOC_RT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi (0552 tanpa manajer junior)

Pertanyaan keterbandingan dan jawabannya:

1. **Mengapa 0552 lebih rendah?** Manajer junior (ISCO 14/13) tidak dihitung (deskripsi DSD).

### P3: Perkawinan anak: BPS vs WDI (UNICEF)
- Seri utama: `var1360` (rincian `total`)
- Pembanding: `SP.M18.2024.FE.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2017
- Dugaan kategori selisih (diuji di Sprint 2): tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017)

Pertanyaan keterbandingan dan jawabannya:

1. **Batas umur sama?** Ya: 20–24, sebelum 18 (var.note dan name WDI); BPS juga menghitung hidup bersama.
