"""06 — Export PDF du rapport final.

Convertit docs/RAPPORT_FINAL.md en docs/RAPPORT_FINAL.pdf avec reportlab (aucune
dépendance système : ni pandoc, ni LaTeX, ni navigateur headless — indisponibles ici).

Gère : titres # .. ####, paragraphes, listes à puces, citations >, blocs de code ```,
tables pipe `| a | b |`, règles ---, et le formatage inline **gras** *italique*
`code` [texte](url).

Usage : python scripts/06_report_pdf.py
"""

from __future__ import annotations

import html
import os
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image, ListFlowable, ListItem, PageBreak, Paragraph, Preformatted, SimpleDocTemplate,
    Spacer, Table, TableStyle, HRFlowable,
)

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "RAPPORT_FINAL.md"
OUT = ROOT / "docs" / "RAPPORT_FINAL.pdf"


def _register_font() -> tuple[str, str, str, str]:
    """Police Unicode complète si dispo (macOS Arial), sinon Helvetica (Latin-1)."""
    d = "/System/Library/Fonts/Supplemental"
    fam = {
        "Doc": f"{d}/Arial.ttf",
        "Doc-Bold": f"{d}/Arial Bold.ttf",
        "Doc-Italic": f"{d}/Arial Italic.ttf",
        "Doc-BoldItalic": f"{d}/Arial Bold Italic.ttf",
    }
    if all(os.path.exists(p) for p in fam.values()):
        for name, path in fam.items():
            pdfmetrics.registerFont(TTFont(name, path))
        pdfmetrics.registerFontFamily("Doc", normal="Doc", bold="Doc-Bold",
                                      italic="Doc-Italic", boldItalic="Doc-BoldItalic")
        return "Doc", "Doc-Bold", "Doc-Italic", "Doc-BoldItalic"
    return ("Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique")


F, FB, FI, FBI = _register_font()

ACCENT = colors.HexColor("#6d28d9")
LINK = colors.HexColor("#2563eb")
GREY = colors.HexColor("#6b7280")

ss = getSampleStyleSheet()
BODY = ParagraphStyle("body", parent=ss["BodyText"], fontName=F,
                      fontSize=9.2, leading=13, spaceAfter=5, alignment=TA_LEFT)
H1 = ParagraphStyle("h1", parent=BODY, fontName=FB, fontSize=17,
                    leading=21, spaceBefore=6, spaceAfter=10, textColor=ACCENT)
H2 = ParagraphStyle("h2", parent=BODY, fontName=FB, fontSize=13.5,
                    leading=17, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor("#111827"))
H3 = ParagraphStyle("h3", parent=BODY, fontName=FB, fontSize=11,
                    leading=14, spaceBefore=9, spaceAfter=4)
H4 = ParagraphStyle("h4", parent=BODY, fontName=FBI, fontSize=9.6,
                    leading=13, spaceBefore=7, spaceAfter=3)
QUOTE = ParagraphStyle("quote", parent=BODY, leftIndent=10, textColor=GREY,
                       borderColor=ACCENT, borderWidth=0, fontSize=8.8, leading=12)
CAPT = ParagraphStyle("capt", parent=BODY, fontSize=7.6, leading=10, textColor=GREY,
                      spaceBefore=2, spaceAfter=2, alignment=TA_LEFT)
CELL = ParagraphStyle("cell", parent=BODY, fontSize=7.4, leading=9.5, spaceAfter=0)
CELLH = ParagraphStyle("cellh", parent=CELL, fontName=FB, textColor=colors.white)
CODE = ParagraphStyle("code", parent=BODY, fontName="Courier", fontSize=7.6, leading=9.5,
                      backColor=colors.HexColor("#f3f4f6"), borderPadding=4)

INLINE_CODE = re.compile(r"`([^`]+)`")
IMG = re.compile(r"^\s*!\[([^\]]*)\]\(([^)]+)\)\s*$")
LINKRE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
TRISTAR = re.compile(r"\*\*\*(.+?)\*\*\*")
BOLD = re.compile(r"\*\*(.+?)\*\*")
ITALIC = re.compile(r"\*(.+?)\*")


