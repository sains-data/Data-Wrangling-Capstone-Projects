# Data dictionary — Kasus 09 Keterampilan TIK dan PAUD

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,653 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | IT.NET.USER.ZS, SE.PRE.ENRR, var1221, var1439, var1447, var1451 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1970, 1971, 1972, 1973, 1974, 1975, … (56 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 99.54 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen, persen_apk | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 17.8.1, 4.2.2, 4.4.1(a), 4.4.1(b), 5.b.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1653 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1653 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1653 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg4_4_4_1_a_v1451.json, bps/2026-10-17/json/sdg4_4_4_1_b_v1447.json, bps/2026-10-17/json/sdg4_apk_paud.json, bps/2026-10-20/json/sdg5_5_b_1_v1221.json, wdi/2026-10-20/data/kelompok-02-hal-01.json, wdi/2026-10-20/data/kelompok-03-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0d660fabf0dd9f55bfa085f1389319add00e95460df49c478a0392fc7860805a, 30875615b1ea72a6037ab7fd6ff15f2c94d0ccc045c16bad45e4e0f747696cf6, 7b649c5de4bbceb93fa223984c3cdf47bd48a58155c17f7f7125115cdc6500c3, d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34, ef1cc76ad2b3cfdcfb262b3522c36dde363de4aa30eb806539682d56246f6b44, fbe8cf28d6155e4a441897df1a03ecc3ef5f16768b88af01127d83434a07024b | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- (tidak ada dimensi)

| rincian | dipakai_seri |
|---|---|
| total | IT.NET.USER.ZS, SE.PRE.ENRR, var1221, var1439, var1447, var1451 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1451 | persen | 4.4.1(a) | umur 15–24; Susenas KOR; 2015–2025 | var.unit: 'Persen' |
| var1447 | persen | 4.4.1(b) | umur 15–59; 2015–2025 | var.unit: 'Persen' |
| var1439 | persen_apk | 4.2.2 | anak 3–6 tahun (var.note); Susenas; Papua Pegunungan 2024–2025 RSE 25–50% | judul 'Angka Partisipasi Kasar'; var.unit kosong; APK bisa > 100 |
| var1221 | persen | 5.b.1 | individu umur 5 tahun ke atas (var.note); Susenas KOR; ada di snapshot 17 dan 20 Oktober | var.unit: 'Persen' |
| SE.PRE.ENRR | persen_apk | 4.2.2 | UNESCO; kelompok umur resmi prasekolah; 1970–2018 | name: '(% gross)' |
| IT.NET.USER.ZS | persen | 17.8.1 | ITU; memakai internet dalam 3 bulan terakhir | name: '(% of population)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1221 | 1100 | 2015 | total | 51.50 | bps/2026-10-20/json/sdg5_5_b_1_v1221.json | d8597519b86a12d5955b0339db523e03ad125c89e7b393b05060bb691df84e34 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg5_5_b_1_v1221.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `d8597519b86a…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
