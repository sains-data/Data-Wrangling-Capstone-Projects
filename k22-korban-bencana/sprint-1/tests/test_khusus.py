"""Aturan khas Kasus 22 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_keras_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_pecahan_pada_cacah_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "korban_meninggal"][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] + 0.5
    assert len(khusus.cacah_bilangan_bulat(rusak)) == 1


def test_jenis_tidak_menjumlah_ke_total_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    total = rusak[(rusak["rincian"] == "total") & (rusak["seri_kode"] == "kejadian") & (rusak["wilayah_kode"] == 9999)]
    berkas = total["_berkas_raw"].iloc[0]
    i = rusak.index[(rusak["_berkas_raw"] == berkas) & (rusak["rincian"] == "jenis_bencana=banjir")
                    & (rusak["seri_kode"] == "kejadian")][0]
    rusak.loc[i, "nilai"] += 1
    assert not khusus.jenis_menjumlah_ke_total(rusak).empty


def test_per_100rb_salah_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "korban_mengungsi_per_100rb") & (rusak["rincian"] == "jenis_bencana=banjir")
                    & (rusak["wilayah_kode"] == 1100)][0]
    rusak.loc[i, "nilai"] *= 1.1
    assert len(khusus.per_100rb_dihitung_ulang(rusak)) == 1


def test_peringatan_kabkota_menemukan_kasus_nyata(silver_contoh):
    # Tanah longsor 2024 masuk DKI Jakarta di tabel provinsi tetapi kab/kota Jawa Barat di tabel kab/kota
    kej = khusus.kejadian_kabkota_tidak_kurang(silver_contoh)
    korban = khusus.korban_kabkota_sama_provinsi(silver_contoh)
    assert set(kej["wilayah_kode"]) == {3100}
    assert set(korban["wilayah_kode"]) == {3100, 3200}


def test_nilai_kabkota_dijumlah_bukan_baris_pertama(silver_contoh):
    # rekap kab/kota 2021: Aceh banjir dari semua kab/kota = rekap provinsi (100), bukan satu kab/kota pertama
    s = silver_contoh
    pilih = (s["seri_kode"] == "kejadian") & (s["wilayah_kode"] == 1100) & (s["periode"] == "2021") \
        & (s["rincian"] == "jenis_bencana=banjir")
    kab = s[pilih & s["_berkas_raw"].str.contains("per-kabupaten-kota")]["nilai"]
    prov = s[pilih & s["_berkas_raw"].str.contains("2021-per-provinsi")]["nilai"]
    assert list(kab) == list(prov) == [100.0]


def test_peringatan_indonesia_menemukan_salah_ketik(silver_contoh):
    # tanah longsor 2024: baris INDONESIA tabel provinsi 27, tabel nasional dan kab/kota 207 (= jumlah 38 provinsi)
    g = khusus.indonesia_sama_lintas_berkas(silver_contoh)
    assert len(g) == 1 and (g["min"].iloc[0], g["max"].iloc[0]) == (27.0, 207.0)
