"""Aturan validasi khas Kasus 04 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K
from src import wilayah as W


def bps_hanya_tahun_terbit(silver):
    """Tidak ada baris BPS di luar tahun terbit (hipertensi tidak diisi pada tahun antarsurvei)."""
    b = silver[silver["sumber"] == "bps"]
    terbit = [p in K.TAHUN_TERBIT.get(s, set()) for s, p in zip(b["seri_kode"], b["periode"])]
    return b[[not t for t in terbit]][["seri_kode", "wilayah_kode", "periode", "nilai"]]


def tahun_depan_terdaftar_proyeksi(silver):
    """Setiap baris dengan tahun sesudah tahun unduh harus terdaftar sebagai proyeksi di konfigurasi."""
    tahun = silver["periode"].str[:4].astype(int)
    depan = silver[tahun > K.TAHUN_UNDUH]
    terdaftar = [p in K.PROYEKSI.get(s, set()) for s, p in zip(depan["seri_kode"], depan["periode"])]
    return depan[[not t for t in terdaftar]][["seri_kode", "periode", "nilai"]]


def satuan_malaria_dibedakan(silver):
    """Malaria BPS (per seluruh penduduk) tidak boleh bersatuan sama dengan WHO/WDI (per penduduk berisiko)."""
    m = silver[silver["seri_kode"].isin(["var1393", "MALARIA_EST_INCIDENCE", "SH.MLR.INCD.P3"])]
    harus = {"var1393": "per_1000_penduduk", "MALARIA_EST_INCIDENCE": "per_1000_penduduk_berisiko",
             "SH.MLR.INCD.P3": "per_1000_penduduk_berisiko"}
    return m[m["satuan"] != m["seri_kode"].map(harus)][["seri_kode", "periode", "satuan"]]


def lonjakan_malaria(silver):
    """Peringatan: kejadian malaria satu provinsi berubah lebih dari 10 kali lipat antartahun berurutan."""
    m = silver[(silver["seri_kode"] == "var1393") & (silver["wilayah_kode"] != W.INDONESIA)]
    lebar = m.pivot_table(index="wilayah_kode", columns="periode", values="nilai").sort_index(axis=1)
    baris = []
    per = list(lebar.columns)
    for a, b in zip(per, per[1:]):
        rasio = (lebar[b] / lebar[a]).dropna()
        for w, r in rasio[(rasio > 10) | (rasio < 0.1)].items():
            baris.append({"nama_wilayah": W.NAMA[w], "dari": a, "ke": b, "nilai_dari": f"{lebar.loc[w, a]:.3f}",
                          "nilai_ke": f"{lebar.loc[w, b]:.3f}", "rasio": f"{r:.2f}"})
    return pd.DataFrame(baris)


ATURAN = [
    ("bps_hanya_tahun_terbit", "tidak ada tahun BPS di luar tahun terbit (tidak ada interpolasi)", True, bps_hanya_tahun_terbit),
    ("tahun_depan_terdaftar_proyeksi", "baris dengan tahun > 2026 terdaftar di PROYEKSI", True, tahun_depan_terdaftar_proyeksi),
    ("satuan_malaria_dibedakan", "malaria BPS per 1.000 penduduk, WHO/WDI per 1.000 penduduk berisiko", True, satuan_malaria_dibedakan),
    ("lonjakan_malaria", "kejadian malaria provinsi berubah > 10 kali lipat antartahun (peringatan: galat atau nyata?)", False,
     lonjakan_malaria),
]
