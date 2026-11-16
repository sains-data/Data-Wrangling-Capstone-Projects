# Data dictionary — Kasus 06 Melek aksara

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (5,762 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci, var1458 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1980, 1990, 2004, 2006, 2008, 2009, … (22 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | daerah=RURAL, daerah=RURAL;jenis_kelamin=FEMALE, daerah=RURAL;jenis_kelamin=MALE, daerah=URBAN, daerah=URBAN;jenis_kelamin=FEMALE, daerah=URBAN;jenis_kelamin=MALE, … (9 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 43.12 – 99.98 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 4.6.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 5762 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 5762 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 5762 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_amh.json, bps/2026-10-17/json/sdg4_amh_rinci.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 6a81eaf2622acf1a3ac1c188a34716d0d5490e2851383b96cca8ee4f2a490102, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `jenis_kelamin`: `FEMALE`, `MALE`

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | tabel:sdg4_amh_rinci |
| daerah=RURAL;jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| daerah=RURAL;jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| daerah=URBAN | tabel:sdg4_amh_rinci |
| daerah=URBAN;jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| daerah=URBAN;jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| jenis_kelamin=FEMALE | tabel:sdg4_amh_rinci |
| jenis_kelamin=MALE | tabel:sdg4_amh_rinci |
| total | SE.ADT.LITR.ZS, tabel:sdg4_amh_rinci, var1458 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1458 | persen | 4.6.1 | penduduk 15+; Susenas; 2014–2025; tabel ringkas tanpa rincian | var.unit: 'Persen' |
| tabel:sdg4_amh_rinci | persen | 4.6.1 | penduduk 15+; tabel statis (HTML) 2009–2025; rincian perkotaan/perdesaan x laki-laki/perempuan | judul tabel statis (angka melek aksara, persen) |
| SE.ADT.LITR.ZS | persen | 4.6.1 | penduduk 15+; UNESCO UIS; 13 tahun tidak berurutan 1980–2020 | name: '(% of people ages 15 and above)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | tabel:sdg4_amh_rinci | 1100 | 2009 | daerah=RURAL | 95.33 | bps/2026-10-17/json/sdg4_amh_rinci.json | 90eedd9a42664ebb4f4d86ca50c8588d32dd7a3e93f1a22db29a7447d74d4cc7 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg4_amh_rinci.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `90eedd9a4266…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
