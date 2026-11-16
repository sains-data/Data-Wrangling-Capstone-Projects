"""Aturan validasi khas Kasus 01 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K
from src import wilayah as W

UTAMA = ["var1473", "var1474"]


def satu_baris_per_provinsi_tahun(silver):
    """Setiap seri BPS x wilayah x tahun (rincian total) muncul tepat satu kali."""
    b = silver[silver["seri_kode"].isin(UTAMA) & (silver["rincian"] == "total")]
    n = b.groupby(["seri_kode", "wilayah_kode", "periode"]).size()
    return n[n > 1].rename("jumlah").reset_index()


def who_satu_total_per_tahun(silver):
    """Setiap seri WHO punya paling banyak satu baris rincian total per tahun (duplikat setara sudah dibuang)."""
    w = silver[(silver["sumber"] == "who_gho") & (silver["rincian"] == "total")]
    n = w.groupby(["seri_kode", "periode"]).size()
    return n[n > 1].rename("jumlah").reset_index()


def tidak_ada_angka_sensor(silver):
    """Nilai WDI pada batas sensor (2.5 = 'kurang dari 2,5%') tidak boleh masuk sebagai angka pasti."""
    buruk = []
    for seri, batas in K.SENSOR_WDI.items():
        s = silver[(silver["seri_kode"] == seri) & (silver["nilai"] <= batas)]
        buruk.append(s[["seri_kode", "periode", "nilai"]])
    return pd.concat(buruk, ignore_index=True)


def bps_wdi_pou_berdekatan(silver):
    """Peringatan: PoU Indonesia BPS (var1473) dan WDI berbeda lebih dari 2 poin persentase pada tahun yang sama."""
    s = silver[silver["seri_kode"].isin(["var1473", "SN.ITK.DEFC.ZS"]) & (silver["wilayah_kode"] == W.INDONESIA)
               & (silver["rincian"] == "total")]
    lebar = s.pivot_table(index="periode", columns="seri_kode", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    beda = lebar["var1473"] - lebar["SN.ITK.DEFC.ZS"]
    return lebar[beda.abs() > 2].assign(selisih_poin=beda[beda.abs() > 2].round(2)).reset_index()


ATURAN = [
    ("satu_baris_per_provinsi_tahun", "setiap seri BPS × wilayah × tahun muncul tepat satu kali", True,
     satu_baris_per_provinsi_tahun),
    ("who_satu_total_per_tahun", "setiap seri WHO × tahun punya paling banyak satu baris rincian total", True,
     who_satu_total_per_tahun),
    ("tidak_ada_angka_sensor", "tidak ada nilai SN.ITK.DEFC.ZS ≤ 2,5 yang terbaca sebagai angka pasti", True,
     tidak_ada_angka_sensor),
    ("bps_wdi_pou_berdekatan", "PoU Indonesia BPS vs WDI berbeda > 2 poin (peringatan: periksa metode, bukan galat)", False,
     bps_wdi_pou_berdekatan),
]
