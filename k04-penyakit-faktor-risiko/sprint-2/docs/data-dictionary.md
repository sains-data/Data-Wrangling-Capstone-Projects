# Data dictionary — Kasus 04 Penyakit dan faktor risiko

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,058 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | MALARIA_EST_INCIDENCE, M_Est_tob_curr_std, NCDMORT3070, SH.MLR.INCD.P3, var1393, var1435, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2000, 2001, 2002, 2003, 2004, 2005, … (27 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_kelamin=FEMALE, jenis_kelamin=MALE, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 80.05 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_penduduk, per_1000_penduduk_berisiko, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 3.3.3, 3.4.1, 3.4.1(b), 3.a.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 938 | 1.8 – 59.5 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 938 | 2.69927 – 95.6 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1058 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_3_3_v1393.json, bps/2026-10-20/json/sdg3_3_4_1_b_v1480.json, bps/2026-10-20/json/sdg3_3_a_1_v1435.json, wdi/2026-10-20/data/kelompok-05-hal-01.json, who_gho/2026-10-20/datadot/1F96863_NCDMORT3070.csv, who_gho/2026-10-20/datadot/442CEA8_MALARIA_EST_INCIDENCE.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 169a51a13766a16d365fcf0e873b4a377f67ec45f069cec49c2c33ccefa9b13c, 680084abcc4f9ba5f8468e366f3fe7e6b8c1eb1bae3f7d90ef48e34ca9017009, 6b358d9cbb03451834a181aa411a3eac4fc574cbe714d1dcc4b0ee74921dc936, 888fb8489ab0f4e0fc4118d5405c45df6a4605469464ea492aeb4c190036bd02, 96ea045ffa45717d4983f731f624fd2c2e2e9e27c8528de649d2c4dcc95ee914, a4efadaea837f2271cc645c56f0a0d758a8a6e8aa2561113142ca0919bf4dea6, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `umur`: kode sumber apa adanya

| rincian | dipakai_seri |
|---|---|
| jenis_kelamin=FEMALE | M_Est_tob_curr_std, NCDMORT3070 |
| jenis_kelamin=MALE | M_Est_tob_curr_std, NCDMORT3070 |
| total | MALARIA_EST_INCIDENCE, M_Est_tob_curr_std, NCDMORT3070, SH.MLR.INCD.P3, var1393, var1435, var1480 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1393 | per_1000_penduduk | 3.3.3 | kasus yang dilaporkan; sumber Kementerian Kesehatan, Profil Kesehatan Indonesia (var.note); penyebut seluruh penduduk ('per 1000 orang'), tahunan 2010–2021 | var.label: 'Kejadian Malaria Per 1000 Orang'; var.unit, kolom satuan CSV, dan satuan di manifest_asal kosong |
| var1480 | persen | 3.4.1(b) | survei: Riskesdas 2007 dan 2013, Sirkesnas 2016 (hanya Indonesia), Susenas+Riskesdas 2018 (var.note) | var.label: 'Prevalensi ...'; var.unit kosong; besaran angka 20–40 sesuai persen penduduk |
| var1435 | persen | 3.a.1 | penduduk 15+; Susenas Maret; var.def: data sebelum 2015 tidak tersedia (variabel belum dikumpulkan) | var.unit: 'Persen' |
| SH.MLR.INCD.P3 | per_1000_penduduk_berisiko | 3.3.3 | estimasi WHO (sourceOrganization: Global Health Observatory) | name: '(per 1,000 population at risk)' |
| MALARIA_EST_INCIDENCE | per_1000_penduduk_berisiko | 3.3.3 | estimasi model; penyebut penduduk di daerah penularan | kolom RATE_PER_1000_N; Denominator: 'Population living in areas where malaria transmission occurs' |
| NCDMORT3070 | persen | 3.4.1 | umur 30–69 (DIM_AGE tunggal); estimasi WHO Global Health Estimates [dimensi tetap di berkas: DIM_AGE=YEARS30-69] | kolom RATE_PER_100_N; UnitOfMeasure: percentage of 30-year-old people |
| M_Est_tob_curr_std | persen | 3.a.1 | penduduk 15+; semua produk tembakau (diisap dan tidak diisap); distandarkan umur; model Bayesian; 2025 dan 2030 proyeksi | kolom PERCENT_POP_N |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1393 | 1100 | 2010 | total | 0.88 | bps/2026-10-20/json/sdg3_3_3_3_v1393.json | 6b358d9cbb03451834a181aa411a3eac4fc574cbe714d1dcc4b0ee74921dc936 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg3_3_3_3_v1393.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `6b358d9cbb03…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,026 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1393, var1435, var1480 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1393, var1435, var1480 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2007, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 140 | 0 – 80.05 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 872 | outlier, patahan_seri, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1026 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 140 | bps/2026-10-20/json/sdg3_3_3_3_v1393.json, bps/2026-10-20/json/sdg3_3_4_1_b_v1480.json, bps/2026-10-20/json/sdg3_3_a_1_v1435.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 140 | 680084abcc4f9ba5f8468e366f3fe7e6b8c1eb1bae3f7d90ef48e34ca9017009, 6b358d9cbb03451834a181aa411a3eac4fc574cbe714d1dcc4b0ee74921dc936, 96ea045ffa45717d4983f731f624fd2c2e2e9e27c8528de649d2c4dcc95ee914 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1393 | per_1000_penduduk |
| var1435 | persen |
| var1480 | persen |

## data/gold/nasional.parquet (108 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | MALARIA_EST_INCIDENCE, M_Est_tob_curr_std, NCDMORT3070, SH.MLR.INCD.P3, var1393, var1435, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 2000, 2001, 2002, 2003, 2004, 2005, … (27 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 0.84 – 39.8 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_penduduk, per_1000_penduduk_berisiko, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 52 | 2.23876 – 30.9 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 52 | 2.69927 – 49.4 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 108 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_3_3_v1393.json, bps/2026-10-20/json/sdg3_3_4_1_b_v1480.json, bps/2026-10-20/json/sdg3_3_a_1_v1435.json, wdi/2026-10-20/data/kelompok-05-hal-01.json, who_gho/2026-10-20/datadot/1F96863_NCDMORT3070.csv, who_gho/2026-10-20/datadot/442CEA8_MALARIA_EST_INCIDENCE.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 169a51a13766a16d365fcf0e873b4a377f67ec45f069cec49c2c33ccefa9b13c, 680084abcc4f9ba5f8468e366f3fe7e6b8c1eb1bae3f7d90ef48e34ca9017009, 6b358d9cbb03451834a181aa411a3eac4fc574cbe714d1dcc4b0ee74921dc936, 888fb8489ab0f4e0fc4118d5405c45df6a4605469464ea492aeb4c190036bd02, 96ea045ffa45717d4983f731f624fd2c2e2e9e27c8528de649d2c4dcc95ee914, a4efadaea837f2271cc645c56f0a0d758a8a6e8aa2561113142ca0919bf4dea6, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (71 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3, P4 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | MALARIA_EST_INCIDENCE, var1393, var1435, var1480 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | MALARIA_EST_INCIDENCE, M_Est_tob_curr_std, NCDMORT3070, SH.MLR.INCD.P3 | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2000, 2001, 2002, 2003, 2004, 2005, … (26 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 8 | 0.84 – 34.1 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 6 | 1.56 – 38.7 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | per_1000_penduduk, per_1000_penduduk_berisiko, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 19 | -9.94 – 2.15421 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 19 | -78.5905 – 114.123 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan, vintage berbeda | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi), definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan, definisi berbeda: prevalensi faktor risiko vs probabilitas kematian, vintage | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 66 | pasangan konteks: selisih tidak dihitung, tahun proyeksi, tidak dibandingkan | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1393 | 1100 | 2010 | 0.88 | bps/2026-10-20/json/sdg3_3_3_3_v1393.json |

1. Sel ini berasal dari baris Silver `var1393` × 1100 × 2010 × rincian `total` × berkas `bps/2026-10-20/json/sdg3_3_3_3_v1393.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
