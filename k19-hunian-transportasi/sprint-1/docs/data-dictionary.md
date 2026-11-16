# Data dictionary — Kasus 19 Hunian dan transportasi

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,305 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | EN.POP.SLUM.UR.ZS, var1241, var2012, var2013, var2753, var2754 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2000, 2002, 2004, 2006, 2008, 2010, … (19 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | arus=bongkar, arus=muat, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.52 – 6.89e+08 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | kilogram, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 11.1.1, 11.1.1(a), 11.2.1(a), 11.2.1(b), 9.1.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1305 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1305 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1305 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg11_11_1_1_a_v1241.json, bps/2026-10-20/json/sdg11_11_2_1_a_v2012.json, bps/2026-10-20/json/sdg11_11_2_1_b_v2013.json, bps/2026-10-20/json/sdg9_9_1_2_v2753.json, bps/2026-10-20/json/sdg9_9_1_2_v2754.json, wdi/2026-10-20/data/kelompok-01-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 6c5fe138931395fcf158bddd477898225bc691f945baf0301a8c35259b2563b8, 8701670cc93f2694bdf983ab34a05ad32c81379077f2430c32ce0eb58a1e9764, 8d2fae3a96415bd41299bf08abfc356d33448bdd6b66ff2f492aca4eb0e63226, e043c82edb22270cb8b802fca7cab80f3a0d62f6d32307020b6fd724f20258e5, e6553c5bb49e8b2e3d7032186180253bf8550e11b82b1be2f93561d8d92b4ba2, e7456ea606505e1986ba048f44a931d5c212234581b8b116ae9980214e78d23b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `arus`: `bongkar`, `muat`
- `arus` (var2753, dari turvar BPS): `bongkar` = Bongkar, `muat` = Muat
- `arus` (var2754, dari turvar BPS): `bongkar` = Bongkar, `muat` = Muat

| rincian | dipakai_seri |
|---|---|
| arus=bongkar | var2753, var2754 |
| arus=muat | var2753, var2754 |
| total | EN.POP.SLUM.UR.ZS, var1241, var2012, var2013 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1241 | persen | 11.1.1(a) | rumah tangga; Susenas; empat kriteria hunian layak sejak 2019 (var.note) | var.unit: 'Persen' |
| var2012 | persen | 11.2.1(a) | Susenas Modul Ketahanan Sosial; hanya 2017 dan 2020 | judul 'Persentase rumah tangga'; var.unit kosong |
| var2013 | persen | 11.2.1(b) | penduduk 10+; Susenas Modul Ketahanan Sosial; hanya 2017 dan 2020 | judul 'Persentase penduduk'; var.unit kosong |
| var2753 | kilogram | 9.1.2 | rincian bongkar dan muat (turvar), tanpa jumlah; 2021–2025 | var.unit: 'KG' |
| var2754 | kilogram | 9.1.2 | rincian bongkar dan muat (turvar), tanpa jumlah; 2021–2025 | var.unit: 'KG' |
| EN.POP.SLUM.UR.ZS | persen | 11.1.1 | penduduk perkotaan; arah berlawanan dengan hunian layak; UN-Habitat | name: '(% of urban population)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1241 | 1100 | 2015 | total | 88.96 | bps/2026-10-20/json/sdg11_11_1_1_a_v1241.json | e7456ea606505e1986ba048f44a931d5c212234581b8b116ae9980214e78d23b |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg11_11_1_1_a_v1241.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `e7456ea60650…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
