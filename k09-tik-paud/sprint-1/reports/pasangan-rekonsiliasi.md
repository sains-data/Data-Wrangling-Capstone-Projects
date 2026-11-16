# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1439 | SE.PRE.ENRR [total] | selisih | 4 | 2015, 2016, 2017, 2018 | definisi (kelompok umur acuan dan jenis layanan PAUD vs pendidikan prasekolah) |
| P2 | var1221 | IT.NET.USER.ZS [total] | konteks | 10 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | konsep berbeda: kepemilikan perangkat vs penggunaan internet |
| P3 | var1451 | var1447 [total] | konteks | 11 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | kelompok umur berbeda; tidak dijumlah atau dirata-rata |

## Rincian per pasangan

### P1: APK PAUD: BPS (3–6 tahun) vs WDI prasekolah (umur resmi)
- Seri utama: `var1439` (rincian `total`)
- Pembanding: `SE.PRE.ENRR` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2015, 2016, 2017, 2018
- Dugaan kategori selisih (diuji di Sprint 2): definisi (kelompok umur acuan dan jenis layanan PAUD vs pendidikan prasekolah)

Pertanyaan keterbandingan dan jawabannya:

1. **Kelompok umur BPS?** 3–6 tahun (var.note).
2. **WDI?** Prasekolah pada umur resmi jenjang; sourceNote tidak menyebut angka umur. WDI berakhir 2018.

### P2: Telepon genggam (BPS) vs pengguna internet (WDI): konteks
- Seri utama: `var1221` (rincian `total`)
- Pembanding: `IT.NET.USER.ZS` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
- Dugaan kategori selisih (diuji di Sprint 2): konsep berbeda: kepemilikan perangkat vs penggunaan internet

Pertanyaan keterbandingan dan jawabannya:

1. **Konsep sama?** Tidak: menguasai/memiliki telepon genggam (umur 5+) vs memakai internet 3 bulan terakhir.

### P3: Keterampilan TIK 15–24 vs 15–59 (BPS dengan BPS)
- Seri utama: `var1451` (rincian `total`)
- Pembanding: `var1447` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): kelompok umur berbeda; tidak dijumlah atau dirata-rata

Pertanyaan keterbandingan dan jawabannya:

1. **Boleh digabung?** Tidak: 15–59 mencakup 15–24; menggabungkan menghitung dua kali.
