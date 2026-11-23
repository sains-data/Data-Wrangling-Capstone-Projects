# Data dictionary — Kasus 02 Kematian anak dan ibu

Ditulis ulang otomatis oleh `python pipeline.py` (`src/dokumen.py`). Tipe, rentang, dan jumlah kosong dihitung dari `data/silver/silver.parquet`.

## data/silver/silver.parquet (867 baris)

Satu baris = satu seri x wilayah x periode x rincian x berkas sumber. Kunci unik: sumber, seri_kode, wilayah_kode, periode, rincian, _berkas_raw.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| seri_kode | str | 0 | MDG_0000000007, MDG_0000000026, SH.DYN.MORT, SH.STA.BRTC.ZS, SH.STA.MMRT, WHOSIS_000003, … (9 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| wilayah_kode | int64 | 0 | 1100 – 9999 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (35 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 1951, 1952, 1953, 1954, 1955, 1956, … (74 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| rincian | str | 0 | jenis_kelamin=FEMALE, jenis_kelamin=MALE, kuintil=WQ1, kuintil=WQ2, kuintil=WQ3, kuintil=WQ4, … (8 nilai) | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| nilai | float64 | 0 | 10.5261 – 474 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_100000_kh, per_1000_kh, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| sdg_kode | str | 0 | 3.1.1, 3.1.2, 3.1.2(b), 3.2.1, 3.2.1(b), 3.2.2 | src/konfigurasi.py, bukti di docs/seri.csv | kode indikator SDG (kolom tambahan) |
| batas_bawah | float64 | 370 | 7.65085 – 342.939 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 370 | 14.3664 – 634.067 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | Int64 | 797 | 5 – 10 | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_1_2_v1541.json, bps/2026-10-20/json/sdg3_3_2_1_v1373.json, bps/2026-10-20/json/sdg3_3_2_1_v1584.json, wdi/2026-10-20/data/kelompok-05-hal-01.json, who_gho/2026-10-20/datadot/2322814_MDG_0000000007.csv, who_gho/2026-10-20/datadot/A4C49D3_WHOSIS_000003.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0a8ee3da84b45a9a237b5e188976b44b9a2c5d6c1d7fd11f538c9790dd7aaf7f, 55caba4491921f976ea8ce66b8852c2bba49a37682b4f6286a0eb7dcfca8647e, 64e49e246c377ee2d991f58c1dc7b09901330395260937fb35617e9c50883849, 7512780e34bc137cce49db6bdd213765ad52cb3bce3a56dbd0778bf57ffcd9bb, a57f712cfa3bfddffd55b8cf9b5884f3981b6ecc3320860ebae633fb16dd3103, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## Kamus rincian

Aturan menulis rincian (log): dimensi yang bervariasi ditulis `nama=kode`, dipisah `;`, urut abjad; nilai total sumber dibuang; baris tanpa dimensi bervariasi ditulis `total`. Dimensi yang nilainya tetap di seluruh berkas dianggap bagian definisi seri dan dicatat di kolom `cakupan` docs/seri.csv.

Nama dimensi dan kode yang sah:

- `jenis_kelamin`: `FEMALE`, `MALE`
- `kuintil`: `WQ1`, `WQ2`, `WQ3`, `WQ4`, `WQ5`
- `umur`: kode sumber apa adanya

| rincian | dipakai_seri |
|---|---|
| jenis_kelamin=FEMALE | MDG_0000000007 |
| jenis_kelamin=MALE | MDG_0000000007 |
| kuintil=WQ1 | MDG_0000000007 |
| kuintil=WQ2 | MDG_0000000007 |
| kuintil=WQ3 | MDG_0000000007 |
| kuintil=WQ4 | MDG_0000000007 |
| kuintil=WQ5 | MDG_0000000007 |
| total | MDG_0000000007, MDG_0000000026, SH.DYN.MORT, SH.STA.BRTC.ZS, SH.STA.MMRT, WHOSIS_000003, var1373, var1541, var1584 |

## Satuan, kode SDG, dan cakupan per seri

| seri_kode | satuan | sdg_kode | cakupan | bukti_satuan |
|---|---|---|---|---|
| var1373 | per_1000_kh | 3.2.1 | kematian sebelum umur 5 tahun; sumber SDKI; nasional rujukan 5 tahun, provinsi 10 tahun sebelum survei | var.label: 'Angka Kematian Balita Per 1000 Kelahiran Hidup'; var.unit kosong; CSV kolom satuan kosong |
| var1584 | per_1000_kh | 3.2.1(b) | kematian sebelum umur 1 tahun; sumber SDKI; nasional rujukan 5 tahun, provinsi 10 tahun sebelum survei | var.label: 'Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup'; var.unit kosong |
| var1541 | persen | 3.1.2(b) | perempuan pernah kawin 15–49, kelahiran terakhir, kelompok 40% pengeluaran terbawah | var.unit: 'Persen' |
| SH.DYN.MORT | per_1000_kh | 3.2.1 | estimasi model UN IGME, tahunan | name: '(per 1,000 live births)' |
| SH.STA.MMRT | per_100000_kh | 3.1.1 | estimasi model regresi (sourceNote) | name: '(modeled estimate, per 100,000 live births)' |
| SH.STA.BRTC.ZS | persen | 3.1.2 | semua persalinan, ditolong tenaga kesehatan terlatih; dari survei (DHS dsb.), banyak tahun kosong | name: '(% of total)' |
| MDG_0000000007 | per_1000_kh | 3.2.1 | estimasi UN IGME, tahunan [dimensi tetap di berkas: DIM_AGE=Y_LT5] | kolom RATE_PER_1000_N |
| MDG_0000000026 | per_100000_kh | 3.1.1 | estimasi model MMEIG, tahunan | kolom RATE_PER_100000_N |
| WHOSIS_000003 | per_1000_kh | 3.2.2 | kematian 0–27 hari, estimasi UN IGME [dimensi tetap di berkas: DIM_SEX=TOTAL; DIM_AGE=D_LE27] | kolom RATE_PER_1000_N |

## Kode wilayah

9999 = Indonesia; provinsi = kode BPS dua digit x 100, susunan 38 provinsi 2025 (38 kode). WDI menulis Indonesia `ID`/`IDN`, WHO GHO menulis `360` (M49); keduanya dipetakan ke 9999 di `src/wilayah.py`.

## Contoh penelusuran satu baris

| sumber | seri_kode | wilayah_kode | periode | rincian | nilai | _berkas_raw | _sha256_raw |
|---|---|---|---|---|---|---|---|
| bps | var1373 | 1100 | 2012 | total | 52.00 | bps/2026-10-20/json/sdg3_3_2_1_v1373.json | 7512780e34bc137cce49db6bdd213765ad52cb3bce3a56dbd0778bf57ffcd9bb |

1. `_berkas_raw` menunjuk `data/raw/bps/2026-10-20/json/sdg3_3_2_1_v1373.json`.

2. Baris berkas itu di `data/raw/MANIFEST.csv` memuat sha256 `7512780e34bc…`; nilainya sama dengan `_sha256_raw`, jadi berkas yang dibaca adalah berkas yang tercatat.

3. Di berkas mentah, angka ditemukan pada wilayah, periode, dan rincian yang sama (untuk JSON BPS: kunci `datacontent` = kode wilayah + var + turvar + kode tahun + turtahun).

## data/gold/panel.parquet (342 baris)

Satu baris = satu indikator × provinsi × periode, termasuk sel kosong dari grid. Kunci unik: indikator, wilayah_kode, periode. Tampilan lebar (satu kolom per indikator, hanya sel terisi): `data/gold/panel_lebar.parquet`.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| indikator | str | 0 | var1373, var1541, var1584 | label deret utama (src/silver/deret.py) | kode seri, atau 'kode [rincian]' untuk deret berincian |
| seri_kode | str | 0 | var1373, var1541, var1584 | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| wilayah_kode | int64 | 0 | 1100 – 9700 | kamus src/wilayah.py; log K-001 | kode BPS dua digit x 100; 9999 = Indonesia |
| nama_wilayah | str | 0 | Aceh, Bali, Banten, Bengkulu, DI Yogyakarta, DKI Jakarta, … (38 nilai) | kamus src/wilayah.py | nama baku susunan 38 provinsi 2025, bukan label sumber |
| periode | str | 0 | 2012, 2015, 2016, 2017, 2018, 2019 | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 106 | 13.06 – 115 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_1000_kh, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| status_sel | str | 0 | belum_ada, terisi, tidak_diterbitkan | grid Sprint 1 (reports/grid-sel-kosong.csv) | terisi, missing, tidak_diterbitkan, belum_ada, batas_lama |
| penanda | str | 337 | outlier | reports/anomali.csv | kategori anomali Sprint 1 (outlier, patahan_seri, ...); nilai tidak diubah |
| rujukan_tahun | float64 | 276 | 10 – 10 | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| _berkas_raw | str | 106 | bps/2026-10-20/json/sdg3_3_1_2_v1541.json, bps/2026-10-20/json/sdg3_3_2_1_v1373.json, bps/2026-10-20/json/sdg3_3_2_1_v1584.json | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 106 | 55caba4491921f976ea8ce66b8852c2bba49a37682b4f6286a0eb7dcfca8647e, 64e49e246c377ee2d991f58c1dc7b09901330395260937fb35617e9c50883849, 7512780e34bc137cce49db6bdd213765ad52cb3bce3a56dbd0778bf57ffcd9bb | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

Satuan per indikator:

| indikator | satuan |
|---|---|
| var1373 | per_1000_kh |
| var1541 | persen |
| var1584 | per_1000_kh |

## data/gold/nasional.parquet (317 baris)

Satu baris = satu seri × rincian × periode tingkat Indonesia. Kunci unik: seri_kode, rincian, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| seri_kode | str | 0 | MDG_0000000007, MDG_0000000026, SH.DYN.MORT, SH.STA.BRTC.ZS, SH.STA.MMRT, WHOSIS_000003, … (9 nilai) | kode seri di sumbernya (BPS: 'var' + var.val) | identitas seri; arti lengkap di docs/seri.csv |
| rincian | str | 0 | total | turvar BPS; kolom DIM_* WHO yang bervariasi | 'total' atau 'dimensi=kode;...'; lihat kamus di bawah |
| sumber | str | 0 | bps, wdi, who_gho | nama folder sumber di data/raw/ | lembaga penerbit: bps, wdi, who_gho, ilostat, bnpb |
| periode | str | 0 | 1951, 1952, 1953, 1954, 1955, 1956, … (74 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| jenis_periode | str | 0 | tahun | diturunkan dari periode | tahun, semester, triwulan, atau bulan |
| nilai | float64 | 0 | 10.5261 – 474 | datacontent BPS; value WDI; RATE_*_N WHO | angka sesuai satuan; baris tanpa angka tidak masuk Silver |
| satuan | str | 0 | per_100000_kh, per_1000_kh, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| batas_bawah | float64 | 134 | 7.65085 – 342.939 | RATE_*_NL WHO | batas bawah ketidakpastian; kosong bila sumber tidak memberi |
| batas_atas | float64 | 134 | 14.3664 – 634.067 | RATE_*_NU WHO | batas atas ketidakpastian; kosong bila sumber tidak memberi |
| rujukan_tahun | float64 | 313 | 5 – 5 | var.note BPS; log | lebar jendela rujukan survei (tahun sebelum survei); kosong bila tidak berlaku |
| asal | str | 0 | baris_indonesia, pembanding | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| _berkas_raw | str | 0 | bps/2026-10-20/json/sdg3_3_1_2_v1541.json, bps/2026-10-20/json/sdg3_3_2_1_v1373.json, bps/2026-10-20/json/sdg3_3_2_1_v1584.json, wdi/2026-10-20/data/kelompok-05-hal-01.json, who_gho/2026-10-20/datadot/2322814_MDG_0000000007.csv, who_gho/2026-10-20/datadot/A4C49D3_WHOSIS_000003.csv, … (7 nilai) | jalur berkas mentah relatif data/raw/ | lineage: berkas asal baris ini |
| _sha256_raw | str | 0 | 0a8ee3da84b45a9a237b5e188976b44b9a2c5d6c1d7fd11f538c9790dd7aaf7f, 55caba4491921f976ea8ce66b8852c2bba49a37682b4f6286a0eb7dcfca8647e, 64e49e246c377ee2d991f58c1dc7b09901330395260937fb35617e9c50883849, 7512780e34bc137cce49db6bdd213765ad52cb3bce3a56dbd0778bf57ffcd9bb, a57f712cfa3bfddffd55b8cf9b5884f3981b6ecc3320860ebae633fb16dd3103, ad8155b7117914929b2c91b16ade1654b94c0632b3364bbfc97dc4214b9abc8e, … (7 nilai) | src.common.manifest.sha256_raw | lineage: sidik isi berkas asal, dicocokkan dengan MANIFEST.csv |

## data/gold/rekonsiliasi.parquet (135 baris)

Satu baris = satu pasangan × pembanding × periode. Kunci unik: pasangan_id, seri_pembanding, rincian_pembanding, periode.

| kolom | tipe | kosong | rentang_atau_nilai | asal | arti |
|---|---|---|---|---|---|
| pasangan_id | str | 0 | P1, P1J, P2, P3, P4, P5 | PASANGAN di src/konfigurasi.py | id pasangan rekonsiliasi (P1, P2, ...) |
| jenis | str | 0 | konteks, selisih | PASANGAN | selisih (dihitung) atau konteks (ditampilkan berdampingan) |
| seri_utama | str | 0 | MDG_0000000007, MDG_0000000026, var1373, var1541, var1584 | PASANGAN | seri yang direkonsiliasi (BPS/BNPB, atau seri nasional untuk pasangan antarpembanding) |
| rincian_utama | str | 0 | total | PASANGAN | rincian seri utama yang dibandingkan |
| seri_pembanding | str | 0 | , MDG_0000000007, SH.DYN.MORT, SH.STA.BRTC.ZS, SH.STA.MMRT | PASANGAN | seri pembanding; kosong bila pasangan tidak punya pembanding di paket |
| rincian_pembanding | str | 0 | , total | PASANGAN | rincian pembanding yang sebanding |
| periode | str | 0 | 1951, 1952, 1953, 1954, 1955, 1956, … (73 nilai) | tahun/turtahun BPS, date WDI, DIM_TIME WHO | bentuk baku: 2019, 2019-S1, 2019-Q3, 2019-07 |
| nilai_utama | float64 | 8 | 20.6244 – 473.585 | gold_nasional.nilai | nilai seri utama pada periode itu |
| nilai_pembanding | float64 | 12 | 18.4 – 474 | gold_nasional.nilai x faktor GOLD_KONVERSI | nilai pembanding dalam satuan seri utama |
| satuan | str | 0 | per_100000_kh, per_1000_kh, persen | src/konfigurasi.py, bukti di docs/seri.csv | satuan baku; satu satuan per seri |
| selisih | float64 | 24 | -0.846799 – 10.1 | dihitung | nilai_utama − nilai_pembanding; kosong bila tidak dibandingkan (lihat catatan) |
| selisih_relatif | float64 | 24 | -0.368334 – 34.4538 | dihitung | 100 × selisih / nilai_pembanding (persen) |
| asal | str | 0 | hanya_pembanding, hanya_utama, keduanya | src/gold/nasional_gold.py; src/gold/rekonsiliasi.py | nasional: baris_indonesia/pembanding/agregat; rekonsiliasi: keduanya/hanya_utama/hanya_pembanding |
| kategori | str | 0 | definisi berbeda, metode berbeda, tanpa pasangan, vintage berbeda | PASANGAN (kategori_baku atau teks kategori) | kategori baku penjelasan selisih |
| penjelasan | str | 0 | definisi berbeda: tidak ada seri kematian bayi (0–11 bulan) di paket pembanding, definisi dan cakupan berbeda; tidak dihitung sebagai selisih, metode (survei SDKI vs estimasi model UN IGME); periode rujukan sudah disamakan dengan merata-ratakan pembanding pada 5 tahun sebelum survei, metode dan definisi periode (survei dengan rujukan 5 tahun vs estimasi model tahunan), vintage (rilis estimasi UN IGME berbeda), vintage; tidak ada padanan BPS di paket | PASANGAN kategori | alasan selisih dengan bukti dari Sprint 1 |
| catatan | str | 127 | pasangan konteks: selisih tidak dihitung, pembanding = rata-rata 2007–2011 (jendela rujukan survei), pembanding = rata-rata 2012–2016 (jendela rujukan survei) | dihitung | mengapa selisih tidak dihitung pada baris ini (proyeksi, konteks, satuan) |

## Contoh penelusuran satu sel Gold

| indikator | wilayah_kode | periode | nilai | _berkas_raw |
|---|---|---|---|---|
| var1373 | 1100 | 2012 | 52.00 | bps/2026-10-20/json/sdg3_3_2_1_v1373.json |

1. Sel ini berasal dari baris Silver `var1373` × 1100 × 2012 × rincian `total` × berkas `bps/2026-10-20/json/sdg3_3_2_1_v1373.json` (aturan *gold: sel tertelusur ke Silver*).

2. Baris Silver itu membawa `_sha256_raw` yang sama dengan `data/raw/MANIFEST.csv` (lihat penelusuran Silver di atas).
