"""Aturan validasi khas Kasus 19 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import wilayah as W

ARUS = ["var2753", "var2754"]


def bongkar_muat_seragam(silver):
    """Bongkar muat tidak negatif dan bersatuan kilogram."""
    s = silver[silver["seri_kode"].isin(ARUS)]
    return s[(s["nilai"] < 0) | (s["satuan"] != "kilogram")][["seri_kode", "wilayah_kode", "periode", "nilai", "satuan"]]


def arus_hanya_bongkar_muat(silver):
    """Rincian seri bongkar muat hanya arus=bongkar atau arus=muat (tidak ada total buatan)."""
    s = silver[silver["seri_kode"].isin(ARUS)]
    return s[~s["rincian"].isin(["arus=bongkar", "arus=muat"])][["seri_kode", "periode", "rincian"]]


def satu_snapshot_per_seri(silver):
    """Setiap seri BPS dari satu berkas (snapshot terbaru)."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby("seri_kode")["_berkas_raw"].nunique()
    return n[n > 1].rename("berkas").reset_index()


def jumlah_provinsi_dekat_indonesia(silver):
    """Peringatan: jumlah provinsi bongkar muat berbeda > 1% dari baris Indonesia (seri x arus x tahun)."""
    s = silver[silver["seri_kode"].isin(ARUS)]
    prov = s[s["wilayah_kode"] != W.INDONESIA].groupby(["seri_kode", "rincian", "periode"])["nilai"].sum()
    nas = s[s["wilayah_kode"] == W.INDONESIA].set_index(["seri_kode", "rincian", "periode"])["nilai"]
    g = pd.DataFrame({"jumlah_provinsi": prov, "indonesia": nas}).dropna()
    g["selisih_relatif"] = ((g["jumlah_provinsi"] - g["indonesia"]) / g["indonesia"]).round(4)
    return g[g["selisih_relatif"].abs() > 0.01].reset_index()


ATURAN = [
    ("bongkar_muat_seragam", "bongkar muat >= 0 dan bersatuan kilogram", True, bongkar_muat_seragam),
    ("arus_hanya_bongkar_muat", "rincian bongkar muat hanya bongkar/muat", True, arus_hanya_bongkar_muat),
    ("satu_snapshot_per_seri", "setiap seri BPS dari satu berkas", True, satu_snapshot_per_seri),
    ("jumlah_provinsi_dekat_indonesia", "jumlah provinsi bongkar muat ≠ Indonesia > 1% (peringatan)", False,
     jumlah_provinsi_dekat_indonesia),
]
