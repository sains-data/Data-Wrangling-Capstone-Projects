# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1458 | tabel:sdg4_amh_rinci [total] | selisih | 12 | 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | dua tabel penerbit yang sama; selisih (bila ada) dilaporkan, tidak disamakan paksa |
| P2 | var1458 | SE.ADT.LITR.ZS [total] | selisih | 5 | 2014, 2015, 2016, 2018, 2020 | metode (Susenas vs kompilasi UNESCO dari sensus/survei) |
| P3 | tabel:sdg4_amh_rinci | SE.ADT.LITR.ZS [total] | selisih | 8 | 2009, 2010, 2011, 2014, 2015, 2016, 2018, 2020 | metode |

## Rincian per pasangan

### P1: Total tabel rinci vs tabel ringkas var1458 (BPS dengan BPS)
- Seri utama: `var1458` (rincian `total`)
- Pembanding: `tabel:sdg4_amh_rinci` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): dua tabel penerbit yang sama; selisih (bila ada) dilaporkan, tidak disamakan paksa

Pertanyaan keterbandingan dan jawabannya:

1. **Mana sumber total kanonik?** var1458 (tabel dinamis, ber-kode wilayah); tabel rinci dipakai untuk rincian.
2. **Apakah identik?** Dihitung untuk semua provinsi dan tahun yang sama di aturan peringatan total_rinci_sama_ringkas.

### P2: Melek aksara BPS (Indonesia) vs WDI (UNESCO)
- Seri utama: `var1458` (rincian `total`)
- Pembanding: `SE.ADT.LITR.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2014, 2015, 2016, 2018, 2020
- Dugaan kategori selisih (diuji di Sprint 2): metode (Susenas vs kompilasi UNESCO dari sensus/survei)

Pertanyaan keterbandingan dan jawabannya:

1. **Tahun yang sama?** WDI hanya 13 tahun; irisan dengan var1458 dihitung di reports/pasangan-rekonsiliasi.md.
2. **Definisi sama?** Keduanya bisa membaca dan menulis, penduduk 15+ (sourceNote WDI, judul BPS).

### P3: Melek aksara tabel rinci (2009–2025) vs WDI
- Seri utama: `tabel:sdg4_amh_rinci` (rincian `total`)
- Pembanding: `SE.ADT.LITR.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2009, 2010, 2011, 2014, 2015, 2016, 2018, 2020
- Dugaan kategori selisih (diuji di Sprint 2): metode

Pertanyaan keterbandingan dan jawabannya:

1. **Mengapa pasangan ini?** Tabel rinci mulai 2009, lebih banyak tahun beririsan dengan WDI.
