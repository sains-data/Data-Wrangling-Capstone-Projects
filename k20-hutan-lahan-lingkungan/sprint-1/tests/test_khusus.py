"""Aturan khas Kasus 20 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_luas_negatif_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var588"][0], "nilai"] = -5.0
    assert not khusus.luas_tidak_negatif_satu_satuan(rusak).empty


def test_komponen_baru_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var2532"][0], "rincian"] = "komponen=iklh"
    assert not khusus.komponen_dari_kamus(rusak).empty


def test_jumlah_tidak_cocok_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "var588") & (rusak["rincian"] == "total")][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] * 2 + 100
    assert not khusus.jumlah_rincian_lahan(rusak).empty
