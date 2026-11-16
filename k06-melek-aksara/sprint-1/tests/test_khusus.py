"""Aturan khas Kasus 06 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src import konfigurasi as K
from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_total_ganda_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1458"].iloc[[0]].copy()
    baris["_berkas_raw"] = "bps/2026-10-17/sdg4_amh.csv"
    assert not khusus.satu_total_kanonik(pd.concat([silver_contoh, baris], ignore_index=True)).empty


def test_rincian_hilang_tertangkap(silver_contoh):
    i = silver_contoh.index[silver_contoh["seri_kode"] == K.RINCI][0]
    assert not khusus.rincian_konsisten_per_provinsi(silver_contoh.drop(index=i)).empty


def test_total_di_luar_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == K.RINCI) & (rusak["rincian"] == "total")][0]
    rusak.loc[i, "nilai"] = 10.0
    assert not khusus.total_di_antara_kota_desa(rusak).empty
