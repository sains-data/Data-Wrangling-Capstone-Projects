# Data dictionary — Kasus 21 Keamanan dan pencatatan sipil

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,370 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SP.REG.BRTH.ZS, VC.IHR.PSRC.P5, var1311, var1312, var1410, var1831, … (8 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1998, 1999, 2000, 2002, 2003, 2004, … (21 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 100 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_100000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 16.1.1, 16.1.3(a), 16.1.4, 16.2.1(a), 16.3.1(a), 16.9.1, … (7 nilai) | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1370 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1370 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1370 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json, bps/2026-10-20/json/sdg16_16_1_4_v1312.json, bps/2026-10-20/json/sdg16_16_2_1_a_v2738.json, bps/2026-10-20/json/sdg16_16_3_1_a_v2740.json, bps/2026-10-20/json/sdg16_16_9_1_b_v1831.json, bps/2026-10-20/json/sdg16_16_9_1_v1410.json, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 14f30e70d545fd8e5e5fac61d41fb0d220dcf493f3d64dedaa3aae05eb1297a6, 2729511103be3b96bc01f74f66f642310249f3ebccaf1177731a230c47e2f629, 65217f9aeb4550dd9742848fd5eac79e754f3950f40e9f385622c0f7f2bb8f75, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, a9770f81c98c9675c9fe219ee1facb7838fa4aafe214d6f6c2df44bb46b452a5, ce796563d5698b7aed791c6fbeb7e0f9610e8077c1bd8bd4fa55e3d2169337a1, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- (tidak ada dimensi)

| rincian | dipakai_seri |
|---|---|
| total | SP.REG.BRTH.ZS, VC.IHR.PSRC.P5, var1311, var1312, var1410, var1831, var2738, var2740 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1311 | persen | 16.1.3(a) | Susenas; periode = tahun rujukan kejadian (angka 2017 dari Susenas 2018, var.note); 2015–2024; banyak provinsi tidak ada sejak 2020 | var.unit: 'Persen' |
| var1312 | persen | 16.1.4 | Susenas Modul Hansos; 2014, 2017, 2020, 2025 | var.unit: 'Persen' |
| var2738 | persen | 16.2.1(a) | rumah tangga dengan anak 1–17; 2014 dan 2020 | var.unit: 'Persen' |
| var2740 | persen | 16.3.1(a) | korban kekerasan; 2020–2024; jumlah provinsi berubah setiap tahun | var.unit: 'Persen' |
| var1410 | persen | 16.9.1 | anak < 5 tahun; Susenas; 2015–2025 | var.unit: 'Persen' |
| var1831 | persen | 16.9.1(b) | anak 0–17 tahun; 2015–2023; var.note hanya mengulang judul | var.unit: 'Persen' |
| SP.REG.BRTH.ZS | persen | 16.9.1 | anak < 5 tahun dengan akta terlihat atau dilaporkan (survei rumah tangga, UNICEF) | name: '(%)' |
| VC.IHR.PSRC.P5 | per_100000_penduduk | 16.1.1 | UNODC; 6 tahun 1998–2022 | name: '(per 100,000 people)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1311 | 1100 | 2015 | total | 0.02 | bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json | ce796563d5698b7aed791c6fbeb7e0f9610e8077c1bd8bd4fa55e3d2169337a1 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `ce796563d569…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (1,558 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1311, var1312, var1410, var1831, var2738, var2740 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1311, var1312, var1410, var1831, var2738, var2740 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2014, 2015, 2016, 2017, 2018, 2019, … (12 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 243 | 0 – 100 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 1443 | outlier, patahan_seri, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 1558 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 243 | bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json, bps/2026-10-20/json/sdg16_16_1_4_v1312.json, bps/2026-10-20/json/sdg16_16_2_1_a_v2738.json, bps/2026-10-20/json/sdg16_16_3_1_a_v2740.json, bps/2026-10-20/json/sdg16_16_9_1_b_v1831.json, bps/2026-10-20/json/sdg16_16_9_1_v1410.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 243 | 14f30e70d545fd8e5e5fac61d41fb0d220dcf493f3d64dedaa3aae05eb1297a6, 2729511103be3b96bc01f74f66f642310249f3ebccaf1177731a230c47e2f629, 65217f9aeb4550dd9742848fd5eac79e754f3950f40e9f385622c0f7f2bb8f75, a9770f81c98c9675c9fe219ee1facb7838fa4aafe214d6f6c2df44bb46b452a5, ce796563d5698b7aed791c6fbeb7e0f9610e8077c1bd8bd4fa55e3d2169337a1, e6b8ba50715851c7b33c05af0a8625e73ea77a707c485796577b5d2b90d9f266 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1311 | persen |
| var1312 | persen |
| var1410 | persen |
| var1831 | persen |
| var2738 | persen |
| var2740 | persen |

## data/gold/nasional.parquet (55 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SP.REG.BRTH.ZS, VC.IHR.PSRC.P5, var1311, var1312, var1410, var1831, … (8 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1998, 1999, 2000, 2002, 2003, 2004, … (21 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 0.02 – 91.79 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_100000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 55 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 55 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 55 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json, bps/2026-10-20/json/sdg16_16_1_4_v1312.json, bps/2026-10-20/json/sdg16_16_2_1_a_v2738.json, bps/2026-10-20/json/sdg16_16_3_1_a_v2740.json, bps/2026-10-20/json/sdg16_16_9_1_b_v1831.json, bps/2026-10-20/json/sdg16_16_9_1_v1410.json, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 14f30e70d545fd8e5e5fac61d41fb0d220dcf493f3d64dedaa3aae05eb1297a6, 2729511103be3b96bc01f74f66f642310249f3ebccaf1177731a230c47e2f629, 65217f9aeb4550dd9742848fd5eac79e754f3950f40e9f385622c0f7f2bb8f75, 9a8729675761d697bd5556d66fd903ed841ee454e7324d41084dc09b9905f912, a9770f81c98c9675c9fe219ee1facb7838fa4aafe214d6f6c2df44bb46b452a5, ce796563d5698b7aed791c6fbeb7e0f9610e8077c1bd8bd4fa55e3d2169337a1, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (32 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1311, var1410 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | SP.REG.BRTH.ZS, VC.IHR.PSRC.P5, var1831 | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2015, 2016, 2017, 2018, 2019, 2020, … (11 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 0.02 – 86.76 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 18 | 0.303769 – 91.79 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 28 | -4.72 – 0.04 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 28 | -6.05905 – 0.0551724 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | cakupan berbeda, definisi berbeda, metode berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi), kelompok umur berbeda; tetap dua seri, metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun) | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 22 | pasangan konteks: selisih tidak dihitung | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1311 | 1100 | 2015 | 0.02 | bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json |

1. Sel ini berasal dari baris Silver `var1311` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
