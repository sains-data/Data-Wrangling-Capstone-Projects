# Data dictionary — Kasus 08 Kesetaraan pendidikan

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (5,418 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SE.ENR.PRSC.FM.ZS, SE.PRM.CMPT.ZS, var1980, var2211, var2595, var2600, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1970, 1971, 1972, 1973, 1974, 1975, … (53 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenjang=sd, jenjang=sm, jenjang=sma, jenjang=smp, total, umur=13-15, … (9 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.77275 – 260.23 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk, rasio, rasio_x100 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 4.1, 4.1.2, 4.5.1, — | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 5418 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 5418 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 5418 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_5_1_v2595.json, bps/2026-10-17/json/sdg4_4_5_1_v2600.json, bps/2026-10-17/json/sdg4_apm.json, bps/2026-10-17/json/sdg4_aps.json, bps/2026-10-17/json/sdg4_completion.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 06c48066f084752f88c482b94decbbacaf6991ea8507b699f351d9653756c5af, 684f1d2cc37f2ae7cbb57da4690ffa4173f3ed38e8f81dd53d7c332af301da3f, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, ac1d12474a59846c4e487beef7d1011f916b2dd26a02a0ccf4b11b6e8ed7883d, ce205cbf83a8c34c941c1c96d35911a201d70f095f03c956308e0e3de4948dc8, e0b1421956b6673054b20aa8b5ecab4dce37ae2b73a7b1b9b0eb6d040652132f | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenjang`: `sd`, `sm`, `sma`, `smp`
- `umur`: `13-15`, `16-18`, `19-23`, `7-12`
- `jenjang` (var304, dari turvar BPS): `sd` = SD/sederajat, `smp` = SMP/sederajat, `sm` = SM/sederajat
- `jenjang` (var1980, dari turvar BPS): `sd` = SD / Sederajat, `smp` = SMP / Sederajat, `sma` = SMA / Sederajat
- `umur` (var2211, dari turvar BPS): `7-12` = 7-12, `13-15` = 13-15, `16-18` = 16-18, `19-23` = 19-23

| rincian | dipakai_seri |
|---|---|
| jenjang=sd | var1980, var304 |
| jenjang=sm | var304 |
| jenjang=sma | var1980 |
| jenjang=smp | var1980, var304 |
| total | SE.ENR.PRSC.FM.ZS, SE.PRM.CMPT.ZS, var2595, var2600 |
| umur=13-15 | var2211 |
| umur=16-18 | var2211 |
| umur=19-23 | var2211 |
| umur=7-12 | var2211 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var304 | persen | 4.1 | Susenas; 2003–2025; mulai 2007 termasuk paket A/B/C (var.note) | judul 'Angka Partisipasi Murni'; var.unit kosong; APM hanya siswa usia jenjang, jadi <= 100 |
| var2595 | rasio_x100 | 4.5.1 | jenjang SMA; paritas kuintil (bukan jenis kelamin); 2020–2025 | judul 'Rasio APK ... kuintil terendah/kuintil tertinggi'; var.unit kosong; nilai 32–124, Indonesia ±77: rasio dikali 100 |
| var2600 | rasio_x100 | 4.5.1 | jenjang perguruan tinggi; paritas jenis kelamin; 2020–2025 | judul 'Rasio APK ... perempuan/laki-laki'; var.unit kosong; nilai 62–260, Indonesia ±115: rasio dikali 100 |
| var1980 | persen | 4.1.2 | SD, SMP, SMA; 2015–2023 | var.note: 'persentase anak dan remaja yang berhasil menyelesaikan' |
| var2211 | persen | — | umur 7–12, 13–15, 16–18, 19–23; 2015–2025; var.note berisi definisi indikator lain (disabilitas) | judul 'Angka Partisipasi Sekolah'; var.unit kosong; nilai <= 100 |
| SE.ENR.PRSC.FM.ZS | rasio | 4.5.1 | SD dan sekolah menengah; paritas jenis kelamin; 1970–2018 | name: 'gender parity index' |
| SE.PRM.CMPT.ZS | persen_apk | 4.1.2 | rasio masuk kasar ke kelas terakhir SD; UNESCO | sourceNote: gross intake ratio to the last grade, tanpa memandang umur (bisa > 100) |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1980 | 1100 | 2015 | jenjang=sd | 96.47 | bps/2026-10-17/json/sdg4_completion.json | e0b1421956b6673054b20aa8b5ecab4dce37ae2b73a7b1b9b0eb6d040652132f |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg4_completion.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `e0b1421956b6…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (5,776 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1980 [jenjang=sd], var1980 [jenjang=sma], var1980 [jenjang=smp], var2211 [umur=13-15], var2211 [umur=16-18], var2211 [umur=19-23], … (12 nilai) | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1980, var2211, var2595, var2600, var304 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | jenjang=sd, jenjang=sm, jenjang=sma, jenjang=smp, total, umur=13-15, … (9 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2003, 2004, 2005, 2006, 2007, 2008, … (23 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 599 | 12.48 – 260.23 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, rasio_x100 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 5225 | outlier, patahan_seri, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 5776 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 599 | bps/2026-10-17/json/sdg4_4_5_1_v2595.json, bps/2026-10-17/json/sdg4_4_5_1_v2600.json, bps/2026-10-17/json/sdg4_apm.json, bps/2026-10-17/json/sdg4_aps.json, bps/2026-10-17/json/sdg4_completion.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 599 | 06c48066f084752f88c482b94decbbacaf6991ea8507b699f351d9653756c5af, 684f1d2cc37f2ae7cbb57da4690ffa4173f3ed38e8f81dd53d7c332af301da3f, ac1d12474a59846c4e487beef7d1011f916b2dd26a02a0ccf4b11b6e8ed7883d, ce205cbf83a8c34c941c1c96d35911a201d70f095f03c956308e0e3de4948dc8, e0b1421956b6673054b20aa8b5ecab4dce37ae2b73a7b1b9b0eb6d040652132f | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1980 [jenjang=sd] | persen |
| var1980 [jenjang=sma] | persen |
| var1980 [jenjang=smp] | persen |
| var2211 [umur=13-15] | persen |
| var2211 [umur=16-18] | persen |
| var2211 [umur=19-23] | persen |
| var2211 [umur=7-12] | persen |
| var2595 | rasio_x100 |
| var2600 | rasio_x100 |
| var304 [jenjang=sd] | persen |
| var304 [jenjang=sm] | persen |
| var304 [jenjang=smp] | persen |

## data/gold/nasional.parquet (110 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SE.ENR.PRSC.FM.ZS, SE.PRM.CMPT.ZS, var1980, var2595, var2600 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | jenjang=sd, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1970, 1971, 1972, 1973, 1974, 1975, … (53 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 0.77275 – 121.96 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk, rasio, rasio_x100 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 110 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 110 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 110 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_5_1_v2595.json, bps/2026-10-17/json/sdg4_4_5_1_v2600.json, bps/2026-10-17/json/sdg4_completion.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 684f1d2cc37f2ae7cbb57da4690ffa4173f3ed38e8f81dd53d7c332af301da3f, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, ce205cbf83a8c34c941c1c96d35911a201d70f095f03c956308e0e3de4948dc8, e0b1421956b6673054b20aa8b5ecab4dce37ae2b73a7b1b9b0eb6d040652132f | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (21 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1980, var2595, var2600 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | jenjang=sd, total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | , SE.ENR.PRSC.FM.ZS, SE.PRM.CMPT.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | , total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 75.67 – 121.96 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 12 | 99.9522 – 108.897 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen, rasio_x100 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 12 | -17.4567 – -2.12217 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 12 | -16.0305 – -2.12319 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi berbeda: jenjang berbeda (PT vs SD dan menengah); skala BPS x100, WDI x1, definisi berbeda: umur 3–5 tahun di atas umur lulus (BPS) vs siswa baru kelas terakhir tanpa memandang umur (WDI), tidak ada seri paritas kuintil di paket pembanding | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 21 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1980 [jenjang=sd] | 1100 | 2015 | 96.47 | bps/2026-10-17/json/sdg4_completion.json |

1. Sel ini berasal dari baris Silver `var1980` × 1100 × 2015 × rincian `jenjang=sd` × berkas `bps/2026-10-17/json/sdg4_completion.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
