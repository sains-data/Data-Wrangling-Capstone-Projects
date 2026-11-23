"""Aturan khas Kasus 19 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_satuan_ton_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var2753"][0], "satuan"] = "ton"
    assert not khusus.bongkar_muat_seragam(rusak).empty


def test_total_buatan_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var2754"].iloc[[0]].copy()
    baris["rincian"] = "total"
    assert not khusus.arus_hanya_bongkar_muat(pd.concat([silver_contoh, baris], ignore_index=True)).empty
