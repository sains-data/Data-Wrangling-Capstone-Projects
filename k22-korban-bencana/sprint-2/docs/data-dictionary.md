# Data dictionary — Kasus 22 Korban bencana

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (14,193 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bnpb, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | EN.CLC.MDAT.ZS, jumlah_penduduk, kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, … (11 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2009, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_bencana=banjir, jenis_bencana=cuaca_ekstrem, jenis_bencana=erupsi_gunung_api, jenis_bencana=gelombang_pasang_dan_abrasi, jenis_bencana=gempabumi, jenis_bencana=kebakaran_hutan_dan_lahan, … (10 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 2.84439e+08 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | jiwa, kejadian, per_100000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 13.1.1\|1.5.1\|11.5.1, — | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 14193 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 14193 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 14193 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bnpb/2026-10-20/datastore/data-bencana-indonesia/21044ffd-c397-4b3c-acbd-5adaa03d79e3.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/318f541a-5b0d-448c-8b78-9ba56c0478f2.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/5dfcae7e-acb3-4548-82b5-61d876ea478a.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/69605ad2-73ea-4967-b2d5-639ad9291833.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/7f9e5218-bbba-4916-a2b8-13cf1764dc96.json, … (40 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 022de0979c40cfcafa7eb8c42c126a97d4e3c624d866234630e41c30bf5ebd05, 1925a9ac1fe60238f0b068f15e349331ab92b27dcc16984bf0678a4b964afbe9, 2240e000c822a242501c0b8650c8757c1df17ec081b2fb9b10a2ec9c87558519, 366808cdc3a85b45dc25d7e67220b8ae9b83b13d85962286601727ee65541e55, 382dfc323598fa2f36da91bfb2d05227a31b81abc86146067b2de754551d37e2, 4315e35e043ffd6a95099f2ec552406a2901b6df1476ae156a33d3951839dd3e, … (40 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_bencana`: `banjir`, `cuaca_ekstrem`, `erupsi_gunung_api`, `gelombang_pasang_dan_abrasi`, `gempabumi`, `kebakaran_hutan_dan_lahan`, `kekeringan`, `tanah_longsor`, `tsunami`
- `tingkat_kerusakan`: `berat`, `ringan`, `sedang`

| rincian | dipakai_seri |
|---|---|
| jenis_bencana=banjir | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=cuaca_ekstrem | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=erupsi_gunung_api | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=gelombang_pasang_dan_abrasi | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=gempabumi | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=kebakaran_hutan_dan_lahan | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=kekeringan | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=tanah_longsor | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak, korban_terdampak_mengungsi |
| jenis_bencana=tsunami | kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, korban_meninggal, korban_meninggal_hilang_per_100rb, korban_terdampak |
| total | EN.CLC.MDAT.ZS, jumlah_penduduk, kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_meninggal, korban_terdampak |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| kejadian | kejadian | — | satu kejadian satu jenis utama; kejadian lintas provinsi dihitung di setiap provinsi terdampak tetapi sekali secara nasional (Keterangan); ambang batas kejadian (Keterangan) | Keterangan: 'Jumlah Kejadian: Jumlah Total Kejadian Bencana Menurut Klasifikasi Penyajian' |
| korban_meninggal | jiwa | 13.1.1\|1.5.1\|11.5.1 | provinsi per jenis 2021, 2022, 2024, 2025; nasional 2010–2024 ada di katalog tetapi tidak di paket (resource b2fa5c46, judul resource di ckan/package_search-pusdatinkom-01.json) | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_hilang | jiwa | 13.1.1\|1.5.1\|11.5.1 | provinsi per jenis 2021, 2022, 2024, 2025; nasional per jenis 2010–2024 | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_luka_sakit | jiwa | 13.1.1\|1.5.1\|11.5.1 | provinsi per jenis 2021, 2022, 2024, 2025; nasional per jenis 2010–2024; judul 2025 'Korban Luka', kepala rekap 'Luka-Luka' | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_mengungsi | jiwa | 13.1.1\|1.5.1\|11.5.1 | provinsi per jenis 2024, 2025; nasional per jenis 2010–2024; tabel 2024 banyak sel kosong | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_terdampak | jiwa | 13.1.1\|1.5.1\|11.5.1 | provinsi per jenis 2024, 2025; nasional per jenis 2010–2024 | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_terdampak_mengungsi | jiwa | 13.1.1\|1.5.1\|11.5.1 | hanya rekap 2021/2022; kepala 'Terdampak - Mengungsi' tidak memisahkan keduanya, jadi tidak digabung dengan korban_terdampak atau korban_mengungsi | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) |
| korban_mengungsi_per_100rb | per_100000_penduduk | 13.1.1\|1.5.1\|11.5.1 | 2025; penyebut = kolom Jumlah Penduduk di berkas yang sama (Keterangan: publikasi BPS) | judul resource di ckan/package_search-pusdatinkom-01.json: 'Jumlah Korban Mengungsi per 100.000 Orang ...' |
| korban_meninggal_hilang_per_100rb | per_100000_penduduk | 13.1.1\|1.5.1\|11.5.1 | 2025; penyebut = kolom Jumlah Penduduk di berkas yang sama | judul resource di ckan/package_search-pusdatinkom-01.json: 'Jumlah Korban Meninggal dan Hilang per 100.000 Orang ...' |
| jumlah_penduduk | jiwa | — | 2025; muncul di dua berkas per 100.000 (nilai sama, lihat reports/bnpb-lintas-berkas.csv) | Keterangan: 'Jumlah Penduduk Berdasarkan Publikasi Badan Pusat Statistik' |
| EN.CLC.MDAT.ZS | persen | — | satu angka rata-rata 1990–2009 yang ditulis sebagai date 2009; hanya kekeringan, banjir, suhu ekstrem | name: '(% of population, average 1990-2009)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bnpb | jumlah_penduduk | 1100 | 2025 | total | 5,626,000.00 | bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/31a0d329-a363-4a16-852c-f4fa51f313bf-jumlah-korban-mengungsi-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx | 804d953ed748a1c85da940ae890233d1ee368c6eb05d5ddc90e4a23e25c89bcd |

1. `_berkas_raw` menunjuk `data/raw/bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/31a0d329-a363-4a16-852c-f4fa51f313bf-jumlah-korban-mengungsi-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `804d953ed748…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (3,382 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | jumlah_penduduk, kejadian [jumlah], korban_hilang [jumlah], korban_luka_sakit [jumlah], korban_mengungsi [jumlah], korban_mengungsi_per_100rb [jumlah], … (10 nilai) | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | jumlah_penduduk, kejadian, korban_hilang, korban_luka_sakit, korban_mengungsi, korban_mengungsi_per_100rb, … (10 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | jumlah, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2010, 2011, 2012, 2013, 2014, 2015, … (16 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 2008 | 0 – 5.0759e+07 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | jiwa, kejadian, per_100000_penduduk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | belum_ada, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 3263 | outlier, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 3382 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 2008 | bnpb/2026-10-20/datastore/data-bencana-indonesia/318f541a-5b0d-448c-8b78-9ba56c0478f2.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/5dfcae7e-acb3-4548-82b5-61d876ea478a.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/69605ad2-73ea-4967-b2d5-639ad9291833.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/b1e58b39-8dc4-4b9b-abc6-50139acd2fda.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/d1fd9f08-26e1-453a-9be0-422538f01b5e.json, … (16 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 2008 | 49075b3e1b18ec00a5238815ffcae6eb8497f658cc9dbab582032ccaec6db0b0, 4bd09547ab755f2d2c7396ca5cc7cd3f74c7e5e125e69377be154dae9a2a53ca, 5d6f131c857403cf28b2e8a5da84000017bd66dbc3a7bace8f1546370b990773, 619490fc3463e0c8810796a5abd50b6da41aa285cc3291cab17fa741454c31fd, 623019598556c7bb97f622059e364f7632fcaf64fdee59ca43427cb103b630f6, 6fd1cb7b58ff05003e312701ac73226838af58038ec9ad1cfea2f09c3c9b48c5, … (16 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| jumlah_penduduk | jiwa |
| kejadian [jumlah] | kejadian |
| korban_hilang [jumlah] | jiwa |
| korban_luka_sakit [jumlah] | jiwa |
| korban_mengungsi [jumlah] | jiwa |
| korban_mengungsi_per_100rb [jumlah] | per_100000_penduduk |
| korban_meninggal [jumlah] | jiwa |
| korban_meninggal_hilang_per_100rb [jumlah] | per_100000_penduduk |
| korban_terdampak [jumlah] | jiwa |
| korban_terdampak_mengungsi [jumlah] | jiwa |

## data/gold/nasional.parquet (78 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | EN.CLC.MDAT.ZS, jumlah_penduduk, kejadian, kejadian (agregat provinsi), korban_hilang, korban_luka_sakit, … (11 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | jenis_bencana=banjir, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bnpb, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 2009, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 0.16059 – 2.84439e+08 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | jiwa, kejadian, per_100000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 78 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 78 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 78 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | agregat, baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bnpb/2026-10-20/datastore/data-bencana-indonesia/318f541a-5b0d-448c-8b78-9ba56c0478f2.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/69605ad2-73ea-4967-b2d5-639ad9291833.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/7f9e5218-bbba-4916-a2b8-13cf1764dc96.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/9b41007e-c998-456b-8cbc-385b17986e46.json, bnpb/2026-10-20/datastore/data-bencana-indonesia/a19366cf-0ac4-45d1-bc6e-89a020ab45a1.json, … (14 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | object | 2 | 022de0979c40cfcafa7eb8c42c126a97d4e3c624d866234630e41c30bf5ebd05, 382dfc323598fa2f36da91bfb2d05227a31b81abc86146067b2de754551d37e2, 4bd09547ab755f2d2c7396ca5cc7cd3f74c7e5e125e69377be154dae9a2a53ca, 6fd1cb7b58ff05003e312701ac73226838af58038ec9ad1cfea2f09c3c9b48c5, 7af2d161a543bfa7c8c2143bb993040185a36f887122331c481571f286e7e2a2, 804d953ed748a1c85da940ae890233d1ee368c6eb05d5ddc90e4a23e25c89bcd, … (12 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (19 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2, P3, P4 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | EN.CLC.MDAT.ZS, kejadian, korban_mengungsi_per_100rb, korban_meninggal_hilang_per_100rb | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | jenis_bencana=banjir, total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | (korban_meninggal + korban_hilang) / jumlah_penduduk x 100.000, kejadian (agregat provinsi), korban_mengungsi / jumlah_penduduk x 100.000, korban_terdampak | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | hitung, jenis_bencana=banjir | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 2009, 2010, 2011, 2012, 2013, 2014, … (17 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 0 | 0.16059 – 2009 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 15 | 0.539659 – 2009 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | kejadian, per_100000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 15 | -8 – 0 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 15 | -0.560224 – 0 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan, tidak berselisih | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional, pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah, pembulatan; pembilang dari dua berkas terpisah, periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025 | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 15 | agregat provinsi (GOLD_AGREGAT), pembanding = hitungan ulang dari meninggal + hilang dan jumlah penduduk, pembanding = hitungan ulang dari pengungsi dan jumlah penduduk | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| jumlah_penduduk | 1100 | 2025 | 5,626,000.00 | bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/31a0d329-a363-4a16-852c-f4fa51f313bf-jumlah-korban-mengungsi-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx |

1. Sel ini berasal dari baris Silver `jumlah_penduduk` × 1100 × 2025 × rincian `total` × berkas `bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/31a0d329-a363-4a16-852c-f4fa51f313bf-jumlah-korban-mengungsi-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
