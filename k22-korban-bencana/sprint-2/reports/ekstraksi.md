# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bnpb/2026-10-20/ckan/package_search-pusdatinkom-01.json | bnpb_ckan | meta | 355 | 78 dataset, 355 resource; judul resource = nama ukuran |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/21044ffd-c397-4b3c-acbd-5adaa03d79e3.json | bnpb_sel | data | 7650 | DataStore 510 record; tata tahun/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/318f541a-5b0d-448c-8b78-9ba56c0478f2.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/5dfcae7e-acb3-4548-82b5-61d876ea478a.json | bnpb_sel | data | 570 | DataStore 38 record; tata tahun/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/69605ad2-73ea-4967-b2d5-639ad9291833.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/7f9e5218-bbba-4916-a2b8-13cf1764dc96.json | bnpb_sel | data | 124 | DataStore 9 record; tata tahun/nasional; 11 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/9b41007e-c998-456b-8cbc-385b17986e46.json | bnpb_sel | data | 135 | DataStore 9 record; tata tahun/nasional; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/a19366cf-0ac4-45d1-bc6e-89a020ab45a1.json | bnpb_sel | data | 133 | DataStore 9 record; tata tahun/nasional; 2 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/a4daec53-1119-43ef-b05e-00ec3a4c42a4.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/b1e58b39-8dc4-4b9b-abc6-50139acd2fda.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/ce67795b-57e4-4c84-8c2a-3bf03828ff0d.json | bnpb_sel | data | 134 | DataStore 9 record; tata tahun/nasional; 1 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/d1fd9f08-26e1-453a-9be0-422538f01b5e.json | bnpb_sel | data | 209 | DataStore 39 record; tata jenis/provinsi; 142 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/d7b61b56-43d5-4dcc-8d7b-45c993e1bdb0.json | bnpb_sel | data | 135 | DataStore 9 record; tata tahun/nasional; 0 sel kosong |
| bnpb/2026-10-20/datastore/data-bencana-indonesia/faeb2406-b800-4b8e-9e09-37d4b2aa5879.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/1852744b-f6b1-4010-933e-cf60087dd54e.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/39ceb577-b49f-45c9-b909-7dd8daef417a.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/4cddaa9f-45b1-47f5-9428-519e876a8e20.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/5ff9f41f-8312-4b7c-aa18-fdbedac6ee7e.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/68c4448c-3de9-42e3-987d-31f5c05c37ba.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/7a42016e-ce4d-402e-b10e-4e691a3c436f.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/820e56bc-fd26-4e47-ae12-5b23f1d5fd08.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/89eb9dac-a891-477e-b264-2265f72f4e56.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/bf415deb-7076-4aaf-90ad-013b9a5292f7.json | bnpb_sel | data | 4059 | DataStore 451 record; tata jenis/kabkota; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/d528ad3f-5159-4c7d-b87e-e41d614df191.json | bnpb_sel | data | 209 | DataStore 39 record; tata jenis/provinsi; 142 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/e5c7f8e7-c3b4-44ff-9581-e7d187240886.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/f345ba43-99aa-428c-82d8-4b6a0bba380e.json | bnpb_sel | data | 351 | DataStore 39 record; tata jenis/provinsi; 0 sel kosong |
| bnpb/2026-10-20/tangan/data-bencana/0c165adc-5be2-489d-8b1a-e90c6715e73e-tabel-jumlah-kejadian-korban-dan-kerusakan-akibat-bencana-tahun-2021-per-provinsi.xlsx | bnpb_sel | data | 2310 | XLSX 1 lembar data; tata rekap/provinsi; 0 sel kosong |
| bnpb/2026-10-20/tangan/data-bencana/692df9e1-a8f8-49b3-a78f-de5795fb6e79-tabel-jumlah-kejadian-korban-dan-kerusakan-akibat-bencana-tahun-2022-per-provinsi.xlsx | bnpb_sel | data | 1974 | XLSX 1 lembar data; tata rekap/provinsi; 0 sel kosong |
| bnpb/2026-10-20/tangan/data-bencana/6ec0418d-1590-45c3-b731-9fa1ab2af5c8-tabel-jumlah-kejadian-korban-dan-kerusakan-akibat-bencana-tahun-2021-per-kabupaten-kota.xlsx | bnpb_sel | data | 16170 | XLSX 1 lembar data; tata rekap/kabkota; 0 sel kosong |
| bnpb/2026-10-20/tangan/data-bencana/9170802b-7f71-4d8f-a326-8e478d0463e8-tabel-jumlah-kejadian-korban-dan-kerusakan-akibat-bencana-tahun-2022-per-kabupten-kota.xlsx | bnpb_sel | data | 12754 | XLSX 1 lembar data; tata rekap/kabkota; 0 sel kosong |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/31a0d329-a363-4a16-852c-f4fa51f313bf-jumlah-korban-mengungsi-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 390 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 8 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/50b99a45-d8ff-496e-a64f-9e689754371c-jumlah-korban-luka-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/6e947c9c-2404-4c02-b743-34dc5320f399-rekapitulasi-jumlah-kejadian-dan-dampak-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 140 | XLSX 1 lembar data; tata rekap_nasional/nasional; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/8d8db1c8-d79b-4fb1-b735-d8b9c1e0517a-jumlah-korban-terdampak-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/aefe8331-5962-4610-8b0c-2de637a336cd-jumlah-korban-meninggal-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/df39e8c3-117e-40fa-b518-ff1037743955-jumlah-kejadian-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/eefa5746-5c65-4156-ac74-2eff2bfac767-jumlah-korban-mengungsi-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/f1de565c-c028-43e7-a48d-109ebb8f3081-jumlah-korban-hilang-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 351 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 15 baris |
| bnpb/2026-10-20/tangan/kompilasi-data-kejadian-dan-dampak-bencana-2025/f800105c-ac2f-4b47-b097-0cd4f5d63b82-jumlah-korban-meninggal-dan-hilang-per-100.000-orang-akibat-bencana-menurut-provinsi-2025.xlsx | bnpb_sel | data | 390 | XLSX 1 lembar data; tata jenis/provinsi; 0 sel kosong; lembar Keterangan 8 baris |
| wdi/2026-10-20/data/kelompok-01-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |

Jumlah: 44 berkas dari 44 di MANIFEST, 77,522 baris mentah di berkas data.
