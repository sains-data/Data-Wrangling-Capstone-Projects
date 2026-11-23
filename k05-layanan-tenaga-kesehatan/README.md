# Kasus 05 — Layanan dan tenaga kesehatan

Klaster A. Pangan dan kesehatan, Tujuan SDG 3. Tiga seri provinsi BPS (`var1402` unmet need pelayanan, `var2279`
JKN, `var1477` tenaga kesehatan per profesi) dan empat pembanding nasional WHO (`HWF_0001`, `HWF_0006`,
`UHC_INDEX_REPORTED`, `FINPROTECTION_CATA_TOT_10_POP`). Paket `k05-layanan-tenaga-kesehatan.zip`, 13 berkas,
snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | validasi lengkap dan laporan (kasus ini tanpa WDI) | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Satuan `var1477` hanya ada di `var.note`: per 100.000 penduduk. WHO per 10.000.
- `var1477` tidak punya baris total; menyaring `rincian == total` membuat seri ini hilang dari profil dan grid.
- WHO "medical doctors" termasuk spesialis; BPS memisahkan dokter umum dan dokter gigi.
- Unmet need dan JKN adalah butir nasional (a), bukan indikator global 3.8.1 dan 3.8.2.
- JKN baru terbit 2022; tahun sebelumnya bukan missing.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
