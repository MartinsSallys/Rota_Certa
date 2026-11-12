# -*- coding: utf-8 -*-
"""Gera o DOCX 'RotaCerta — Briefing do Produto e Planejamento do MVP'."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

from gerar_documento import (
    AMBER_BG,
    AMBER_DK,
    BG_LABEL,
    BG_LIGHT,
    CONTENT_W,
    FAINT,
    F_BODY,
    F_HEAD,
    GREEN_OK,
    INK,
    LINE,
    MUTED,
    NAVY,
    RED_BAD,
    TEAL,
    TEAL_DK,
    WHITE,
    add_field,
    add_runs,
    add_toc,
    add_toc_field,
    build_styles,
    bullet,
    bullets,
    callout,
    cell_borders,
    cell_margins,
    cell_par,
    cell_shade,
    h1,
    h2,
    h3,
    keep_next,
    make_table,
    new_par,
    numbered,
    page_break_before,
    par_border,
    row_no_split,
    row_repeat_header,
    rgb,
    run_shade,
    run_spacing,
)
import conteudo_rotacerta as cr

ACCENT_BLUE = "2E6BE6"
GREEN_LT = "E8F6EE"
RED_LT = "FBEDEC"


# ---------------------------------------------------------------- utilitários


def cell_no_border(cell):
    cell_borders(cell, top=None, bottom=None, left=None, right=None)


def cell_box(cell, fill=BG_LIGHT, accent=None):
    cell_shade(cell, fill)
    if accent:
        cell_borders(cell, top=(4, accent), bottom=(4, accent),
                     left=(4, accent), right=(4, accent))
    else:
        cell_borders(cell, top=(4, LINE), bottom=(4, LINE),
                     left=(4, LINE), right=(4, LINE))


def cell_text(cell, text, size=8.5, color=INK, bold=False, font=F_BODY,
              align=WD_ALIGN_PARAGRAPH.LEFT, space_after=0, line_spacing=1.12,
              first=True):
    p = cell.paragraphs[0] if first and cell.paragraphs else cell.add_paragraph()
    if not first and p.text.strip():
        p = cell.add_paragraph()
    p.alignment = align
    add_runs(p, text, font=font, size=size, color=color, bold=bold)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    return p


def write_line(par, label, width_hint=None):
    """Linha 'Rótulo: ______' para respostas manuais."""
    r = par.add_run(label)
    r.font.name = F_BODY
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = rgb(NAVY)
    r2 = par.add_run(" " + "_" * (62 if width_hint is None else width_hint))
    r2.font.name = F_BODY
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = rgb(FAINT)
    return par


# ---------------------------------------------------------------- capa


def build_cover(doc, section):
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(0.6)
    section.bottom_margin = Cm(0.6)
    section.left_margin = Cm(0.6)
    section.right_margin = Cm(0.6)

    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    table.columns[0].width = Cm(19.8)
    row = table.rows[0]
    row.height = Cm(28.5)
    row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    cell = row.cells[0]
    cell.width = Cm(19.8)
    cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    cell_shade(cell, NAVY)
    cell_no_border(cell)
    cell_margins(cell, top=210, bottom=170, left=340, right=340)

    p = cell.paragraphs[0]
    r = p.add_run(cr.META["evento"] + "  ·  DOCUMENTO DE TRABALHO")
    r.font.name = F_BODY
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL)
    run_spacing(r, 60)
    p.paragraph_format.space_after = Pt(0)

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(90)
    for r in p.runs:
        r.font.size = Pt(4)

    p = cell.add_paragraph()
    r = p.add_run("RotaCerta")
    r.font.name = F_HEAD
    r.font.size = Pt(40)
    r.font.bold = True
    r.font.color.rgb = rgb(WHITE)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.0

    p = cell.add_paragraph()
    r = p.add_run("Briefing do Produto e Planejamento do MVP")
    r.font.name = F_HEAD
    r.font.size = Pt(17)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL)
    p.paragraph_format.space_after = Pt(14)

    p = cell.add_paragraph()
    par_border(p, "bottom", sz=16, color=TEAL, space=2)
    p.paragraph_format.space_after = Pt(14)

    p = cell.add_paragraph()
    r = p.add_run(cr.META["descricao_capa"])
    r.font.name = F_BODY
    r.font.size = Pt(11.5)
    r.font.color.rgb = rgb("C9D4E4")
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.space_after = Pt(0)

    p = cell.add_paragraph()
    r = p.add_run(cr.META["tagline"])
    r.font.name = F_BODY
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = rgb(WHITE)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(0)

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(280)

    # faixa de identidade visual: quatro etapas do ciclo do produto
    stripe = cell.add_table(rows=1, cols=4)
    stripe.autofit = False
    etapas = [
        ("Planejar", TEAL),
        ("Otimizar", ACCENT_BLUE),
        ("Executar", GREEN_OK),
        ("Medir", "7C5CFF"),
    ]
    for i, (nome, cor) in enumerate(etapas):
        w = 14.6 / 4.0
        stripe.columns[i].width = Cm(w)
        c = stripe.rows[0].cells[i]
        c.width = Cm(w)
        cell_shade(c, cor)
        cell_no_border(c)
        cell_margins(c, top=0, bottom=0, left=0, right=0)
        cp = c.paragraphs[0]
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.paragraph_format.space_after = Pt(0)
        cp.paragraph_format.space_before = Pt(0)
        rr = cp.add_run(nome)
        rr.font.name = F_BODY
        rr.font.size = Pt(8)
        rr.font.bold = True
        rr.font.color.rgb = rgb(WHITE)
        run_spacing(rr, 20)
    sr = stripe.rows[0]
    sr.height = Cm(0.55)
    sr.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)

    p = cell.add_paragraph()
    r = p.add_run("Planejamento · Otimização · Execução · Indicadores")
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.color.rgb = rgb("7E8CA6")
    run_spacing(r, 20)
    p.paragraph_format.space_after = Pt(10)

    p = cell.add_paragraph()
    r = p.add_run(cr.META["versao"])
    r.font.name = F_BODY
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = rgb("9FADC3")
    p.paragraph_format.space_after = Pt(2)

    p = cell.add_paragraph()
    r = p.add_run(
        "Hack Brasil 2026 · Equipe de 3 integrantes · Prazo de desenvolvimento: "
        "12 a 30 de novembro de 2026"
    )
    r.font.name = F_BODY
    r.font.size = Pt(9)
    r.font.color.rgb = rgb("9FADC3")
    p.paragraph_format.space_after = Pt(4)

    p = cell.add_paragraph()
    r = p.add_run(cr.META["aviso_capa"])
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.italic = True
    r.font.color.rgb = rgb("7E8CA6")
    p.paragraph_format.space_after = Pt(0)


# ---------------------------------------------------------------- corpo


def setup_body_section(section):
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.1)
    section.bottom_margin = Cm(1.9)
    section.left_margin = Cm(2.3)
    section.right_margin = Cm(2.3)
    section.header_distance = Cm(1.0)
    section.footer_distance = Cm(0.9)

    header = section.header
    header.is_linked_to_previous = False
    for p in list(header.paragraphs)[1:]:
        p._element.getparent().remove(p._element)
    hp = header.paragraphs[0]
    for r in list(hp.runs):
        r._element.getparent().remove(r._element)
    hp.text = ""
    r = hp.add_run("ROTACERTA  ·  BRIEFING DO PRODUTO E PLANEJAMENTO DO MVP  ·  HACK BRASIL 2026")
    r.font.name = F_BODY
    r.font.size = Pt(7.5)
    r.font.bold = True
    r.font.color.rgb = rgb(FAINT)
    run_spacing(r, 24)
    hp.paragraph_format.space_after = Pt(2)
    par_border(hp, "bottom", sz=6, color=LINE, space=3)

    footer = section.footer
    footer.is_linked_to_previous = False
    for p in list(footer.paragraphs)[1:]:
        p._element.getparent().remove(p._element)
    fp = footer.paragraphs[0]
    for r in list(fp.runs):
        r._element.getparent().remove(r._element)
    fp.text = ""
    fp.paragraph_format.space_before = Pt(2)
    fp.paragraph_format.tab_stops.add_tab_stop(Cm(CONTENT_W), WD_TAB_ALIGNMENT.RIGHT)
    par_border(fp, "top", sz=6, color=LINE, space=4)
    r = fp.add_run("RotaCerta · Briefing do Produto e Planejamento do MVP\t")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.color.rgb = rgb(FAINT)
    r = fp.add_run("Página ")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.color.rgb = rgb(FAINT)
    add_field(fp, " PAGE ", "1")
    r = fp.add_run(" de ")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.color.rgb = rgb(FAINT)
    add_field(fp, " NUMPAGES ", "1")


# ---------------------------------------------------------------- diagramas


def build_fluxo(doc):
    """Diagrama horizontal do fluxo do produto."""
    n_box, n_arrow = len(cr.FLUXO), len(cr.FLUXO) - 1
    w_arrow = 0.5
    w_box = (CONTENT_W - n_arrow * w_arrow) / n_box
    cols = []
    for i in range(n_box):
        cols.append(w_box)
        if i < n_arrow:
            cols.append(w_arrow)
    table = doc.add_table(rows=1, cols=len(cols))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)

    row = table.rows[0]
    row_no_split(row)
    row.height = Cm(1.55)
    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST

    for i, w in enumerate(cols):
        table.columns[i].width = Cm(w)
        cell = row.cells[i]
        cell.width = Cm(w)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        if i % 2 == 0:
            idx = i // 2
            cell_box(cell, fill=BG_LIGHT, accent=TEAL)
            cell_margins(cell, top=70, bottom=70, left=50, right=50)
            lines = cr.FLUXO[idx].split("\n")
            for j, line in enumerate(lines):
                p = cell.paragraphs[0] if j == 0 else cell.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.05
                r = p.add_run(line)
                r.font.name = F_BODY
                r.font.size = Pt(7.8)
                r.font.bold = True
                r.font.color.rgb = rgb(NAVY)
        else:
            cell_no_border(cell)
            cell_margins(cell, top=0, bottom=0, left=0, right=0)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run("→")
            r.font.name = F_BODY
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = rgb(TEAL)

    p = new_par(doc, cr.FLUXO_TITULO, size=8.5, italic=True, color=MUTED,
                align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=10)
    return p


def build_arquitetura(doc):
    """Diagrama em camadas da arquitetura."""
    table = doc.add_table(rows=4, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)

    widths = [CONTENT_W / 3.0] * 3
    for i, w in enumerate(widths):
        table.columns[i].width = Cm(w)

    def full_band(row_idx, titulo, sub, fill, accent):
        cells = table.rows[row_idx].cells
        merged = cells[0].merge(cells[1]).merge(cells[2])
        merged.width = Cm(CONTENT_W)
        cell_box(merged, fill=fill, accent=accent)
        cell_margins(merged, top=70, bottom=70, left=140, right=140)
        p = merged.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(1 if sub else 0)
        keep_next(p)
        r = p.add_run(titulo)
        r.font.name = F_HEAD
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = rgb(NAVY)
        if sub:
            p2 = merged.add_paragraph()
            p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p2.paragraph_format.space_after = Pt(0)
            keep_next(p2)
            r2 = p2.add_run(sub)
            r2.font.name = F_BODY
            r2.font.size = Pt(8)
            r2.font.color.rgb = rgb(MUTED)
        row_no_split(table.rows[row_idx])

    # camada 1 — frontend
    full_band(0, cr.ARQUITETURA[0][0], cr.ARQUITETURA[0][1], BG_LIGHT, TEAL)

    # faixa de comunicação
    cells = table.rows[1].cells
    merged = cells[0].merge(cells[1]).merge(cells[2])
    merged.width = Cm(CONTENT_W)
    cell_shade(merged, TEAL_DK)
    cell_no_border(merged)
    cell_margins(merged, top=40, bottom=40, left=60, right=60)
    p = merged.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    keep_next(p)
    r = p.add_run("↑   " + cr.ARQUITETURA[1][0] + "   ↓")
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = rgb(WHITE)
    run_spacing(r, 16)
    row_no_split(table.rows[1])

    # camada 2 — backend
    full_band(2, cr.ARQUITETURA[2][0], cr.ARQUITETURA[2][1], BG_LABEL, ACCENT_BLUE)

    # camada 3 — dados e serviços
    row = table.rows[3]
    row_no_split(row)
    row.height = Cm(1.2)
    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    for i, titulo in enumerate(cr.ARQUITETURA[3]):
        cell = row.cells[i]
        cell.width = Cm(widths[i])
        cell_box(cell, fill=WHITE, accent=LINE)
        cell_margins(cell, top=70, bottom=70, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.08
        keep_next(p)
        r = p.add_run(titulo)
        r.font.name = F_BODY
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL_DK)

    cap = new_par(doc, cr.ARQUITETURA_NOTA, size=8.5, italic=True, color=MUTED,
                  align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=3)
    keep_next(cap)
    new_par(doc, cr.ARQUITETURA_LEGENDA, size=9.5, color=INK,
            align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=10)


def build_cronograma_visual(doc):
    """Gantt do cronograma: uma coluna por dia (12 a 30/11)."""
    dias = list(range(12, 31))
    w_label = 4.6
    w_day = (CONTENT_W - w_label) / len(dias)
    cols = [w_label] + [w_day] * len(dias)
    table = doc.add_table(rows=2 + len(cr.CRONO), cols=len(cols))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i, w in enumerate(cols):
        table.columns[i].width = Cm(w)

    # cabeçalho: números dos dias
    hdr = table.rows[0]
    row_no_split(hdr)
    hdr.height = Cm(0.52)
    hdr.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    cell = hdr.cells[0]
    cell.width = Cm(w_label)
    cell_shade(cell, NAVY)
    cell_no_border(cell)
    cell_margins(cell, top=30, bottom=30, left=80, right=60)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("Atividade")
    r.font.name = F_BODY
    r.font.size = Pt(7.5)
    r.font.bold = True
    r.font.color.rgb = rgb(WHITE)

    import datetime
    for j, d in enumerate(dias):
        c = hdr.cells[1 + j]
        c.width = Cm(w_day)
        eh_fds = datetime.date(2026, 11, d).weekday() >= 5
        cell_shade(c, MUTED if eh_fds else NAVY)
        cell_no_border(c)
        cell_margins(c, top=30, bottom=30, left=0, right=0)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(str(d))
        r.font.name = F_BODY
        r.font.size = Pt(6.5)
        r.font.bold = True
        r.font.color.rgb = rgb(WHITE)

    # cabeçalho: dias da semana
    hdr2 = table.rows[1]
    row_no_split(hdr2)
    hdr2.height = Cm(0.42)
    hdr2.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
    cell = hdr2.cells[0]
    cell.width = Cm(w_label)
    cell_shade(cell, BG_LABEL)
    cell_borders(cell, top=(4, LINE), bottom=(4, LINE), left=None, right=(4, LINE))
    cell_margins(cell, top=20, bottom=20, left=80, right=60)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("novembro de 2026")
    r.font.name = F_BODY
    r.font.size = Pt(7)
    r.font.color.rgb = rgb(MUTED)

    siglas = ["s", "t", "q", "q", "s", "s", "d"]
    for j, d in enumerate(dias):
        c = hdr2.cells[1 + j]
        c.width = Cm(w_day)
        wd = datetime.date(2026, 11, d).weekday()
        eh_fds = wd >= 5
        cell_shade(c, "E4E9F1" if eh_fds else BG_LABEL)
        cell_borders(c, top=None, bottom=(4, LINE),
                     left=None, right=(4, LINE) if j == len(dias) - 1 else None)
        cell_margins(c, top=20, bottom=20, left=0, right=0)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(siglas[wd])
        r.font.name = F_BODY
        r.font.size = Pt(6.5)
        r.font.color.rgb = rgb(MUTED if not eh_fds else FAINT)
        r.font.bold = eh_fds

    # barras
    for i, (periodo, atividade, d_ini, d_fim) in enumerate(cr.CRONO):
        row = table.rows[2 + i]
        row_no_split(row)
        row.height = Cm(0.78)
        row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        cell = row.cells[0]
        cell.width = Cm(w_label)
        cell_shade(cell, WHITE if i % 2 == 0 else BG_LIGHT)
        cell_borders(cell, top=None, bottom=(4, LINE),
                     left=None, right=(4, LINE))
        cell_margins(cell, top=45, bottom=45, left=80, right=50)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        r = p.add_run(atividade)
        r.font.name = F_BODY
        r.font.size = Pt(8)
        r.font.bold = True
        r.font.color.rgb = rgb(NAVY)
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.0
        r2 = p2.add_run(periodo)
        r2.font.name = F_BODY
        r2.font.size = Pt(7)
        r2.font.color.rgb = rgb(MUTED)

        for j, d in enumerate(dias):
            c = row.cells[1 + j]
            c.width = Cm(w_day)
            inside = d_ini <= d <= d_fim
            eh_fds = datetime.date(2026, 11, d).weekday() >= 5
            if inside:
                cell_shade(c, TEAL)
            elif eh_fds:
                cell_shade(c, "EEF1F6")
            else:
                cell_shade(c, WHITE)
            cell_borders(c, top=None, bottom=(4, LINE),
                         left=None, right=(4, LINE) if j == len(dias) - 1 else None)
            cell_margins(c, top=0, bottom=0, left=0, right=0)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            r = p.add_run(" ")
            r.font.size = Pt(3)

    # legenda
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("  ")
    run_shade(r, TEAL)
    r.font.size = Pt(7)
    r = p.add_run("  fase de trabalho   ")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.color.rgb = rgb(MUTED)
    r = p.add_run("  ")
    run_shade(r, "EEF1F6")
    r.font.size = Pt(7)
    r = p.add_run("  fim de semana (cronograma de competição)   ·   ")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.color.rgb = rgb(MUTED)
    r = p.add_run("dias de 12 a 30/11/2026")
    r.font.name = F_BODY
    r.font.size = Pt(8)
    r.font.italic = True
    r.font.color.rgb = rgb(FAINT)


# ---------------------------------------------------------------- blocos


def table_header(table, labels, widths, fill=NAVY, size=8.5):
    row = table.rows[0]
    row_no_split(row)
    row_repeat_header(row)
    for i, (lab, w) in enumerate(zip(labels, widths)):
        cell = row.cells[i]
        cell.width = Cm(w)
        cell_shade(cell, fill)
        cell_borders(cell, top=None, bottom=(6, fill), left=None, right=None)
        cell_margins(cell, top=70, bottom=70, left=110, right=90)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(lab)
        r.font.name = F_BODY
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.color.rgb = rgb(WHITE)
    return row


def build_problemas(doc):
    table = make_table(doc, [5.6, 10.8])
    for i, (titulo, texto) in enumerate(cr.PROBLEMAS):
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(5.6)
        right.width = Cm(10.8)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=85, bottom=85, left=130, right=110)
        cell_margins(right, top=85, bottom=85, left=150, right=110)
        p = cell_par(left)
        r = p.add_run("%02d" % (i + 1))
        r.font.name = F_HEAD
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        p.paragraph_format.space_after = Pt(2)
        p2 = left.add_paragraph()
        add_runs(p2, titulo, font=F_HEAD, size=9.5, color=NAVY, bold=True)
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.1
        pr = cell_par(right)
        add_runs(pr, texto, font=F_BODY, size=9.5, color=INK)
        pr.paragraph_format.space_after = Pt(0)
        pr.paragraph_format.line_spacing = 1.15
    new_par(doc, "", space_after=4)


def build_concorrentes(doc):
    widths = cr.CONC_TABELA_COLS
    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i, w in enumerate(widths):
        table.columns[i].width = Cm(w)
    table_header(table, ["Solução", "Posicionamento", "Funcionalidades conhecidas",
                         "Preço público"], widths)
    for i, c in enumerate(cr.CONCORRENTES):
        row = table.add_row()
        row_no_split(row)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        for j, w in enumerate(widths):
            cell = row.cells[j]
            cell.width = Cm(w)
            cell_shade(cell, fill)
            cell_borders(cell, top=None, bottom=(6, LINE), left=None, right=None)
            cell_margins(cell, top=80, bottom=80, left=110, right=90)
        p = row.cells[0].paragraphs[0]
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(c["nome"])
        r.font.name = F_HEAD
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = rgb(NAVY)
        p2 = row.cells[0].add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(c["origem"])
        r2.font.name = F_BODY
        r2.font.size = Pt(7.5)
        r2.font.color.rgb = rgb(TEAL_DK)
        r2.font.bold = True

        for col, key in ((1, "posicao"), (2, "funcs"), (3, "preco")):
            p = row.cells[col].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.12
            add_runs(p, c[key], font=F_BODY,
                     size=8.2 if col != 3 else 7.8,
                     color=INK if col != 3 else MUTED)
    new_par(doc, "", space_after=6)


def build_diferenciais(doc):
    table = make_table(doc, [4.6, 11.8])
    for i, (titulo, texto) in enumerate(cr.DIFERENCIAIS):
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(4.6)
        right.width = Cm(11.8)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        cell_shade(left, fill)
        cell_shade(right, fill)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=75, bottom=75, left=130, right=110)
        cell_margins(right, top=75, bottom=75, left=150, right=110)
        p = cell_par(left)
        r = p.add_run("✓  ")
        r.font.name = F_BODY
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        r2 = p.add_run(titulo)
        r2.font.name = F_HEAD
        r2.font.size = Pt(9.3)
        r2.font.bold = True
        r2.font.color.rgb = rgb(NAVY)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        pr = cell_par(right)
        add_runs(pr, texto, font=F_BODY, size=9.3, color=INK)
        pr.paragraph_format.space_after = Pt(0)
        pr.paragraph_format.line_spacing = 1.15
    new_par(doc, "", space_after=4)


def build_tecnologias(doc):
    for area in cr.TEC_AREAS:
        h3(doc, area["titulo"] + " — " + area["cor_titulo"])
        for nome, papel in area["itens"]:
            bullet(doc, "**%s** — %s" % (nome, papel), size=9.8, indent=0.62,
                   space_after=3)
        new_par(doc, "", space_after=2)


def build_otimizacao_vs(doc):
    box = cr.OTIMIZACAO_VS_ROTEAMENTO
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i in range(2):
        table.columns[i].width = Cm(CONTENT_W / 2)
    row = table.rows[0]
    row_no_split(row)
    for i, key in enumerate(("esquerda", "direita")):
        cell = row.cells[i]
        cell.width = Cm(CONTENT_W / 2)
        cell_box(cell, fill=BG_LIGHT, accent=TEAL if i == 0 else ACCENT_BLUE)
        cell_margins(cell, top=110, bottom=110, left=150, right=150)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.18
        add_runs(p, box[key], font=F_BODY, size=9.3, color=INK)
    row2 = table.rows[1]
    row_no_split(row2)
    merged = row2.cells[0].merge(row2.cells[1])
    merged.width = Cm(CONTENT_W)
    cell_shade(merged, NAVY)
    cell_no_border(merged)
    cell_margins(merged, top=70, bottom=70, left=150, right=150)
    p = merged.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_runs(p, box["rodape"], font=F_BODY, size=9, color=WHITE, bold=True)
    new_par(doc, "", space_after=8)


def build_equipe(doc):
    widths = [3.7, 7.4, 5.3]
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i, w in enumerate(widths):
        table.columns[i].width = Cm(w)
    table_header(table, ["Frente", "Responsabilidades sugeridas", "Primeiras entregas"],
                 widths, fill=TEAL_DK)
    for i, f in enumerate(cr.EQUIPE):
        row = table.add_row()
        row_no_split(row)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        for j, w in enumerate(widths):
            cell = row.cells[j]
            cell.width = Cm(w)
            cell_shade(cell, fill)
            cell_borders(cell, top=None, bottom=(6, LINE), left=None, right=None)
            cell_margins(cell, top=85, bottom=85, left=110, right=90)
        p = row.cells[0].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        r = p.add_run("%d" % (i + 1))
        r.font.name = F_HEAD
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        p2 = row.cells[0].add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.1
        add_runs(p2, f["frente"], font=F_HEAD, size=9.3, color=NAVY, bold=True)

        p = row.cells[1].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        add_runs(p, f["resp"], font=F_BODY, size=9, color=INK)

        cell = row.cells[2]
        first = True
        for item in f["entregas"]:
            if first:
                p = cell.paragraphs[0]
                first = False
            else:
                p = cell.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.38)
            pf.first_line_indent = Cm(-0.38)
            pf.space_after = Pt(2)
            pf.line_spacing = 1.08
            pf.tab_stops.add_tab_stop(Cm(0.38), WD_TAB_ALIGNMENT.LEFT)
            r = p.add_run("•\t")
            r.font.name = F_BODY
            r.font.size = Pt(8.3)
            r.font.bold = True
            r.font.color.rgb = rgb(TEAL_DK)
            add_runs(p, item, font=F_BODY, size=8.3, color=INK)
        if cell.paragraphs:
            cell.paragraphs[-1].paragraph_format.space_after = Pt(0)
    new_par(doc, "", space_after=6)


def build_escopo(doc):
    widths = [CONTENT_W / 2, CONTENT_W / 2]
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i, w in enumerate(widths):
        table.columns[i].width = Cm(w)

    # cabeçalhos
    hdr = table.rows[0]
    row_no_split(hdr)
    for i, (lab, fill) in enumerate((("✓   No escopo do MVP", TEAL_DK),
                                     ("✕   Fora do escopo inicial", MUTED))):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        cell_shade(cell, fill)
        cell_no_border(cell)
        cell_margins(cell, top=80, bottom=80, left=140, right=120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(lab)
        r.font.name = F_HEAD
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = rgb(WHITE)

    row = table.rows[1]
    row_no_split(row)
    for i, items in enumerate((cr.MVP_DENTRO, cr.MVP_FORA)):
        cell = row.cells[i]
        cell.width = Cm(widths[i])
        cell_shade(cell, GREEN_LT if i == 0 else RED_LT)
        cell_borders(cell, top=None, bottom=(6, LINE),
                     left=(6, LINE) if i == 0 else None,
                     right=None if i == 0 else (6, LINE))
        cell_margins(cell, top=110, bottom=110, left=150, right=140)
        first = True
        for titulo, nota in items:
            if first:
                p = cell.paragraphs[0]
                first = False
            else:
                p = cell.add_paragraph()
            pf = p.paragraph_format
            pf.space_after = Pt(5)
            pf.line_spacing = 1.12
            mark = "✓  " if i == 0 else "✕  "
            r = p.add_run(mark)
            r.font.name = F_BODY
            r.font.size = Pt(9.3)
            r.font.bold = True
            r.font.color.rgb = rgb(GREEN_OK if i == 0 else RED_BAD)
            add_runs(p, "**%s** — %s" % (titulo, nota), font=F_BODY, size=9.3,
                     color=INK)
        if cell.paragraphs:
            cell.paragraphs[-1].paragraph_format.space_after = Pt(0)
    new_par(doc, "", space_after=8)


def build_demo(doc):
    callout(doc, cr.DEMO_CENARIO["titulo"], cr.DEMO_CENARIO["texto"],
            accent=TEAL, fill=BG_LIGHT)
    h2(doc, "Roteiro da demonstração")
    for i, (titulo, texto) in enumerate(cr.DEMO_PASSOS):
        numbered(doc, i + 1, "**%s.** %s" % (titulo, texto), size=9.8,
                 indent=0.85, space_after=4)
    new_par(doc, "", space_after=4)
    callout(doc, cr.DEMO_PROVA["titulo"], cr.DEMO_PROVA["texto"],
            accent=ACCENT_BLUE, fill=BG_LABEL)


def build_riscos(doc):
    widths = [4.4, 2.3, 9.7]
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for i, w in enumerate(widths):
        table.columns[i].width = Cm(w)
    table_header(table, ["Risco", "Tipo", "Estratégia de mitigação"], widths)
    tipo_cor = {
        "Técnico": TEAL_DK,
        "Técnico / comercial": AMBER_DK,
        "Comercial": RED_BAD,
        "Processo": MUTED,
    }
    for i, (risco, tipo, mit) in enumerate(cr.RISCOS):
        row = table.add_row()
        row_no_split(row)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        for j, w in enumerate(widths):
            cell = row.cells[j]
            cell.width = Cm(w)
            cell_shade(cell, fill)
            cell_borders(cell, top=None, bottom=(6, LINE), left=None, right=None)
            cell_margins(cell, top=80, bottom=80, left=110, right=90)
        p = row.cells[0].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        add_runs(p, risco, font=F_BODY, size=9, color=NAVY, bold=True)

        p = row.cells[1].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        r = p.add_run(tipo)
        r.font.name = F_BODY
        r.font.size = Pt(8)
        r.font.bold = True
        r.font.color.rgb = rgb(tipo_cor.get(tipo, MUTED))

        p = row.cells[2].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        add_runs(p, mit, font=F_BODY, size=9, color=INK)
    new_par(doc, "", space_after=6)


def build_validacao(doc):
    h2(doc, cr.VALIDACAO_TITULO)
    new_par(doc, cr.VALIDACAO_INTRO, size=10)
    for grupo, perguntas in cr.VALIDACAO_GRUPOS:
        h3(doc, grupo)
        for i, q in enumerate(perguntas):
            numbered(doc, i + 1, q, size=9.6, indent=0.8, space_after=3)
        new_par(doc, "", space_after=2)
    callout(doc, "Registro das entrevistas", cr.VALIDACAO_NOTA,
            accent=AMBER_DK, fill=AMBER_BG)


def build_decisoes(doc):
    for i, (pergunta, contexto) in enumerate(cr.DECISOES):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(8)
        pf.space_after = Pt(3)
        r = p.add_run("%d.  " % (i + 1))
        r.font.name = F_HEAD
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        r2 = p.add_run(pergunta)
        r2.font.name = F_HEAD
        r2.font.size = Pt(11)
        r2.font.bold = True
        r2.font.color.rgb = rgb(NAVY)
        keep_next(p)

        p2 = doc.add_paragraph()
        p2.paragraph_format.left_indent = Cm(0.75)
        p2.paragraph_format.space_after = Pt(6)
        p2.paragraph_format.line_spacing = 1.15
        add_runs(p2, contexto, font=F_BODY, size=9.5, color=MUTED, italic=True)
        keep_next(p2)

        p3 = doc.add_paragraph()
        p3.paragraph_format.left_indent = Cm(0.75)
        p3.paragraph_format.space_after = Pt(10)
        write_line(p3, "Resposta:")
        keep_next(p3)
        p4 = doc.add_paragraph()
        p4.paragraph_format.left_indent = Cm(0.75)
        p4.paragraph_format.space_after = Pt(12)
        write_line(p4, "Decidido por / data:")


# ---------------------------------------------------------------- seções


def build_contexto(doc):
    h1(doc, "1.", "Contexto do projeto", new_page=True)
    for txt in cr.CONTEXTO["paragrafos"]:
        new_par(doc, txt, size=10.5)
    new_par(doc, "", space_after=4)
    build_fluxo(doc)
    callout(doc, cr.COMO_LER["titulo"], cr.COMO_LER["texto"], accent=TEAL,
            fill=BG_LIGHT)


def build_publico(doc):
    h1(doc, "2.", "Público-alvo", new_page=True)
    new_par(doc, cr.PUBLICO_INTRO, size=10.5)
    h2(doc, "Segmentos de interesse (hipótese)")
    table = make_table(doc, [5.4, 11.0])
    for i, (seg, obs) in enumerate(cr.SEGMENTOS):
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(5.4)
        right.width = Cm(11.0)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        cell_shade(left, fill)
        cell_shade(right, fill)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=75, bottom=75, left=130, right=110)
        cell_margins(right, top=75, bottom=75, left=150, right=110)
        p = cell_par(left)
        add_runs(p, seg, font=F_HEAD, size=9.3, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        pr = cell_par(right)
        add_runs(pr, obs, font=F_BODY, size=9.3, color=INK)
        pr.paragraph_format.space_after = Pt(0)
        pr.paragraph_format.line_spacing = 1.15
    new_par(doc, "", space_after=6)

    h2(doc, "Perfil operacional esperado")
    callout(doc, cr.PERFIL_HIPOTESE["titulo"], cr.PERFIL_HIPOTESE["texto"],
            accent=AMBER_DK, fill=AMBER_BG)
    table = make_table(doc, [5.4, 11.0])
    for i, (chave, valor) in enumerate(cr.PERFIL_LINHAS):
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(5.4)
        right.width = Cm(11.0)
        fill = WHITE if i % 2 == 0 else BG_LIGHT
        cell_shade(left, fill)
        cell_shade(right, fill)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=70, bottom=70, left=130, right=110)
        cell_margins(right, top=70, bottom=70, left=150, right=110)
        p = cell_par(left)
        add_runs(p, chave, font=F_BODY, size=9.3, color=MUTED, bold=True)
        p.paragraph_format.space_after = Pt(0)
        pr = cell_par(right)
        add_runs(pr, valor, font=F_BODY, size=9.3, color=INK)
        pr.paragraph_format.space_after = Pt(0)
    new_par(doc, "", space_after=4)


def build_problema(doc):
    h1(doc, "3.", "Problema que queremos resolver", new_page=True)
    new_par(doc, cr.PROBLEMA_INTRO, size=10.5)
    build_problemas(doc)
    callout(doc, cr.PROBLEMA_AVISO["titulo"], cr.PROBLEMA_AVISO["texto"],
            accent=AMBER_DK, fill=AMBER_BG)


def build_concorrentes_sec(doc):
    h1(doc, "4.", "Concorrentes", new_page=True)
    new_par(doc, cr.CONC_INTRO, size=10.5)
    build_concorrentes(doc)
    callout(doc, cr.POSICIONAMENTO["titulo"], cr.POSICIONAMENTO["texto"],
            accent=TEAL, fill=BG_LIGHT)


def build_proposta(doc):
    h1(doc, "5.", "Proposta de valor e diferenciais", new_page=False)
    new_par(doc, cr.PROPOSTA_INTRO, size=10.5)
    build_diferenciais(doc)
    callout(doc, cr.PROPOSTA_AVISO["titulo"], cr.PROPOSTA_AVISO["texto"],
            accent=AMBER_DK, fill=AMBER_BG)


def build_tecnologias_sec(doc):
    h1(doc, "6.", "Tecnologias propostas", new_page=True)
    new_par(doc, cr.TEC_INTRO, size=10.5)
    build_tecnologias(doc)
    new_par(doc, "", space_after=4)
    build_arquitetura(doc)
    build_otimizacao_vs(doc)


def build_equipe_sec(doc):
    h1(doc, "7.", "Divisão da equipe", new_page=False)
    new_par(doc, cr.EQUIPE_INTRO, size=10.5)
    build_equipe(doc)
    new_par(doc, cr.EQUIPE_NOTA, size=9.5, italic=True, color=MUTED,
            space_before=4)


def build_escopo_sec(doc):
    h1(doc, "8.", "Escopo do MVP", new_page=False)
    new_par(doc, cr.ESCOPO_INTRO, size=10.5)
    build_escopo(doc)


def build_cronograma_sec(doc):
    h1(doc, "9.", "Cronograma", new_page=True)
    new_par(doc, cr.CRONO_INTRO, size=10.5)
    build_cronograma_visual(doc)
    callout(doc, cr.CRONO_AVISO["titulo"], cr.CRONO_AVISO["texto"],
            accent=AMBER_DK, fill=AMBER_BG)


def build_demo_sec(doc):
    h1(doc, "10.", "Demonstração do produto", new_page=True)
    build_demo(doc)


def build_riscos_sec(doc):
    h1(doc, "11.", "Riscos e validação", new_page=True)
    new_par(doc, cr.RISCOS_INTRO, size=10.5)
    build_riscos(doc)

    h2(doc, cr.SUCESSO_TITULO)
    for item in cr.SUCESSO:
        bullet(doc, item, size=9.7, indent=0.62, space_after=3)
    new_par(doc, "", space_after=4)

    build_validacao(doc)


def build_decisoes_sec(doc):
    h1(doc, "12.", "Decisões pendentes", new_page=True)
    new_par(doc, cr.DECISOES_INTRO, size=10.5)
    build_decisoes(doc)
    callout(
        doc,
        "Nada foi presumido",
        "As respostas acima não existem neste documento de propósito: registrá-las com "
        "informação inventada criaria falsa certeza. Cada pergunta será respondida pela "
        "equipe e anotada aqui antes do início do desenvolvimento.",
        accent=RED_BAD,
        fill=RED_LT,
    )


# ---------------------------------------------------------------- main


def build(path_saida):
    doc = Document()
    build_styles(doc)

    cover_section = doc.sections[0]
    build_cover(doc, cover_section)

    body_section = doc.add_section(WD_SECTION.NEW_PAGE)
    setup_body_section(body_section)

    add_toc(doc)

    build_contexto(doc)
    build_publico(doc)
    build_problema(doc)
    build_concorrentes_sec(doc)
    build_proposta(doc)
    build_tecnologias_sec(doc)
    build_equipe_sec(doc)
    build_escopo_sec(doc)
    build_cronograma_sec(doc)
    build_demo_sec(doc)
    build_riscos_sec(doc)
    build_decisoes_sec(doc)

    props = doc.core_properties
    props.title = "RotaCerta — Briefing do Produto e Planejamento do MVP"
    props.subject = "Plataforma B2B de otimização de rotas de entrega para pequenos negócios"
    props.author = "Equipe RotaCerta — Hack Brasil 2026"
    props.keywords = "RotaCerta, Hack Brasil 2026, MVP, roteirização, entregas, briefing"
    props.comments = (
        "Documento de trabalho. Hipóteses de público, problema, diferenciais e cronograma "
        "sujeitas a validação — não é pesquisa de mercado."
    )
    props.category = "Briefing de produto"

    doc.save(path_saida)
    return path_saida


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "rotacerta.docx"
    print("Gerado:", build(out))
