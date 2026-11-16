"""Aturan validasi khas Kasus 14 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def satu_satuan_per_seri_dan_rincian(silver):
    """Setiap seri_kode dan rincian punya satu satuan."""
    n = silver.groupby(["seri_kode", "rincian"])["satuan"].nunique()
    return n[n > 1].rename("satuan").reset_index()


def tahun_depan_terdaftar_proyeksi(silver):
    """Baris dengan tahun > tahun unduh harus terdaftar sebagai proyeksi."""
    tahun = silver["periode"].str[:4].astype(int)
    depan = silver[tahun > K.TAHUN_UNDUH]
    terdaftar = [p in K.PROYEKSI.get(s, set()) for s, p in zip(depan["seri_kode"], depan["periode"])]
    return depan[[not t for t in terdaftar]][["seri_kode", "periode", "nilai"]]


def satu_snapshot_per_seri(silver):
    """Setiap seri BPS dari satu berkas (snapshot terbaru)."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby("seri_kode")["_berkas_raw"].nunique()
    return n[n > 1].rename("berkas").reset_index()


def laju_provinsi_dekat_nasional(silver):
    """Peringatan: median laju produktivitas provinsi berbeda > 3 poin dari angka Indonesia pada tahun sama."""
    s = silver[silver["seri_kode"] == "var1161"]
    prov = s[s["wilayah_kode"] != 9999].groupby("periode")["nilai"].median()
    nas = s[s["wilayah_kode"] == 9999].set_index("periode")["nilai"]
    g = pd.DataFrame({"median_provinsi": prov.round(2), "indonesia": nas}).dropna()
    return g[(g["median_provinsi"] - g["indonesia"]).abs() > 3].reset_index()


ATURAN = [
    ("satu_satuan_per_seri_dan_rincian", "satu satuan per seri dan rincian", True, satu_satuan_per_seri_dan_rincian),
    ("tahun_depan_terdaftar_proyeksi", "tahun > 2026 terdaftar di PROYEKSI", True, tahun_depan_terdaftar_proyeksi),
    ("satu_snapshot_per_seri", "setiap seri BPS dari satu berkas", True, satu_snapshot_per_seri),
    ("laju_provinsi_dekat_nasional", "median laju provinsi vs Indonesia > 3 poin (peringatan)", False, laju_provinsi_dekat_nasional),
]
