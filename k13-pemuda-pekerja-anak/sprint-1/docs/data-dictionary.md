# Data dictionary — Kasus 13 Pemuda dan pekerja anak

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (720 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0861_SEX_RT, SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT, SL.TLF.0714.ZS, SL.UEM.NEET.ZS, var1186, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1996, 1997, 1998, 1999, 2000, 2001, … (30 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_kelamin=FEMALE, jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17, jenis_kelamin=MALE, jenis_kelamin=MALE;umur=CLDVERSION_Y15-17, total, umur=CLDVERSION_Y15-17 | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0.38 – 41.23 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 8.6.1, 8.7.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 720 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 720 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 720 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 711 | B | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg8_8_7_1_v2658.json, bps/2026-10-17/json/sdg8_neet.json, ilostat/2026-10-20/data/DF_SDG_0861_SEX_RT.csv, ilostat/2026-10-20/data/DF_SDG_A871_SEX_AGE_RT.csv, ilostat/2026-10-20/data/DF_SDG_B871_SEX_AGE_RT.csv, wdi/2026-10-20/data/kelompok-06-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 41b13e4b1df67909c8d41e1527a585fa576ff107c1e5d7f87d8b109203e5e5ac, 51ab5e7080ffe32ce20a0914bf7002e5d5c5523366fd72c207a5ce4732e8fc75, 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, cc4fc24190b0dbc8610ff3db8ef1db700180ccac03833ab5093d300fdec7e443, d1fc787eb33130a2ab8ef479ca46a5b3704cc8e5e13b0edb03b756406bfe9c2b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `umur`: `CLDVERSION_Y15-17`

| rincian | dipakai_seri |
|---|---|
| jenis_kelamin=FEMALE | SDG_0861_SEX_RT |
| jenis_kelamin=FEMALE;umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |
| jenis_kelamin=MALE | SDG_0861_SEX_RT |
| jenis_kelamin=MALE;umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |
| total | SDG_0861_SEX_RT, SL.TLF.0714.ZS, SL.UEM.NEET.ZS, var1186, var2658 |
| umur=CLDVERSION_Y15-17 | SDG_A871_SEX_AGE_RT, SDG_B871_SEX_AGE_RT |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1186 | persen | 8.6.1 | umur 15–24; Sakernas; 2015–2025 | var.unit: 'Persen' |
| var2658 | persen | 8.7.1 | umur 5–17; 2020–2025; DKI dan DIY tidak ada 2024–2025 | var.unit: 'Persen' (judul menyebut 'Persentase dan Jumlah', berkas hanya persentase) |
| SL.UEM.NEET.ZS | persen | 8.6.1 | ILO Labour Force Statistics; kelompok umur pemuda | name: '(% of youth population)' |
| SL.TLF.0714.ZS | persen | 8.7.1 | umur 7–14; bekerja minimal satu jam seminggu; 2000–2010 | name: '(% of children ages 7-14)' |
| SDG_0861_SEX_RT | persen | 8.6.1 | umur 15–24; rincian jenis kelamin; OBS_STATUS B = patahan | UNIT_MEASURE PT |
| SDG_A871_SEX_AGE_RT | persen | 8.7.1 | kegiatan ekonomi saja; berkas hanya umur 15–17 (AGE_CLDVERSION_Y15-17); 2009 (survei pekerja anak), 2019, 2023 (Sakernas) | UNIT_MEASURE PT |
| SDG_B871_SEX_AGE_RT | persen | 8.7.1 | kegiatan ekonomi dan pekerjaan rumah tangga; hanya umur 15–17 dan 2009 | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1186 | 1100 | 2015 | total | 25.65 | bps/2026-10-17/json/sdg8_neet.json | 6af01a80b8cbdeb54b76f056632708724ffd93cdb1c307513101d851fe63a97f |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg8_neet.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `6af01a80b8cb…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
