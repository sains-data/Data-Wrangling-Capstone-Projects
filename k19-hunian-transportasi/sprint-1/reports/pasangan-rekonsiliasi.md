# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1241 | EN.POP.SLUM.UR.ZS [total] | konteks | 4 | 2016, 2018, 2020, 2022 | definisi berbeda: arah berlawanan dan populasi berbeda; dibandingkan arah perubahannya |
| P2 | var2753 | var2754 [arus=bongkar] | konteks | 5 | 2021, 2022, 2023, 2024, 2025 | moda berbeda; rekonsiliasi internal: jumlah provinsi vs baris Indonesia di Gold |

## Rincian per pasangan

### P1: Hunian layak (BPS, rumah tangga) vs penduduk kumuh perkotaan (WDI): konteks
- Seri utama: `var1241` (rincian `total`)
- Pembanding: `EN.POP.SLUM.UR.ZS` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2016, 2018, 2020, 2022
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: arah berlawanan dan populasi berbeda; dibandingkan arah perubahannya

Pertanyaan keterbandingan dan jawabannya:

1. **Arah?** Hunian layak naik = baik; penduduk kumuh naik = buruk.
2. **Populasi?** BPS semua rumah tangga; WDI penduduk perkotaan.

### P2: Bongkar muat kapal vs pesawat (BPS): jumlah provinsi vs Indonesia
- Seri utama: `var2753` (rincian `arus=bongkar`)
- Pembanding: `var2754` (rincian `arus=bongkar`)
- Jenis: **konteks**; tahun beririsan: 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): moda berbeda; rekonsiliasi internal: jumlah provinsi vs baris Indonesia di Gold

Pertanyaan keterbandingan dan jawabannya:

1. **Moda?** var2753 kapal, var2754 pesawat terbang (judul JSON).
2. **Cakupan wilayah?** Kapal dan pesawat tidak memuat provinsi yang sama; lihat grid.
