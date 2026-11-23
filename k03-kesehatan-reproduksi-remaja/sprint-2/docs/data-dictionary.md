# Data dictionary — Kasus 03 Kesehatan reproduksi remaja

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (235 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | MDG_0000000003, SDGFPALL, SP.ADO.TFRT, var1353, var1394 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (35 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1960, 1961, 1962, 1963, 1964, 1965, … (65 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total, umur=10-14, umur=15-19 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.264736 – 151.704 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_perempuan_seumur, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 3.7.1, 3.7.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 235 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 235 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 235 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_7_1_v1394.json, bps/2026-10-20/json/sdg3_3_7_2_v1353.json, wdi/2026-10-20/data/kelompok-07-hal-01.json, who_gho/2026-10-20/datadot/27D371A_MDG_0000000003.csv, who_gho/2026-10-20/datadot/8074BD9_SDGFPALL.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 230ce163135e9ea9e078649b2812136780e9e2db9d4c110dc3e21f2fe50faf5a, 6ae359c6df0dfd6ce210233dc28ada9060be0996f855288d6c4fbfee88b55c74, 894de8e94f8c2c76aaa44f3a3f541607429e924d9101a80a2d5eebcfe433284b, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, efd85410d3d2939a3fabcb1a17489a3860985eec2685d49787919c3657a7e702 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `umur`: `10-14`, `15-19`

| rincian | dipakai_seri |
|---|---|
| total | SDGFPALL, SP.ADO.TFRT, var1353, var1394 |
| umur=10-14 | MDG_0000000003 |
| umur=15-19 | MDG_0000000003 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1394 | persen | 3.7.1 | perempuan 15–49 atau pasangannya; sumber SDKI (var.note); hanya tahun survei 2012 dan 2017 | var.unit: 'Persen' |
| var1353 | per_1000_perempuan_seumur | 3.7.2 | umur 15–19 saja (judul var.label; tidak ada kelompok 10–14); sumber IDHS/SDKI (var.note); judul berakhir dengan spasi | var.unit dan kolom satuan CSV kosong; judul menyebut perempuan 15–19; definisi baku indikator yang sama di metadata WHO ('per 1,000 females in the respective age group') dan nama WDI ('births per 1,000 women ages 15-19'); besaran angka (puluhan) sesuai per 1.000, bukan persen |
| SP.ADO.TFRT | per_1000_perempuan_seumur | 3.7.2 | umur 15–19; estimasi model World Population Prospects (UN Population Division), tahunan | name: '(births per 1,000 women ages 15-19)' |
| MDG_0000000003 | per_1000_perempuan_seumur | 3.7.2 | perempuan; dua kelompok umur (10–14, 15–19) di kolom rincian; data survei/registrasi, tahun tidak lengkap [dimensi tetap di berkas: DIM_SEX=FEMALE] | kolom RATE_PER_1000_N; UnitOfMeasure: 'Annual number of births per 1000 adolescent women' |
| SDGFPALL | persen | 3.7.1 | perempuan 15–49; penyebut = permintaan KB total (pemakai semua metode + kebutuhan tak terpenuhi) [dimensi tetap di berkas: DIM_SEX=FEMALE; DIM_AGE=Y15T49] | kolom RATE_PER_100_N |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1353 | 1100 | 2012 | total | 25.00 | bps/2026-10-20/json/sdg3_3_7_2_v1353.json | 230ce163135e9ea9e078649b2812136780e9e2db9d4c110dc3e21f2fe50faf5a |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg3_3_7_2_v1353.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `230ce163135e…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (152 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1353, var1394 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1353, var1394 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2012, 2017 | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 18 | 15 – 104 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_perempuan_seumur, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 149 | outlier | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 152 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 18 | bps/2026-10-20/json/sdg3_3_7_1_v1394.json, bps/2026-10-20/json/sdg3_3_7_2_v1353.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 18 | 230ce163135e9ea9e078649b2812136780e9e2db9d4c110dc3e21f2fe50faf5a, 6ae359c6df0dfd6ce210233dc28ada9060be0996f855288d6c4fbfee88b55c74 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1353 | per_1000_perempuan_seumur |
| var1394 | persen |

## data/gold/nasional.parquet (89 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | MDG_0000000003, SDGFPALL, SP.ADO.TFRT, var1353, var1394 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total, umur=15-19 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1960, 1961, 1962, 1963, 1964, 1965, … (65 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 25.646 – 151.704 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_perempuan_seumur, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 89 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 89 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 89 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_7_1_v1394.json, bps/2026-10-20/json/sdg3_3_7_2_v1353.json, wdi/2026-10-20/data/kelompok-07-hal-01.json, who_gho/2026-10-20/datadot/27D371A_MDG_0000000003.csv, who_gho/2026-10-20/datadot/8074BD9_SDGFPALL.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 230ce163135e9ea9e078649b2812136780e9e2db9d4c110dc3e21f2fe50faf5a, 6ae359c6df0dfd6ce210233dc28ada9060be0996f855288d6c4fbfee88b55c74, 894de8e94f8c2c76aaa44f3a3f541607429e924d9101a80a2d5eebcfe433284b, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, efd85410d3d2939a3fabcb1a17489a3860985eec2685d49787919c3657a7e702 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (28 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3, P4 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | MDG_0000000003, var1353, var1394 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total, umur=15-19 | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | MDG_0000000003, SDGFPALL, SP.ADO.TFRT | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total, umur=15-19 | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2001, 2002, 2003, 2004, 2005, 2006, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 8 | 36 – 57.9 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 0 | 32.792 – 79 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | per_1000_perempuan_seumur, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 8 | -21.1 – 5.50605 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 8 | -26.7089 – 10.9975 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (penyebut berbeda: BPS lebih dekat ke prevalensi kontrasepsi modern), metode (survei dengan periode rujukan vs estimasi model penduduk tahunan), sumber berbeda (WHO: data survei/registrasi yang dihimpun; WDI: model WPP), tidak ada tahun beririsan; dibandingkan dengan tahun terdekat di Gold (Sprint 2) dengan penanda | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 26 | pembanding tahun 2011 (tidak ada tahun yang sama; tahun terdekat), pembanding tahun 2016 (tidak ada tahun yang sama; tahun terdekat) | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1353 | 1100 | 2012 | 25.00 | bps/2026-10-20/json/sdg3_3_7_2_v1353.json |

1. Sel ini berasal dari baris Silver `var1353` × 1100 × 2012 × rincian `total` × berkas `bps/2026-10-20/json/sdg3_3_7_2_v1353.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
