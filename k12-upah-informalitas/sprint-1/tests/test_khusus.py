"""Aturan khas Kasus 12 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_upah_negatif_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var1172"][0], "nilai"] = -1.0
    assert not khusus.upah_positif_satu_satuan(rusak).empty


def test_total_klasifikasi_berbeda_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "SDG_0831_SEX_ECO_RT") & (rusak["rincian"] == "sektor=AGGREGATE_TOTAL")][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] + 3
    assert not khusus.total_klasifikasi_lain_sama(rusak).empty
