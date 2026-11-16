# Kasus 17 — Air minum, sanitasi, dan kebersihan

Klaster E. Infrastruktur dan permukiman, Tujuan SDG 6. Enam seri provinsi BPS (`var845` air layak, `var2741` air
aman, `var847` sanitasi layak, `var2179` dan `var2749` sanitasi aman, `var1273` cuci tangan) dan lima pembanding
nasional (WDI `SH.H2O.SMDW.ZS`, `SH.H2O.BASW.ZS`; WHO `WSH_WATER_SAFELY_MANAGED`, `WSH_HYGIENE_BASIC`, `SDGODAWS`).
Paket `k17-air-sanitasi.zip`, 22 berkas, snapshot BPS 17 Oktober 2026, WDI dan WHO 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, seri kanonik per konsep, Silver dan Gold di SQL, rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var847` berkode 11.1.1 di katalog, padahal isinya sanitasi layak (judul dan nama berkas).
- Kode tahun di JSON 1993–1999 dua digit, 2000 ke atas tiga digit.
- `var.def` air layak dan sanitasi layak memuat lima catatan: provinsi tidak dicacah (2000, 2001), hanya ibu kota
  (2002), definisi berganti (2011, 2019), dan Kalimantan Utara bergabung dengan Kalimantan Timur sampai 2014.
- Air layak tidak terbit 2011–2020; sanitasi layak tidak terbit 2005.
- `var2749` sama dengan `var2179` gabungan, kecuali Papua Pegunungan yang tidak ada.
- BPS menghitung rumah tangga, WHO dan WDI menghitung penduduk.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
