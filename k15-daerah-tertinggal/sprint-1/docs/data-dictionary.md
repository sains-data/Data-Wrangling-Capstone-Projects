# Data dictionary — Kasus 15 Kemiskinan dan daerah tertinggal

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (3,897 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SI.POV.NAHC, var192, var2190, var2191 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1996, 1999, 2000, 2001, 2002, 2003, … (56 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | semester, tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | daerah=RURAL, daerah=URBAN, status_desa=sangat_tertinggal, status_desa=tertinggal, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 19152 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | desa, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 1.2.1, 10.1.1(c), 10.1.1(d) | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 3897 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 3897 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 3897 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg10_10_1_1_c_v2191.json, bps/2026-10-20/json/sdg10_10_1_1_d_v2190.json, bps/2026-10-20/json/sdg10_10_1_1_f_v192.json, wdi/2026-10-20/data/kelompok-06-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 02fe55d612d4e1ea058d3e33caa250cc2e9dd400f7ffc52d41000f3cd4b8bcdf, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, 88b48cc13a4046cd4cc2a027e923dfe95fa31fe13a34b5c69d552b4592cd8a70, 8d3c028b5e6b246865af1c635fd4e835e5cd12aca7a9387fc2b53e2270771fc4 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `status_desa`: `sangat_tertinggal`, `tertinggal`
- `daerah` (var192, dari turvar BPS): `URBAN` = Perkotaan, `RURAL` = Perdesaan
- `status_desa` (var2191, dari turvar BPS): `sangat_tertinggal` = Desa Sangat Tertinggal, `tertinggal` = Desa Tertinggal

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | var192 |
| daerah=URBAN | var192 |
| status_desa=sangat_tertinggal | var2191 |
| status_desa=tertinggal | var2191 |
| total | SI.POV.NAHC, var192, var2190, var2191 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var192 | persen | 1.2.1 | 2007–2011 tahunan; 2012 ke atas Semester 1 (Maret) dan Semester 2 (September); 2023 hanya Maret; Kalimantan Utara 2013–2014 dan Papua sebelum 2024 berbatas lama (var.note) | var.unit: 'Persen' |
| var2190 | desa | 10.1.1(d) | Indeks Desa (Podes) mulai 2019; 2018 memakai Indeks Pembangunan Desa yang tidak sebanding (var.note); 34 provinsi, tanpa baris Indonesia | var.unit: 'Desa' |
| var2191 | desa | 10.1.1(c) | Indeks Desa (Podes) mulai 2019; 2018 memakai Indeks Pembangunan Desa yang tidak sebanding (var.note); 34 provinsi, tanpa baris Indonesia; rincian sangat tertinggal, tertinggal, jumlah | var.unit: 'Desa' |
| SI.POV.NAHC | persen | 1.2.1 | angka tahunan = P0 BPS Maret dibulatkan satu desimal (dicek di data) | name: '(% of population)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var192 | 1100 | 2007 | daerah=RURAL | 29.87 | bps/2026-10-20/json/sdg10_10_1_1_f_v192.json | 8d3c028b5e6b246865af1c635fd4e835e5cd12aca7a9387fc2b53e2270771fc4 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg10_10_1_1_f_v192.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `8d3c028b5e6b…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
