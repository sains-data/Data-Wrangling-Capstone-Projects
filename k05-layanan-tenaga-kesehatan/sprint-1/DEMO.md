# Naskah Demo Sprint 1 (±10 menit) — Kasus 05

Demo memperlihatkan alur yang bisa diulang, bukan tampilan yang cantik. Rekam layar terminal dan editor.

| Menit | Tunjukkan | Perintah atau berkas |
|---|---|---|
| 0–1 | Kasus dan Sprint Goal | `sprint/sprint-1/sprint-goal.md` |
| 1–2 | Data mentah lolos sha256 dari klon bersih | `python unduh_data.py --kasus 5` |
| 2–4 | Satu perintah dari mentah sampai Silver dan validasi | `python pipeline.py` (±2.3 detik) |
| 4–5 | Pemeriksa skema | `python -m src.common.skema data/silver/silver.parquet` → LOLOS 1.722 baris |
| 5–6 | Satu pembaca dan jumlah baris per berkas | `src/ekstraksi/`, `reports/ekstraksi.md` |
| 6–7 | Rincian profesi `var1477` dari `turvar`; satuan per 100.000 vs per 10.000 | `docs/data-dictionary.md` (kamus profesi), `docs/seri.csv` |
| 7–8 | Kode butir nasional (a); patahan unmet need 2021→2022 dan bidan 2016→2017 | `reports/metadata.md`, `reports/anomali.md` |
| 8–9 | Validasi dan tes baris yang sengaja dirusak | `reports/validasi.md`, `python -m pytest -q` |
| 9–10 | Satu baris Silver ditelusuri ke berkas mentah; rencana Sprint 2 | `docs/data-dictionary.md` bagian contoh penelusuran |

Uji reproduksi (tugas Reproduksi): klon repo ke folder baru, jalankan tiga perintah di atas, lalu
bandingkan `data/silver/silver.parquet` hasil jalan ulang dengan yang di-commit:

```bash
python - <<'EOF'
import pandas as pd
a = pd.read_parquet("data/silver/silver.parquet")
b = pd.read_parquet("/jalur/repo-asli/data/silver/silver.parquet")
print("sama" if a.equals(b) else "berbeda")
EOF
```

Catat waktu jalan di komentar tugas Reproduksi.
