# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1373 | MDG_0000000007 [total], SH.DYN.MORT [total] | selisih | 2 | 2012, 2017 | metode dan definisi periode (survei dengan rujukan 5 tahun vs estimasi model tahunan) |
| P2 | var1584 | — | konteks | 0 | — | definisi berbeda: tidak ada seri kematian bayi (0–11 bulan) di paket pembanding |
| P3 | var1541 | SH.STA.BRTC.ZS [total] | konteks | 4 | 2016, 2017, 2018, 2019 | definisi dan cakupan berbeda; tidak dihitung sebagai selisih |
| P4 | MDG_0000000007 | SH.DYN.MORT [total] | selisih | 64 | 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | vintage (rilis estimasi UN IGME berbeda) |
| P5 | MDG_0000000026 | SH.STA.MMRT [total] | selisih | 39 | 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | vintage; tidak ada padanan BPS di paket |

## Rincian per pasangan

### P1: Kematian balita: titik survei BPS vs estimasi tahunan WHO dan WDI
- Seri utama: `var1373` (rincian `total`)
- Pembanding: `MDG_0000000007` (rincian `total`), `SH.DYN.MORT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2012, 2017
- Dugaan kategori selisih (diuji di Sprint 2): metode dan definisi periode (survei dengan rujukan 5 tahun vs estimasi model tahunan)

Pertanyaan keterbandingan dan jawabannya:

1. **Seri BPS mana yang balita?** var1373: var.label 'Angka Kematian Balita'.
2. **Periode apa yang diwakili angka BPS?** Angka Indonesia merujuk 5 tahun sebelum survei (var.note); WHO/WDI satu tahun kalender.
3. **Dari mana estimasi WHO/WDI?** Keduanya UN IGME (sourceOrganization WDI), dibuat dengan model dari banyak survei.

### P2: Kematian bayi BPS dan pembanding yang tersedia
- Seri utama: `var1584` (rincian `total`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: tidak ada seri kematian bayi (0–11 bulan) di paket pembanding

Pertanyaan keterbandingan dan jawabannya:

1. **Seri BPS mana yang bayi?** var1584: var.label 'Angka Kematian Bayi (AKB)'.
2. **Apakah WHOSIS_000003 setara?** Tidak: neonatal (0–27 hari) adalah sebagian dari kematian bayi. Dipakai sebagai konteks.

### P3: Persalinan: di fasilitas (BPS, 40% terbawah) vs ditolong tenaga kesehatan (WDI, semua)
- Seri utama: `var1541` (rincian `total`)
- Pembanding: `SH.STA.BRTC.ZS` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2016, 2017, 2018, 2019
- Dugaan kategori selisih (diuji di Sprint 2): definisi dan cakupan berbeda; tidak dihitung sebagai selisih

Pertanyaan keterbandingan dan jawabannya:

1. **Apa yang diukur var1541?** Kelahiran terakhir di fasilitas kesehatan (bukan ditolong tenaga kesehatan).
2. **Siapa yang dihitung?** Perempuan pernah kawin 15–49 pada 40% pengeluaran terbawah; WDI: semua persalinan.

### P4: Kematian balita: WHO vs WDI (dua rilis estimasi yang sama)
- Seri utama: `MDG_0000000007` (rincian `total`)
- Pembanding: `SH.DYN.MORT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): vintage (rilis estimasi UN IGME berbeda)

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah sumbernya sama?** Ya, UN IGME; selisih menunjukkan perbedaan waktu rilis, diuji lagi di Sprint 3 dengan arsip WDI.

### P5: Rasio kematian ibu: WHO vs WDI (konteks nasional)
- Seri utama: `MDG_0000000026` (rincian `total`)
- Pembanding: `SH.STA.MMRT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): vintage; tidak ada padanan BPS di paket

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah ada padanan BPS?** Tidak di paket ini; seri ini masuk Gold sebagai konteks nasional.
