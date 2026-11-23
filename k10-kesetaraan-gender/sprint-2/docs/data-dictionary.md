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

## data/gold/panel.parquet (836 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1360, var2003 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1360, var2003 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 74 | 0.64 – 51.72 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 787 | outlier, patahan_wilayah | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 836 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 74 | bps/2026-10-20/json/sdg5_5_3_1_v1360.json, bps/2026-10-20/json/sdg5_5_5_2_v2003.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 74 | 5d0a4943de00ff7278b7dc7fababda580e5b350e7301397fb2018fe32b6cf9ba, 5ecb345dd398f24777fd9aeee46246db328cad89ae26f29555a4efaf816b8afb | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1360 | persen |
| var2003 | persen |

## data/gold/nasional.parquet (78 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SDG_0552_NOC_RT, SDG_T552_NOC_RT, SG.GEN.PARL.ZS, SP.M18.2024.FE.ZS, var1360, var2003 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1987, 1991, 1994, 1997, 1998, 2000, … (31 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 4.56 – 44.78 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 78 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 78 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 78 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg5_5_3_1_v1360.json, bps/2026-10-20/json/sdg5_5_5_2_v2003.json, ilostat/2026-10-20/data/DF_SDG_0552_NOC_RT.csv, ilostat/2026-10-20/data/DF_SDG_T552_NOC_RT.csv, wdi/2026-10-20/data/kelompok-05-hal-01.json, wdi/2026-10-20/data/kelompok-07-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 5d0a4943de00ff7278b7dc7fababda580e5b350e7301397fb2018fe32b6cf9ba, 5ecb345dd398f24777fd9aeee46246db328cad89ae26f29555a4efaf816b8afb, 8a0b52ec9c306fcdf9ea22fe3029c68e896ec3a019b5cc8a9770f0d59940d4fc, 9506e861063379cec23c823508eba8940ca9e16542c9481a7e9337b918c243bb, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (33 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1360, var2003 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | SDG_0552_NOC_RT, SDG_T552_NOC_RT, SP.M18.2024.FE.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 4.56 – 36.68 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 23 | 16.3 – 44.78 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 23 | -21.18 – 10.125 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 23 | -47.2979 – 40.6708 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (0552 tanpa manajer junior), metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen), tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 33 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1360 | 1100 | 2015 | 4.17 | bps/2026-10-20/json/sdg5_5_3_1_v1360.json |

1. Sel ini berasal dari baris Silver `var1360` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-20/json/sdg5_5_3_1_v1360.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
