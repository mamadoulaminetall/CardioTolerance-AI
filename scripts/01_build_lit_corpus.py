"""01 — Construction du corpus bibliographique (PubMed E-utilities).

Exécute un jeu de requêtes PubMed **figées et journalisées** (blocs de mots-clés du brief
§2 / section_04 §4.3), dédoublonne par PMID, récupère titre + résumé + métadonnées via
efetch, et écrit :

  meta-analysis/data/query_log.csv   une ligne par requête (chaîne exacte, count, date)
  meta-analysis/data/lit_corpus.csv  une ligne par article unique (pmid, doi, year,
                                     journal, title, abstract, query_ids)

Aucune donnée inventée : tout vient de l'API NCBI. Read-only. Sans clé API → ~3 req/s.

Usage : python scripts/01_build_lit_corpus.py
"""

from __future__ import annotations

import csv
import datetime as dt
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "meta-analysis" / "data"
OUTDIR.mkdir(parents=True, exist_ok=True)

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "CardioTolerance-AI"
EMAIL = "contact@medflow-ai.fr"
SLEEP = 0.4  # s entre requêtes (respect du quota NCBI sans clé)

TIAB = "[Title/Abstract]"

# Blocs (OR intra-bloc). On combine ensuite en AND entre blocs.
A_HEART = f'("heart transplantation"{TIAB} OR "cardiac allograft"{TIAB} OR "heart transplant recipients"{TIAB})'
A_TOL = (f'("operational tolerance"{TIAB} OR "immune tolerance"{TIAB} OR "immunological tolerance"{TIAB} '
         f'OR "spontaneous tolerance"{TIAB} OR "allograft tolerance"{TIAB} OR "rejection-free"{TIAB} '
         f'OR "immunosuppression withdrawal"{TIAB} OR "immunosuppression minimization"{TIAB} '
         f'OR "long-term survivors"{TIAB})')
B_IMMUNE = (f'("regulatory T cells"{TIAB} OR "Treg"{TIAB} OR "regulatory B cells"{TIAB} OR "T-cell exhaustion"{TIAB} '
            f'OR "TCR sequencing"{TIAB} OR "T-cell repertoire"{TIAB} OR "BCR sequencing"{TIAB} '
            f'OR "donor-specific antibodies"{TIAB} OR "HLA molecular mismatch"{TIAB} OR "mass cytometry"{TIAB} '
            f'OR "immune transcriptomics"{TIAB})')
C_OMICS = (f'("RNA-seq"{TIAB} OR "single-cell RNA"{TIAB} OR "scRNA-seq"{TIAB} OR "spatial transcriptomics"{TIAB} '
           f'OR "proteomics"{TIAB} OR "metabolomics"{TIAB} OR "methylation"{TIAB} OR "multi-omics"{TIAB} '
           f'OR "multiomics"{TIAB} OR "longitudinal omics"{TIAB} OR "gene expression profiling"{TIAB})')
D_AI = (f'("machine learning"{TIAB} OR "deep learning"{TIAB} OR "artificial intelligence"{TIAB} '
        f'OR "random forest"{TIAB} OR "survival model"{TIAB} OR "multimodal"{TIAB} OR "explainable AI"{TIAB} '
        f'OR "biomarker discovery"{TIAB} OR "rejection prediction"{TIAB} OR "outcome prediction"{TIAB})')
E_DDCFDNA = (f'("donor-derived cell-free DNA"{TIAB} OR "dd-cfDNA"{TIAB} OR "cell-free DNA"{TIAB} OR "cfDNA"{TIAB})')
F_REJ = (f'("rejection"{TIAB} OR "endomyocardial biopsy"{TIAB} OR "antibody-mediated rejection"{TIAB} '
         f'OR "cardiac allograft vasculopathy"{TIAB})')

QUERIES = {
    "Q1_heart_tolerance": f"{A_HEART} AND {A_TOL}",
    "Q2_heart_tol_immune": f"{A_HEART} AND {A_TOL} AND {B_IMMUNE}",
    "Q3_heart_tol_omics": f"{A_HEART} AND {A_TOL} AND {C_OMICS}",
    "Q4_heart_tol_ai": f"{A_HEART} AND {A_TOL} AND {D_AI}",
    "Q5_heart_omics_ai_rejection": f"{A_HEART} AND {C_OMICS} AND {D_AI} AND {F_REJ}",
    "Q6_heart_ddcfdna_rejection": f"{A_HEART} AND {E_DDCFDNA} AND {F_REJ}",
    "Q7_heart_immune_signature_rejection": f"{A_HEART} AND {B_IMMUNE} AND {C_OMICS} AND {F_REJ}",
    "Q8_heart_tcr_bcr": f"{A_HEART} AND (\"TCR repertoire\"{TIAB} OR \"BCR repertoire\"{TIAB} OR \"clonal deletion\"{TIAB} OR \"donor-reactive\"{TIAB})",
}


