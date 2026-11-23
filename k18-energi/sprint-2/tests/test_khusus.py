"""Aturan khas Kasus 18 diuji dengan baris yang sengaja dirusak."""
from src import konfigurasi as K
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_jumlah_tidak_100_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == K.BB) & (rusak["rincian"] == "bahan_bakar=kayu")][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] + 10
    assert not khusus.jumlah_bahan_bakar_mendekati_100(rusak).empty


def test_jenis_tanpa_kategori_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[(rusak["seri_kode"] == K.BB) & (rusak["rincian"] != "total")][0], "rincian"] = "bahan_bakar=batubara"
    assert not khusus.setiap_jenis_punya_kategori(rusak).empty
