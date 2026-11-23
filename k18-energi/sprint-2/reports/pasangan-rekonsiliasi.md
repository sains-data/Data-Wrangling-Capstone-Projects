# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var87 | EG.ELC.ACCS.ZS [total] | selisih | 31 | 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | definisi (PLN saja vs semua sumber listrik; rumah tangga vs penduduk) |
| P2 | tabel:sdg7_bahan_bakar | EG.CFT.ACCS.ZS [total] | selisih | 16 | 2001, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 | definisi (kategori bersih; rumah tangga vs penduduk); BPS berakhir 2021 |

## Rincian per pasangan

### P1: Listrik: BPS (rumah tangga, PLN saja) vs WDI (penduduk, semua sumber)
- Seri utama: `var87` (rincian `total`)
- Pembanding: `EG.ELC.ACCS.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
- Dugaan kategori selisih (diuji di Sprint 2): definisi (PLN saja vs semua sumber listrik; rumah tangga vs penduduk)

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah BPS mencakup semua listrik?** Tidak: judul 'Sumber Penerangan Utama dari Listrik PLN'.
2. **Unit WDI?** Persentase penduduk (name WDI).

### P2: Bahan bakar bersih: BPS (gas/elpiji + listrik, dijumlahkan di Gold) vs WDI
- Seri utama: `tabel:sdg7_bahan_bakar` (rincian `bahan_bakar=gas_elpiji`)
- Pembanding: `EG.CFT.ACCS.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2001, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
- Dugaan kategori selisih (diuji di Sprint 2): definisi (kategori bersih; rumah tangga vs penduduk); BPS berakhir 2021

Pertanyaan keterbandingan dan jawabannya:

1. **Apa yang bersih menurut WDI?** sourceNote: pedoman WHO, minyak tanah tidak termasuk.
2. **Bagaimana 'lainnya'?** Termasuk rumah tangga yang tidak memasak (catatan tabel); tidak dimasukkan ke bersih.
