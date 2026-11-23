"""Aturan khas Kasus 11 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_triwulan_salah_jenis_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak.index[rusak["jenis_periode"] == "triwulan"][0], "jenis_periode"] = "tahun"
    assert not khusus.jenis_periode_sesuai_bentuk(rusak).empty


def test_rata_rata_tahunan_buatan_tertangkap(silver_contoh):
    baris = silver_contoh[(silver_contoh["seri_kode"] == "var543") & (silver_contoh["jenis_periode"] == "bulan")].iloc[[0]].copy()
    baris["periode"], baris["jenis_periode"] = "2019", "tahun"
    assert not khusus.bps_hanya_feb_agu_atau_tahun(pd.concat([silver_contoh, baris], ignore_index=True)).empty