_SUB = {"≫": ">>", "≪": "<<", "ʳᵉ": "re", "ᵉ": "e",
        "ʳ": "r", "ᵈ": "d", "‑": "-",
        "☑": "[x]", "☐": "[ ]", "◐": "[~]", "☒": "[x]"}


def inline(text: str) -> str:
    """Markdown inline -> mini-HTML reportlab (échappe d'abord le XML)."""
    for k, v in _SUB.items():
        text = text.replace(k, v)
    text = html.escape(text, quote=False)

    # 1. isole les spans de code pour les protéger des passes suivantes
    codes: list[str] = []

    def _stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = INLINE_CODE.sub(_stash, text)

    # 2. gras / italique
    text = re.sub(r"\*\*([^*]+?)\*([^*]+?)\*\*\*", r"<b>\1<i>\2</i></b>", text)  # **a *b***
    text = TRISTAR.sub(r"<b><i>\1</i></b>", text)                                # ***x***
    text = BOLD.sub(r"<b>\1</b>", text)                                         # **x**
    text = re.sub(r"\*([^*<>]+?)\*", r"<i>\1</i>", text)                        # *x* (pas de croisement de balise)
    text = text.replace("*", "")  # astérisques orphelines (nesting markdown résiduel)

    # 3. liens : URL absolue -> cliquable ; ancre/relatif -> texte simple
    def _link(m):
        label, href = m.group(1), m.group(2).strip()
        if href.startswith("#"):
            return f"<i>{label}</i>"
        if not re.match(r"^[a-zA-Z][\w+.-]*:", href):
            return label
        return (f'<link href="{html.escape(href, quote=True)}">'
                f'<font color="#2563eb">{label}</font></link>')

    text = LINKRE.sub(_link, text)

    # 4. restaure les spans de code
    text = re.sub(r"\x00(\d+)\x00",
                  lambda m: f'<font face="Courier" size="8">{codes[int(m.group(1))]}</font>',
                  text)
    return text


