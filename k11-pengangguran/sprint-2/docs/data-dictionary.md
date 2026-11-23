# Data dictionary — Kasus 11 Pengangguran

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (7,572 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0852_SEX_AGE_RT, SDG_0852_SEX_DSB_RT, SL.UEM.TOTL.NE.ZS, SL.UEM.TOTL.ZS, UNE_DEAP_SEX_AGE_RT, var543 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1976, 1977, 1978, 1980, 1982, 1985, … (121 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | bulan, tahun, triwulan | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | disabilitas=STATUS_DIS, disabilitas=STATUS_DIS;jenis_kelamin=FEMALE, disabilitas=STATUS_DIS;jenis_kelamin=MALE, disabilitas=STATUS_NODIS, disabilitas=STATUS_NODIS;jenis_kelamin=FEMALE, disabilitas=STATUS_NODIS;jenis_kelamin=MALE, … (90 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 36.578 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 8.5.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 7572 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 7572 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 7572 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 6727 | B, U | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_tpt.json, ilostat/2026-10-20/data/DF_SDG_0852_SEX_AGE_RT.csv, ilostat/2026-10-20/data/DF_SDG_0852_SEX_DSB_RT.csv, ilostat/2026-10-20/data/DF_UNE_DEAP_SEX_AGE_RT.csv, wdi/2026-10-20/data/kelompok-07-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 130335a771927e70f21770db81760d8a4c4a67812257a800dcc9c06e1a850c4b, 5a4c3144d1c15236923d79484c570ca3af8f39b3ba794b94b7da6e0fc9fbc6bc, 75f10f84e24cfe9e7a885a23c9d8d7e4aa56da82c6f47ac8c0e0a9d8b3b81ce4, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, fa50f5223f54f49183805551e2078d51e4002a8199bc16398ee58f4b29776654 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `disabilitas`: kode sumber apa adanya
- `jenis_kelamin`: `FEMALE`, `MALE`
- `umur`: kode sumber apa adanya

| rincian | dipakai_seri |
|---|---|
| disabilitas=STATUS_DIS | SDG_0852_SEX_DSB_RT |
| disabilitas=STATUS_DIS;jenis_kelamin=FEMALE | SDG_0852_SEX_DSB_RT |
| disabilitas=STATUS_DIS;jenis_kelamin=MALE | SDG_0852_SEX_DSB_RT |
| disabilitas=STATUS_NODIS | SDG_0852_SEX_DSB_RT |
| disabilitas=STATUS_NODIS;jenis_kelamin=FEMALE | SDG_0852_SEX_DSB_RT |
| disabilitas=STATUS_NODIS;jenis_kelamin=MALE | SDG_0852_SEX_DSB_RT |
| jenis_kelamin=FEMALE | SDG_0852_SEX_AGE_RT, SDG_0852_SEX_DSB_RT, UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_Y25-34 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_Y35-44 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_Y45-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=10YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y15-19 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y20-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y25-29 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y30-34 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y35-39 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y40-44 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y45-49 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y50-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y55-59 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_Y60-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=5YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=AGGREGATE_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=AGGREGATE_Y25-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=AGGREGATE_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=AGGREGATE_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=AGGREGATE_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=YTHADULT_Y15-24 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=YTHADULT_Y15-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=YTHADULT_YGE25 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE | SDG_0852_SEX_AGE_RT, SDG_0852_SEX_DSB_RT, UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_Y25-34 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_Y35-44 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_Y45-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=10YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y15-19 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y20-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y25-29 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y30-34 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y35-39 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y40-44 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y45-49 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y50-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y55-59 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_Y60-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=5YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=AGGREGATE_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=AGGREGATE_Y25-54 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=AGGREGATE_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=AGGREGATE_YGE15 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=AGGREGATE_YGE65 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=YTHADULT_Y15-24 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=YTHADULT_Y15-64 | UNE_DEAP_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=YTHADULT_YGE25 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |
| total | SDG_0852_SEX_AGE_RT, SDG_0852_SEX_DSB_RT, SL.UEM.TOTL.NE.ZS, SL.UEM.TOTL.ZS, UNE_DEAP_SEX_AGE_RT, var543 |
| umur=10YRBANDS_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_Y25-34 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_Y35-44 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_Y45-54 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| umur=10YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y15-19 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y20-24 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y25-29 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y30-34 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y35-39 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y40-44 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y45-49 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y50-54 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y55-59 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_Y60-64 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_YGE15 | UNE_DEAP_SEX_AGE_RT |
| umur=5YRBANDS_YGE65 | UNE_DEAP_SEX_AGE_RT |
| umur=AGGREGATE_Y15-24 | UNE_DEAP_SEX_AGE_RT |
| umur=AGGREGATE_Y25-54 | UNE_DEAP_SEX_AGE_RT |
| umur=AGGREGATE_Y55-64 | UNE_DEAP_SEX_AGE_RT |
| umur=AGGREGATE_YGE15 | UNE_DEAP_SEX_AGE_RT |
| umur=AGGREGATE_YGE65 | UNE_DEAP_SEX_AGE_RT |
| umur=YTHADULT_Y15-24 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |
| umur=YTHADULT_Y15-64 | UNE_DEAP_SEX_AGE_RT |
| umur=YTHADULT_YGE25 | SDG_0852_SEX_AGE_RT, UNE_DEAP_SEX_AGE_RT |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var543 | persen | 8.5.2 | Sakernas; tahunan 1986–2004 (tanpa 1995), Februari dan Agustus sejak 2005 sampai Februari 2026; backcast penimbang 2011–2013 dan 2018–2020 (var.note) | var.unit: 'Persen' |
| SL.UEM.TOTL.ZS | persen | 8.5.2 | estimasi model ILO (ILOEST), termasuk tahun tanpa survei | name: '(% of total labor force)' |
| SL.UEM.TOTL.NE.ZS | persen | 8.5.2 | ILO Labour Force Statistics (olahan survei nasional) | name: '(% of total labor force)' |
| SDG_0852_SEX_AGE_RT | persen | 8.5.2 | rincian jenis kelamin dan umur (15+, 15–24, 25+); ILOSTAT; olahan mikrodata Sakernas (SOURCE LFS) dan sensus; OBS_STATUS B = patahan seri | UNIT_MEASURE PT |
| SDG_0852_SEX_DSB_RT | persen | 8.5.2 | rincian jenis kelamin dan disabilitas; 2010 dari sensus; ILOSTAT; olahan mikrodata Sakernas (SOURCE LFS) dan sensus; OBS_STATUS B = patahan seri | UNIT_MEASURE PT |
| UNE_DEAP_SEX_AGE_RT | persen | 8.5.2 | tahunan dan triwulanan (FREQ A/Q, Q1 dan Q3 = Februari dan Agustus); 28 kode umur dari 4 klasifikasi; rujukan Agustus (NOTE_SOURCE); ILOSTAT; olahan mikrodata Sakernas (SOURCE LFS) dan sensus; OBS_STATUS B = patahan seri | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var543 | 1100 | 1986 | total | 2.40 | bps/2026-10-17/json/sdg8_tpt.json | fa50f5223f54f49183805551e2078d51e4002a8199bc16398ee58f4b29776654 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg8_tpt.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `fa50f5223f54…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (2,318 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var543 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var543 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1986, 1987, 1988, 1989, 1990, 1991, … (61 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | bulan, tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 379 | 0.56 – 18.91 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 2139 | outlier, patahan_seri, patahan_wilayah | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 2318 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 379 | bps/2026-10-17/json/sdg8_tpt.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 379 | fa50f5223f54f49183805551e2078d51e4002a8199bc16398ee58f4b29776654 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var543 | persen |

## data/gold/nasional.parquet (254 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SDG_0852_SEX_AGE_RT, SDG_0852_SEX_DSB_RT, SL.UEM.TOTL.NE.ZS, SL.UEM.TOTL.ZS, UNE_DEAP_SEX_AGE_RT, var543 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | disabilitas=STATUS_DIS, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1976, 1977, 1978, 1980, 1982, 1985, … (121 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | bulan, tahun, triwulan | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 1.292 – 11.24 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 254 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 254 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 254 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_tpt.json, ilostat/2026-10-20/data/DF_SDG_0852_SEX_AGE_RT.csv, ilostat/2026-10-20/data/DF_SDG_0852_SEX_DSB_RT.csv, ilostat/2026-10-20/data/DF_UNE_DEAP_SEX_AGE_RT.csv, wdi/2026-10-20/data/kelompok-07-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 130335a771927e70f21770db81760d8a4c4a67812257a800dcc9c06e1a850c4b, 5a4c3144d1c15236923d79484c570ca3af8f39b3ba794b94b7da6e0fc9fbc6bc, 75f10f84e24cfe9e7a885a23c9d8d7e4aa56da82c6f47ac8c0e0a9d8b3b81ce4, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, fa50f5223f54f49183805551e2078d51e4002a8199bc16398ee58f4b29776654 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (91 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | SDG_0852_SEX_DSB_RT, SL.UEM.TOTL.NE.ZS, var543 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | disabilitas=STATUS_DIS, total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | , SDG_0852_SEX_AGE_RT, SL.UEM.TOTL.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | , total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 1976, 1977, 1978, 1980, 1982, 1985, … (46 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 1 | 1.292 – 11.24 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 34 | 2.617 – 8.06 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 35 | 0 – 3.295 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 35 | 0 – 69.5845 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan, tidak berselisih | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan, metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan, tidak ada padanan BPS di paket | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 91 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var543 | 1100 | 1986 | 2.40 | bps/2026-10-17/json/sdg8_tpt.json |

1. Sel ini berasal dari baris Silver `var543` × 1100 × 1986 × rincian `total` × berkas `bps/2026-10-17/json/sdg8_tpt.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
