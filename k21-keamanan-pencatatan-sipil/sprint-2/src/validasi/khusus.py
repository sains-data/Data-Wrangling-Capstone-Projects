"""Aturan validasi khas Kasus 21 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd


def satu_nilai_per_kunci(silver):
    """Setiap seri x provinsi x tahun punya satu nilai setelah aturan snapshot diterapkan."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby(["seri_kode", "wilayah_kode", "periode"]).size()
    return n[n > 1].rename("jumlah").reset_index()


def satu_snapshot_per_seri(silver):
    """Setiap seri BPS dari satu berkas (snapshot terbaru)."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby("seri_kode")["_berkas_raw"].nunique()
    return n[n > 1].rename("berkas").reset_index()


def akta_dua_seri_terpisah(silver):
    """Dua seri akta kelahiran (balita dan 0–17) tidak pernah tergabung dalam satu seri_kode."""
    s = silver[silver["seri_kode"].isin(["var1410", "var1831"])]
    salah = s[s["_berkas_raw"].str.contains("v1410") != (s["seri_kode"] == "var1410")]
    return salah[["seri_kode", "periode", "_berkas_raw"]]


def akta_anak_tidak_di_bawah_balita(silver):
    """Peringatan: akta anak 0–17 lebih rendah dari balita pada provinsi dan tahun yang sama."""
    a = silver[silver["seri_kode"] == "var1410"].set_index(["wilayah_kode", "periode"])["nilai"]
    b = silver[silver["seri_kode"] == "var1831"].set_index(["wilayah_kode", "periode"])["nilai"]
    g = pd.DataFrame({"balita": a, "anak_0_17": b}).dropna()
    return g[g["anak_0_17"] < g["balita"]].reset_index()


ATURAN = [
    ("satu_nilai_per_kunci", "seri x provinsi x tahun satu nilai", True, satu_nilai_per_kunci),
    ("satu_snapshot_per_seri", "setiap seri BPS dari satu berkas", True, satu_snapshot_per_seri),
    ("akta_dua_seri_terpisah", "seri akta balita dan 0–17 tidak tertukar", True, akta_dua_seri_terpisah),
    ("akta_anak_tidak_di_bawah_balita", "akta 0–17 < balita (peringatan)", False, akta_anak_tidak_di_bawah_balita),
]
