# Data dictionary — Kasus 05 Layanan dan tenaga kesehatan

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,722 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | FINPROTECTION_CATA_TOT_10_POP, HWF_0001, HWF_0006, UHC_INDEX_REPORTED, var1402, var1477, … (7 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1992, 1993, 1999, 2000, 2001, 2002, … (29 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | daerah=RURAL, daerah=RURAL;komposisi_rt=HH_COMP_ADULTS_WITH_KIDS, daerah=URBAN, jenis_kelamin=FEMALE;jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD, jenis_kelamin=MALE;jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD, jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD;umur=AGE60+, … (24 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 377 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | indeks, per_100000_penduduk, per_10000_penduduk, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 3.8.1, 3.8.1(a), 3.8.2, 3.8.2(a), 3.c.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1722 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1722 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1722 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_8_1_a_v1402.json, bps/2026-10-20/json/sdg3_3_8_2_a_v2279.json, bps/2026-10-20/json/sdg3_3_c_1_v1477.json, who_gho/2026-10-20/datadot/217795A_HWF_0001.csv, who_gho/2026-10-20/datadot/5C8435F_HWF_0006.csv, who_gho/2026-10-20/datadot/9A706FD_UHC_INDEX_REPORTED.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0512abf0307bd83a559276cc7e068b28b49ba69e0068630a500b47b2436cddd1, 11f300d467f595a6b5e2250a84ff31452b4036828ac8e47f3e1b4bfe0cb7883f, 28ffd7f28e35a54da609618ee3fd164c20cd39e248ab69aa2cda94c90e50b15d, 37486df9e57ea83efdadd057f9f6672252cc26e516e147ca5b5154e4884e7f7c, 4a255fcbe3f557505a8a1f8513d1dbe4c39628e8c6d542266aac95a5653537b2, 96c995afe4898d3f2892d747b1eb835b773a363cbe27ae23a371fff3a56c3c16, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `daerah`: `RURAL`, `URBAN`
- `jenis_kelamin`: `FEMALE`, `MALE`
- `jenis_penduduk`: kode sumber apa adanya
- `komposisi_rt`: kode sumber apa adanya
- `profesi`: `atlm`, `bidan`, `dokter_gigi`, `dokter_umum`, `farmasi`, `gizi`, `kesehatan_lingkungan`, `kesehatan_masyarakat`, `pekarya`, `perawat`
- `umur`: kode sumber apa adanya
- `profesi` (var1477, dari turvar BPS): `dokter_umum` = Dokter Umum, `dokter_gigi` = Dokter Gigi, `perawat` = Perawat, `bidan` = Bidan, `farmasi` = Farmasi, `kesehatan_masyarakat` = Kesehatan Masyarakat, `kesehatan_lingkungan` = Kesehatan Lingkungan, `gizi` = Gizi, `atlm` = Ahli Teknologi Laboratorium Medik, `pekarya` = Pekarya

| rincian | dipakai_seri |
|---|---|
| daerah=RURAL | FINPROTECTION_CATA_TOT_10_POP |
| daerah=RURAL;komposisi_rt=HH_COMP_ADULTS_WITH_KIDS | FINPROTECTION_CATA_TOT_10_POP |
| daerah=URBAN | FINPROTECTION_CATA_TOT_10_POP |
| jenis_kelamin=FEMALE;jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD | FINPROTECTION_CATA_TOT_10_POP |
| jenis_kelamin=MALE;jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD | FINPROTECTION_CATA_TOT_10_POP |
| jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD;umur=AGE60+ | FINPROTECTION_CATA_TOT_10_POP |
| jenis_penduduk=POP_TYPE_HOUSEHOLD_HEAD;umur=AGELT60 | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_ADULTS | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_ADULTS_WITH_KIDS | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_ADULTS_WITH_OLDER | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_MULTIGEN | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_MULTIGEN_WITH_OLDER | FINPROTECTION_CATA_TOT_10_POP |
| komposisi_rt=HH_COMP_ONLY_OLDER_ADULTS | FINPROTECTION_CATA_TOT_10_POP |
| profesi=atlm | var1477 |
| profesi=bidan | var1477 |
| profesi=dokter_gigi | var1477 |
| profesi=dokter_umum | var1477 |
| profesi=farmasi | var1477 |
| profesi=gizi | var1477 |
| profesi=kesehatan_lingkungan | var1477 |
| profesi=kesehatan_masyarakat | var1477 |
| profesi=pekarya | var1477 |
| profesi=perawat | var1477 |
| total | FINPROTECTION_CATA_TOT_10_POP, HWF_0001, HWF_0006, UHC_INDEX_REPORTED, var1402, var2279 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1402 | persen | 3.8.1(a) | penduduk yang punya keluhan kesehatan tetapi tidak berobat; Susenas; 2015–2025 | var.unit: 'Persen' |
| var2279 | persen | 3.8.2(a) | memiliki BPJS PBI, BPJS Non PBI, atau Jamkesda (var.note); Susenas Maret; seri baru terbit 2022 | var.unit: 'Persen' |
| var1477 | per_100000_penduduk | 3.c.1 | 10 profesi di turvar; SDM Kesehatan Kemenkes (var.note); 2016–2018; Indonesia hanya 2018 | var.note: '(per 100.000 penduduk)'; var.unit dan kolom satuan CSV kosong |
| HWF_0001 | per_10000_penduduk | 3.c.1 | dokter umum, spesialis, dan dokter tanpa rincian (DefinitionText) | kolom RATE_PER_10000_N; UnitOfMeasure |
| HWF_0006 | per_10000_penduduk | 3.c.1 | perawat dan bidan digabung; aktif atau terdaftar tergantung sumber (DefinitionText) | kolom RATE_PER_10000_N; UnitOfMeasure |
| UHC_INDEX_REPORTED | indeks | 3.8.1 | indeks 0–100, tahunan 2000–2023 | kolom INDEX_N; UnitOfMeasure: rata-rata skor 14 indikator penanda |
| FINPROTECTION_CATA_TOT_10_POP | persen | 3.8.2 | rincian komposisi rumah tangga, daerah, jenis kelamin dan umur kepala rumah tangga | kolom PERCENT_POP_N |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1402 | 1100 | 2015 | total | 3.09 | bps/2026-10-20/json/sdg3_3_8_1_a_v1402.json | 28ffd7f28e35a54da609618ee3fd164c20cd39e248ab69aa2cda94c90e50b15d |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg3_3_8_1_a_v1402.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `28ffd7f28e35…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
