"""Aturan khas Kasus 14 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_proyeksi_tak_terdaftar_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "SDG_0922_NOC_RT"].iloc[[0]].copy()
    baris["periode"] = "2028"
    assert not khusus.tahun_depan_terdaftar_proyeksi(pd.concat([silver_contoh, baris], ignore_index=True)).empty


def test_satuan_ganda_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var1214"][0], "satuan"] = "persen_per_tahun"
    assert not khusus.satu_satuan_per_seri_dan_rincian(rusak).empty
