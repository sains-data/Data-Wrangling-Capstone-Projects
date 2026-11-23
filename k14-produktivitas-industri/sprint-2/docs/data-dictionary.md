# Data dictionary — Kasus 14 Produktivitas dan industri

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,779 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | NV.IND.MANF.ZS, SDG_0821_NOC_RT, SDG_0922_NOC_RT, SDG_B821_NOC_RT, SL.GDP.PCAP.EM.KD, var1161, … (9 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1983, 1984, 1985, 1986, 1987, 1988, … (45 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | -22.96 – 2.35351e+08 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_per_tahun, rupiah_per_tenaga_kerja, usd_ppp_2021 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 2.3.1(a), 8.2.1, 9.2.1, 9.2.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1779 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1779 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1779 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 1776 | B | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_produktivitas.json, bps/2026-10-20/json/sdg2_2_3_1_a_v1344.json, bps/2026-10-20/json/sdg9_9_2_1_v1214.json, bps/2026-10-20/json/sdg9_9_2_2_v2755.json, ilostat/2026-10-20/data/DF_SDG_0821_NOC_RT.csv, ilostat/2026-10-20/data/DF_SDG_0922_NOC_RT.csv, … (9 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0d660fabf0dd9f55bfa085f1389319add00e95460df49c478a0392fc7860805a, 15ea5e50768fda5f97447431e5d782a227945459c3c2774e823e39efca8e184f, 44a9d3d767406853932ac1c69afd2b2fefdf08e81f9d5a94117779576ea4d7fe, 5291422b0cf01e2e73ce65b25e348a3ac56bc17ab57e508af6b97e9b22b79074, 6027bfdef8581e770f831f1bff1bab8d774f1e39ffd1c1e6cc2ce663c00e3c44, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, … (9 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- (tidak ada dimensi)

| rincian | dipakai_seri |
|---|---|
| total | NV.IND.MANF.ZS, SDG_0821_NOC_RT, SDG_0922_NOC_RT, SDG_B821_NOC_RT, SL.GDP.PCAP.EM.KD, var1161, var1214, var1344, var2755 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1161 | persen_per_tahun | 8.2.1 | BPS diolah; 2011–2025; 2024 angka sementara, 2025 sangat sementara; 2024 provinsi Papua baru dihitung pada provinsi induk (var.note) | judul 'Laju Pertumbuhan ... Per Tahun'; var.unit kosong; nilai bisa negatif |
| var1344 | rupiah_per_tenaga_kerja | 2.3.1(a) | 2015–2023; 2022 angka sementara, 2023 sangat sementara | var.unit: 'Rupiah/Tenaga Kerja' |
| var1214 | persen | 9.2.1 | satu ukuran (proporsi terhadap PDB; bagian per kapita 9.2.1 tidak ada); dasar harga tidak disebut; 2010–2023 | judul 'Proporsi ... Terhadap PDB'; var.unit kosong; nilai 0–50 |
| var2755 | persen | 9.2.2 | Sakernas; 2018–2025; ada di dua snapshot | var.unit: 'Persen' |
| SL.GDP.PCAP.EM.KD | usd_ppp_2021 | 8.2.1 | tingkat PDB per orang bekerja; laju dihitung di Gold | name: '(constant 2021 PPP $)' |
| NV.IND.MANF.ZS | persen | 9.2.1 | ISIC Rev.3 C; dasar harga tidak disebut di name/sourceNote | name: '(% of GDP)' |
| SDG_0821_NOC_RT | persen_per_tahun | 8.2.1 | ILO modelled estimates; basis USD konstan 2015; sampai 2027 (2026–2027 proyeksi) | UNIT_MEASURE PT; judul DSD 'Annual growth rate' |
| SDG_B821_NOC_RT | persen_per_tahun | 8.2.1 | ILO modelled estimates; basis PPP 2021; nilainya sama dengan SDG_0821; sampai 2027 | UNIT_MEASURE PT; judul DSD 'Annual growth rate' |
| SDG_0922_NOC_RT | persen | 9.2.2 | olahan Sakernas (LFS); OBS_STATUS B = patahan | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1161 | 1100 | 2011 | total | 2.46 | bps/2026-10-17/json/sdg8_produktivitas.json | 5291422b0cf01e2e73ce65b25e348a3ac56bc17ab57e508af6b97e9b22b79074 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg8_produktivitas.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `5291422b0cf0…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,748 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1161, var1214, var1344, var2755 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1161, var1214, var1344, var2755 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2010, 2011, 2012, 2013, 2014, 2015, … (16 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 173 | -22.96 – 2.35351e+08 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_per_tahun, rupiah_per_tenaga_kerja | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 1508 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1748 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 173 | bps/2026-10-17/json/sdg8_produktivitas.json, bps/2026-10-20/json/sdg2_2_3_1_a_v1344.json, bps/2026-10-20/json/sdg9_9_2_1_v1214.json, bps/2026-10-20/json/sdg9_9_2_2_v2755.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 173 | 44a9d3d767406853932ac1c69afd2b2fefdf08e81f9d5a94117779576ea4d7fe, 5291422b0cf01e2e73ce65b25e348a3ac56bc17ab57e508af6b97e9b22b79074, 7ae7ec4aff93fb9e211efde623eb5010c3f4c655c7c187f0f6b59bd6b8af5c26, d8034830bd3de50fa76b40f4c7d89ff1fc1a4974b24cdb673cd6638bdc41be33 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1161 | persen_per_tahun |
| var1214 | persen |
| var1344 | rupiah_per_tenaga_kerja |
| var2755 | persen |

## data/gold/nasional.parquet (204 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | NV.IND.MANF.ZS, SDG_0821_NOC_RT, SDG_0922_NOC_RT, SDG_B821_NOC_RT, SL.GDP.PCAP.EM.KD, var1161, … (9 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1983, 1984, 1985, 1986, 1987, 1988, … (45 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | -1.84 – 6.6352e+07 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_per_tahun, rupiah_per_tenaga_kerja, usd_ppp_2021 | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 204 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 204 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 204 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_produktivitas.json, bps/2026-10-20/json/sdg2_2_3_1_a_v1344.json, bps/2026-10-20/json/sdg9_9_2_1_v1214.json, bps/2026-10-20/json/sdg9_9_2_2_v2755.json, ilostat/2026-10-20/data/DF_SDG_0821_NOC_RT.csv, ilostat/2026-10-20/data/DF_SDG_0922_NOC_RT.csv, … (9 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0d660fabf0dd9f55bfa085f1389319add00e95460df49c478a0392fc7860805a, 15ea5e50768fda5f97447431e5d782a227945459c3c2774e823e39efca8e184f, 44a9d3d767406853932ac1c69afd2b2fefdf08e81f9d5a94117779576ea4d7fe, 5291422b0cf01e2e73ce65b25e348a3ac56bc17ab57e508af6b97e9b22b79074, 6027bfdef8581e770f831f1bff1bab8d774f1e39ffd1c1e6cc2ce663c00e3c44, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, … (9 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (67 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3, P4 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1161, var1214, var2755 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | NV.IND.MANF.ZS, SDG_0821_NOC_RT, SDG_0922_NOC_RT, SDG_B821_NOC_RT, SL.GDP.PCAP.EM.KD (laju) | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | hitung, total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2010, 2011, 2012, 2013, 2014, 2015, … (16 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | -1.84 – 22.06 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 2 | -1.35 – 22.0386 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen, persen_per_tahun | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 2 | -2.887 – 3.437 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 2 | -73.7803 – 97.8366 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | WDI tingkat (USD PPP 2021), bukan laju; laju WDI dihitung di Gold sebelum dibandingkan, dasar harga belum diketahui di kedua sumber; dicek di Sprint 2, metode (PDB riil BPS vs estimasi model ILO); proyeksi ILO dikeluarkan, metode (olahan Sakernas yang sama) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 52 | pembanding = laju tahunan WDI dihitung dari tingkat | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1161 | 1100 | 2011 | 2.46 | bps/2026-10-17/json/sdg8_produktivitas.json |

1. Sel ini berasal dari baris Silver `var1161` × 1100 × 2011 × rincian `total` × berkas `bps/2026-10-17/json/sdg8_produktivitas.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
