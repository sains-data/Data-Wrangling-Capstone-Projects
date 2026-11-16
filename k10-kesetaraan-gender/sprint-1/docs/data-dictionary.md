# Data dictionary — Kasus 10 Kesetaraan gender

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (840 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0552_NOC_RT, SDG_T552_NOC_RT, SG.GEN.PARL.ZS, SP.M18.2024.FE.ZS, var1360, var2003 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1987, 1991, 1994, 1997, 1998, 2000, … (31 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.64 – 51.72 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 5.3.1, 5.5.1, 5.5.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 840 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 840 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 840 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 836 | B | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg5_5_3_1_v1360.json, bps/2026-10-20/json/sdg5_5_5_2_v2003.json, ilostat/2026-10-20/data/DF_SDG_0552_NOC_RT.csv, ilostat/2026-10-20/data/DF_SDG_T552_NOC_RT.csv, wdi/2026-10-20/data/kelompok-05-hal-01.json, wdi/2026-10-20/data/kelompok-07-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 5d0a4943de00ff7278b7dc7fababda580e5b350e7301397fb2018fe32b6cf9ba, 5ecb345dd398f24777fd9aeee46246db328cad89ae26f29555a4efaf816b8afb, 8a0b52ec9c306fcdf9ea22fe3029c68e896ec3a019b5cc8a9770f0d59940d4fc, 9506e861063379cec23c823508eba8940ca9e16542c9481a7e9337b918c243bb, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- (tidak ada dimensi)

| rincian | dipakai_seri |
|---|---|
| total | SDG_0552_NOC_RT, SDG_T552_NOC_RT, SG.GEN.PARL.ZS, SP.M18.2024.FE.ZS, var1360, var2003 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1360 | persen | 5.3.1 | perempuan 20–24; kawin atau hidup bersama pertama sebelum 18 tahun; Susenas 2015–2025 | var.unit: 'Persen' |
| var2003 | persen | 5.5.2 | Sakernas; seluruh lapangan usaha KBLI 2015 (var.note); 2015–2025 | judul 'Proporsi'; var.unit kosong; nilai 10–50 dan dekat dengan ILO (UNIT_MEASURE PT = persen) |
| SG.GEN.PARL.ZS | persen | 5.5.1 | kursi parlemen nasional (IPU) | name: '(%)' |
| SP.M18.2024.FE.ZS | persen | 5.3.1 | perempuan 20–24, kawin pertama sebelum 18 (UNICEF, survei); 8 tahun 1987–2017 | name: '(% of women ages 20-24)' |
| SDG_0552_NOC_RT | persen | 5.5.2 | manajer senior dan menengah saja (ISCO kategori 1 dikurangi 14/13); ILOSTAT, Sakernas (SOURCE: LFS); OBS_STATUS B = patahan seri (NOTE_INDICATOR 'Break in series') | UNIT_MEASURE PT |
| SDG_T552_NOC_RT | persen | 5.5.2 | seluruh manajemen (ISCO kategori 1); ILOSTAT, Sakernas (SOURCE: LFS); OBS_STATUS B = patahan seri (NOTE_INDICATOR 'Break in series') | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1360 | 1100 | 2015 | total | 4.17 | bps/2026-10-20/json/sdg5_5_3_1_v1360.json | 5d0a4943de00ff7278b7dc7fababda580e5b350e7301397fb2018fe32b6cf9ba |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg5_5_3_1_v1360.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `5d0a4943de00…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
