"""Aturan khas Kasus 16 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_imputasi_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1254"].iloc[[0]].copy()
    baris["periode"] = "2017"
    assert not khusus.tanpa_imputasi(pd.concat([silver_contoh, baris], ignore_index=True)).empty


def test_layanan_tak_dikenal_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var2016"][0], "rincian"] = "total"
    assert not khusus.layanan_dari_kamus(rusak).empty
