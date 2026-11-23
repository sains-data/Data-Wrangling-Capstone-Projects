# Kasus 12 — Upah dan informalitas

Klaster C. Gender dan ketenagakerjaan, Tujuan SDG 8. Dua seri provinsi BPS (`var1172` upah per jam, `var2153`
informalitas) dan dua seri ILOSTAT (`SDG_0851_SEX_OCU_NB`, `SDG_0831_SEX_ECO_RT`). Tanpa WDI. Paket
`k12-upah-informalitas.zip`, 10 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, upah riil, Silver dan Gold di SQL, rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | validasi lengkap dan laporan (kasus ini tanpa WDI) | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Berkas ILO memuat beberapa klasifikasi jabatan dan sektor, masing-masing dengan total.
- Unit upah ILO hanya terbaca dari `UNIT_MEASURE` (LC) dan `NOTE_INDICATOR` (IDR).
- Informalitas ILO dan BPS berbeda definisi; selisihnya lebih dari 20 poin.
- Upah nominal; upah riil butuh indeks harga yang dicatat sumbernya.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
