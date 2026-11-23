# Kasus 07 — Partisipasi dan lama sekolah

Klaster B. Pendidikan, Tujuan SDG 4. Lima seri provinsi BPS (`var303` APK per jenjang, `var1443` APK perguruan
tinggi, `var2685` partisipasi pendidikan/pelatihan, `var417` harapan lama sekolah, `var1429` rata-rata lama sekolah)
dan satu pembanding nasional (WDI `SE.TER.ENRR`). Paket `k07-partisipasi-lama-sekolah.zip`, 15 berkas, snapshot
BPS 17 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var303` berkode 4.3.1 di katalog, padahal jenjangnya SD, SMP, SM.
- APK bisa melebihi 100; aturan "persen 0–100" menolak data yang benar.
- Berkas HLS memuat kabupaten/kota (label provinsi bertanda `<b>`).
- Kelompok umur `var2685` tumpang tindih; jangan dijumlah.
- APK mencakup paket A/B/C mulai 2007; Aceh 2005 kosong.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
