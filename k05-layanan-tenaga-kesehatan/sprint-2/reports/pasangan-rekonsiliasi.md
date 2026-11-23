# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | var1477 | HWF_0001 [total] | selisih | 1 | 2018 | definisi (WHO termasuk dokter spesialis) setelah satuan diseragamkan (BPS x 0,1) |
| P2 | var1477 | HWF_0006 [total] | selisih | 1 | 2018 | definisi (aktif vs terdaftar) setelah perawat + bidan dijumlahkan dan satuan diseragamkan |
| P3 | var1402 | UHC_INDEX_REPORTED [total] | konteks | 9 | 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023 | definisi berbeda: persentase penduduk tidak berobat vs indeks 14 indikator layanan |
| P4 | var2279 | FINPROTECTION_CATA_TOT_10_POP [total] | konteks | 0 | — | definisi berbeda: kepemilikan jaminan vs beban pengeluaran rumah tangga |

## Rincian per pasangan

### P1: Dokter: BPS dokter umum (per 100.000) vs WHO semua dokter (per 10.000)
- Seri utama: `var1477` (rincian `profesi=dokter_umum`)
- Pembanding: `HWF_0001` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2018
- Dugaan kategori selisih (diuji di Sprint 2): definisi (WHO termasuk dokter spesialis) setelah satuan diseragamkan (BPS x 0,1)

Pertanyaan keterbandingan dan jawabannya:

1. **Satuan?** BPS per 100.000 penduduk (var.note), WHO per 10.000; disamakan di Gold dengan faktor 0,1.
2. **Siapa yang dihitung WHO?** Generalists, specialist medical practitioners, dan medical doctors not further defined.
3. **Tahun mana?** Hanya 2018: baris Indonesia var1477 hanya ada untuk 2018.

### P2: Perawat dan bidan: BPS (dua rincian dijumlahkan di Gold) vs WHO HWF_0006
- Seri utama: `var1477` (rincian `profesi=perawat`)
- Pembanding: `HWF_0006` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2018
- Dugaan kategori selisih (diuji di Sprint 2): definisi (aktif vs terdaftar) setelah perawat + bidan dijumlahkan dan satuan diseragamkan

Pertanyaan keterbandingan dan jawabannya:

1. **Boleh menjumlahkan perawat dan bidan?** Ya: keduanya per 100.000 penduduk yang sama, jadi kepadatannya bisa dijumlahkan.
2. **Aktif atau terdaftar?** DefinitionText WHO: tergantung sumber data; BPS tidak menyebut.

### P3: Unmet need pelayanan (BPS) vs indeks cakupan UHC (WHO): konteks
- Seri utama: `var1402` (rincian `total`)
- Pembanding: `UHC_INDEX_REPORTED` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: persentase penduduk tidak berobat vs indeks 14 indikator layanan

Pertanyaan keterbandingan dan jawabannya:

1. **Kode sama?** Katalog 3.8.1 untuk keduanya; var1402 butir nasional (a).

### P4: Kepemilikan JKN (BPS) vs pengeluaran kesehatan katastrofik (WHO): konteks
- Seri utama: `var2279` (rincian `total`)
- Pembanding: `FINPROTECTION_CATA_TOT_10_POP` (rincian `total`)
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): definisi berbeda: kepemilikan jaminan vs beban pengeluaran rumah tangga

Pertanyaan keterbandingan dan jawabannya:

1. **Tahun bersama?** WHO berakhir 2021, JKN mulai 2022: tidak ada.
