# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| kejadian | Jumlah Kejadian Bencana Menurut Kabupaten Tahun 2010-2024 | Jumlah kejadian bencana |
| korban_meninggal | Jumlah Korban Meninggal Dunia Akibat Bencana Menurut Provinsi, 2024 | Jumlah korban meninggal dunia akibat bencana |
| korban_hilang | Jumlah Korban Hilang Akibat Bencana Menurut Provinsi, 2024 | Jumlah korban hilang akibat bencana |
| korban_luka_sakit | Jumlah Korban Luka/Sakit Akibat Bencana Menurut Provinsi, 2024 | Jumlah korban luka/sakit akibat bencana |
| korban_mengungsi | Jumlah Korban Mengungsi Akibat Bencana Menurut Provinsi, 2024 | Jumlah korban mengungsi akibat bencana |
| korban_terdampak | Jumlah Korban Terdampak Akibat Bencana Menurut Provinsi, 2024 | Jumlah korban terdampak akibat bencana |
| korban_terdampak_mengungsi | kolom 'Terdampak - Mengungsi' di Rekapitulasi Jumlah Kejadian, Korban dan Kerusakan Akibat Bencana Tahun 2021 per Provinsi | Jumlah korban terdampak dan mengungsi (satu kolom di rekap 2021/2022) |
| korban_mengungsi_per_100rb | Jumlah Korban Mengungsi per 100.000 Orang Akibat Bencana Menurut Provinsi 2025.xlsx | Jumlah korban mengungsi per 100.000 orang |
| korban_meninggal_hilang_per_100rb | Jumlah Korban Meninggal dan Hilang per 100.000 Orang Akibat Bencana Menurut Provinsi 2025.xlsx | Jumlah korban meninggal dan hilang per 100.000 orang |
| jumlah_penduduk | kolom 'Jumlah Penduduk' di Jumlah Korban Mengungsi per 100.000 Orang Akibat Bencana Menurut Provinsi 2025.xlsx | Jumlah penduduk (penyebut angka per 100.000) |
| EN.CLC.MDAT.ZS | Droughts, floods, extreme temperatures (% of population, average 1990-2009) | Droughts, floods, extreme temperatures (% of population, average 1990-2009) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| kejadian | kejadian | kejadian | Keterangan: 'Jumlah Kejadian: Jumlah Total Kejadian Bencana Menurut Klasifikasi Penyajian' | — | — |
| korban_meninggal | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_hilang | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_luka_sakit | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_mengungsi | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_terdampak | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_terdampak_mengungsi | jiwa | jiwa | baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan) | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_mengungsi_per_100rb | per_100000_penduduk | per_100000_penduduk | judul resource di ckan/package_search-pusdatinkom-01.json: 'Jumlah Korban Mengungsi per 100.000 Orang ...' | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| korban_meninggal_hilang_per_100rb | per_100000_penduduk | per_100000_penduduk | judul resource di ckan/package_search-pusdatinkom-01.json: 'Jumlah Korban Meninggal dan Hilang per 100.000 Orang ...' | 13.1.1\|1.5.1\|11.5.1 | 13.1.1\|1.5.1\|11.5.1 |
| jumlah_penduduk | jiwa | jiwa | Keterangan: 'Jumlah Penduduk Berdasarkan Publikasi Badan Pusat Statistik' | — | — |
| EN.CLC.MDAT.ZS | — | persen | name: '(% of population, average 1990-2009)' | — | — |

## Koreksi katalog

Tidak ada.

## Catatan BPS (var.note)

Tidak ada seri BPS.

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| EN.CLC.MDAT.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
