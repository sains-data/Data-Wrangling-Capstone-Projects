"""Aturan validasi khas Kasus 06 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def satu_total_kanonik(silver):
    """Setiap provinsi x tahun punya tepat satu angka total kanonik (var1458)."""
    s = silver[(silver["seri_kode"] == "var1458") & (silver["rincian"] == "total")]
    n = s.groupby(["wilayah_kode", "periode"]).size()
    return n[n > 1].rename("jumlah").reset_index()


def rincian_konsisten_per_provinsi(silver):
    """Tabel rinci: susunan rincian satu provinsi sama di semua tahunnya (9, atau 6 untuk provinsi tanpa
    perdesaan seperti DKI Jakarta). Rincian yang hilang di sebagian tahun saja berarti salah baca."""
    s = silver[silver["seri_kode"] == K.RINCI]
    n = s.groupby(["wilayah_kode", "periode"])["rincian"].nunique().rename("rincian").reset_index()
    ragam = n.groupby("wilayah_kode")["rincian"].transform("nunique")
    return n[(ragam > 1) | ~n["rincian"].isin([6, 9])]


def total_di_antara_kota_desa(silver):
    """Angka total tabel rinci berada di antara perkotaan dan perdesaan (toleransi 0,05 poin)."""
    s = silver[silver["seri_kode"] == K.RINCI]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai")
    kol = ["daerah=URBAN", "daerah=RURAL", "total"]
    lebar = lebar[[k for k in kol if k in lebar]].dropna()
    if len(lebar.columns) < 3:
        return pd.DataFrame()
    lo = lebar[kol[:2]].min(axis=1) - 0.05
    hi = lebar[kol[:2]].max(axis=1) + 0.05
    return lebar[(lebar["total"] < lo) | (lebar["total"] > hi)].reset_index()


def total_rinci_sama_ringkas(silver):
    """Peringatan: total tabel rinci berbeda dari var1458 pada provinsi dan tahun yang sama (> 0,005 poin)."""
    a = silver[(silver["seri_kode"] == "var1458")].set_index(["wilayah_kode", "periode"])["nilai"]
    b = silver[(silver["seri_kode"] == K.RINCI) & (silver["rincian"] == "total")].set_index(["wilayah_kode", "periode"])["nilai"]
    g = pd.DataFrame({"ringkas": a, "rinci": b}).dropna()
    g["selisih"] = (g["rinci"] - g["ringkas"]).round(3)
    return g[g["selisih"].abs() > 0.005].reset_index()


ATURAN = [
    ("satu_total_kanonik", "setiap provinsi x tahun tepat satu angka total kanonik (var1458)", True, satu_total_kanonik),
    ("rincian_konsisten_per_provinsi", "tabel rinci: susunan rincian sama di semua tahun satu provinsi (9, atau 6 tanpa perdesaan)",
     True, rincian_konsisten_per_provinsi),
    ("total_di_antara_kota_desa", "total tabel rinci di antara perkotaan dan perdesaan", True, total_di_antara_kota_desa),
    ("total_rinci_sama_ringkas", "total tabel rinci ≠ var1458 pada sel yang sama (peringatan: dilaporkan, tidak disamakan)", False,
     total_rinci_sama_ringkas),
]
