"""Aturan khas Kasus 05 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_profesi_baru_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "var1477"][0]
    rusak.loc[i, "rincian"] = "profesi=dokter"
    assert not khusus.profesi_dari_kamus(rusak).empty


def test_satuan_tercampur_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == "var1477"][0]
    rusak.loc[i, "satuan"] = "per_10000_penduduk"
    assert not khusus.kepadatan_dua_satuan_terpisah(rusak).empty


def test_jkn_imputasi_belakang_tertangkap(silver_contoh):
    baris = silver_contoh[silver_contoh["seri_kode"] == "var2279"].iloc[[0]].copy()
    baris["periode"] = "2021"
    rusak = pd.concat([silver_contoh, baris], ignore_index=True)
    assert not khusus.jkn_tidak_sebelum_terbit(rusak).empty
