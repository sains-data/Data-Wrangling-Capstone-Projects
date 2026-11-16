# Data dictionary — Kasus 16 Ketimpangan dan layanan dasar

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (1,137 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, ilostat, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | SDG_0111_SEX_AGE_RT, SDG_0131_SEX_SOC_RT, SDG_1041_NOC_RT, SI.DST.50MD, SI.POV.DDAY, var1254, … (8 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (35 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1984, 1987, 1990, 1993, 1996, 1998, … (34 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_kelamin=FEMALE, jenis_kelamin=FEMALE;perlindungan_sosial=CONTIG_MAT, jenis_kelamin=FEMALE;perlindungan_sosial=CONTIG_UNE, jenis_kelamin=FEMALE;umur=YTHADULT_Y15-24, jenis_kelamin=FEMALE;umur=YTHADULT_YGE25, jenis_kelamin=MALE, … (22 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 100 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 1.1.1, 1.3.1, 1.4.1, 10.2.1, 10.4.1, 17.1.1 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 1137 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 1137 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 1137 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| status_obs | string | 900 | A, M, R | OBS_STATUS CSV ILOSTAT | kode status pengamatan ILOSTAT apa adanya (B = patahan seri menurut NOTE_INDICATOR; arti kode lain tidak ada di paket, lihat reports/ilostat-status.csv); kosong untuk sumber lain |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg10_10_2_1_v2011.json, bps/2026-10-20/json/sdg17_17_1_1_v1254.json, bps/2026-10-20/json/sdg1_1_4_1_v2016.json, ilostat/2026-10-20/data/DF_SDG_0111_SEX_AGE_RT.csv, ilostat/2026-10-20/data/DF_SDG_0131_SEX_SOC_RT.csv, ilostat/2026-10-20/data/DF_SDG_1041_NOC_RT.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 090033aba4597bdb3f949a2abdffc129698b0d32a8d88e3cbf29be216f655f6c, 0bdc1b62f4a7ec0d96175254a4a4e0df7421b3ee89e0d08fd29a5b878d67c531, 458f8cab8eb810c52df5dccc9e61011140bc13309962d22abf1120bf7cf266cb, 6ce652c5f1a982a33d89b625211b9610d718da9afe6258012821f185ed24da9c, 71851285cf2e3d256a725a283af5b4c2966faf853f90c420c333e9550ed5c235, 91ba6f705812d6b0ba24f626094bb90f9c9957316280ef405ef8dcf255eafdb2, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `layanan`: `air_minum`, `kesehatan`, `mobilitas`, `sanitasi`
- `perlindungan_sosial`: kode sumber apa adanya
- `umur`: kode sumber apa adanya
- `layanan` (var2016, dari turvar BPS): `air_minum` = Akses pada layanan air minum, `sanitasi` = Akses pada layanan sanitasi dasar, `mobilitas` = Akses pada mobilitas dasar, `kesehatan` = Akses pada fasilitas kesehatan dasar

| rincian | dipakai_seri |
|---|---|
| jenis_kelamin=FEMALE | SDG_0111_SEX_AGE_RT |
| jenis_kelamin=FEMALE;perlindungan_sosial=CONTIG_MAT | SDG_0131_SEX_SOC_RT |
| jenis_kelamin=FEMALE;perlindungan_sosial=CONTIG_UNE | SDG_0131_SEX_SOC_RT |
| jenis_kelamin=FEMALE;umur=YTHADULT_Y15-24 | SDG_0111_SEX_AGE_RT |
| jenis_kelamin=FEMALE;umur=YTHADULT_YGE25 | SDG_0111_SEX_AGE_RT |
| jenis_kelamin=MALE | SDG_0111_SEX_AGE_RT |
| jenis_kelamin=MALE;perlindungan_sosial=CONTIG_UNE | SDG_0131_SEX_SOC_RT |
| jenis_kelamin=MALE;umur=YTHADULT_Y15-24 | SDG_0111_SEX_AGE_RT |
| jenis_kelamin=MALE;umur=YTHADULT_YGE25 | SDG_0111_SEX_AGE_RT |
| layanan=air_minum | var2016 |
| layanan=kesehatan | var2016 |
| layanan=sanitasi | var2016 |
| perlindungan_sosial=CONTIG_CHILD | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_DISAB | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_INJ | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_PENSION | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_POOR | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_UNE | SDG_0131_SEX_SOC_RT |
| perlindungan_sosial=CONTIG_VULN | SDG_0131_SEX_SOC_RT |
| total | SDG_0111_SEX_AGE_RT, SDG_0131_SEX_SOC_RT, SDG_1041_NOC_RT, SI.DST.50MD, SI.POV.DDAY, var1254, var2011 |
| umur=YTHADULT_Y15-24 | SDG_0111_SEX_AGE_RT |
| umur=YTHADULT_YGE25 | SDG_0111_SEX_AGE_RT |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var2011 | persen | 10.2.1 | Susenas; 2018–2023; provinsi dengan RSE terlalu tinggi tidak ditampilkan (var.note); judul menyebut pendapatan | judul 'Proporsi penduduk'; var.unit kosong; nilai 0–30 |
| var2016 | persen | 1.4.1 | rumah tangga; turvar menyebut empat layanan, tetapi hanya air minum, sanitasi, dan fasilitas kesehatan yang berisi angka (mobilitas kosong); tanpa total; 2019–2023 | var.unit: 'Persen' |
| var1254 | persen | 17.1.1 | hanya 2015 dan 2016; judul menyebut 'menurut sumbernya' tetapi berkas tanpa rincian sumber | judul 'sebagai proporsi terhadap PDB'; var.unit kosong |
| SI.DST.50MD | persen | 10.2.1 | pendapatan atau konsumsi per kapita (sourceNote); median diukur dalam PPP 2021; Bank Dunia PIP | name: '(%)' |
| SI.POV.DDAY | persen | 1.1.1 | seluruh penduduk; garis US$3 per hari PPP 2021 | name: '(% of population)' |
| SDG_0111_SEX_AGE_RT | persen | 1.1.1 | pekerja (bukan seluruh penduduk); garis US$3 per hari PPP (deskripsi dataflow); ILO modelled estimates (SOURCE); kode OBS_STATUS A, R, M tidak dijelaskan di paket | UNIT_MEASURE PT |
| SDG_0131_SEX_SOC_RT | persen | 1.3.1 | rincian fungsi perlindungan sosial; tahun tidak berurutan | UNIT_MEASURE PT |
| SDG_1041_NOC_RT | persen | 10.4.1 | 2004–2026; 2026 proyeksi; ILO modelled estimates (SOURCE); kode OBS_STATUS A, R, M tidak dijelaskan di paket | UNIT_MEASURE PT |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1254 | 1100 | 2015 | total | 1.54 | bps/2026-10-20/json/sdg17_17_1_1_v1254.json | 0bdc1b62f4a7ec0d96175254a4a4e0df7421b3ee89e0d08fd29a5b878d67c531 |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg17_17_1_1_v1254.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `0bdc1b62f4a7…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).
