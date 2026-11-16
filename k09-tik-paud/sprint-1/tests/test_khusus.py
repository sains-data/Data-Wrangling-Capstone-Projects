"""Aturan khas Kasus 09 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_dua_snapshot_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1221"].iloc[[0]].copy()
    baris["_berkas_raw"] = "bps/2026-10-17/json/sdg5_5_b_1_v1221.json"
    baris["periode"] = "2014"
    assert not khusus.satu_snapshot_per_seri(pd.concat([silver_contoh, baris], ignore_index=True)).empty


def test_sel_ganda_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1221"].iloc[[0]].copy()
    baris["_berkas_raw"] = "bps/2026-10-17/json/sdg5_5_b_1_v1221.json"
    assert not khusus.unik_per_provinsi_tahun(pd.concat([silver_contoh, baris], ignore_index=True)).empty
