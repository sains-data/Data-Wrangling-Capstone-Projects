# Data dictionary — Kasus 20 Hutan, lahan, dan lingkungan

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (4,045 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | AG.LND.FRST.K2, AG.LND.FRST.ZS, EN.ATM.PM25.MC.M3, tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen, var1304, … (8 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1990, 1991, 1992, 1993, 1994, 1995, … (36 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | kawasan=apl, kawasan=kawasan_hutan, kekritisan=kritis, kekritisan=sangat_kritis, komponen=ika, komponen=ikal, … (13 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.3 – 3.01968e+07 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | hektar, indeks, km2, mikrogram_per_m3, persen, ribu_hektar | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 11.6.2, 15, 15.1.1, 15.3.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 4045 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 4045 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 4045 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg15_iklh.json, bps/2026-10-17/json/sdg15_lahan_kritis.json, bps/2026-10-17/json/sdg15_tutupan_hutan.json, bps/2026-10-17/json/sdg15_tutupan_kawasan.json, wdi/2026-10-20/data/kelompok-01-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0caaa3885b61b989d8d054a87a340fe01ec06482588eebd99b43ae64229fd8fa, 531e280713fc414a25dcd20e5ae00ba95056e7b4bc83d4c9c87bea2441414090, 8d2fae3a96415bd41299bf08abfc356d33448bdd6b66ff2f492aca4eb0e63226, b0730aae437965729da7d468b5d54282e7a3f6df4d078e68947948ecb259c28f, b9b586cc1472a9be4344352cde702f6894188a1881d21d9d78b2d525daf30ada | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `kawasan`: `apl`, `kawasan_hutan`
- `kekritisan`: `kritis`, `sangat_kritis`
- `komponen`: `ika`, `ikal`, `ikeg`, `ikl`, `iktl`, `iku`
- `tutupan`: `hutan`, `non_hutan`
- `kawasan` (var1304, dari turvar BPS): `kawasan_hutan` = Kawasan Hutan, `apl` = Di Luar Kawasan Hutan/Areal Penggunaan Lain (APL)
- `kekritisan` (var588, dari turvar BPS): `kritis` = Kritis, `sangat_kritis` = Sangat Kritis
- `komponen` (var2532, dari turvar BPS): `ika` = Indeks Kualitas Air, `ikal` = Indeks Kualitas Air Laut (IKAL), `ikeg` = Indeks Kualitas Ekosistem Gambut (IKEG), `ikl` = Indeks Kualitas Lahan (IKL), `iktl` = Indeks Kualitas Tutupan Lahan (IKTL), `iku` = Indeks Kualitas Udara

| rincian | dipakai_seri |
|---|---|
| kawasan=apl | var1304 |
| kawasan=kawasan_hutan | var1304 |
| kekritisan=kritis | var588 |
| kekritisan=sangat_kritis | var588 |
| komponen=ika | var2532 |
| komponen=ikal | var2532 |
| komponen=ikeg | var2532 |
| komponen=ikl | var2532 |
| komponen=iktl | var2532 |
| komponen=iku | var2532 |
| total | AG.LND.FRST.K2, AG.LND.FRST.ZS, EN.ATM.PM25.MC.M3, tabel:sdg15_tutupan_hutan:luas_ribu_ha, var1304, var588 |
| tutupan=hutan | tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen |
| tutupan=non_hutan | tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | ribu_hektar | 15.1.1 | tabel statis (HTML) rekalkulasi penutupan lahan 2014–2023; Kalimantan Timur = gabungan dengan Kalimantan Utara (keterangan tabel); rincian hutan, non hutan, jumlah | judul tabel '(Ribu Ha)'; header 'Luas Penutupan Lahan (Ribu Ha)' |
| tabel:sdg15_tutupan_hutan:persen | persen | 15.1.1 | tabel statis (HTML) rekalkulasi penutupan lahan 2014–2023; Kalimantan Timur = gabungan dengan Kalimantan Utara (keterangan tabel); rincian hutan, non hutan | header '%' |
| var1304 | ribu_hektar | 15.1.1 | rekalkulasi penutupan lahan KLHK 2014–2018, 2023; rincian kawasan hutan, APL, jumlah | var.unit: 'Ribu Hektar' |
| var588 | hektar | 15.3.1 | review lahan kritis tiap ±5 tahun (var.note): 2006, 2011, 2013, 2018; rincian kritis, sangat kritis, jumlah | var.unit: 'Hektar' |
| var2532 | indeks | 15 | enam komponen di turvar; air laut dan gambut hanya provinsi yang punya; KLHK 2019–2024 | judul 'Indeks'; nilai 0–100 |
| AG.LND.FRST.K2 | km2 | 15.1.1 | FAO; pohon >= 5 m; tidak termasuk perkebunan (sourceNote) | name: '(sq. km)' |
| AG.LND.FRST.ZS | persen | 15.1.1 | penyebut luas daratan | name: '(% of land area)' |
| EN.ATM.PM25.MC.M3 | mikrogram_per_m3 | 11.6.2 | paparan rata-rata tertimbang penduduk; GBD | name: '(micrograms per cubic meter)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | tabel:sdg15_tutupan_hutan:luas_ribu_ha | 1100 | 2014 | total | 5,647.30 | bps/2026-10-17/json/sdg15_tutupan_hutan.json | b0730aae437965729da7d468b5d54282e7a3f6df4d078e68947948ecb259c28f |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg15_tutupan_hutan.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `b0730aae4379…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,824 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen [tutupan=hutan], var1304, var2532 [komponen=ika], var2532 [komponen=iktl], var2532 [komponen=iku], … (7 nilai) | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen, var1304, var2532, var588 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | komponen=ika, komponen=iktl, komponen=iku, total, tutupan=hutan | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2006, 2011, 2013, 2014, 2015, 2016, … (14 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 183 | 0.5 – 5.1447e+06 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | hektar, indeks, persen, ribu_hektar | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 1511 | outlier, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1824 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 183 | bps/2026-10-17/json/sdg15_iklh.json, bps/2026-10-17/json/sdg15_lahan_kritis.json, bps/2026-10-17/json/sdg15_tutupan_hutan.json, bps/2026-10-17/json/sdg15_tutupan_kawasan.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 183 | 0caaa3885b61b989d8d054a87a340fe01ec06482588eebd99b43ae64229fd8fa, 531e280713fc414a25dcd20e5ae00ba95056e7b4bc83d4c9c87bea2441414090, b0730aae437965729da7d468b5d54282e7a3f6df4d078e68947948ecb259c28f, b9b586cc1472a9be4344352cde702f6894188a1881d21d9d78b2d525daf30ada | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | ribu_hektar |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | persen |
| var1304 | ribu_hektar |
| var2532 [komponen=ika] | indeks |
| var2532 [komponen=iktl] | indeks |
| var2532 [komponen=iku] | indeks |
| var588 | hektar |

## data/gold/nasional.parquet (151 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | AG.LND.FRST.K2, AG.LND.FRST.ZS, EN.ATM.PM25.MC.M3, tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen, var1304, … (8 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | komponen=iku, total, tutupan=hutan | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1990, 1991, 1992, 1993, 1994, 1995, … (36 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 17.8028 – 3.01968e+07 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | hektar, indeks, km2, mikrogram_per_m3, persen, ribu_hektar | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 151 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 151 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 151 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg15_iklh.json, bps/2026-10-17/json/sdg15_lahan_kritis.json, bps/2026-10-17/json/sdg15_tutupan_hutan.json, bps/2026-10-17/json/sdg15_tutupan_kawasan.json, wdi/2026-10-20/data/kelompok-01-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0caaa3885b61b989d8d054a87a340fe01ec06482588eebd99b43ae64229fd8fa, 531e280713fc414a25dcd20e5ae00ba95056e7b4bc83d4c9c87bea2441414090, 8d2fae3a96415bd41299bf08abfc356d33448bdd6b66ff2f492aca4eb0e63226, b0730aae437965729da7d468b5d54282e7a3f6df4d078e68947948ecb259c28f, b9b586cc1472a9be4344352cde702f6894188a1881d21d9d78b2d525daf30ada | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (36 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3, P4 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | tabel:sdg15_tutupan_hutan:luas_ribu_ha, tabel:sdg15_tutupan_hutan:persen, var1304, var2532 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | komponen=iku, total, tutupan=hutan | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | AG.LND.FRST.K2, AG.LND.FRST.ZS, EN.ATM.PM25.MC.M3, tabel:sdg15_tutupan_hutan:luas_ribu_ha | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2014, 2015, 2016, 2017, 2018, 2019, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 4 | 49.8 – 187939 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 1 | 18.8647 – 187939 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | indeks, persen, ribu_hektar | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 10 | -1822.1 – 483.04 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 10 | -1.938 – 1.22641 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan, tidak berselisih | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | arah berlawanan: indeks tinggi = baik, PM2.5 tinggi = buruk, definisi (penyebut: luas penutupan lahan vs luas daratan), definisi (tutupan lahan berhutan KLHK vs definisi FAO) setelah satuan diseragamkan (1 ribu ha = 10 km2), sumber sama (rekalkulasi KLHK); jumlah luas seharusnya sama | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 21 | pasangan konteks: selisih tidak dihitung, pembanding dikali 0.1 (km2 → ribu_hektar) | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 1100 | 2014 | 5,647.30 | bps/2026-10-17/json/sdg15_tutupan_hutan.json |

1. Sel ini berasal dari baris Silver `tabel:sdg15_tutupan_hutan:luas_ribu_ha` × 1100 × 2014 × rincian `total` × berkas `bps/2026-10-17/json/sdg15_tutupan_hutan.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
