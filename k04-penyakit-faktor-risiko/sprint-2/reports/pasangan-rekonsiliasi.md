# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1393 | MALARIA_EST_INCIDENCE [total], SH.MLR.INCD.P3 [total] | selisih | 12 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 | definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi) |
| P2 | var1435 | M_Est_tob_curr_std [total] | selisih | 4 | 2015, 2020, 2021, 2022 | definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan |
| P3 | var1480 | NCDMORT3070 [total] | konteks | 4 | 2007, 2013, 2016, 2018 | definisi berbeda: prevalensi faktor risiko vs probabilitas kematian |
| P4 | MALARIA_EST_INCIDENCE | SH.MLR.INCD.P3 [total] | selisih | 24 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | vintage |

## Rincian per pasangan

### P1: Malaria: kasus dilaporkan per 1.000 penduduk (BPS) vs estimasi per 1.000 penduduk berisiko (WHO, WDI)
- Seri utama: `var1393` (rincian `total`)
- Pembanding: `MALARIA_EST_INCIDENCE` (rincian `total`), `SH.MLR.INCD.P3` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Dugaan kategori selisih (diuji di Sprint 2): definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi)

Pertanyaan keterbandingan dan jawabannya:

1. **Penyebut WHO?** Penduduk di daerah penularan malaria (Denominator), bukan seluruh penduduk.
2. **Penyebut BPS?** 'Per 1000 Orang' (judul), seluruh penduduk; angka dari laporan Kemenkes.
3. **WHO vs WDI?** WDI meneruskan WHO GHO (sourceOrganization); selisih keduanya vintage.

### P2: Merokok (BPS, kasar, rokok) vs penggunaan tembakau (WHO, distandarkan umur)
- Seri utama: `var1435` (rincian `total`)
- Pembanding: `M_Est_tob_curr_std` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2020, 2021, 2022
- Dugaan kategori selisih (diuji di Sprint 2): definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan

Pertanyaan keterbandingan dan jawabannya:

1. **Apa yang dihitung WHO?** Semua produk tembakau, harian atau tidak, distandarkan umur (DefinitionText, kode _std).
2. **Tahun mana yang sah?** 2025 dan 2030 proyeksi; hanya tahun estimasi yang beririsan dengan BPS yang dibandingkan.

### P3: Hipertensi (BPS) vs kematian PTM 30–70 (WHO): konteks
- Seri utama: `var1480` (rincian `total`)
- Pembanding: `NCDMORT3070` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2007, 2013, 2016, 2018
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: prevalensi faktor risiko vs probabilitas kematian

Pertanyaan keterbandingan dan jawabannya:

1. **Kode SDG sama?** Di katalog ya (3.4.1), tetapi var1480 adalah butir nasional 3.4.1(b).

### P4: Malaria WHO vs WDI (estimasi yang sama, rilis berbeda)
- Seri utama: `MALARIA_EST_INCIDENCE` (rincian `total`)
- Pembanding: `SH.MLR.INCD.P3` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): vintage

Pertanyaan keterbandingan dan jawabannya:

1. **Sumbernya sama?** Ya, WDI mengutip WHO GHO; diuji lagi di Sprint 3 dengan arsip WDI.
