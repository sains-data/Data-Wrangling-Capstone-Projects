# Data dictionary — Kasus 06 Melek aksara

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (5,762 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci, var1458 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1980, 1990, 2004, 2006, 2008, 2009, … (22 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | daerah=RURAL, daerah=RURAL;jenis_kelamin=FEMALE, daerah=RURAL;jenis_kelamin=MALE, daerah=URBAN, daerah=URBAN;jenis_kelamin=FEMALE, daerah=URBAN;jenis_kelamin=MALE, … (9 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 43.12 – 99.98 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 4.6.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 5762 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 5762 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 5762 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_amh.json, bps/2026-10-17/json/sdg4_amh_rinci.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 6a81eaf2622acf1a3ac1c188a34716d0d5490e2851383b96cca8ee4f2a490102, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `jenis_kelamin`: `FEMALE`, `MALE`

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | tabel:sdg4_amh_rinci |
| daerah=RURAL;jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| daerah=RURAL;jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| daerah=URBAN | tabel:sdg4_amh_rinci |
| daerah=URBAN;jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| daerah=URBAN;jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| total | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci, var1458 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1458 | persen | 4.6.1 | penduduk 15+; Susenas; 2014–2025; tabel ringkas tanpa rincian | var.unit: 'Persen' |
| tabel:sdg4_amh_rinci | persen | 4.6.1 | penduduk 15+; tabel statis (HTML) 2009–2025; rincian perkotaan/perdesaan x laki-laki/perempuan | judul tabel statis (angka melek aksara, persen) |
| SE.ADT.LITR.ZS | persen | 4.6.1 | penduduk 15+; UNESCO UIS; 13 tahun tidak berurutan 1980–2020 | name: '(% of people ages 15 and above)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | tabel:sdg4_amh_rinci | 1100 | 2009 | daerah=RURAL | 95.33 | bps/2026-10-17/json/sdg4_amh_rinci.json | 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg4_amh_rinci.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `90eedd9a4266…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,102 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | tabel:sdg4_amh_rinci, var1458 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | tabel:sdg4_amh_rinci, var1458 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2009, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 107 | 64.08 – 99.87 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 969 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1102 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 107 | bps/2026-10-17/json/sdg4_amh.json, bps/2026-10-17/json/sdg4_amh_rinci.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 107 | 6a81eaf2622acf1a3ac1c188a34716d0d5490e2851383b96cca8ee4f2a490102, 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| tabel:sdg4_amh_rinci | persen |
| var1458 | persen |

## data/gold/nasional.parquet (42 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci, var1458 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1980, 1990, 2004, 2006, 2008, 2009, … (22 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 67.31 – 97.1 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 42 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 42 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 42 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_amh.json, bps/2026-10-17/json/sdg4_amh_rinci.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 6a81eaf2622acf1a3ac1c188a34716d0d5490e2851383b96cca8ee4f2a490102, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (41 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | tabel:sdg4_amh_rinci, var1458 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2009, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 92.58 – 97.1 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 16 | 92.32 – 97.1 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 16 | -0.42 – 0.59 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 16 | -0.437865 – 0.639082 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | belum terjelaskan, metode berbeda, tanpa pasangan, tidak berselisih | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | dua tabel penerbit yang sama; selisih (bila ada) dilaporkan, tidak disamakan paksa, metode, metode (Susenas vs kompilasi UNESCO dari sensus/survei) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 41 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| tabel:sdg4_amh_rinci | 1100 | 2009 | 96.39 | bps/2026-10-17/json/sdg4_amh_rinci.json |

1. Sel ini berasal dari baris Silver `tabel:sdg4_amh_rinci` × 1100 × 2009 × rincian `total` × berkas `bps/2026-10-17/json/sdg4_amh_rinci.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
