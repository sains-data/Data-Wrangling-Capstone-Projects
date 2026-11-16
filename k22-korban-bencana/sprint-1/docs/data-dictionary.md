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
