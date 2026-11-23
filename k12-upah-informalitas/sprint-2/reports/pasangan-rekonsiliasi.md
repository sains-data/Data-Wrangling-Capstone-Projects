# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1172 | SDG_0851_SEX_OCU_NB [total] | selisih | 8 | 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023 | metode (pengolahan Sakernas; nominal keduanya, rupiah per jam) |
| P2 | var2153 | SDG_0831_SEX_ECO_RT [total] | selisih | 4 | 2018, 2019, 2022, 2023 | definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda) |

## Rincian per pasangan

### P1: Upah per jam: BPS (pekerja) vs ILO (rata-rata penghasilan per jam pekerja)
- Seri utama: `var1172` (rincian `total`)
- Pembanding: `SDG_0851_SEX_OCU_NB` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2016, 2017, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): metode (pengolahan Sakernas; nominal keduanya, rupiah per jam)

Pertanyaan keterbandingan dan jawabannya:

1. **Unit sama?** Ya: rupiah per jam, nominal (var.unit; NOTE_INDICATOR 'IDR'). Upah riil butuh indeks harga yang dicatat sumbernya (Sprint 2).
2. **Apakah sudah disesuaikan inflasi?** Tidak: keduanya nominal.

### P2: Informalitas: BPS vs ILO
- Seri utama: `var2153` (rincian `total`)
- Pembanding: `SDG_0831_SEX_ECO_RT` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2018, 2019, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda)

Pertanyaan keterbandingan dan jawabannya:

1. **Cakupan sektor?** Keduanya semua sektor; ILO punya rincian tanpa pertanian (SECTOR_NAG) untuk diuji di Sprint 2.
2. **Mengapa beda besar?** ILO menilai informalitas dari ciri pekerjaan dan unit usaha; BPS dari status pekerjaan. Dipastikan dari dokumentasi di Sprint 2.
