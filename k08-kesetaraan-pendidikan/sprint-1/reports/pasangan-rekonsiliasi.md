# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1980 | SE.PRM.CMPT.ZS [total] | selisih | 9 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | definisi berbeda: umur 3–5 tahun di atas umur lulus (BPS) vs siswa baru kelas terakhir tanpa memandang umur (WDI) |
| P2 | var2600 | SE.ENR.PRSC.FM.ZS [total] | konteks | 0 | — | definisi berbeda: jenjang berbeda (PT vs SD dan menengah); skala BPS x100, WDI x1 |
| P3 | var2595 | — | konteks | 0 | — | tidak ada seri paritas kuintil di paket pembanding |

## Rincian per pasangan

### P1: Penyelesaian SD: BPS (kohort umur) vs WDI (rasio masuk kasar kelas terakhir)
- Seri utama: `var1980` (rincian `jenjang=sd`)
- Pembanding: `SE.PRM.CMPT.ZS` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: umur 3–5 tahun di atas umur lulus (BPS) vs siswa baru kelas terakhir tanpa memandang umur (WDI)

Pertanyaan keterbandingan dan jawabannya:

1. **Definisi BPS?** var.note: persentase anak yang menyelesaikan jenjang pada rentang umur 3–5 tahun di atas umur lulus.
2. **Definisi WDI?** sourceNote: gross intake ratio to the last grade of primary, regardless of age; bisa > 100.

### P2: Paritas: BPS APK PT perempuan/laki-laki vs WDI GPI SD+menengah
- Seri utama: `var2600` (rincian `total`)
- Pembanding: `SE.ENR.PRSC.FM.ZS` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: jenjang berbeda (PT vs SD dan menengah); skala BPS x100, WDI x1

Pertanyaan keterbandingan dan jawabannya:

1. **Jenis paritas sama?** Ya, jenis kelamin. Jenjang berbeda, dan WDI berakhir 2018 sedangkan BPS mulai 2020.

### P3: Paritas kuintil APK SMA (BPS): tanpa pembanding di paket
- Seri utama: `var2595` (rincian `total`)
- Pembanding: tidak ada di paket
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): tidak ada seri paritas kuintil di paket pembanding

Pertanyaan keterbandingan dan jawabannya:

1. **Apa jenis rasionya?** Kuintil pengeluaran terendah dibagi tertinggi (judul JSON), bukan jenis kelamin.
