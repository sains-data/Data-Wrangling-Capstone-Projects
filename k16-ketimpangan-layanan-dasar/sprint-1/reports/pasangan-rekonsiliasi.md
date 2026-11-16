# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var2011 | SI.DST.50MD [total] | selisih | 6 | 2018, 2019, 2020, 2021, 2022, 2023 | definisi dan metode: BPS menyebut pendapatan; WDI pendapatan atau konsumsi per kapita dengan median PPP |
| P2 | SDG_0111_SEX_AGE_RT | SI.POV.DDAY [total] | selisih | 26 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | populasi berbeda (pekerja vs seluruh penduduk); garis kemiskinan sama (US$3 PPP 2021) |
| P3 | var2016 | — | konteks | 0 | — | tidak ada padanan langsung di paket |

## Rincian per pasangan

### P1: Di bawah 50% median: BPS vs WDI
- Seri utama: `var2011` (rincian `total`)
- Pembanding: `SI.DST.50MD` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi dan metode: BPS menyebut pendapatan; WDI pendapatan atau konsumsi per kapita dengan median PPP

Pertanyaan keterbandingan dan jawabannya:

1. **Pendapatan atau pengeluaran?** Judul BPS menyebut pendapatan; sourceNote WDI menyebut pendapatan atau konsumsi. Untuk Indonesia keduanya perlu dipastikan dari dokumentasi Susenas dan PIP di Sprint 2.

### P2: Kemiskinan pekerja (ILO) vs kemiskinan ekstrem penduduk (WDI)
- Seri utama: `SDG_0111_SEX_AGE_RT` (rincian `total`)
- Pembanding: `SI.POV.DDAY` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): populasi berbeda (pekerja vs seluruh penduduk); garis kemiskinan sama (US$3 PPP 2021)

Pertanyaan keterbandingan dan jawabannya:

1. **Garis kemiskinannya?** Keduanya US$3 per hari PPP (deskripsi dataflow ILO, name WDI).
2. **Populasinya?** ILO: orang bekerja; WDI: seluruh penduduk.

### P3: Layanan dasar, pendapatan pemerintah (BPS) dan perlindungan sosial, porsi upah (ILO): konteks
- Seri utama: `var2016` (rincian `layanan=air_minum`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): tidak ada padanan langsung di paket

Pertanyaan keterbandingan dan jawabannya:

1. **Ada padanan?** Tidak; SDG_0131 dan SDG_1041 dipakai sebagai konteks nasional.
