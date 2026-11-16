# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1241 | 11.1.1.(a) Persentase Rumah Tangga yang Memiliki Akses Terhadap Hunian Yang Layak Menurut Provinsi | Persentase rumah tangga yang memiliki akses terhadap hunian yang layak |
| var2012 | Persentase rumah tangga yang memiliki akses nyaman (jarak 0.5 km) ke transportasi umum menurut provinsi | Persentase rumah tangga dengan akses nyaman (jarak 0,5 km) ke transportasi umum |
| var2013 | Persentase penduduk berumur 10 tahun ke atas yang menggunakan kendaraan bermotor umum dengan rute tertentu menurut provinsi | Persentase penduduk 10 tahun ke atas yang menggunakan kendaraan bermotor umum dengan rute tertentu |
| var2753 | 9.1.2* Jumlah Bongkar Muat Barang Moda Transportasi Kapal | Jumlah bongkar muat barang moda transportasi kapal |
| var2754 | 9.1.2*. Jumlah Bongkar Muat Barang Moda Transportasi Pesawat Terbang | Jumlah bongkar muat barang moda transportasi pesawat terbang |
| EN.POP.SLUM.UR.ZS | Population living in slums (% of urban population) | Population living in slums (% of urban population) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1241 | persen | persen | var.unit: 'Persen' | 11.1.1 | 11.1.1(a) |
| var2012 | tidak_ada | persen | judul 'Persentase rumah tangga'; var.unit kosong | 11.2.1 | 11.2.1(a) |
| var2013 | tidak_ada | persen | judul 'Persentase penduduk'; var.unit kosong | 11.2.1 | 11.2.1(b) |
| var2753 | kilogram | kilogram | var.unit: 'KG' | 9.1.2 | 9.1.2 |
| var2754 | kilogram | kilogram | var.unit: 'KG' | 9.1.2 | 9.1.2 |
| EN.POP.SLUM.UR.ZS | — | persen | name: '(% of urban population)' | — | 11.1.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1241 | kode SDG 11.1.1 -> 11.1.1(a) |
| var2012 | satuan tidak_ada -> persen; kode SDG -> 11.2.1(a) |
| var2013 | satuan tidak_ada -> persen; kode SDG -> 11.2.1(b) |
| EN.POP.SLUM.UR.ZS | kode SDG kosong -> 11.1.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1241 | Sumber: BPS-RI, Susenas Catatan: Sejak tahun 2019, rumah tangga diklasifikasikan memiliki akses terhadap hunian/rumah layak huni apabila memenuhi 4 (empat) kriteria, yaitu: 1) kecukupan luas tempat tinggal minimal 7,2 m2 per kapita (sufficient living space) 2) memiliki akses terhadap air minum layak 3) memiliki akses terhadap sanitasi layak 4) ketahanan bangunan (durable housing), yaitu atap terluas berupa beton/ genteng/ seng/ kayu/ sirap; dinding terluas berupa tembok/ plesteran anyaman bambu/kawat, kayu/papan dan batang kayu; dan lantai terluas berupa marmer/ granit/ keramik/ parket/vinil/karpet/ ubin/tegel/teraso/ kayu/papan/ semen/bata merah. |
| 2753 | Sumber: Badan Pusat Statistik |
| 2754 | Sumber: Badan Pusat Statistik |
| 2012 | Sumber Data: Susenas Modul Ketahanan Sosial |
| 2013 | Sumber Data: Susenas Modul Ketahanan Sosial |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| EN.POP.SLUM.UR.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
