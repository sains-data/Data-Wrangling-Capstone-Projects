"""Aturan khas Kasus 15 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_jumlah_desa_tidak_cocok_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "var2191") & (rusak["rincian"] == "total")][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] + 10
    assert not khusus.jumlah_desa_sama_rincian(rusak).empty


def test_desa_pecahan_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var2190"][0], "nilai"] = 12.5
    assert not khusus.jumlah_desa_bilangan_bulat(rusak).empty


def test_semester_salah_format_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["jenis_periode"] == "semester"][0], "periode"] = "2015"
    assert not khusus.semester_hanya_untuk_s1_s2(rusak).empty
