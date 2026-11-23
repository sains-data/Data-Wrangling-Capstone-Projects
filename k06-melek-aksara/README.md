# Kasus 06 — Melek aksara

Klaster B. Pendidikan, Tujuan SDG 4. Dua tabel BPS (`var1458` ringkas, `tabel:sdg4_amh_rinci` rinci menurut daerah
dan jenis kelamin) dan satu pembanding nasional (WDI `SE.ADT.LITR.ZS`). Paket `k06-melek-aksara.zip`, 9 berkas,
snapshot BPS 17 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- JSON tabel rinci berisi HTML Excel: tiga blok bertumpuk, header bertingkat, nama provinsi yang melebar dua kolom.
- Nama wilayah di tabel statis tidak punya kode dan ejaannya berbeda (`KEP. RIAU`).
- Total tabel rinci dan tabel ringkas sama, kecuali 2017.
- DKI Jakarta tidak punya baris perdesaan.
- Angka WDI sama dengan BPS (diteruskan UNESCO), dengan derau *float32*.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
