"""CardioTolerance-AI — application de cadrage scientifique et de montage de collaboration.

AI-driven discovery of immune tolerance signatures after heart transplantation.

Squelette : 10 pages alignées sur docs/01_PROJECT_SPEC.md §7. Le contenu de chaque page
est chargé depuis docs/ et data/ au fur et à mesure de leur remplissage
(voir docs/02_ROADMAP.md). Tant qu'une source est absente, la page affiche un encart
"section en cours de rédaction" — jamais de contenu inventé.

Garde-fou : le projet ne suppose jamais l'arrêt de l'immunosuppression.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
OUTREACH = ROOT / "outreach"

st.set_page_config(
    page_title="CardioTolerance-AI · MedFlow AI",
    page_icon="🫀",
    layout="wide",
)

ACCENT = "#8b5cf6"
MINT = "#34d399"

st.markdown(
    f"""
    <style>
      .stApp {{ background: #05070d; }}
      h1, h2, h3 {{ letter-spacing: -0.02em; }}
      .ct-tag {{ display:inline-block; padding:2px 10px; border-radius:999px;
                 background:{ACCENT}22; color:{ACCENT}; font-size:0.8rem; font-weight:600; }}
      .ct-guard {{ border-left:3px solid {MINT}; padding:.6rem 1rem; background:{MINT}11;
                   border-radius:6px; font-size:0.92rem; }}
      .ct-wip {{ border:1px dashed #ffffff33; padding:1rem 1.2rem; border-radius:8px;
                 color:#c9cbd6; background:#ffffff08; }}
    </style>
    """,
    unsafe_allow_html=True,
)


def load_markdown(name: str) -> str | None:
    path = DOCS / name
    return path.read_text(encoding="utf-8") if path.exists() else None


def load_csv(name: str) -> pd.DataFrame | None:
    path = DATA / name
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:  # noqa: BLE001 - affichage défensif dans l'app
        return None


def wip(section: str, source: str) -> None:
    st.markdown(
        f"<div class='ct-wip'>🚧 <b>{section}</b> — section en cours de rédaction.<br>"
        f"Sera alimentée depuis <code>{source}</code> (cf. <code>docs/02_ROADMAP.md</code>). "
        f"Aucun contenu provisoire n'est affiché ici pour éviter toute donnée non vérifiée.</div>",
        unsafe_allow_html=True,
    )


def doc_or_wip(section: str, doc_name: str) -> None:
    content = load_markdown(doc_name)
    if content:
        st.markdown(content, unsafe_allow_html=True)
    else:
        wip(section, f"docs/{doc_name}")


def table_or_wip(section: str, csv_name: str, **filters_note: str) -> None:
    df = load_csv(csv_name)
    if df is None or df.empty:
        wip(section, f"data/{csv_name}")
        return
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption(f"{len(df)} lignes · source : `data/{csv_name}`")


# ----------------------------------------------------------------------------- #
# Sidebar
# ----------------------------------------------------------------------------- #
with st.sidebar:
    st.markdown("### 🫀 CardioTolerance-AI")
    st.caption("MedFlow AI · Dr. M. L. Tall — cadrage scientifique & collaboration")
    page = st.radio(
        "Navigation",
        [
            "1 · Résumé",
            "2 · État de l'art",
            "3 · Revue systématique",
            "4 · Méta-analyse",
            "5 · Datasets accessibles",
            "6 · Paysage français",
            "7 · Gap & méthodologie",
            "8 · Faisabilité (A/B/C)",
            "9 · Collaboration & TOP 5",
            "10 · Prise de contact",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown(
        "<span class='ct-tag'>Non-dispositif médical</span>", unsafe_allow_html=True
    )
    st.caption(
        "Document de cadrage — pas un avis médical, pas un protocole déposé, "
        "pas un dispositif médical."
    )


# ----------------------------------------------------------------------------- #
# Pages
# ----------------------------------------------------------------------------- #
if page.startswith("1"):
    st.title("AI-driven discovery of immune tolerance signatures after heart transplantation")
    st.markdown(
        "<div class='ct-guard'>⚠️ Garde-fou scientifique : le projet <b>ne suppose jamais</b> "
        "qu'un patient puisse arrêter son immunosuppression. Objectif = identifier des "
        "biomarqueurs et des profils de tolérance, à valider prospectivement sous "
        "supervision médicale.</div>",
        unsafe_allow_html=True,
    )
    st.subheader("Question scientifique centrale")
    st.markdown(
        "Existe-t-il, chez certains receveurs de greffe cardiaque, une **signature "
        "immunologique / moléculaire / cellulaire / multi-omique** associée à une tolérance "
        "particulièrement élevée du greffon — et l'IA peut-elle :\n"
        "1. identifier cette signature ;\n"
        "2. séparer rejet vs stabilité durable ;\n"
        "3. repérer des profils de tolérance immunologique exceptionnelle ;\n"
        "4. prédire longitudinalement l'évolution du risque de rejet ;\n"
        "5. à terme, aider à identifier des candidats à une **réduction contrôlée et "
        "supervisée** de l'immunosuppression."
    )
    st.subheader("Boucle de collaboration visée")
    st.markdown(
        "`Clinical data` → `AI / Bioinformatics` → `candidate biomarker` → "
        "`biological validation` → `clinical validation`"
    )
    doc_or_wip("Executive summary", "section_01_executive_summary.md")

elif page.startswith("2"):
    st.title("État de l'art")
    doc_or_wip("State of the art", "section_03_state_of_the_art.md")

elif page.startswith("3"):
    st.title("Revue systématique")
    doc_or_wip("Stratégie de recherche & PRISMA", "section_04_systematic_review.md")
    st.subheader("Registre des études incluses")
    table_or_wip("Tableau d'extraction par étude", "studies_registry.csv")

elif page.startswith("4"):
    st.title("Méta-analyse")
    doc_or_wip("Méta-analyse / evidence synthesis", "section_05_meta_analysis.md")
    st.subheader("Estimations poolées")
    table_or_wip("Estimations poolées (effets aléatoires)", "meta_estimates.csv")

elif page.startswith("5"):
    st.title("Datasets réellement accessibles")
    st.caption(
        "Accès : Public · Controlled access · Non public (collaboration) · "
        "Mentionné mais non disponible → à contacter"
    )
    table_or_wip("Registre des datasets", "datasets_registry.csv")
    doc_or_wip("Synthèse datasets", "section_06_datasets.md")

elif page.startswith("6"):
    st.title("Paysage français — équipes & cohortes")
    table_or_wip("Équipes françaises", "french_teams.csv")
    doc_or_wip("Analyse du paysage français", "section_07_french_landscape.md")

elif page.startswith("7"):
    st.title("Gap scientifique & méthodologie IA / multi-omics")
    doc_or_wip("Gap (Q1–Q10) + Aims + plan statistique", "section_08_09_gap_method.md")

elif page.startswith("8"):
    st.title("Faisabilité — scénarios A / B / C")
    doc_or_wip("Analyse de faisabilité", "section_13_feasibility.md")

elif page.startswith("9"):
    st.title("Collaboration & classement TOP 5")
    doc_or_wip("Apports respectifs & recommandation", "section_15_16_17_collab.md")
    st.subheader("Scoring des équipes candidates")
    table_or_wip("Grille de scoring (6 axes /10)", "french_teams_scoring.csv")

elif page.startswith("10"):
    st.title("Kit de prise de contact")
    for label, fname in [
        ("Projet en 1 page", OUTREACH / "one_pager.md"),
        ("Brouillon email — Français", OUTREACH / "email_fr.md"),
        ("Brouillon email — English", OUTREACH / "email_en.md"),
    ]:
        st.subheader(label)
        if fname.exists():
            st.code(fname.read_text(encoding="utf-8"), language="markdown")
        else:
            wip(label, str(fname.relative_to(ROOT)))
    st.info(
        "Aucun envoi sans validation préalable de Dr. Tall. Les emails sont personnalisés "
        "pour l'équipe #1 issue du scoring (page 9)."
    )
