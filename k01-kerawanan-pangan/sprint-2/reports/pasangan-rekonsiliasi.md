# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1473 | SN.ITK.DEFC.ZS [total] | selisih | 8 | 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket |
| P2 | var1474 | SN.ITK.MSFI.ZS [total] | selisih | 8 | 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | sumber data dan cara estimasi berbeda; definisi FIES sama |
| P3 | NUTSTUNTINGPREV | NUTOVERWEIGHTPREV [total], NUTRITION_WH_2 [total] | konteks | 11 | 2000, 2001, 2004, 2008, 2010, 2013, 2018, 2019, 2021, 2022, 2023 | definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk |

## Rincian per pasangan

### P1: Ketidakcukupan konsumsi pangan: BPS (Susenas) vs WDI (FAO)
- Seri utama: `var1473` (rincian `total`)
- Pembanding: `SN.ITK.DEFC.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
- Dugaan kategori selisih (diuji di Sprint 2): metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah definisinya sama?** Ya: keduanya prevalence of undernourishment (judul var1473 dan name WDI).
2. **Apakah angka FAO satu tahun atau rata-rata beberapa tahun?** Metadata WDI di paket tidak menyebutnya (name, sourceNote, sourceOrganization). Dicatat sebagai pertanyaan terbuka; Sprint 2 memastikannya dari dokumentasi FAO sebelum selisih per tahun ditafsirkan.
3. **Dari survei apa angkanya?** BPS: Susenas (var.note). WDI: sourceOrganization FAO, tanpa keterangan survei.

### P2: Kerawanan pangan sedang atau berat (FIES): BPS vs WDI (FAO)
- Seri utama: `var1474` (rincian `total`)
- Pembanding: `SN.ITK.MSFI.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
- Dugaan kategori selisih (diuji di Sprint 2): sumber data dan cara estimasi berbeda; definisi FIES sama

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah keduanya FIES?** Ya: var.note BPS menyebut FIES 12 bulan terakhir; sourceNote WDI menyebut moderately or severely food insecure.
2. **Apa satuan analisisnya?** BPS: penduduk. WDI: penduduk yang tinggal di rumah tangga rawan pangan (rumah tangga sebagai unit klasifikasi).

### P3: Gizi balita WHO (stunting, overweight, wasting): konteks, bukan pasangan BPS
- Seri utama: `NUTSTUNTINGPREV` (rincian `total`)
- Pembanding: `NUTOVERWEIGHTPREV` (rincian `total`), `NUTRITION_WH_2` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2000, 2001, 2004, 2008, 2010, 2013, 2018, 2019, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah ada padanan BPS di paket?** Tidak; dua seri BPS mengukur penduduk, ketiga seri WHO mengukur balita.
2. **Mengapa NUTRITION_WH_2 hanya 12 tahun?** Angka survei (bukan estimasi tahunan model); tahun antara survei tidak ada.
