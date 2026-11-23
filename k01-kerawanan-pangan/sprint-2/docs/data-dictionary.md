# Data dictionary — Kasus 01 Kerawanan pangan provinsi

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,414 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | NUTOVERWEIGHTPREV, NUTRITION_WH_2, NUTSTUNTINGPREV, SN.ITK.DEFC.ZS, SN.ITK.MSFI.ZS, var1473, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1996, 2000, 2001, 2002, 2003, 2004, … (27 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | daerah=RURAL, daerah=URBAN, daerah=URBAN;umur=MONTHS36-47, jenis_kelamin=FEMALE, jenis_kelamin=FEMALE;umur=MONTHS0-11, jenis_kelamin=FEMALE;umur=MONTHS0-23, … (69 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.76 – 41.3 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 2.1.1, 2.1.2, 2.2.1, 2.2.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 743 | 2 – 39.7 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 743 | 3 – 43.2 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1414 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg2_2_1_1_v1473.json, bps/2026-10-20/json/sdg2_2_1_2_v1474.json, wdi/2026-10-20/data/kelompok-07-hal-01.json, who_gho/2026-10-20/datadot/5F8A486_NUTSTUNTINGPREV.csv, who_gho/2026-10-20/datadot/64E2430_NUTOVERWEIGHTPREV.csv, who_gho/2026-10-20/datadot/FC5231F_NUTRITION_WH_2.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 1fe5692210b0680a498b54109dce833337d30c8dc4aa99e878c086ca2f1ccd7c, 3b24b0d262a260773947ab85ed1d4b5b4c7c31323c5b9ddf89b4195b685b4143, 541e092ddd477ac63087a2bf687866ad198f638f342aab78de44b205134547e7, 6f82d02015acd806bba1cfd4a135afe5a58e9fb681ea3e2761373edbe94b55bf, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, fb558326c07b808df527b7b01dbdf5453975e464d2dede3f2a75b319e631355c | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `desil`: kode sumber apa adanya
- `jenis_kelamin`: `FEMALE`, `MALE`
- `kekayaan`: kode sumber apa adanya
- `kuintil`: kode sumber apa adanya
- `pendidikan_ibu`: kode sumber apa adanya
- `tersil`: kode sumber apa adanya
- `umur`: kode sumber apa adanya

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | NUTRITION_WH_2 |
| daerah=URBAN | NUTRITION_WH_2 |
| daerah=URBAN;umur=MONTHS36-47 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE | NUTOVERWEIGHTPREV, NUTRITION_WH_2, NUTSTUNTINGPREV |
| jenis_kelamin=FEMALE;umur=MONTHS0-11 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS0-23 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS0-5 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS12-17 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS12-23 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS12-59 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS18-23 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS24-29 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS24-35 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS24-59 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS30-35 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS36-41 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS36-47 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS36-59 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS42-47 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS48-53 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS48-59 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS54-59 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS6-11 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS6-23 | NUTRITION_WH_2 |
| jenis_kelamin=FEMALE;umur=MONTHS6-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE | NUTOVERWEIGHTPREV, NUTRITION_WH_2, NUTSTUNTINGPREV |
| jenis_kelamin=MALE;umur=MONTHS0-11 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS0-23 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS0-5 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS12-17 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS12-23 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS12-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS18-23 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS24-29 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS24-35 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS24-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS30-35 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS36-41 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS36-47 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS36-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS42-47 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS48-53 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS48-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS54-59 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS6-11 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS6-23 | NUTRITION_WH_2 |
| jenis_kelamin=MALE;umur=MONTHS6-59 | NUTRITION_WH_2 |
| total | NUTOVERWEIGHTPREV, NUTRITION_WH_2, NUTSTUNTINGPREV, SN.ITK.DEFC.ZS, SN.ITK.MSFI.ZS, var1473, var1474 |
| umur=MONTHS0-11 | NUTRITION_WH_2 |
| umur=MONTHS0-23 | NUTRITION_WH_2 |
| umur=MONTHS0-5 | NUTRITION_WH_2 |
| umur=MONTHS12-17 | NUTRITION_WH_2 |
| umur=MONTHS12-23 | NUTRITION_WH_2 |
| umur=MONTHS12-59 | NUTRITION_WH_2 |
| umur=MONTHS18-23 | NUTRITION_WH_2 |
| umur=MONTHS24-29 | NUTRITION_WH_2 |
| umur=MONTHS24-35 | NUTRITION_WH_2 |
| umur=MONTHS24-59 | NUTRITION_WH_2 |
| umur=MONTHS30-35 | NUTRITION_WH_2 |
| umur=MONTHS36-41 | NUTRITION_WH_2 |
| umur=MONTHS36-47 | NUTRITION_WH_2 |
| umur=MONTHS36-59 | NUTRITION_WH_2 |
| umur=MONTHS42-47 | NUTRITION_WH_2 |
| umur=MONTHS48-53 | NUTRITION_WH_2 |
| umur=MONTHS48-59 | NUTRITION_WH_2 |
| umur=MONTHS54-59 | NUTRITION_WH_2 |
| umur=MONTHS6-11 | NUTRITION_WH_2 |
| umur=MONTHS6-23 | NUTRITION_WH_2 |
| umur=MONTHS6-59 | NUTRITION_WH_2 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1473 | persen | 2.1.1 | seluruh penduduk; sumber Susenas (var.note); tahunan 2017–2025 | var.unit: 'Persen'; kolom satuan CSV 'Persen' |
| var1474 | persen | 2.1.2 | seluruh penduduk; FIES setidaknya sekali dalam 12 bulan terakhir; sumber Susenas (var.note) | var.unit: 'Persen' |
| SN.ITK.DEFC.ZS | persen | 2.1.1 | estimasi FAO; sourceNote: angka 2.5 dapat berarti kurang dari 2,5% | name: '(% of population)' |
| SN.ITK.MSFI.ZS | persen | 2.1.2 | estimasi FAO; rumah tangga dengan sedikitnya satu orang dewasa mengalami kerawanan sedang atau berat | name: '(%)' |
| NUTSTUNTINGPREV | persen | 2.2.1 | balita; estimasi tahunan 2000–2024 | kolom RATE_PER_100_N |
| NUTOVERWEIGHTPREV | persen | 2.2.2 | balita; estimasi tahunan 2000–2024 | kolom RATE_PER_100_N |
| NUTRITION_WH_2 | persen | 2.2.2 | balita; angka survei (12 tahun survei 1996–2023) dengan rincian umur, jenis kelamin, daerah | kolom RATE_PER_100_N |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1473 | 1100 | 2017 | total | 8.40 | bps/2026-10-20/json/sdg2_2_1_1_v1473.json | 541e092ddd477ac63087a2bf687866ad198f638f342aab78de44b205134547e7 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg2_2_1_1_v1473.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `541e092ddd47…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (684 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1473, var1474 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1473, var1474 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2017, 2018, 2019, 2020, 2021, 2022, … (9 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 56 | 0.76 – 38.35 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 570 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 684 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 56 | bps/2026-10-20/json/sdg2_2_1_1_v1473.json, bps/2026-10-20/json/sdg2_2_1_2_v1474.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 56 | 541e092ddd477ac63087a2bf687866ad198f638f342aab78de44b205134547e7, 6f82d02015acd806bba1cfd4a135afe5a58e9fb681ea3e2761373edbe94b55bf | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1473 | persen |
| var1474 | persen |

## data/gold/nasional.parquet (114 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | NUTOVERWEIGHTPREV, NUTRITION_WH_2, NUTSTUNTINGPREV, SN.ITK.DEFC.ZS, SN.ITK.MSFI.ZS, var1473, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1996, 2000, 2001, 2002, 2003, 2004, … (27 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 2.6 – 39.8 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 56 | 2.1 – 38 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 56 | 3.2 – 41.7 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 114 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg2_2_1_1_v1473.json, bps/2026-10-20/json/sdg2_2_1_2_v1474.json, wdi/2026-10-20/data/kelompok-07-hal-01.json, who_gho/2026-10-20/datadot/5F8A486_NUTSTUNTINGPREV.csv, who_gho/2026-10-20/datadot/64E2430_NUTOVERWEIGHTPREV.csv, who_gho/2026-10-20/datadot/FC5231F_NUTRITION_WH_2.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 1fe5692210b0680a498b54109dce833337d30c8dc4aa99e878c086ca2f1ccd7c, 3b24b0d262a260773947ab85ed1d4b5b4c7c31323c5b9ddf89b4195b685b4143, 541e092ddd477ac63087a2bf687866ad198f638f342aab78de44b205134547e7, 6f82d02015acd806bba1cfd4a135afe5a58e9fb681ea3e2761373edbe94b55bf, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, fb558326c07b808df527b7b01dbdf5453975e464d2dede3f2a75b319e631355c | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (68 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | NUTSTUNTINGPREV, var1473, var1474 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | NUTOVERWEIGHTPREV, NUTRITION_WH_2, SN.ITK.DEFC.ZS, SN.ITK.MSFI.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2000, 2001, 2002, 2003, 2004, 2005, … (26 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 4 – 39.8 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 16 | 2.6 – 14.8 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 52 | -0.38 – 3.61 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 52 | -6.55172 – 54.697 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan, tidak berselisih | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk, metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket, sumber data dan cara estimasi berbeda; definisi FIES sama | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 32 | pasangan konteks: selisih tidak dihitung | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1473 | 1100 | 2017 | 8.40 | bps/2026-10-20/json/sdg2_2_1_1_v1473.json |

1. Sel ini berasal dari baris Silver `var1473` × 1100 × 2017 × rincian `total` × berkas `bps/2026-10-20/json/sdg2_2_1_1_v1473.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