def _get(url: str) -> bytes:
    # curl plutôt qu'urllib : l'environnement de dev intercale un proxy TLS
    # (cert self-signed) qui fait échouer la vérification urllib.
    res = subprocess.run(
        ["curl", "-sS", "--max-time", "40", "-A", f"{TOOL} ({EMAIL})", url],
        capture_output=True, check=True,
    )
    return res.stdout


def esearch(term: str, retmax: int = 1000) -> tuple[int, list[str]]:
    q = urllib.parse.urlencode({
        "db": "pubmed", "term": term, "retmode": "json", "retmax": retmax,
        "tool": TOOL, "email": EMAIL,
    })
    import json
    data = json.loads(_get(f"{EUTILS}/esearch.fcgi?{q}"))
    res = data.get("esearchresult", {})
    return int(res.get("count", 0)), res.get("idlist", [])


def efetch(pmids: list[str]) -> list[dict]:
    out = []
    for i in range(0, len(pmids), 200):
        batch = pmids[i:i + 200]
        q = urllib.parse.urlencode({
            "db": "pubmed", "id": ",".join(batch), "retmode": "xml",
            "tool": TOOL, "email": EMAIL,
        })
        root = ET.fromstring(_get(f"{EUTILS}/efetch.fcgi?{q}"))
        for art in root.findall(".//PubmedArticle"):
            mc = art.find(".//MedlineCitation")
            pmid = (mc.findtext("PMID") or "").strip()
            title = " ".join((mc.findtext(".//ArticleTitle") or "").split())
            abst = " ".join(
                " ".join((t.text or "").split())
                for t in mc.findall(".//Abstract/AbstractText")
            ).strip()
            journal = (mc.findtext(".//Journal/ISOAbbreviation")
                       or mc.findtext(".//Journal/Title") or "").strip()
            year = (mc.findtext(".//JournalIssue/PubDate/Year")
                    or (mc.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]).strip()
            doi = ""
            for aid in art.findall(".//ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = (aid.text or "").strip()
            out.append(dict(pmid=pmid, doi=doi, year=year, journal=journal,
                            title=title, abstract=abst))
        time.sleep(SLEEP)
    return out


def main() -> None:
    today = dt.date.today().isoformat()
    log_rows = []
    hits: dict[str, set[str]] = {}
    for qid, term in QUERIES.items():
        try:
            total, ids = esearch(term)
        except Exception as e:  # noqa: BLE001
            log_rows.append(dict(query_id=qid, date=today, count="ERROR", retrieved="0",
                                 error=str(e), term=term))
            print(f"{qid}: ERREUR {e}")
            time.sleep(SLEEP)
            continue
        log_rows.append(dict(query_id=qid, date=today, count=total, retrieved=len(ids),
                             error="", term=term))
        print(f"{qid}: {total} hits (récupérés : {len(ids)})")
        for pid in ids:
            hits.setdefault(pid, set()).add(qid)
        time.sleep(SLEEP)

    with (OUTDIR / "query_log.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["query_id", "date", "count", "retrieved",
                                           "error", "term"])
        w.writeheader()
        w.writerows(log_rows)

    all_pmids = sorted(hits)
    print(f"\n{len(all_pmids)} PMIDs uniques → efetch…")
    records = efetch(all_pmids) if all_pmids else []
    for r in records:
        r["query_ids"] = ";".join(sorted(hits.get(r["pmid"], [])))

    records.sort(key=lambda r: (r["year"] or "0"), reverse=True)
    with (OUTDIR / "lit_corpus.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["pmid", "doi", "year", "journal", "title",
                                           "abstract", "query_ids"])
        w.writeheader()
        w.writerows(records)

    print(f"Écrit : {(OUTDIR / 'query_log.csv').relative_to(ROOT)} ({len(log_rows)} requêtes)")
    print(f"Écrit : {(OUTDIR / 'lit_corpus.csv').relative_to(ROOT)} ({len(records)} articles)")


if __name__ == "__main__":
    main()
