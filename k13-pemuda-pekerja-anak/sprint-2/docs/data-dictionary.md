# Data dictionary — Kasus 13 Pemuda dan pekerja anak

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (720 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0861_SEX_RT, SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT, SL.TLF.0714.ZS, SL.UEM.NEET.ZS, var1186, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1996, 1997, 1998, 1999, 2000, 2001, … (30 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_kelamin=FEMALE, jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17, jenis_kelamin=MALE, jenis_kelamin=MALE;umur=CLDVERSION_Y15-17, total, umur=CLDVERSION_Y15-17 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.38 – 41.23 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 8.6.1, 8.7.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 720 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 720 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 720 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 711 | B | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_8_7_1_v2658.json, bps/2026-10-17/json/sdg8_neet.json, ilostat/2026-10-20/data/DF_SDG_0861_SEX_RT.csv, ilostat/2026-10-20/data/DF_SDG_A871_SEX_AGE_RT.csv, ilostat/2026-10-20/data/DF_SDG_B871_SEX_AGE_RT.csv, wdi/2026-10-20/data/kelompok-06-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 41b13e4b1df67909c8d41e1527a585fa576ff107c1e5d7f87d8b109203e5e5ac, 51ab5e7080ffe32ce20a0914bf7002e5d5c5523366fd72c207a5ce4732e8fc75, 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, cc4fc24190b0dbc8610ff3db8ef1db700180ccac03833ab5093d300fdec7e443, d1fc787eb33130a2ab8ef479ca46a5b3704cc8e5e13b0edb03b756406bfe9c2b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `umur`: `CLDVERSION_Y15-17`

| rincian | dipakai_seri |
|---|---|
| jenis_kelamin=FEMALE | SDG_0861_SEX_RT |
| jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |
| jenis_kelamin=MALE | SDG_0861_SEX_RT |
| jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |
| total | SDG_0861_SEX_RT, SL.TLF.0714.ZS, SL.UEM.NEET.ZS, var1186, var2658 |
| umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1186 | persen | 8.6.1 | umur 15–24; Sakernas; 2015–2025 | var.unit: 'Persen' |
| var2658 | persen | 8.7.1 | umur 5–17; 2020–2025; DKI dan DIY tidak ada 2024–2025 | var.unit: 'Persen' (judul menyebut 'Persentase dan Jumlah', berkas hanya persentase) |
| SL.UEM.NEET.ZS | persen | 8.6.1 | ILO Labour Force Statistics; kelompok umur pemuda | name: '(% of youth population)' |
| SL.TLF.0714.ZS | persen | 8.7.1 | umur 7–14; bekerja minimal satu jam seminggu; 2000–2010 | name: '(% of children ages 7-14)' |
| SDG_0861_SEX_RT | persen | 8.6.1 | umur 15–24; rincian jenis kelamin; OBS_STATUS B = patahan | UNIT_MEASURE PT |
| SDG_A871_SEX_AGE_RT | persen | 8.7.1 | kegiatan ekonomi saja; berkas hanya umur 15–17 (AGE_CLDVERSION_Y15-17); 2009 (survei pekerja anak), 2019, 2023 (Sakernas) | UNIT_MEASURE PT |
| SDG_B871_SEX_AGE_RT | persen | 8.7.1 | kegiatan ekonomi dan pekerjaan rumah tangga; hanya umur 15–17 dan 2009 | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1186 | 1100 | 2015 | total | 25.65 | bps/2026-10-17/json/sdg8_neet.json | 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg8_neet.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `6af01a80b8cb…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (646 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1186, var2658 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1186, var2658 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 58 | 0.38 – 35.38 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 574 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 646 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 58 | bps/2026-10-17/json/sdg8_8_7_1_v2658.json, bps/2026-10-17/json/sdg8_neet.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 58 | 41b13e4b1df67909c8d41e1527a585fa576ff107c1e5d7f87d8b109203e5e5ac, 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1186 | persen |
| var2658 | persen |

## data/gold/nasional.parquet (75 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SDG_0861_SEX_RT, SDG_A871_SEX_AGE_RT, SL.TLF.0714.ZS, SL.UEM.NEET.ZS, var1186, var2658 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total, umur=CLDVERSION_Y15-17 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1996, 1997, 1998, 1999, 2000, 2001, … (30 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 1.53 – 31.86 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 75 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 75 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 75 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_8_7_1_v2658.json, bps/2026-10-17/json/sdg8_neet.json, ilostat/2026-10-20/data/DF_SDG_0861_SEX_RT.csv, ilostat/2026-10-20/data/DF_SDG_A871_SEX_AGE_RT.csv, wdi/2026-10-20/data/kelompok-06-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 41b13e4b1df67909c8d41e1527a585fa576ff107c1e5d7f87d8b109203e5e5ac, 51ab5e7080ffe32ce20a0914bf7002e5d5c5523366fd72c207a5ce4732e8fc75, 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, cc4fc24190b0dbc8610ff3db8ef1db700180ccac03833ab5093d300fdec7e443 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (31 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | SL.TLF.0714.ZS, var1186, var2658 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | , SDG_0861_SEX_RT, SDG_A871_SEX_AGE_RT, SL.UEM.NEET.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | , total, umur=CLDVERSION_Y15-17 | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2000, 2009, 2010, 2015, 2016, 2017, … (14 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 1.53 – 24.77 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 12 | 1.567 – 22.919 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 12 | -0.055 – 2.48 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 12 | -2.3612 – 11.3761 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | cakupan berbeda, metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023, kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025), metode (olahan Sakernas yang sama); kelompok umur sama (15–24) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 31 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1186 | 1100 | 2015 | 25.65 | bps/2026-10-17/json/sdg8_neet.json |

1. Sel ini berasal dari baris Silver `var1186` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-17/json/sdg8_neet.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
