"""Aturan validasi khas Kasus 10 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K

ILO = ["SDG_0552_NOC_RT", "SDG_T552_NOC_RT"]


def status_ilo_terdaftar(silver):
    """Setiap baris ILO punya status_obs yang terdaftar (STATUS_ILO) atau kosong."""
    s = silver[silver["sumber"] == "ilostat"]
    return s[s["status_obs"].notna() & ~s["status_obs"].isin(K.STATUS_ILO)][["seri_kode", "periode", "status_obs"]]


def dua_definisi_ilo_terpisah(silver):
    """Dua definisi ILO tidak berbagi seri_kode: setiap seri ILO berasal dari berkas dataflow-nya sendiri."""
    s = silver[silver["seri_kode"].isin(ILO)]
    salah = [k not in b for k, b in zip(s["seri_kode"], s["_berkas_raw"])]
    return s[salah][["seri_kode", "periode", "_berkas_raw"]]


def senior_tidak_melebihi_total(silver):
    """Manajer senior dan menengah perempuan (0552) tidak jauh melebihi seluruh manajemen (T552) pada tahun sama."""
    lebar = silver[silver["seri_kode"].isin(ILO)].pivot_table(index="periode", columns="seri_kode", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    return lebar[lebar["SDG_0552_NOC_RT"] > lebar["SDG_T552_NOC_RT"] + 1].reset_index()


def ilo_dekat_bps(silver):
    """Peringatan: ILO T552 berbeda > 5 poin dari BPS var2003 (Indonesia) pada tahun sama."""
    a = silver[(silver["seri_kode"] == "var2003") & (silver["wilayah_kode"] == 9999)].set_index("periode")["nilai"]
    b = silver[silver["seri_kode"] == "SDG_T552_NOC_RT"].set_index("periode")["nilai"]
    g = pd.DataFrame({"bps": a, "ilo_t552": b}).dropna()
    return g[(g["bps"] - g["ilo_t552"]).abs() > 5].reset_index()


ATURAN = [
    ("status_ilo_terdaftar", "status_obs ILO terdaftar (B) atau kosong", True, status_ilo_terdaftar),
    ("dua_definisi_ilo_terpisah", "dua definisi ILO dari berkas masing-masing", True, dua_definisi_ilo_terpisah),
    ("senior_tidak_melebihi_total", "0552 tidak melebihi T552 lebih dari 1 poin", True, senior_tidak_melebihi_total),
    ("ilo_dekat_bps", "ILO T552 vs BPS > 5 poin (peringatan)", False, ilo_dekat_bps),
]
