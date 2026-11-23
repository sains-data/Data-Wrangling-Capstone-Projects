# Data dictionary — Kasus 18 Energi: listrik dan bahan bakar memasak

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (4,889 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | EG.CFT.ACCS.ZS, EG.ELC.ACCS.ZS, tabel:sdg7_bahan_bakar, var87 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (39 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1991, 1992, 1993, 1994, 1995, 1996, … (35 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | bahan_bakar=arang_briket, bahan_bakar=gas_elpiji, bahan_bakar=kayu, bahan_bakar=lainnya, bahan_bakar=listrik, bahan_bakar=minyak_tanah, … (7 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 0 – 100.01 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 7.1.1, 7.1.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 4889 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 4889 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 4889 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg7_bahan_bakar.json, bps/2026-10-17/json/sdg7_listrik_pln.json, wdi/2026-10-20/data/kelompok-01-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 88d2ddbd3ccfeb6cb395345f034be0e39b8e732996a2824ae414d90a6153828e, 8d2fae3a96415bd41299bf08abfc356d33448bdd6b66ff2f492aca4eb0e63226, f409057fc1d66ee527cb9675149c1925390094162cdf997d387ad1dab1ecf8ac | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `bahan_bakar`: `arang_briket`, `gas_elpiji`, `kayu`, `lainnya`, `listrik`, `minyak_tanah`

| rincian | dipakai_seri |
|---|---|
| bahan_bakar=arang_briket | tabel:sdg7_bahan_bakar |
| bahan_bakar=gas_elpiji | tabel:sdg7_bahan_bakar |
| bahan_bakar=kayu | tabel:sdg7_bahan_bakar |
| bahan_bakar=lainnya | tabel:sdg7_bahan_bakar |
| bahan_bakar=listrik | tabel:sdg7_bahan_bakar |
| bahan_bakar=minyak_tanah | tabel:sdg7_bahan_bakar |
| total | EG.CFT.ACCS.ZS, EG.ELC.ACCS.ZS, tabel:sdg7_bahan_bakar, var87 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var87 | persen | 7.1.1 | rumah tangga; hanya listrik PLN (bukan semua sumber listrik); Susenas 1993–2025 tanpa 2005; var.def: provinsi tidak dicacah 2000–2001, hanya ibu kota 2002 | var.unit: 'Persen' |
| tabel:sdg7_bahan_bakar | persen | 7.1.2 | tabel statis (HTML) 2001, 2007–2021; 6 jenis + jumlah; gas/elpiji termasuk gas kota/biogas, lainnya termasuk rumah tangga yang tidak memasak (catatan tabel) | judul tabel statis 'Persentase Rumah Tangga' |
| EG.ELC.ACCS.ZS | persen | 7.1.1 | penduduk; semua sumber listrik (industri, survei nasional, sumber internasional) | name: '(% of population)' |
| EG.CFT.ACCS.ZS | persen | 7.1.2 | penduduk; menurut pedoman WHO minyak tanah tidak termasuk bersih (sourceNote) | name: '(% of population)' |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | tabel:sdg7_bahan_bakar | 1100 | 2007 | bahan_bakar=arang_briket | 0.35 | bps/2026-10-17/json/sdg7_bahan_bakar.json | f409057fc1d66ee527cb9675149c1925390094162cdf997d387ad1dab1ecf8ac |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-17/json/sdg7_bahan_bakar.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `f409057fc1d6…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (3,040 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji], tabel:sdg7_bahan_bakar [bahan_bakar=kayu], tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah], var87 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | tabel:sdg7_bahan_bakar, var87 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | bahan_bakar=gas_elpiji, bahan_bakar=kayu, bahan_bakar=minyak_tanah, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1993, 1994, 1995, 1996, 1997, 1998, … (32 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 450 | 0 – 100 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | batas_lama, belum_ada, missing, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 2703 | cakupan_parsial, outlier, patahan_seri, patahan_wilayah, perbedaan_struktural | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 3040 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 450 | bps/2026-10-17/json/sdg7_bahan_bakar.json, bps/2026-10-17/json/sdg7_listrik_pln.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 450 | 88d2ddbd3ccfeb6cb395345f034be0e39b8e732996a2824ae414d90a6153828e, f409057fc1d66ee527cb9675149c1925390094162cdf997d387ad1dab1ecf8ac | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | persen |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | persen |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | persen |
| var87 | persen |

## data/gold/nasional.parquet (123 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | EG.CFT.ACCS.ZS, EG.ELC.ACCS.ZS, tabel:sdg7_bahan_bakar, var87 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | bahan_bakar=gas_elpiji, total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1991, 1992, 1993, 1994, 1995, 1996, … (35 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 6 – 100.01 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 123 | — | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 123 | — | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 123 | — | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-17/json/sdg7_bahan_bakar.json, bps/2026-10-17/json/sdg7_listrik_pln.json, wdi/2026-10-20/data/kelompok-01-hal-01.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 88d2ddbd3ccfeb6cb395345f034be0e39b8e732996a2824ae414d90a6153828e, 8d2fae3a96415bd41299bf08abfc356d33448bdd6b66ff2f492aca4eb0e63226, f409057fc1d66ee527cb9675149c1925390094162cdf997d387ad1dab1ecf8ac | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (54 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P2 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | tabel:sdg7_bahan_bakar, var87 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | bahan_bakar=gas_elpiji, total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | EG.CFT.ACCS.ZS, EG.ELC.ACCS.ZS | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 1993, 1994, 1995, 1996, 1997, 1998, … (33 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 6 | 8.22 – 98.46 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 1 | 6 – 100 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 7 | -11.43 – 2.22 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 7 | -51.9545 – 37 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, tanpa pasangan | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi (PLN saja vs semua sumber listrik; rumah tangga vs penduduk), definisi (kategori bersih; rumah tangga vs penduduk); BPS berakhir 2021 | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | object | 54 |  | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 1200 | 2001 | 5.26 | bps/2026-10-17/json/sdg7_bahan_bakar.json |

1. Sel ini berasal dari baris Silver `tabel:sdg7_bahan_bakar` × 1200 × 2001 × rincian `bahan_bakar=gas_elpiji` × berkas `bps/2026-10-17/json/sdg7_bahan_bakar.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
