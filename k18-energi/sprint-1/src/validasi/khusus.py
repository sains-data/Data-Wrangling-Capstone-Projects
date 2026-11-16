"""Aturan validasi khas Kasus 18 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def jumlah_bahan_bakar_mendekati_100(silver):
    """Jumlah enam jenis bahan bakar per provinsi x tahun berada di 99–101 persen (pembulatan)."""
    s = silver[(silver["seri_kode"] == K.BB) & (silver["rincian"] != "total")]
    j = s.groupby(["wilayah_kode", "periode"])["nilai"].sum()
    return j[(j < 99) | (j > 101)].round(2).rename("jumlah").reset_index()


def setiap_jenis_punya_kategori(silver):
    """Setiap jenis bahan bakar terpetakan ke tepat satu kategori (bersih, tidak bersih, tidak ditentukan)."""
    s = silver[(silver["seri_kode"] == K.BB) & (silver["rincian"] != "total")]
    jenis = s["rincian"].str.split("=").str[1]
    return s[~jenis.isin(K.KATEGORI_BAHAN_BAKAR)][["periode", "wilayah_kode", "rincian"]]


def total_tabel_100(silver):
    """Rincian jumlah tabel bahan bakar = 100 (toleransi 0,05)."""
    s = silver[(silver["seri_kode"] == K.BB) & (silver["rincian"] == "total")]
    return s[(s["nilai"] - 100).abs() > 0.05][["wilayah_kode", "periode", "nilai"]]


def pln_tidak_melebihi_akses(silver):
    """Peringatan: listrik PLN (rumah tangga) Indonesia melebihi akses listrik WDI (semua sumber) pada tahun sama."""
    a = silver[(silver["seri_kode"] == "var87") & (silver["wilayah_kode"] == 9999)].set_index("periode")["nilai"]
    b = silver[silver["seri_kode"] == "EG.ELC.ACCS.ZS"].set_index("periode")["nilai"]
    g = pd.DataFrame({"pln": a, "akses": b}).dropna()
    return g[g["pln"] > g["akses"]].reset_index()


ATURAN = [
    ("jumlah_bahan_bakar_mendekati_100", "jumlah enam jenis bahan bakar 99–101%", True, jumlah_bahan_bakar_mendekati_100),
    ("setiap_jenis_punya_kategori", "setiap jenis bahan bakar punya satu kategori", True, setiap_jenis_punya_kategori),
    ("total_tabel_100", "rincian jumlah tabel bahan bakar = 100", True, total_tabel_100),
    ("pln_tidak_melebihi_akses", "PLN Indonesia > akses listrik WDI (peringatan)", False, pln_tidak_melebihi_akses),
]
