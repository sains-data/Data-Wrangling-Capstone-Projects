# Data dictionary — Kasus 12 Upah dan informalitas

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,584 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB, var1172, var2153 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2007, 2008, 2009, 2010, 2012, 2013, … (18 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jabatan=ISCO08_0, jabatan=ISCO08_0;jenis_kelamin=FEMALE, jabatan=ISCO08_0;jenis_kelamin=MALE, jabatan=ISCO08_1, jabatan=ISCO08_1;jenis_kelamin=FEMALE, jabatan=ISCO08_1;jenis_kelamin=MALE, … (117 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 29.57 – 52167.3 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, rupiah_per_jam | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 8.3.1, 8.5.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1584 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1584 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1584 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 1440 | B | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_informal.json, bps/2026-10-17/json/sdg8_upah.json, ilostat/2026-10-20/data/DF_SDG_0831_SEX_ECO_RT.csv, ilostat/2026-10-20/data/DF_SDG_0851_SEX_OCU_NB.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 2885bba78ad1680f6b69b016af6a7f572b7052ece051b378367f79be59000538, 61c59b5214390beb353baf69c2cffffce148357e84863f82352162fa8926b4f2, 8de35e0462037775b72e7ac41bc7e4e59c129a8c59026531effcf4e46f8b1007, e5c31b36f2856989022c3e3865d88de07454b0bf7f4192891b56b1111934f8ec | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jabatan`: kode sumber apa adanya
- `jenis_kelamin`: `FEMALE`, `MALE`
- `sektor`: kode sumber apa adanya

| rincian | dipakai_seri |
|---|---|
| jabatan=ISCO08_0 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_0;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_0;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_1 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_1;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_1;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_2 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_2;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_2;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_3 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_3;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_3;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_4 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_4;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_4;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_5 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_5;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_5;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_6 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_6;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_6;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_7 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_7;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_7;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_8 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_8;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_8;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_9 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_9;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_9;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_TOTAL | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_TOTAL;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO08_TOTAL;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_0 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_0;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_0;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_1 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_1;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_1;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_2 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_2;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_2;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_3 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_3;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_3;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_4 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_4;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_4;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_5 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_5;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_5;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_6 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_6;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_6;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_7 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_7;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_7;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_8 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_8;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_8;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_9 | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_9;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_9;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_TOTAL | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_TOTAL;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_TOTAL;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_X | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_X;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=ISCO88_X;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L1 | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L1;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L1;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L2 | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L2;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L2;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L3-4 | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L3-4;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_L3-4;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_X | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_X;jenis_kelamin=FEMALE | SDG_0851_SEX_OCU_NB |
| jabatan=SKILL_X;jenis_kelamin=MALE | SDG_0851_SEX_OCU_NB |
| jenis_kelamin=FEMALE | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_AGR | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_CON | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_MAN | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_MEL | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_MKT | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_PUB | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=AGGREGATE_TOTAL | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=SECTOR_AGR | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=SECTOR_IND | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=SECTOR_NAG | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=FEMALE;sektor=SECTOR_SER | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB |
| jenis_kelamin=MALE;sektor=AGGREGATE_AGR | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_CON | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_MAN | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_MEL | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_MKT | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_PUB | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=AGGREGATE_TOTAL | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=SECTOR_AGR | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=SECTOR_IND | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=SECTOR_NAG | SDG_0831_SEX_ECO_RT |
| jenis_kelamin=MALE;sektor=SECTOR_SER | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_AGR | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_CON | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_MAN | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_MEL | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_MKT | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_PUB | SDG_0831_SEX_ECO_RT |
| sektor=AGGREGATE_TOTAL | SDG_0831_SEX_ECO_RT |
| sektor=SECTOR_AGR | SDG_0831_SEX_ECO_RT |
| sektor=SECTOR_IND | SDG_0831_SEX_ECO_RT |
| sektor=SECTOR_NAG | SDG_0831_SEX_ECO_RT |
| sektor=SECTOR_SER | SDG_0831_SEX_ECO_RT |
| total | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB, var1172, var2153 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1172 | rupiah_per_jam | 8.5.1 | pekerja (buruh/karyawan); nominal; Sakernas; 2015–2019 angka revisi karena perubahan penimbang (var.note) | var.unit: 'Rupiah/Jam' |
| var2153 | persen | 8.3.1 | Sakernas; 2018–2025; semua sektor (tidak disebut tanpa pertanian) | judul 'Proporsi'; var.unit kosong; nilai 20–90 |
| SDG_0851_SEX_OCU_NB | rupiah_per_jam | 8.5.1 | pekerja; nominal; rincian jenis kelamin x jabatan (ISCO-08, ISCO-88, tingkat keahlian); OBS_STATUS B = patahan | UNIT_MEASURE LC (mata uang lokal); NOTE_INDICATOR 'IDR: Indonesian rupiah'; judul DSD 'hourly earnings' |
| SDG_0831_SEX_ECO_RT | persen | 8.3.1 | semua sektor termasuk pertanian (rincian SECTOR_AGR dan SECTOR_NAG); rincian jenis kelamin x sektor (dua klasifikasi) | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1172 | 1100 | 2015 | total | 11,226.00 | bps/2026-10-17/json/sdg8_upah.json | e5c31b36f2856989022c3e3865d88de07454b0bf7f4192891b56b1111934f8ec |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg8_upah.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `e5c31b36f285…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (722 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1172, var2153 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1172, var2153 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 60 | 29.57 – 42354 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, rupiah_per_jam | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 639 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 722 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 60 | bps/2026-10-17/json/sdg8_informal.json, bps/2026-10-17/json/sdg8_upah.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 60 | 2885bba78ad1680f6b69b016af6a7f572b7052ece051b378367f79be59000538, e5c31b36f2856989022c3e3865d88de07454b0bf7f4192891b56b1111934f8ec | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1172 | rupiah_per_jam |
| var2153 | persen |

## data/gold/nasional.parquet (40 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB, var1172, var2153 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, ilostat | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 2007, 2008, 2009, 2010, 2012, 2013, … (18 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 55.88 – 20030.4 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, rupiah_per_jam | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 40 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 40 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 40 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_informal.json, bps/2026-10-17/json/sdg8_upah.json, ilostat/2026-10-20/data/DF_SDG_0831_SEX_ECO_RT.csv, ilostat/2026-10-20/data/DF_SDG_0851_SEX_OCU_NB.csv | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 2885bba78ad1680f6b69b016af6a7f572b7052ece051b378367f79be59000538, 61c59b5214390beb353baf69c2cffffce148357e84863f82352162fa8926b4f2, 8de35e0462037775b72e7ac41bc7e4e59c129a8c59026531effcf4e46f8b1007, e5c31b36f2856989022c3e3865d88de07454b0bf7f4192891b56b1111934f8ec | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (19 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1172, var2153 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | SDG_0831_SEX_ECO_RT, SDG_0851_SEX_OCU_NB | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 55.88 – 20030.4 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 7 | 80.158 – 16734.7 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen, rupiah_per_jam | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 7 | -25.282 – 2710.04 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 7 | -30.7335 – 16.6087 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda), metode (pengolahan Sakernas; nominal keduanya, rupiah per jam) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 19 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1172 | 1100 | 2015 | 11,226.00 | bps/2026-10-17/json/sdg8_upah.json |

1. Sel ini berasal dari baris Silver `var1172` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-17/json/sdg8_upah.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