def parse(md: str, story: list, avail_w: float) -> None:
    lines = md.splitlines()
    i = 0
    first_h1 = True
    bullets: list = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            story.append(ListFlowable(
                [ListItem(Paragraph(b, BODY), leftIndent=12, value="•") for b in bullets],
                bulletType="bullet", start="•", leftIndent=10))
            story.append(Spacer(1, 3))
            bullets = []

    while i < len(lines):
        ln = lines[i]

        # --- image ![alt](path) sur sa propre ligne ---
        mi = IMG.match(ln)
        if mi:
            flush_bullets()
            alt, rel = mi.group(1), mi.group(2).strip()
            p = (SRC.parent / rel).resolve()
            if p.exists():
                try:
                    iw, ih = ImageReader(str(p)).getSize()
                    w = min(avail_w, iw * 0.72)
                    story.append(Spacer(1, 4))
                    story.append(Image(str(p), width=w, height=w * ih / iw))
                    if alt:
                        story.append(Paragraph(inline(alt), CAPT))
                    story.append(Spacer(1, 8))
                except Exception:  # noqa: BLE001
                    story.append(Paragraph(f"[figure : {html.escape(rel)}]", CAPT))
            else:
                story.append(Paragraph(f"[figure manquante : {html.escape(rel)}]", CAPT))
            i += 1
            continue

        # --- table (bloc de lignes commençant par |) ---
        if ln.lstrip().startswith("|") and "|" in ln[1:]:
            flush_bullets()
            block = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            rows = []
            for r, raw in enumerate(block):
                cells = [c.strip() for c in raw.strip().strip("|").split("|")]
                if r == 1 and set("".join(cells)) <= set("-: "):
                    continue  # ligne de séparation
                sty = CELLH if r == 0 else CELL
                rows.append([Paragraph(inline(c) or "&nbsp;", sty) for c in cells])
            if rows:
                ncol = max(len(r) for r in rows)
                rows = [r + [Paragraph("", CELL)] * (ncol - len(r)) for r in rows]
                cw = avail_w / ncol
                t = Table(rows, colWidths=[cw] * ncol, repeatRows=1)
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 3),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                    ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
            continue

        # --- bloc de code ``` ---
        if ln.startswith("```"):
            flush_bullets()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            story.append(Preformatted("\n".join(buf) or " ", CODE))
            story.append(Spacer(1, 5))
            continue

        # --- titres ---
        m = re.match(r"(#{1,4})\s+(.*)", ln)
        if m:
            flush_bullets()
            level = len(m.group(1))
            txt = inline(m.group(2).strip())
            if level == 1:
                if not first_h1:
                    story.append(PageBreak())
                first_h1 = False
                story.append(Paragraph(txt, H1))
                story.append(HRFlowable(width="100%", thickness=1, color=ACCENT,
                                        spaceBefore=2, spaceAfter=8))
            else:
                story.append(Paragraph(txt, {2: H2, 3: H3, 4: H4}[level]))
            i += 1
            continue

        # --- règle horizontale ---
        if re.match(r"^\s*([-*_])\1{2,}\s*$", ln):
            flush_bullets()
            story.append(HRFlowable(width="100%", thickness=0.6,
                                    color=colors.HexColor("#d1d5db"),
                                    spaceBefore=4, spaceAfter=6))
            i += 1
            continue

        # --- citation (peut s'étendre sur plusieurs lignes) ---
        if ln.lstrip().startswith(">"):
            flush_bullets()
            buf = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                seg = re.sub(r"^\s*>\s?", "", lines[i])
                if not seg.strip():
                    if buf:
                        story.append(Paragraph(inline(" ".join(buf)), QUOTE))
                        buf = []
                else:
                    buf.append(seg.strip())
                i += 1
            if buf:
                story.append(Paragraph(inline(" ".join(buf)), QUOTE))
            story.append(Spacer(1, 3))
            continue

        # --- puces (avec lignes de continuation) ---
        mb = re.match(r"^\s*[-*]\s+(.*)", ln) or re.match(r"^\s*\d+\.\s+(.*)", ln)
        if mb:
            item = [mb.group(1).strip()]
            i += 1
            while (i < len(lines) and lines[i].strip()
                   and not re.match(r"^\s*[-*]\s+", lines[i])
                   and not re.match(r"^\s*\d+\.\s+", lines[i])
                   and not re.match(r"(#{1,4})\s", lines[i])
                   and not lines[i].lstrip().startswith(("|", ">", "```"))
                   and not re.match(r"^\s*([-*_])\1{2,}\s*$", lines[i])):
                item.append(lines[i].strip())
                i += 1
            bullets.append(inline(" ".join(item)))
            continue

        # --- ligne vide ---
        if not ln.strip():
            flush_bullets()
            i += 1
            continue

        # --- paragraphe (fusionne les lignes consécutives) ---
        para = [ln.strip()]
        i += 1
        while (i < len(lines) and lines[i].strip()
               and not re.match(r"(#{1,4})\s", lines[i])
               and not lines[i].lstrip().startswith(("|", ">", "- ", "* ", "```", "!["))
               and not re.match(r"^\s*\d+\.\s", lines[i])
               and not re.match(r"^\s*([-*_])\1{2,}\s*$", lines[i])):
            para.append(lines[i].strip())
            i += 1
        flush_bullets()
        story.append(Paragraph(inline(" ".join(para)), BODY))

    flush_bullets()


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(F, 7)
    canvas.setFillColor(GREY)
    canvas.drawString(1.6 * cm, 1.0 * cm,
                      "CardioTolerance-AI — MedFlow AI — document de travail v1")
    canvas.drawRightString(A4[0] - 1.6 * cm, 1.0 * cm, f"p. {doc.page}")
    canvas.restoreState()


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"{SRC} absent — lancer d'abord scripts/05_assemble_report.py")
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=1.6 * cm, rightMargin=1.6 * cm,
        topMargin=1.5 * cm, bottomMargin=1.6 * cm,
        title="CardioTolerance-AI — Rapport de faisabilité",
        author="MedFlow AI — Dr. M. L. Tall",
    )
    avail_w = A4[0] - 3.2 * cm
    story: list = []
    parse(SRC.read_text(encoding="utf-8"), story, avail_w)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Écrit : {OUT.relative_to(ROOT)}  ({OUT.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
