"""CardioTolerance-AI — application de cadrage scientifique et de montage de collaboration.

AI-driven discovery of immune tolerance signatures after heart transplantation.

10 pages alignées sur docs/01_PROJECT_SPEC.md §7. Chaque page charge son contenu depuis
docs/ et data/. Tant qu'une source est absente, la page affiche un encart
« section en cours de rédaction » — jamais de contenu inventé.

Garde-fou : le projet ne suppose jamais l'arrêt de l'immunosuppression.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
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


def table_or_wip(section: str, csv_name: str) -> pd.DataFrame | None:
    df = load_csv(csv_name)
    if df is None or df.empty:
        wip(section, f"data/{csv_name}")
        return None
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption(f"{len(df)} lignes · source : `data/{csv_name}`")
    return df


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
    st.markdown("<span class='ct-tag'>Non-dispositif médical</span>", unsafe_allow_html=True)
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
    st.write("")
    doc_or_wip("Executive summary", "section_01_executive_summary.md")

elif page.startswith("2"):
    st.title("État de l'art")
    doc_or_wip("State of the art", "section_03_state_of_the_art.md")

elif page.startswith("3"):
    st.title("Revue systématique")
    doc_or_wip("Stratégie de recherche & PRISMA", "section_04_systematic_review.md")
    prisma = FIGURES / "fig_prisma_template.png"
    if prisma.exists():
        st.image(str(prisma), caption="Gabarit PRISMA (compteurs à remplir en Phase 2)", width=460)
    st.subheader("Registre des études incluses")
    table_or_wip("Tableau d'extraction par étude", "studies_registry.csv")

elif page.startswith("4"):
    st.title("Méta-analyse")
    doc_or_wip("Méta-analyse / evidence synthesis", "section_05_meta_analysis.md")
    land = FIGURES / "fig_ddcfdna_landscape.png"
    if land.exists():
        st.image(str(land), use_container_width=True)
    st.subheader("Estimations poolées")
    table_or_wip("Estimations poolées / rapportées", "meta_estimates.csv")

elif page.startswith("5"):
    st.title("Datasets réellement accessibles")
    df = load_csv("datasets_registry.csv")
    if df is None or df.empty:
        wip("Registre des datasets", "data/datasets_registry.csv")
    else:
        if "access" in df.columns:
            opts = sorted(df["access"].dropna().unique().tolist())
            picked = st.multiselect("Filtrer par accès", opts, default=opts)
            df = df[df["access"].isin(picked)]
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"{len(df)} datasets · source : `data/datasets_registry.csv`")
    doc_or_wip("Synthèse datasets", "section_06_datasets.md")

elif page.startswith("6"):
    st.title("Paysage français — équipes & cohortes")
    df = load_csv("french_teams.csv")
    if df is None or df.empty:
        wip("Équipes françaises", "data/french_teams.csv")
    else:
        if "city" in df.columns:
            cities = sorted(df["city"].dropna().unique().tolist())
            picked = st.multiselect("Ville", cities, default=cities)
            df = df[df["city"].isin(picked)]
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"{len(df)} équipes · source : `data/french_teams.csv`")
    doc_or_wip("Analyse du paysage français", "section_07_french_landscape.md")

elif page.startswith("7"):
    st.title("Gap scientifique & méthodologie IA / multi-omics")
    doc_or_wip("Gap (Q1–Q10) + Aims + plan statistique + validation", "section_08_09_gap_method.md")

elif page.startswith("8"):
    st.title("Faisabilité — scénarios A / B / C")
    doc_or_wip("Analyse de faisabilité, impact, publications", "section_13_feasibility.md")

elif page.startswith("9"):
    st.title("Collaboration & classement TOP 5")
    scoring = load_csv("french_teams_scoring.csv")
    if scoring is not None and not scoring.empty and "total_pondere" in scoring.columns:
        s = scoring.sort_values("total_pondere", ascending=False)
        label_col = "team_label" if "team_label" in s.columns else "team_id"
        fig = px.bar(
            s, x="total_pondere", y=label_col, orientation="h",
            range_x=[0, float(s["total_max"].max()) if "total_max" in s.columns else 70],
            color_discrete_sequence=[ACCENT],
        )
        fig.update_layout(
            height=340, margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font_color="#f4f4f7", yaxis_title="", xaxis_title="Score pondéré /70",
            yaxis=dict(autorange="reversed"),
        )
        st.plotly_chart(fig, use_container_width=True)
        radar = FIGURES / "fig_scoring_radar.png"
        if radar.exists():
            st.image(str(radar), width=560)
        st.dataframe(s, use_container_width=True, hide_index=True)
        st.caption("source : `data/french_teams_scoring.csv`")
    else:
        wip("Grille de scoring (6 axes /10)", "data/french_teams_scoring.csv")
    doc_or_wip("Apports respectifs & recommandation", "section_15_16_17_collab.md")

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
