# Kasus 04 — Penyakit dan faktor risiko

Klaster A. Pangan dan kesehatan, Tujuan SDG 3. Tiga seri provinsi BPS (`var1393` malaria, `var1480` hipertensi,
`var1435` merokok) dan empat pembanding nasional (WDI `SH.MLR.INCD.P3`; WHO `MALARIA_EST_INCIDENCE`,
`NCDMORT3070`, `M_Est_tob_curr_std`). Paket `k04-penyakit-faktor-risiko.zip`, 16 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Malaria BPS per 1.000 *penduduk*, WHO dan WDI per 1.000 *penduduk berisiko*.
- Hipertensi berkode 3.4.1 di katalog, tetapi nama tabelnya `sdg3_3_4_1_b`: butir nasional, bukan kematian PTM.
- Hipertensi 2016 hanya angka Indonesia; sumber survei berganti setiap putaran.
- WHO tembakau memuat 2025 dan 2030, yang merupakan proyeksi, dan mengukur semua produk tembakau dengan standardisasi umur.
- JSON BPS malaria dan merokok terdiri atas beberapa halaman tahun.
- Kalimantan Timur sebelum Kalimantan Utara terbit, serta Papua sebelum 2024, mencakup wilayah yang lebih luas.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
