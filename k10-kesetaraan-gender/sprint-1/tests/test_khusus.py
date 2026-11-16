"""Aturan khas Kasus 10 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_status_tak_dikenal_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["sumber"] == "ilostat"][0], "status_obs"] = "Z"
    assert not khusus.status_ilo_terdaftar(rusak).empty


def test_definisi_tertukar_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "SDG_0552_NOC_RT"][0], "seri_kode"] = "SDG_T552_NOC_RT"
    assert not khusus.dua_definisi_ilo_terpisah(rusak).empty
