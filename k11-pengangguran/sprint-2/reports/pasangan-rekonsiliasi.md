# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var543 | SDG_0852_SEX_AGE_RT [total] | selisih | 24 | 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan |
| P2 | SL.UEM.TOTL.NE.ZS | SL.UEM.TOTL.ZS [total] | selisih | 32 | 1991, 1992, 1993, 1994, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan |
| P3 | SDG_0852_SEX_DSB_RT | — | konteks | 0 | — | tidak ada padanan BPS di paket |

## Rincian per pasangan

### P1: TPT BPS Agustus vs ILO SDG 8.5.2 (total, rujukan Agustus)
- Seri utama: `var543` (rincian `total`)
- Pembanding: `SDG_0852_SEX_AGE_RT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan

Pertanyaan keterbandingan dan jawabannya:

1. **Bulan survei ILO?** Agustus (NOTE_SOURCE di UNE_DEAP).
2. **Mengapa BPS lebih tinggi?** ILO memakai definisi harmonisasi; BPS memakai definisi nasional. Dipastikan dari dokumentasi Sakernas di Sprint 2.

### P2: WDI estimasi nasional vs estimasi model ILO
- Seri utama: `SL.UEM.TOTL.NE.ZS` (rincian `total`)
- Pembanding: `SL.UEM.TOTL.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 1991, 1992, 1993, 1994, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan

Pertanyaan keterbandingan dan jawabannya:

1. **Mengapa beda?** NE = olahan survei ILO (sama dengan SDG_0852); ZS = model ILOEST (sourceOrganization).

### P3: Pengangguran menurut disabilitas (ILO): konteks
- Seri utama: `SDG_0852_SEX_DSB_RT` (rincian `disabilitas=STATUS_DIS`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): tidak ada padanan BPS di paket

Pertanyaan keterbandingan dan jawabannya:

1. **Ada padanan BPS?** Tidak di paket ini.
