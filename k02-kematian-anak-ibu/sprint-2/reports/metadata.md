# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1373 | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Provinsi | Angka Kematian Balita (AKBa) per 1.000 kelahiran hidup |
| var1584 | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Provinsi | Angka Kematian Bayi (AKB) per 1.000 kelahiran hidup |
| var1541 | Persentase Perempuan Pernah Kawin Umur 15-49 Tahun Yang Proses Kelahiran Terakhirnya Di Fasilitas Kesehatan (40% Bawah) Menurut Provinsi | Persentase perempuan pernah kawin 15–49 tahun yang kelahiran terakhirnya di fasilitas kesehatan, 40% pengeluaran terbawah |
| SH.DYN.MORT | Mortality rate, under-5 (per 1,000 live births) | Mortality rate, under-5 (per 1,000 live births) |
| SH.STA.MMRT | Maternal mortality ratio (modeled estimate, per 100,000 live births) | Maternal mortality ratio (modeled estimate, per 100,000 live births) |
| SH.STA.BRTC.ZS | Births attended by skilled health staff (% of total) | Births attended by skilled health staff (% of total) |
| MDG_0000000007 | Mortality rate (under 5) | Under-five mortality rate (probability of dying by age 5 per 1000 live births) |
| MDG_0000000026 | Maternal mortality ratio | Maternal mortality ratio (per 100 000 live births) |
| WHOSIS_000003 | Mortality rate (neonetal) | Neonatal mortality rate (per 1000 live births) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1373 | tidak_ada | per_1000_kh | var.label: 'Angka Kematian Balita Per 1000 Kelahiran Hidup'; var.unit kosong; CSV kolom satuan kosong | 3.2.1 | 3.2.1 |
| var1584 | tidak_ada | per_1000_kh | var.label: 'Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup'; var.unit kosong | 3.2.1 | 3.2.1(b) |
| var1541 | persen | persen | var.unit: 'Persen' | 3.1.2 | 3.1.2(b) |
| SH.DYN.MORT | — | per_1000_kh | name: '(per 1,000 live births)' | — | 3.2.1 |
| SH.STA.MMRT | — | per_100000_kh | name: '(modeled estimate, per 100,000 live births)' | — | 3.1.1 |
| SH.STA.BRTC.ZS | — | persen | name: '(% of total)' | — | 3.1.2 |
| MDG_0000000007 | — | per_1000_kh | kolom RATE_PER_1000_N | 3.2.1 | 3.2.1 |
| MDG_0000000026 | — | per_100000_kh | kolom RATE_PER_100000_N | 3.1.1 | 3.1.1 |
| WHOSIS_000003 | — | per_1000_kh | kolom RATE_PER_1000_N | 3.2.2 | 3.2.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1373 | satuan tidak_ada -> per_1000_kh |
| var1584 | satuan tidak_ada -> per_1000_kh; kode SDG 3.2.1 -> 3.2.1(b) (bukan indikator global 3.2.1) |
| var1541 | kode SDG 3.1.2 -> 3.1.2(b); bukan ukuran yang sama dengan indikator global 3.1.2 |
| SH.DYN.MORT | kode SDG kosong -> 3.2.1 |
| SH.STA.MMRT | kode SDG kosong -> 3.1.1 |
| SH.STA.BRTC.ZS | kode SDG kosong -> 3.1.2 |
| WHOSIS_000003 | IND_NAME di CSV tertulis 'Mortality rate (neonetal)'; nama baku dari odata/Indicator.json |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1541 |  |
| 1373 | Sumber : SDKI Catatan : Angka Indonesia tahun 2012 dan 2017 dengan rujukan periode 5 tahun sebelum survei Angka provinsi dengan rujukan periode 10 tahun sebelum survei Angka provinsi tahun 2017 tidak ada |
| 1584 | Sumber : SDKI Catatan : Angka Kematian Bayi (AKB) Indonesia tahun 2012 dan 2017 dengan rujukan periode 5 tahun sebelum survei AKB untuk angka disagregasi menurut provinsi dengan rujukan periode 10 tahun sebelum survei AKB untuk provinsi tahun 2017 tidak ada |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SH.DYN.MORT | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SH.STA.BRTC.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SH.STA.MMRT | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
