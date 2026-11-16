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
