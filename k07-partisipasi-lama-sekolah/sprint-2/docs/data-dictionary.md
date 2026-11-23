# Data dictionary — Kasus 07 Partisipasi dan lama sekolah

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (4,216 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SE.TER.ENRR, var1429, var1443, var2685, var303, var417 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1970, 1972, 1973, 1974, 1975, 1976, … (55 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenjang=sd, jenjang=sm, jenjang=smp, total, umur=15-24, umur=15-64, … (8 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.35 – 121.31 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk, tahun | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 4.1, 4.3.1, — | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 4216 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 4216 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 4216 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_3_1_v2685.json, bps/2026-10-17/json/sdg4_apk.json, bps/2026-10-17/json/sdg4_apk_pt.json, bps/2026-10-17/json/sdg4_hls.json, bps/2026-10-17/json/sdg4_rls.json, wdi/2026-10-20/data/kelompok-05-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 15b9d56e3e2b30cd190900fe758e7a97548e030cf425d618afd37bbc64d726a8, 2bd4a4dc8b92d7b9e10dd187596ee1345218a155a76d2ed51dec09af507cc33f, 3b8245e001bc3614dbddb323e92588c0fcef41e3c7b39838419d817548347c2a, 6e14806cf21835715abbc50745253bfbed82e88ba5fc41f202a2a8150103c47e, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e, bc081b82fe1fa9326027434b5e883f1ef14d4c30efab6a34b87e379b2f642689 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenjang`: `sd`, `sm`, `smp`
- `umur`: `15-24`, `15-64`, `25-54`, `55-64`
- `jenjang` (var303, dari turvar BPS): `sd` = SD/sederajat, `smp` = SMP/sederajat, `sm` = SM/sederajat
- `umur` (var2685, dari turvar BPS): `15-24` = Usia 15-24 tahun, `15-64` = Usia 15-64 tahun, `25-54` = Usia 25-54 tahun, `55-64` = Usia 55-64 tahun

| rincian | dipakai_seri |
|---|---|
| jenjang=sd | var303 |
| jenjang=sm | var303 |
| jenjang=smp | var303 |
| total | SE.TER.ENRR, var1429, var1443, var417 |
| umur=15-24 | var2685 |
| umur=15-64 | var2685 |
| umur=25-54 | var2685 |
| umur=55-64 | var2685 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var303 | persen_apk | 4.1 | Susenas; 2003–2025; mulai 2007 termasuk paket A/B/C (var.note) | judul 'Angka Partisipasi Kasar'; var.unit kosong; nilai di atas 100 ada (APK menghitung siswa semua umur) |
| var1443 | persen_apk | 4.3.1 | kelompok umur acuan 19–23 tahun (var.note); Susenas; 2015–2025 | judul 'Angka Partisipasi Kasar'; var.unit kosong |
| var2685 | persen | 4.3.1 | empat kelompok umur yang tumpang tindih (15–64 mencakup yang lain); 2022–2024 | var.unit: 'Persen' |
| var417 | tahun | — | anak umur 7 tahun; 2010–2025; berkas juga memuat kabupaten/kota (dikeluarkan) | var.unit: 'Tahun' |
| var1429 | tahun | — | penduduk 15+; Susenas; 2015–2025 | judul 'Rata-Rata Lama Sekolah'; var.unit kosong; nilai 6–12 |
| SE.TER.ENRR | persen_apk | 4.3.1 | UNESCO UIS; kelompok umur resmi jenjang tersier (umur tidak disebut di sourceNote) | name: '(% gross)'; sourceNote: rasio kasar, bisa > 100 |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1429 | 1100 | 2015 | total | 9.32 | bps/2026-10-17/json/sdg4_rls.json | bc081b82fe1fa9326027434b5e883f1ef14d4c30efab6a34b87e379b2f642689 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg4_rls.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `bc081b82fe1f…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (4,180 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1429, var1443, var2685 [umur=15-64], var303 [jenjang=sd], var303 [jenjang=sm], var303 [jenjang=smp], … (7 nilai) | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1429, var1443, var2685, var303, var417 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | jenjang=sd, jenjang=sm, jenjang=smp, total, umur=15-64 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2003, 2004, 2005, 2006, 2007, 2008, … (23 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 454 | 4.76 – 121.31 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk, tahun | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 3813 | outlier, patahan_seri, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 4180 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 454 | bps/2026-10-17/json/sdg4_4_3_1_v2685.json, bps/2026-10-17/json/sdg4_apk.json, bps/2026-10-17/json/sdg4_apk_pt.json, bps/2026-10-17/json/sdg4_hls.json, bps/2026-10-17/json/sdg4_rls.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 454 | 15b9d56e3e2b30cd190900fe758e7a97548e030cf425d618afd37bbc64d726a8, 2bd4a4dc8b92d7b9e10dd187596ee1345218a155a76d2ed51dec09af507cc33f, 3b8245e001bc3614dbddb323e92588c0fcef41e3c7b39838419d817548347c2a, 6e14806cf21835715abbc50745253bfbed82e88ba5fc41f202a2a8150103c47e, bc081b82fe1fa9326027434b5e883f1ef14d4c30efab6a34b87e379b2f642689 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1429 | tahun |
| var1443 | persen_apk |
| var2685 [umur=15-64] | persen |
| var303 [jenjang=sd] | persen_apk |
| var303 [jenjang=sm] | persen_apk |
| var303 [jenjang=smp] | persen_apk |
| var417 | tahun |

## data/gold/nasional.parquet (91 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | SE.TER.ENRR, var1429, var1443, var417 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1970, 1972, 1973, 1974, 1975, 1976, … (55 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 2.29891 – 44.8813 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen_apk, tahun | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 91 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 91 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 91 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_apk_pt.json, bps/2026-10-17/json/sdg4_hls.json, bps/2026-10-17/json/sdg4_rls.json, wdi/2026-10-20/data/kelompok-05-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 3b8245e001bc3614dbddb323e92588c0fcef41e3c7b39838419d817548347c2a, 6e14806cf21835715abbc50745253bfbed82e88ba5fc41f202a2a8150103c47e, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e, bc081b82fe1fa9326027434b5e883f1ef14d4c30efab6a34b87e379b2f642689 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (27 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | var1443, var417 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | SE.TER.ENRR, var1429 | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2010, 2011, 2012, 2013, 2014, 2015, … (16 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 11.29 – 32.89 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 7 | 8.32 – 44.8813 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen_apk, tahun | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 18 | -13.4313 – -5.95949 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 18 | -29.9263 – -16.4857 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (kelompok umur acuan penyebut) dan metode (Susenas vs data administrasi UNESCO), dua ukuran berbeda (harapan anak 7 tahun vs rata-rata penduduk 15+); variabel penjelas panel | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 16 | pasangan konteks: selisih tidak dihitung | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1429 | 1100 | 2015 | 9.32 | bps/2026-10-17/json/sdg4_rls.json |

1. Sel ini berasal dari baris Silver `var1429` × 1100 × 2015 × rincian `total` × berkas `bps/2026-10-17/json/sdg4_rls.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
