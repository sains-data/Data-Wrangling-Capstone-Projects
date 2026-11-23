"""Aturan khas Kasus 13 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_umur_tak_terdaftar_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "SDG_A871_SEX_AGE_RT"][0]
    rusak.loc[i, "rincian"] = rusak.loc[i, "rincian"].replace("CLDVERSION_Y15-17", "Y5-17")
    assert not khusus.umur_anak_dari_kamus(rusak).empty


def test_b871_lebih_kecil_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "SDG_B871_SEX_AGE_RT"][0]
    rusak.loc[i, "nilai"] = 0.1
    assert not khusus.b871_tidak_di_bawah_a871(rusak).empty
