# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var1373 | — | 0 |  |  | tidak dapat diuji | hanya 1 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| var1584 | — | 0 |  |  | tidak dapat diuji | hanya 1 periode; pola serentak dari dua titik tidak bisa dibedakan dari perubahan sungguhan |
| var1541 | 2015→2016 | 34 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1541 | 2016→2017 | 34 | 0.06 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1541 | 2017→2018 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var1541 | 2018→2019 | 34 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 0

Tidak ada: tidak ada provinsi pemekaran yang mulai terbit di tengah panel seri provinsi.

## Calon anomali dan kategorinya (5)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var1373 | Papua Barat | 2012 | 109.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1373 | Papua | 2012 | 115.00 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1541 | Papua Barat | 2017 | 38.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var1541 | Maluku | 2019 | 22.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var1541 | Maluku Utara | 2019 | 41.32 | perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var1373 | 35 | 35 | 35 | 0 | 0 | 0 | (kosong) |
| var1541 | 175 | 175 | 175 | 0 | 0 | 0 | Persen |
| var1584 | 35 | 35 | 35 | 0 | 0 | 0 | (kosong) |

## Kunci Silver kembar: 0
