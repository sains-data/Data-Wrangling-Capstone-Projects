"""Aturan khas Kasus 08 diuji dengan baris yang sengaja dirusak."""
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_rasio_persen_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var2600"][0], "nilai"] = 0.95   # skala x1 tercampur di seri x100
    assert not khusus.rasio_paritas_masuk_akal(rusak).empty


def test_satuan_tidak_ada_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak["seri_kode"] == "var304", "satuan"] = "tidak_ada"
    assert not khusus.satu_satuan_per_jenis(rusak).empty


def test_sma_melebihi_sd_memicu_peringatan(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "var1980") & (rusak["rincian"] == "jenjang=sma")][0]
    rusak.loc[i, "nilai"] = 100.0
    assert not khusus.penyelesaian_sma_tidak_melebihi_sd(rusak).empty
