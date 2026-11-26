"""Volet A, étape 2a — téléchargement de GSE124897 depuis GEO (données publiques).

Télécharge, dans data/geo/GSE124897/raw/ (dossier local, ignoré par git) :
  - GSE124897_series_matrix.txt.gz : 889 biopsies, valeurs prétraitées par les auteurs
    (RMA, Bioconductor, d'après la fiche GEO), plateforme GPL15207 (PrimeView) ;
  - GPL15207_table.txt : table d'annotation des sondes (sonde → gène), pour plus tard.

Les fichiers bruts (CEL, 1,7 Go) ne sont pas téléchargés ici.

Provenance (adresse, date, taille, SHA-256) écrite dans
results/rmt_gse124897/telechargements.json (versionné, sans aucune donnée).

Les fichiers téléchargés sont des données non fiables : ils ne sont jamais exécutés,
seulement lus comme du texte par rmt_gse124897_02_split_qc.py (lancé avec python -I).

Usage : python -I scripts/rmt_gse124897_01_download.py [--force]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "geo" / "GSE124897" / "raw"
MANIFEST = ROOT / "results" / "rmt_gse124897" / "telechargements.json"

FILES = {
    "GSE124897_series_matrix.txt.gz":
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE124nnn/GSE124897/matrix/GSE124897_series_matrix.txt.gz",
    "GPL15207_table.txt":
        "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL15207&targ=self&form=text&view=data",
}
CEL_TAR = {"GSE124897_RAW.tar":
           "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE124nnn/GSE124897/suppl/GSE124897_RAW.tar"}
USER_AGENT = "geo-download-script"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    """Téléchargement par curl (certificats du système ; vérification TLS conservée)."""
    tmp = dest.with_suffix(dest.suffix + ".part")
    subprocess.run(["curl", "-fsSL", "--retry", "3", "-A", USER_AGENT, "-o", str(tmp), url],
                   check=True)
    tmp.rename(dest)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--force", action="store_true", help="retélécharger même si présent")
    ap.add_argument("--with-cel", action="store_true",
                    help="télécharger aussi l'archive des 889 fichiers CEL (1,7 Go, décision D1)")
    args = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    entries = dict(old.get("fichiers", {}))
    wanted = {**FILES, **(CEL_TAR if args.with_cel else {})}
    for name, url in wanted.items():
        dest = RAW / name
        if args.force or not dest.exists():
            print(f"téléchargement : {name}", flush=True)
            download(url, dest)
            when = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            print(f"déjà présent : {name}")
            when = old.get("fichiers", {}).get(name, {}).get("telecharge_le", "inconnu")
        entries[name] = {"url": url, "telecharge_le": when,
                         "octets": dest.stat().st_size, "sha256": sha256(dest)}
        print(f"  {entries[name]['octets'] / 1e6:.1f} Mo · sha256 {entries[name]['sha256'][:16]}…")
    MANIFEST.write_text(json.dumps({
        "jeu": "GSE124897 (GEO, public)",
        "note": "Fichiers dans data/geo/GSE124897/raw/ (local, non versionné).",
        "fichiers": entries,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"provenance : {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
