# Data dictionary — Kasus 09 Keterampilan TIK dan PAUD

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,653 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | IT.NET.USER.ZS, SE.PRE.ENRR, var1221, var1439, var1447, var1451 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1970, 1971, 1972, 1973, 1974, 1975, … (56 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 99.54 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 17.8.1, 4.2.2, 4.4.1(a), 4.4.1(b), 5.b.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1653 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1653 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1653 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_4_1_a_v1451.json, bps/2026-10-17/json/sdg4_4_4_1_b_v1447.json, bps/2026-10-17/json/sdg4_apk_paud.json, bps/2026-10-20/json/sdg5_5_b_1_v1221.json, wdi/2026-10-20/data/kelompok-02-hal-01.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0d660fabf0dd9f55bfa085f1389319add00e95460df49c478a0392fc7860805a, 30875615b1ea72a6037ab7fd6ff15f2c94d0ccc045c16bad45e4e0f747696cf6, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34, ef1cc76ad2b3cfdcfb262b3522c36dde363de4aa30eb806539682d56246f6b44, fbe8cf28d6155e4a441897df1a03ecc3ef5f16768b88af01127d83434a07024b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- (tidak ada dimensi)

| rincian | dipakai_seri |
|---|---|
| total | IT.NET.USER.ZS, SE.PRE.ENRR, var1221, var1439, var1447, var1451 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1451 | persen | 4.4.1(a) | umur 15–24; Susenas KOR; 2015–2025 | var.unit: 'Persen' |
| var1447 | persen | 4.4.1(b) | umur 15–59; 2015–2025 | var.unit: 'Persen' |
| var1439 | persen_apk | 4.2.2 | anak 3–6 tahun (var.note); Susenas; Papua Pegunungan 2024–2025 RSE 25–50% | judul 'Angka Partisipasi Kasar'; var.unit kosong; APK bisa > 100 |
| var1221 | persen | 5.b.1 | individu umur 5 tahun ke atas (var.note); Susenas KOR; ada di snapshot 17 dan 20 Oktober | var.unit: 'Persen' |
| SE.PRE.ENRR | persen_apk | 4.2.2 | UNESCO; kelompok umur resmi prasekolah; 1970–2018 | name: '(% gross)' |
| IT.NET.USER.ZS | persen | 17.8.1 | ITU; memakai internet dalam 3 bulan terakhir | name: '(% of population)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1221 | 1100 | 2015 | total | 51.50 | bps/2026-10-20/json/sdg5_5_b_1_v1221.json | d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg5_5_b_1_v1221.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `d8597519b86a…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,672 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1221, var1439, var1447, var1451 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1221, var1439, var1447, var1451 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 144 | 3.08 – 99.54 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 1486 | outlier, patahan_seri, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1672 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 144 | bps/2026-10-17/json/sdg4_4_4_1_a_v1451.json, bps/2026-10-17/json/sdg4_4_4_1_b_v1447.json, bps/2026-10-17/json/sdg4_apk_paud.json, bps/2026-10-20/json/sdg5_5_b_1_v1221.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 144 | 30875615b1ea72a6037ab7fd6ff15f2c94d0ccc045c16bad45e4e0f747696cf6, d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34, ef1cc76ad2b3cfdcfb262b3522c36dde363de4aa30eb806539682d56246f6b44, fbe8cf28d6155e4a441897df1a03ecc3ef5f16768b88af01127d83434a07024b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1221 | persen |
| var1439 | persen_apk |
| var1447 | persen |
| var1451 | persen |

## data/gold/nasional.parquet (125 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | IT.NET.USER.ZS, SE.PRE.ENRR, var1221, var1439, var1447, var1451 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1970, 1971, 1972, 1973, 1974, 1975, … (56 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 0 – 96.5 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 125 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 125 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 125 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_4_1_a_v1451.json, bps/2026-10-17/json/sdg4_4_4_1_b_v1447.json, bps/2026-10-17/json/sdg4_apk_paud.json, bps/2026-10-20/json/sdg5_5_b_1_v1221.json, wdi/2026-10-20/data/kelompok-02-hal-01.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0d660fabf0dd9f55bfa085f1389319add00e95460df49c478a0392fc7860805a, 30875615b1ea72a6037ab7fd6ff15f2c94d0ccc045c16bad45e4e0f747696cf6, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34, ef1cc76ad2b3cfdcfb262b3522c36dde363de4aa30eb806539682d56246f6b44, fbe8cf28d6155e4a441897df1a03ecc3ef5f16768b88af01127d83434a07024b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (33 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1221, var1439, var1451 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | IT.NET.USER.ZS, SE.PRE.ENRR, var1447 | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 33.84 – 96.5 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 8 | 22.0627 – 87.14 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen, persen_apk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 29 | -29.3531 – -12.1684 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 29 | -46.4498 – -25.6997 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | cakupan berbeda, definisi berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (kelompok umur acuan dan jenis layanan PAUD vs pendidikan prasekolah), kelompok umur berbeda; tidak dijumlah atau dirata-rata, konsep berbeda: kepemilikan perangkat vs penggunaan internet | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 12 | pasangan konteks: selisih tidak dihitung | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1221 | 1100 | 2015 | 51.50 | bps/2026-10-20/json/sdg5_5_b_1_v1221.json |

1. Sel ini berasal dari baris Silver `var1221` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-20/json/sdg5_5_b_1_v1221.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
