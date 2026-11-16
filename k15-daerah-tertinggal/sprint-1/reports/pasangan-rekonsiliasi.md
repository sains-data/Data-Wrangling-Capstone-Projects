# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var192 | SI.POV.NAHC [total] | selisih | 19 | 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | pembulatan: WDI = P0 Maret BPS dibulatkan satu desimal; tahun 2007–2011 BPS tahunan |
| P2 | var2191 | var2190 [total] | konteks | 3 | 2019, 2020, 2021 | tidak ada baris Indonesia; agregat nasional dijumlahkan dari 34 provinsi di Gold |

## Rincian per pasangan

### P1: P0 Indonesia: BPS Maret (Semester 1) vs WDI tahunan
- Seri utama: `var192` (rincian `total`)
- Pembanding: `SI.POV.NAHC` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): pembulatan: WDI = P0 Maret BPS dibulatkan satu desimal; tahun 2007–2011 BPS tahunan

Pertanyaan keterbandingan dan jawabannya:

1. **Semester mana yang dipakai WDI?** Maret (S1): nilai WDI sama dengan P0 Maret yang dibulatkan, misalnya 2020 9,78 -> 9,8.
2. **Mengapa bukan rata-rata dua semester?** Rata-rata 2020 (9,98) tidak cocok dengan WDI 9,8; semester tidak dirata-rata di Silver.

### P2: Desa tertinggal dan mandiri: tanpa pembanding nasional di paket
- Seri utama: `var2191` (rincian `total`)
- Pembanding: `var2190` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2019, 2020, 2021
- Dugaan kategori selisih (diuji di Sprint 2): tidak ada baris Indonesia; agregat nasional dijumlahkan dari 34 provinsi di Gold

Pertanyaan keterbandingan dan jawabannya:

1. **Ada angka Indonesia?** Tidak; hanya 34 provinsi (2019–2021).
