"""Aturan khas Kasus 21 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_snapshot_ganda_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1311"].iloc[[0]].copy()
    baris["_berkas_raw"] = "bps/2026-10-17/json/sdg16_16_1_3_a_v1311.json"
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.satu_nilai_per_kunci(rusak).empty
    assert not khusus.satu_snapshot_per_seri(rusak).empty


def test_akta_tertukar_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["seri_kode"] == "var1831"][0], "seri_kode"] = "var1410"
    assert not khusus.akta_dua_seri_terpisah(rusak).empty
