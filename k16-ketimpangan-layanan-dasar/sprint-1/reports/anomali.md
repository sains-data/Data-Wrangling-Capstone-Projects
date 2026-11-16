# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var2011 | 2018→2019 | 34 | 0.03 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2011 | 2019→2020 | 34 | 0.06 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2011 | 2020→2021 | 34 | 0.06 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2011 | 2021→2022 | 34 | 0.06 | 0.32 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2011 | 2022→2023 | 29 | 0.00 | 0.10 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=air_minum] | 2019→2020 | 34 | 0.03 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=air_minum] | 2020→2021 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=air_minum] | 2021→2022 | 34 | 0.09 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=air_minum] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=sanitasi] | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=sanitasi] | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=sanitasi] | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=sanitasi] | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=kesehatan] | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=kesehatan] | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=kesehatan] | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2016 [layanan=kesehatan] | 2022→2023 | 34 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1254 | — | 0 |  |  | tidak dapat diuji | hanya 2 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 0

Tidak ada: tidak ada provinsi pemekaran yang mulai terbit di tengah panel seri provinsi.

## Calon anomali dan kategorinya (58)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1254 | DKI Jakarta | 2015 | 1.69 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1254 | Bali | 2015 | 1.72 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1254 | Kalimantan Selatan | 2015 | 1.95 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1254 | Kalimantan Tengah | 2016 | 1.51 | perubahan | outlier | tandai, nilai tidak diubah |
| var1254 | Kalimantan Selatan | 2016 | 2.01 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var1254 | Maluku | 2016 | 1.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var1254 | Papua | 2016 | 0.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Sulawesi Utara | 2018 | 14.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var2011 | Nusa Tenggara Timur | 2019 | 31.70 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2011 | Maluku | 2019 | 10.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Papua Barat | 2019 | 11.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Jawa Timur | 2020 | 16.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Nusa Tenggara Timur | 2021 | 29.00 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Gorontalo | 2021 | 20.84 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Papua | 2021 | 13.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Nusa Tenggara Timur | 2022 | 21.79 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | Aceh | 2023 | 8.26 | perubahan | outlier | tandai, nilai tidak diubah |
| var2011 | DI Yogyakarta | 2023 | 8.27 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var2011 | Bali | 2023 | 4.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var2011 | Gorontalo | 2023 | 23.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Papua Barat | 2020 | 25.21 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Nusa Tenggara Barat | 2021 | 43.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Kalimantan Utara | 2021 | 20.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Sulawesi Barat | 2021 | 40.80 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | DI Yogyakarta | 2022 | 71.88 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Gorontalo | 2022 | 26.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Jambi | 2023 | 51.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | DKI Jakarta | 2023 | 25.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Maluku | 2023 | 39.85 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=air_minum] | Papua | 2023 | 25.86 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Nusa Tenggara Timur | 2019 | 51.92 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Papua | 2019 | 35.55 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Sumatera Utara | 2020 | 67.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Nusa Tenggara Timur | 2020 | 54.43 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Maluku Utara | 2020 | 80.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Papua | 2020 | 36.44 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Nusa Tenggara Timur | 2021 | 56.33 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Sulawesi Barat | 2021 | 76.25 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Papua | 2021 | 36.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Nusa Tenggara Timur | 2022 | 56.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Papua | 2022 | 40.91 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Nusa Tenggara Timur | 2023 | 43.50 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=kesehatan] | Kalimantan Utara | 2023 | 76.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Papua Barat | 2023 | 65.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=kesehatan] | Papua | 2023 | 31.78 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | DI Yogyakarta | 2019 | 94.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Bali | 2019 | 94.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=sanitasi] | Papua | 2019 | 38.27 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | DI Yogyakarta | 2020 | 96.96 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Papua | 2020 | 40.31 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | DI Yogyakarta | 2021 | 97.12 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Bali | 2021 | 95.95 | ke bawah | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=sanitasi] | Papua | 2021 | 40.81 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Kepulauan Riau | 2022 | 87.74 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=sanitasi] | DI Yogyakarta | 2022 | 96.21 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Papua Barat | 2022 | 73.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var2016 [layanan=sanitasi] | Papua | 2022 | 40.34 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2016 [layanan=sanitasi] | Papua | 2023 | 43.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1254 | 70 | 70 | 70 | 0 | 0 | 0 | (kosong) |
| var2011 | 205 | 205 | 205 | 0 | 0 | 0 | (kosong) |
| var2016 | 525 | 525 | 525 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
