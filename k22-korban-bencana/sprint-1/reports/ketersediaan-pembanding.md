# Ketersediaan seri pembanding nasional

Dihasilkan `python pipeline.py` (`src/silver/pembanding.py`). Tahun survei seri utama: 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.

## Ringkasan per seri dan rincian

| seri_kode | sumber | rincian | satuan | jumlah_tahun | awal | akhir | tahun_survei_utama_tersedia | batas_bawah_atas |
|---|---|---|---|---|---|---|---|---|
| EN.CLC.MDAT.ZS | wdi | total | persen | 1 | 2009 | 2009 | (tidak ada) | tidak |

## WDI: baris ada vs nilai ada

| indicator_id | baris_ada | nilai_ada |
|---|---|---|
| EN.CLC.MDAT.ZS | 66 | 1 |

## Ketersediaan pada tahun survei seri utama (1 = ada)

Tidak ada pembanding pada tahun survei.

## Rincian yang kandidat sebanding

| pasangan | seri_utama | pembanding | alasan |
|---|---|---|---|
| P1 | korban_mengungsi_per_100rb | korban_mengungsi (jenis_bencana=banjir), jumlah_penduduk (total) | banjir: jenis dengan pengungsi terbanyak 2025; jenis lain dihitung sama di Sprint 2 |
| P2 | korban_meninggal_hilang_per_100rb | korban_meninggal (jenis_bencana=banjir), korban_hilang (jenis_bencana=banjir), jumlah_penduduk (total) | banjir, sama dengan P1 |
| P3 | kejadian | kejadian (jenis_bencana=banjir) | baris INDONESIA di tabel per jenis dibandingkan dengan jumlah baris provinsi di berkas yang sama |
| P4 | EN.CLC.MDAT.ZS | korban_terdampak (jenis_bencana=banjir) | WDI tanpa rincian; BNPB banjir sebagai contoh jenis yang tercakup |

Matriks lengkap seri x rincian x tahun: `reports/ketersediaan-pembanding.csv`.
