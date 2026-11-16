"""Aturan khas Kasus 17 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_kode_sdg_katalog_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak["seri_kode"] == "var847", "sdg_kode"] = "11.1.1"
    assert not khusus.tujuan_sdg_sesuai_nama_berkas(rusak).empty


def test_dua_tabel_berbeda_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "var2749"][0]
    rusak.loc[i, "nilai"] = rusak.loc[i, "nilai"] + 5
    assert not khusus.dua_tabel_sanitasi_aman_sama(rusak).empty


def test_total_di_luar_kota_desa_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == "var2179") & (rusak["rincian"] == "total")][0]
    rusak.loc[i, "nilai"] = 99.0
    assert not khusus.total_di_antara_kota_desa(rusak).empty
