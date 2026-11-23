"""Aturan khas Kasus 01 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_provinsi_tahun_kembar_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1473"].iloc[[0]].copy()
    baris["_berkas_raw"] = "bps/2026-10-20/sdg2_2_1_1_v1473.csv"     # CSV ikut masuk Silver
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.satu_baris_per_provinsi_tahun(rusak).empty


def test_total_who_kembar_tertangkap(silver_contoh):
    baris = silver_contoh[(silver_contoh["seri_kode"] == "NUTRITION_WH_2") & (silver_contoh["rincian"] == "total")].iloc[[0]].copy()
    baris["rincian"] = "total"
    baris["_berkas_raw"] = baris["_berkas_raw"] + "#salinan"
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.who_satu_total_per_tahun(rusak).empty


def test_angka_sensor_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "SN.ITK.DEFC.ZS"][0]
    rusak.loc[i, "nilai"] = 2.5
    assert not khusus.tidak_ada_angka_sensor(rusak).empty
