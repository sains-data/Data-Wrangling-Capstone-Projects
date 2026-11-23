"""Aturan validasi khas Kasus 09 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def satu_snapshot_per_seri(silver):
    """Setiap seri BPS hanya dari satu berkas (aturan pemilihan snapshot diterapkan konsisten)."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby("seri_kode")["_berkas_raw"].nunique()
    return n[n > 1].rename("berkas").reset_index()


def unik_per_provinsi_tahun(silver):
    """Setiap seri x provinsi x tahun muncul tepat satu kali (panel gabungan unik)."""
    b = silver[silver["sumber"] == "bps"]
    n = b.groupby(["seri_kode", "wilayah_kode", "periode"]).size()
    return n[n > 1].rename("jumlah").reset_index()


def tik_muda_tidak_lebih_rendah(silver):
    """Peringatan: keterampilan TIK umur 15–24 lebih rendah dari 15–59 pada provinsi dan tahun yang sama."""
    a = silver[silver["seri_kode"] == "var1451"].set_index(["wilayah_kode", "periode"])["nilai"]
    b = silver[silver["seri_kode"] == "var1447"].set_index(["wilayah_kode", "periode"])["nilai"]
    g = pd.DataFrame({"tik_15_24": a, "tik_15_59": b}).dropna()
    return g[g["tik_15_24"] < g["tik_15_59"]].reset_index()


def rse_tinggi(silver):
    """Peringatan: sel APK PAUD yang menurut var.note punya RSE 25–50 persen (pakai dengan hati-hati)."""
    kunci = list(zip(silver["seri_kode"], silver["wilayah_kode"], silver["periode"]))
    return silver[[k in K.RSE_TINGGI for k in kunci]][["seri_kode", "nama_wilayah", "periode", "nilai"]]


ATURAN = [
    ("satu_snapshot_per_seri", "setiap seri BPS dari satu berkas (snapshot terbaru)", True, satu_snapshot_per_seri),
    ("unik_per_provinsi_tahun", "seri x provinsi x tahun unik", True, unik_per_provinsi_tahun),
    ("tik_muda_tidak_lebih_rendah", "TIK 15–24 < TIK 15–59 pada sel yang sama (peringatan)", False, tik_muda_tidak_lebih_rendah),
    ("rse_tinggi", "sel APK PAUD dengan RSE 25–50% (peringatan: tandai di Gold)", False, rse_tinggi),
]
