"""Aturan khas Kasus 04 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_hipertensi_interpolasi_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var1480"].iloc[[0]].copy()
    baris["periode"] = "2010"
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.bps_hanya_tahun_terbit(rusak).empty


def test_proyeksi_tak_terdaftar_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "M_Est_tob_curr_std"].iloc[[0]].copy()
    baris["periode"] = "2035"
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.tahun_depan_terdaftar_proyeksi(rusak).empty


def test_satuan_malaria_disamakan_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    rusak.loc[rusak["seri_kode"] == "var1393", "satuan"] = "per_1000_penduduk_berisiko"
    assert not khusus.satuan_malaria_dibedakan(rusak).empty
