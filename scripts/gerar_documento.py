# -*- coding: utf-8 -*-
"""Gera o DOCX 'Banco de Ideias de MVPs — Hack Brasil 2026'."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

import conteudo_ideias as ci
import conteudo_plano as cp

# ---------------------------------------------------------------- identidade
NAVY = "0E1B33"
INK = "243247"
MUTED = "5B6B84"
FAINT = "8A94A6"
TEAL = "00A99D"
TEAL_DK = "0B7285"
WHITE = "FFFFFF"
BG_LIGHT = "F4F6FA"
BG_LABEL = "EDF1F7"
LINE = "D9E0EA"
AMBER_DK = "B45309"
AMBER_BG = "FDF3E3"
GREEN_OK = "1E9E5A"
RED_BAD = "C0392B"

COR_AVAL = {
    ("facilidade", "Alta"): GREEN_OK,
    ("facilidade", "Média"): AMBER_DK,
    ("facilidade", "Baixa"): RED_BAD,
    ("potencial", "Alta"): GREEN_OK,
    ("potencial", "Média"): AMBER_DK,
    ("potencial", "Baixa"): MUTED,
    ("complexidade", "Alta"): RED_BAD,
    ("complexidade", "Média"): AMBER_DK,
    ("complexidade", "Baixa"): GREEN_OK,
    ("hardware", "Alta"): RED_BAD,
    ("hardware", "Média"): AMBER_DK,
    ("hardware", "Baixa"): GREEN_OK,
}

F_HEAD = "Montserrat"
F_BODY = "Open Sans"

CONTENT_W = 16.4  # cm de largura útil do corpo

# ---------------------------------------------------------------- utilidades


def rgb(hexstr):
    return RGBColor.from_string(hexstr)


def _successors(tag, names):
    return [qn(n) for n in names]


TC_BORDER_SUCC = ("w:shd", "w:noWrap", "w:tcMar", "w:textDirection", "w:tcFitText",
                  "w:vAlign", "w:hideMark")
TC_SHD_SUCC = ("w:noWrap", "w:tcMar", "w:textDirection", "w:tcFitText", "w:vAlign", "w:hideMark")
P_BDR_SUCC = ("w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
              "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
              "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
              "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
              "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl",
              "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange")
R_SHD_SUCC = ("w:fitText", "w:vertAlign", "w:rtl", "w:cs", "w:em", "w:lang",
              "w:eastAsianLayout", "w:specVanish", "w:oMath")
R_SPACING_SUCC = ("w:w", "w:kern", "w:position", "w:sz", "w:szCs", "w:highlight", "w:u",
                  "w:effect", "w:bdr", "w:shd", "w:fitText", "w:vertAlign", "w:rtl",
                  "w:cs", "w:em", "w:lang", "w:eastAsianLayout", "w:specVanish", "w:oMath")
TR_CANTSPLIT_SUCC = ("w:trHeight", "w:tblHeader", "w:tblCellSpacing", "w:jc", "w:hidden",
                     "w:ins", "w:del", "w:trPrChange")
TR_HEIGHT_SUCC = ("w:tblHeader", "w:tblCellSpacing", "w:jc", "w:hidden", "w:ins", "w:del",
                  "w:trPrChange")
TR_HEADER_SUCC = ("w:tblCellSpacing", "w:jc", "w:hidden", "w:ins", "w:del", "w:trPrChange")
SECT_PAGENUM_SUCC = ("w:cols", "w:formProt", "w:vAlign", "w:noEndnote", "w:titlePg",
                     "w:textDirection", "w:bidi", "w:rtlGutter", "w:docGrid",
                     "w:printerSettings", "w:sectPrChange")


def cell_shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.insert_element_before(shd, *TC_SHD_SUCC)


def cell_borders(cell, **edges):
    """edges: top/bottom/left/right -> (sz_eighths, color) ou None para sem borda."""
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn("w:tcBorders"))
    if old is not None:
        tcPr.remove(old)
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement("w:%s" % edge)
        spec = edges.get(edge, None)
        if spec is None:
            el.set(qn("w:val"), "nil")
        else:
            sz, color = spec
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(sz))
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), color)
        borders.append(el)
    tcPr.insert_element_before(borders, *TC_BORDER_SUCC)


def cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn("w:tcMar"))
    if old is not None:
        tcPr.remove(old)
    mar = OxmlElement("w:tcMar")
    for tag, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement("w:%s" % tag)
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tcPr.insert_element_before(mar, *TC_BORDER_SUCC)


def par_border(par, edge="bottom", sz=8, color=LINE, space=4):
    pPr = par._p.get_or_add_pPr()
    old = pPr.find(qn("w:pBdr"))
    if old is not None:
        pPr.remove(old)
    bdr = OxmlElement("w:pBdr")
    el = OxmlElement("w:%s" % edge)
    el.set(qn("w:val"), "single")
    el.set(qn("w:sz"), str(sz))
    el.set(qn("w:space"), str(space))
    el.set(qn("w:color"), color)
    bdr.append(el)
    pPr.insert_element_before(bdr, *P_BDR_SUCC)


def par_shade(par, fill):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pPr.insert_element_before(shd, *P_BDR_SUCC[1:])


def run_shade(run, fill):
    rPr = run._r.get_or_add_rPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    rPr.insert_element_before(shd, *R_SHD_SUCC)


def run_spacing(run, twentieths):
    rPr = run._r.get_or_add_rPr()
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:val"), str(twentieths))
    rPr.insert_element_before(sp, *R_SPACING_SUCC)


def row_no_split(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    trPr.insert_element_before(el, *TR_CANTSPLIT_SUCC)


def row_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    trPr.insert_element_before(el, *TR_HEADER_SUCC)


def row_height(row, cm, rule="exact"):
    row.height = Cm(cm)
    row.height_rule = (WD_ROW_HEIGHT_RULE.EXACTLY if rule == "exact"
                       else WD_ROW_HEIGHT_RULE.AT_LEAST)


def page_break_before(par):
    pPr = par._p.get_or_add_pPr()
    if pPr.find(qn("w:pageBreakBefore")) is None:
        el = OxmlElement("w:pageBreakBefore")
        pPr.insert_element_before(
            el, "w:framePr", "w:widowControl", "w:numPr", "w:suppressLineNumbers",
            "w:pBdr", "w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku",
            "w:wordWrap", "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE",
            "w:autoSpaceDN", "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing",
            "w:ind", "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
            "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl",
            "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange")


def keep_next(par):
    pPr = par._p.get_or_add_pPr()
    for tag in ("w:keepNext", "w:keepLines"):
        if pPr.find(qn(tag)) is None:
            el = OxmlElement(tag)
            pPr.insert_element_before(
                el, "w:pageBreakBefore", "w:framePr", "w:widowControl", "w:numPr",
                "w:suppressLineNumbers", "w:pBdr", "w:shd", "w:tabs", "w:suppressAutoHyphens",
                "w:kinsoku", "w:wordWrap", "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE",
                "w:autoSpaceDN", "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing",
                "w:ind", "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
                "w:textDirection", "w:textAlignment", "w:textboxTightWrap", "w:outlineLvl",
                "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr", "w:pPrChange")


def setup_style(style, font, size, bold=False, color=INK, space_before=0, space_after=6,
                line_spacing=1.15, keep=False, italic=False):
    style.font.name = font
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = italic
    style.font.color.rgb = rgb(color)
    rPr = style.element.get_or_add_rPr()
    rf = rPr.get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(attr), font)
    lang = rPr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rPr.append(lang)
    lang.set(qn("w:val"), "pt-BR")
    pf = style.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    return style


def add_runs(par, text, font=None, size=None, color=None, bold=None, italic=None,
             base_color=None, base_size=None, base_bold=False):
    """Adiciona texto com suporte simples a **negrito**."""
    for i, part in enumerate(text.split("**")):
        if part == "":
            continue
        r = par.add_run(part)
        is_bold = base_bold if bold is None else bold
        if i % 2 == 1:
            is_bold = True
        if font:
            r.font.name = font
            rPr = r._r.get_or_add_rPr()
            rf = rPr.get_or_add_rFonts()
            for attr in ("w:ascii", "w:hAnsi", "w:cs"):
                rf.set(qn(attr), font)
        if (size or base_size) is not None:
            r.font.size = Pt(size or base_size)
        col = color or base_color
        if col:
            r.font.color.rgb = rgb(col)
        r.font.bold = is_bold
        if italic:
            r.font.italic = italic
    return par


def new_par(container, text=None, style=None, size=None, color=None, bold=False,
            italic=False, align=None, space_before=None, space_after=None, font=None,
            line_spacing=None):
    p = container.add_paragraph(style=style)
    if text:
        add_runs(p, text, font=font, size=size, color=color, bold=bold, italic=italic)
    if align is not None:
        p.alignment = align
    if space_before is not None:
        p.paragraph_format.space_before = Pt(space_before)
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    if line_spacing is not None:
        p.paragraph_format.line_spacing = line_spacing
    return p


def cell_par(cell, text=None, **kwargs):
    """Parágrafo em célula reaproveitando o parágrafo vazio inicial, se houver."""
    if text is None:
        existing = [p for p in cell.paragraphs if not p.text.strip()]
        if existing:
            return existing[0]
    p = cell.add_paragraph()
    if text:
        add_runs(p, text, font=kwargs.get("font"), size=kwargs.get("size"),
                 color=kwargs.get("color"), bold=kwargs.get("bold"),
                 italic=kwargs.get("italic"))
    if kwargs.get("align") is not None:
        p.alignment = kwargs["align"]
    if kwargs.get("space_before") is not None:
        p.paragraph_format.space_before = Pt(kwargs["space_before"])
    if kwargs.get("space_after") is not None:
        p.paragraph_format.space_after = Pt(kwargs["space_after"])
    if kwargs.get("line_spacing") is not None:
        p.paragraph_format.line_spacing = kwargs["line_spacing"]
    return p


def bullet(container, text, size=10, color=INK, indent=0.62, space_after=2, bold=False):
    p = container.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent)
    pf.first_line_indent = Cm(-indent)
    pf.space_after = Pt(space_after)
    pf.line_spacing = 1.10
    pf.tab_stops.add_tab_stop(Cm(indent), WD_TAB_ALIGNMENT.LEFT)
    r = p.add_run("•\t")
    r.font.name = F_BODY
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL_DK)
    add_runs(p, text, font=F_BODY, size=size, color=color, base_bold=bold)
    return p


def numbered(container, idx, text, size=10, color=INK, indent=0.8, space_after=3):
    p = container.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(indent)
    pf.first_line_indent = Cm(-indent)
    pf.space_after = Pt(space_after)
    pf.line_spacing = 1.10
    pf.tab_stops.add_tab_stop(Cm(indent), WD_TAB_ALIGNMENT.LEFT)
    r = p.add_run("%d.\t" % idx)
    r.font.name = F_BODY
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL_DK)
    add_runs(p, text, font=F_BODY, size=size, color=color)
    return p


def bullets(container, items, **kw):
    for it in items:
        bullet(container, it, **kw)


def make_table(container, cols_cm, rows=0, borders=True):
    total = sum(cols_cm)
    table = container.add_table(rows=rows, cols=len(cols_cm))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:w"), str(int(total * 567)))
    tblW.set(qn("w:type"), "dxa")
    layout = tblPr.find(qn("w:tblLayout"))
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tblPr.append(layout)
    layout.set(qn("w:type"), "fixed")
    for i, w in enumerate(cols_cm):
        table.columns[i].width = Cm(w)
        for cell in table.columns[i].cells:
            cell.width = Cm(w)
    if borders:
        for row in table.rows:
            for i, cell in enumerate(row.cells):
                cell_borders(cell, bottom=(6, LINE))
    return table


def chip(par, text, fill, text_color=WHITE, size=8):
    r = par.add_run("  " + text + "  ")
    r.font.name = F_BODY
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = rgb(text_color)
    run_shade(r, fill)
    run_spacing(r, 12)
    return r


def add_field(par, instr, display="1"):
    r = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    r._r.append(fld)
    r = par.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = instr
    r._r.append(it)
    r = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "separate")
    r._r.append(fld)
    r = par.add_run(display)
    r2 = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "end")
    r2._r.append(fld)
    for run in par.runs:
        run.font.name = F_BODY
        run.font.size = Pt(8.5)
        run.font.color.rgb = rgb(FAINT)


def add_toc_field(par):
    r = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    fld.set(qn("w:dirty"), "true")
    r._r.append(fld)
    r = par.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = ' TOC \\o "1-2" \\h \\z \\u '
    r._r.append(it)
    r = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "separate")
    r._r.append(fld)
    r = par.add_run("[Sumário será atualizado automaticamente — em Word, use F9 para atualizar.]")
    r.font.name = F_BODY
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = rgb(MUTED)
    r2 = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "end")
    r2._r.append(fld)


# ---------------------------------------------------------------- estilos


def build_styles(doc):
    setup_style(doc.styles["Normal"], F_BODY, 10.5, color=INK, space_after=6,
                line_spacing=1.18)
    h1 = setup_style(doc.styles["Heading 1"], F_HEAD, 17, bold=True, color=NAVY,
                     space_before=4, space_after=12, line_spacing=1.05)
    h1.paragraph_format.keep_with_next = True
    h2 = setup_style(doc.styles["Heading 2"], F_HEAD, 12.5, bold=True, color=NAVY,
                     space_before=16, space_after=7, line_spacing=1.1)
    h2.paragraph_format.keep_with_next = True
    h3 = setup_style(doc.styles["Heading 3"], F_HEAD, 11, bold=True, color=TEAL_DK,
                     space_before=12, space_after=5, line_spacing=1.1)
    h3.paragraph_format.keep_with_next = True
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        doc.styles[name].font.name = F_HEAD
    # o LibreOffice ignora tabulações do parágrafo quando o estilo define as suas
    for name in ("Footer", "Header"):
        st = doc.styles[name]
        pPr = st.element.get_or_add_pPr()
        tabs = pPr.find(qn("w:tabs"))
        if tabs is not None:
            pPr.remove(tabs)


def h1(doc, number, title, new_page=False):
    p = doc.add_paragraph(style="Heading 1")
    if new_page:
        page_break_before(p)
    r = p.add_run("%s " % number)
    r.font.name = F_HEAD
    r.font.size = Pt(17)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL)
    r2 = p.add_run(title)
    r2.font.name = F_HEAD
    r2.font.size = Pt(17)
    r2.font.bold = True
    r2.font.color.rgb = rgb(NAVY)
    par_border(p, "bottom", sz=10, color=LINE, space=6)
    keep_next(p)
    return p


def h2(doc, title):
    p = doc.add_paragraph(title, style="Heading 2")
    keep_next(p)
    return p


def h3(doc, title):
    p = doc.add_paragraph(title, style="Heading 3")
    keep_next(p)
    return p


def callout(doc, titulo, texto, accent=TEAL, fill=BG_LIGHT):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    table.columns[0].width = Cm(CONTENT_W)
    cell = table.rows[0].cells[0]
    cell.width = Cm(CONTENT_W)
    cell_shade(cell, fill)
    cell_borders(cell, left=(24, accent), top=None, bottom=None, right=None)
    cell_margins(cell, top=110, bottom=110, left=170, right=170)
    p0 = cell.paragraphs[0]
    add_runs(p0, titulo, font=F_HEAD, size=10, color=NAVY, bold=True)
    p0.paragraph_format.space_after = Pt(3)
    p = cell.add_paragraph()
    add_runs(p, texto, font=F_BODY, size=9.5, color=INK)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    row_no_split(table.rows[0])
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return table


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
    cell_borders(cell, top=None, bottom=None, left=None, right=None)
    cell_margins(cell, top=210, bottom=170, left=340, right=340)

    p = cell.paragraphs[0]
    r = p.add_run("DOCUMENTO DE TRABALHO")
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
    r = p.add_run("Banco de Ideias de MVPs")
    r.font.name = F_HEAD
    r.font.size = Pt(33)
    r.font.bold = True
    r.font.color.rgb = rgb(WHITE)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.02

    p = cell.add_paragraph()
    r = p.add_run("Hack Brasil 2026")
    r.font.name = F_HEAD
    r.font.size = Pt(33)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.02

    p = cell.add_paragraph()
    r = p.add_run("14 ideias de produtos para as 7 trilhas da competição")
    r.font.name = F_BODY
    r.font.size = Pt(14.5)
    r.font.color.rgb = rgb("C9D4E4")
    p.paragraph_format.space_after = Pt(16)

    p = cell.add_paragraph()
    par_border(p, "bottom", sz=16, color=TEAL, space=2)
    p.paragraph_format.space_after = Pt(14)

    p = cell.add_paragraph()
    r = p.add_run(
        "Material de apoio para escolha, validação e construção de um MVP durante a competição — "
        "com fichas detalhadas, comparativo, plano de validação com clientes e plano de execução "
        "para uma equipe de três pessoas."
    )
    r.font.name = F_BODY
    r.font.size = Pt(11)
    r.font.color.rgb = rgb("9FADC3")
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(0)

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(300)

    # faixa das sete trilhas
    stripe = cell.add_table(rows=1, cols=7)
    stripe.autofit = False
    widths = [14.0 / 7.0] * 7
    for i, tr in enumerate(ci.TRILHAS):
        w = widths[i]
        stripe.columns[i].width = Cm(w)
        c = stripe.rows[0].cells[i]
        c.width = Cm(w)
        cell_shade(c, tr["cor"])
        cell_borders(c, top=None, bottom=None, left=None, right=None)
        cell_margins(c, top=0, bottom=0, left=0, right=0)
        cp_par = c.paragraphs[0]
        cp_par.paragraph_format.space_after = Pt(0)
        cp_par.paragraph_format.space_before = Pt(0)
        rr = cp_par.add_run(" ")
        rr.font.size = Pt(5)
    sr = stripe.rows[0]
    sr.height = Cm(0.32)
    sr.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY

    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)

    p = cell.add_paragraph()
    r = p.add_run("As sete trilhas da competição · 14 ideias de produto")
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.color.rgb = rgb("7E8CA6")
    run_spacing(r, 20)
    p.paragraph_format.space_after = Pt(10)

    p = cell.add_paragraph()
    r = p.add_run("Versão 1.0 · Novembro de 2026 · Uso interno da equipe")
    r.font.name = F_BODY
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = rgb("9FADC3")
    p.paragraph_format.space_after = Pt(0)

    p = cell.add_paragraph()
    r = p.add_run("Hipóteses comerciais sujeitas a validação — não é pesquisa de mercado.")
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

    # numeração contínua a partir da capa: mantém sumário, rodapé e total de páginas coerentes

    header = section.header
    header.is_linked_to_previous = False
    for p in list(header.paragraphs)[1:]:
        p._element.getparent().remove(p._element)
    hp = header.paragraphs[0]
    for r in list(hp.runs):
        r._element.getparent().remove(r._element)
    hp.text = ""
    r = hp.add_run("BANCO DE IDEIAS DE MVPs  ·  HACK BRASIL 2026")
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
    r = fp.add_run("Documento de trabalho · hipóteses sujeitas a validação\t")
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


def add_toc(doc):
    p = doc.add_paragraph()
    r = p.add_run("Sumário")
    r.font.name = F_HEAD
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = rgb(NAVY)
    p.paragraph_format.space_after = Pt(4)
    par_border(p, "bottom", sz=10, color=TEAL, space=6)

    p = doc.add_paragraph()
    r = p.add_run(
        "Se as páginas mudarem após edições, clique com o botão direito sobre o sumário e escolha "
        "“Atualizar campo”."
    )
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.italic = True
    r.font.color.rgb = rgb(MUTED)
    p.paragraph_format.space_after = Pt(10)

    p = doc.add_paragraph()
    add_toc_field(p)
    p.paragraph_format.space_after = Pt(0)


def build_intro(doc):
    h1(doc, "1.", "Introdução", new_page=True)
    for txt in cp.INTRODUCAO["paragrafos"]:
        new_par(doc, txt, size=10.5)
    callout(doc, cp.AVISO["titulo"], cp.AVISO["texto"], accent=AMBER_DK, fill=AMBER_BG)

    h2(doc, "Critérios de seleção das ideias")
    new_par(doc, "As cinco condições abaixo foram aplicadas a todas as propostas:", size=10.5)
    table = make_table(doc, [5.2, 11.2])
    for i, crit in enumerate(cp.INTRODUCAO["criterios"]):
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(5.2)
        right.width = Cm(11.2)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=90, bottom=90, left=140, right=120)
        cell_margins(right, top=90, bottom=90, left=160, right=120)
        p = cell_par(left)
        r = p.add_run("%02d" % (i + 1))
        r.font.name = F_HEAD
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        p.paragraph_format.space_after = Pt(2)
        p2 = left.add_paragraph()
        add_runs(p2, crit["titulo"], font=F_HEAD, size=9.5, color=NAVY, bold=True)
        p2.paragraph_format.space_after = Pt(0)
        p2.paragraph_format.line_spacing = 1.1
        pr = cell_par(right)
        add_runs(pr, crit["texto"], font=F_BODY, size=9.5, color=INK)
        pr.paragraph_format.space_after = Pt(0)
        pr.paragraph_format.line_spacing = 1.15
    new_par(doc, "", space_after=6)

    h2(doc, "Como usar este documento")
    bullets(doc, cp.INTRODUCAO["como_usar"], size=10)
    new_par(doc, cp.INTRODUCAO["nao_e"], size=10, italic=True, color=MUTED,
            space_before=8)


def build_trilhas(doc):
    h1(doc, "2.", "As sete trilhas e suas 14 ideias", new_page=True)
    new_par(
        doc,
        "Cada trilha da competição aparece abaixo com um contexto breve e as duas ideias propostas. "
        "As descrições desta seção são o resumo executivo: o detalhamento de problema, escopo, "
        "monetização, riscos e validação de cada proposta está na seção 3.",
        size=10.5,
    )
    for tr in ci.TRILHAS:
        table = doc.add_table(rows=1, cols=2)
        table.autofit = False
        w_num, w_rest = 1.5, CONTENT_W - 1.5
        table.columns[0].width = Cm(w_num)
        table.columns[1].width = Cm(w_rest)
        row = table.rows[0]
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(w_num)
        right.width = Cm(w_rest)
        left.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        right.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        cell_shade(left, tr["cor"])
        cell_borders(left, top=None, bottom=None, left=None, right=None)
        cell_margins(left, top=80, bottom=80, left=40, right=40)
        pl = left.paragraphs[0]
        pl.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = pl.add_run("0%d" % tr["n"])
        r.font.name = F_HEAD
        r.font.size = Pt(18)
        r.font.bold = True
        r.font.color.rgb = rgb(WHITE)
        pl.paragraph_format.space_after = Pt(0)

        cell_shade(right, BG_LIGHT)
        cell_borders(right, top=None, bottom=None, left=None, right=None)
        cell_margins(right, top=90, bottom=90, left=170, right=140)
        pr = right.paragraphs[0]
        r = pr.add_run("TRILHA %d" % tr["n"])
        r.font.name = F_BODY
        r.font.size = Pt(7.5)
        r.font.bold = True
        r.font.color.rgb = rgb(tr["cor"])
        run_spacing(r, 30)
        pr.paragraph_format.space_after = Pt(2)
        title = doc_add_h2_in(pr, "Trilha %d — %s" % (tr["n"], tr["nome"]), tr["cor"])
        pc = right.add_paragraph()
        add_runs(pc, tr["contexto"], font=F_BODY, size=9.5, color=INK)
        pc.paragraph_format.space_after = Pt(0)
        pc.paragraph_format.line_spacing = 1.15

        for ideia in [i for i in ci.IDEIAS if i["trilha"] == tr["n"]]:
            build_resumo_ideia(doc, ideia, tr["cor"])
    return


def doc_add_h2_in(par, text, color=NAVY):
    """Cria um parágrafo Heading 2 logo após o parágrafo informado (dentro de célula)."""
    p = OxmlElement("w:p")
    par._p.addnext(p)
    from docx.text.paragraph import Paragraph

    newp = Paragraph(p, par._parent)
    newp.style = "Heading 2"
    r = newp.add_run(text)
    r.font.name = F_HEAD
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = rgb(color)
    newp.paragraph_format.space_before = Pt(0)
    newp.paragraph_format.space_after = Pt(3)
    keep_next(newp)
    return newp


def build_resumo_ideia(doc, ideia, cor):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(9)
    pf.space_after = Pt(2)
    pf.left_indent = Cm(0.0)
    r = p.add_run("%02d  " % ideia["num"])
    r.font.name = F_HEAD
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = rgb(cor)
    r = p.add_run(ideia["nome"])
    r.font.name = F_HEAD
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = rgb(NAVY)
    r = p.add_run("  —  " + ideia["tagline"])
    r.font.name = F_BODY
    r.font.size = Pt(10)
    r.font.color.rgb = rgb(MUTED)
    keep_next(p)
    pd = doc.add_paragraph()
    pd.paragraph_format.left_indent = Cm(1.0)
    pd.paragraph_format.space_after = Pt(6)
    pd.paragraph_format.line_spacing = 1.15
    add_runs(pd, ideia["descricao"], font=F_BODY, size=9.8, color=INK)


def build_fichas(doc):
    h1(doc, "3.", "Ficha detalhada de cada ideia", new_page=True)
    new_par(
        doc,
        "As 14 fichas seguem o mesmo formato, para permitir comparação honesta entre as propostas. "
        "Cada uma traz o problema, o público, o funcionamento, o que entra e o que fica de fora do MVP, "
        "tecnologias, comprador, monetização, diferenciais, riscos, ressalvas regulatórias e o caminho "
        "de validação antes do desenvolvimento. As linhas de monetização são sempre hipóteses: preço, "
        "formato de cobrança e canal de venda precisam ser confirmados em conversas com clientes.",
        size=10.5,
    )
    for ideia in ci.IDEIAS:
        build_ficha(doc, ideia)


def build_ficha(doc, ideia):
    tr = ci.TRILHAS[ideia["trilha"] - 1]
    p = doc.add_paragraph()
    r = p.add_run("FICHA %02d" % ideia["num"])
    r.font.name = F_BODY
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = rgb(TEAL)
    run_spacing(r, 40)
    p.paragraph_format.space_after = Pt(3)
    keep_next(p)

    h2(doc, "%02d · %s" % (ideia["num"], ideia["nome"]))

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    keep_next(p)
    chip(p, "TRILHA %d · %s" % (tr["n"], tr["nome"].upper()), tr["cor"], size=7.5)
    r = p.add_run("   " + ideia["tagline"])
    r.font.name = F_BODY
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = rgb(MUTED)

    linhas = [
        ("Descrição do produto", ideia["descricao"], "text"),
        ("Problema que resolve", ideia["problema"], "text"),
        ("Público-alvo", ideia["publico"], "text"),
        ("Como funciona a solução", ideia["como_funciona"], "text"),
        ("Funcionalidades essenciais do MVP", ideia["mvp"], "list"),
        ("O que NÃO deve entrar na primeira versão", ideia["fora"], "list"),
        ("Tecnologias sugeridas", ideia["tecnologias"], "list"),
        ("Quem pagaria pelo produto", ideia["quem_pagaria"], "text"),
        ("Modelo de monetização", ideia["monetizacao"], "money"),
        ("Diferenciais e possíveis riscos", (ideia["diferenciais"], ideia["riscos"]), "split"),
        ("Como validar a demanda antes de desenvolver", ideia["validacao"], "list"),
        ("Ressalvas de segurança, privacidade e regulamentação", ideia["ressalvas"], "warn"),
    ]

    table = make_table(doc, [4.6, CONTENT_W - 4.6])
    w_lab, w_val = 4.6, CONTENT_W - 4.6
    for rotulo, valor, tipo in linhas:
        row = table.add_row()
        row_no_split(row)
        lab, val = row.cells
        lab.width = Cm(w_lab)
        val.width = Cm(w_val)
        cell_shade(lab, BG_LABEL)
        cell_borders(lab, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(val, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(lab, top=85, bottom=85, left=130, right=110)
        cell_margins(val, top=85, bottom=85, left=150, right=110)
        lab.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        val.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        pl = cell_par(lab)
        add_runs(pl, rotulo, font=F_HEAD, size=9, color=NAVY, bold=True)
        pl.paragraph_format.space_after = Pt(0)
        pl.paragraph_format.line_spacing = 1.1

        if tipo in ("text", "warn"):
            if tipo == "warn":
                p0 = cell_par(val)
                chip(p0, "SEGURANÇA E CONFORMIDADE", AMBER_DK, text_color=WHITE, size=6.5)
                p0.paragraph_format.space_after = Pt(3)
                pv = val.add_paragraph()
            else:
                pv = cell_par(val)
            add_runs(pv, valor, font=F_BODY, size=9.5, color=INK)
            pv.paragraph_format.space_after = Pt(0)
            pv.paragraph_format.line_spacing = 1.15
        elif tipo == "list":
            first = True
            for item in valor:
                if first:
                    p = val.paragraphs[0] if not val.paragraphs[0].text.strip() else val.add_paragraph()
                    first = False
                    pf = p.paragraph_format
                    pf.left_indent = Cm(0.5)
                    pf.first_line_indent = Cm(-0.5)
                    pf.space_after = Pt(2)
                    pf.line_spacing = 1.1
                    pf.tab_stops.add_tab_stop(Cm(0.5), WD_TAB_ALIGNMENT.LEFT)
                    r = p.add_run("•\t")
                    r.font.name = F_BODY
                    r.font.size = Pt(9.5)
                    r.font.bold = True
                    r.font.color.rgb = rgb(TEAL_DK)
                    add_runs(p, item, font=F_BODY, size=9.5, color=INK)
                else:
                    bullet(val, item, size=9.5, indent=0.5, space_after=2)
            if val.paragraphs:
                val.paragraphs[-1].paragraph_format.space_after = Pt(0)
        elif tipo == "money":
            p0 = cell_par(val)
            chip(p0, "HIPÓTESE A VALIDAR", AMBER_DK, size=7)
            p0.paragraph_format.space_after = Pt(3)
            pv = val.add_paragraph()
            add_runs(pv, valor, font=F_BODY, size=9.5, color=INK)
            pv.paragraph_format.space_after = Pt(0)
            pv.paragraph_format.line_spacing = 1.15
        elif tipo == "split":
            dif, risc = valor
            p0 = cell_par(val)
            r = p0.add_run("Diferenciais: ")
            r.font.name = F_BODY
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = rgb(GREEN_OK)
            add_runs(p0, dif, font=F_BODY, size=9.5, color=INK)
            p0.paragraph_format.space_after = Pt(4)
            p0.paragraph_format.line_spacing = 1.15
            p1 = val.add_paragraph()
            r = p1.add_run("Riscos: ")
            r.font.name = F_BODY
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = rgb(RED_BAD)
            add_runs(p1, risc, font=F_BODY, size=9.5, color=INK)
            p1.paragraph_format.space_after = Pt(0)
            p1.paragraph_format.line_spacing = 1.15

    new_par(doc, "", space_after=0)


def build_comparativo(doc):
    h1(doc, "4.", "Comparativo das 14 ideias", new_page=True)
    new_par(
        doc,
        "A tabela abaixo padroniza a leitura das 14 propostas nos mesmos quatro eixos. Ela serve para "
        "reduzir o campo de escolha, não para escolher sozinha: uma ideia de complexidade técnica baixa "
        "pode ter comprador fraco, e uma ideia de potencial alto pode ser inviável dentro do prazo da "
        "equipe.",
        size=10.5,
    )
    callout(
        doc,
        "Como interpretar esta tabela",
        "As avaliações em baixa, média e alta são estimativas iniciais da equipe, construídas a partir "
        "da leitura do problema e do escopo proposto — não são resultados de pesquisa de mercado, "
        "levantamento de dados ou benchmarking. Servem para ordenar a conversa e devem ser revistas "
        "depois das entrevistas com clientes.",
        accent=TEAL,
        fill=BG_LIGHT,
    )

    widths = [3.3, 3.5, 2.4, 2.4, 2.4, 2.4]
    headers = [
        "Ideia",
        "Trilha",
        "Facilidade do MVP",
        "Potencial comercial",
        "Complexidade técnica",
        "Hardware / integrações",
    ]
    table = make_table(doc, widths, rows=1, borders=False)
    hdr = table.rows[0]
    row_repeat_header(hdr)
    row_no_split(hdr)
    for i, cell in enumerate(hdr.cells):
        cell.width = Cm(widths[i])
        cell_shade(cell, NAVY)
        cell_borders(cell, bottom=None, top=None, left=None, right=None)
        cell_margins(cell, top=90, bottom=90, left=90, right=90)
        p = cell.paragraphs[0]
        add_runs(p, headers[i], font=F_HEAD, size=8.3, color=WHITE, bold=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i >= 2 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05

    for idx, ideia in enumerate(ci.IDEIAS):
        facil, poten, comp, hard = ci.COMPARATIVO[ideia["num"]]
        tr = ci.TRILHAS[ideia["trilha"] - 1]
        row = table.add_row()
        row_no_split(row)
        vals = [
            ("%02d · %s" % (ideia["num"], ideia["nome"]), None),
            ("%d · %s" % (tr["n"], tr["nome"]), None),
            (facil, COR_AVAL[("facilidade", facil)]),
            (poten, COR_AVAL[("potencial", poten)]),
            (comp, COR_AVAL[("complexidade", comp)]),
            (hard, COR_AVAL[("hardware", hard)]),
        ]
        bg = WHITE if idx % 2 == 0 else BG_LIGHT
        for i, cell in enumerate(row.cells):
            cell.width = Cm(widths[i])
            cell_shade(cell, bg)
            cell_borders(cell, bottom=(6, LINE), top=None, left=None, right=None)
            cell_margins(cell, top=75, bottom=75, left=90, right=90)
            txt, cor = vals[i]
            p = cell.paragraphs[0]
            add_runs(
                p, txt, font=F_BODY, size=8.6,
                color=cor if cor else (NAVY if i == 0 else INK),
                bold=bool(cor) or i == 0,
            )
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i >= 2 else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05

    new_par(doc, "", space_after=4)
    h2(doc, "Legenda dos critérios")
    table = make_table(doc, [4.8, 11.6])
    for titulo, texto in ci.LEGENDA_COMPARATIVO:
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(4.8)
        right.width = Cm(11.6)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=80, bottom=80, left=130, right=110)
        cell_margins(right, top=80, bottom=80, left=150, right=110)
        p = cell_par(left)
        add_runs(p, titulo, font=F_HEAD, size=9, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        p = cell_par(right)
        add_runs(p, texto, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
    new_par(
        doc,
        "Correspondência de leitura: na coluna “facilidade”, verde é melhor; nas colunas de "
        "complexidade e dependência externa, verde é melhor e vermelho indica esforço maior.",
        size=9, italic=True, color=MUTED, space_before=6,
    )


def build_prioridades(doc):
    h1(doc, "5.", "Cinco ideias prioritárias", new_page=True)
    new_par(
        doc,
        "A seleção abaixo não declara que as cinco ideias serão construídas — declara que merecem "
        "investigação primeiro. Elas combinam dor financeira ou de risco claramente percebida, comprador "
        "identificável e um caminho curto até o primeiro contato com cliente. As demais nove ideias "
        "permanecem no banco e podem assumir o lugar de qualquer uma delas assim que as entrevistas "
        "mostrarem outra realidade.",
        size=10.5,
    )
    for pos, pr in enumerate(ci.PRIORIDADES):
        ideia = next(i for i in ci.IDEIAS if i["num"] == pr["num"])
        tr = ci.TRILHAS[ideia["trilha"] - 1]
        ph = h2(doc, "%02d · %s" % (ideia["num"], pr["nome"]))
        if pos > 0:
            page_break_before(ph)
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        keep_next(p)
        chip(p, "TRILHA %d · %s" % (tr["n"], tr["nome"].upper()), tr["cor"], size=7.5)
        r = p.add_run("   " + pr["resumo"])
        r.font.name = F_BODY
        r.font.size = Pt(10)
        r.font.italic = True
        r.font.color.rgb = rgb(MUTED)

        h3(doc, "Por que merece investigação")
        bullets(doc, pr["por_que"], size=9.8)
        h3(doc, "Principais dificuldades")
        bullets(doc, pr["dificuldades"], size=9.8)
        h3(doc, "Caminho para os primeiros clientes")
        for i, item in enumerate(pr["caminho"], start=1):
            numbered(doc, i, item, size=9.8)


def build_validacao(doc):
    h1(doc, "6.", "Plano de validação com potenciais clientes", new_page=True)
    new_par(doc, cp.VALIDACAO_INTRO, size=10.5)

    h2(doc, "6.1 Roteiro em seis etapas")
    widths = [4.4, 7.4, 4.6]
    table = make_table(doc, widths, rows=1, borders=False)
    hdr = table.rows[0]
    row_repeat_header(hdr)
    row_no_split(hdr)
    for i, txt in enumerate(["Etapa", "O que fazer", "Entregável esperado"]):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        cell_shade(cell, NAVY)
        cell_borders(cell, top=None, bottom=None, left=None, right=None)
        cell_margins(cell, top=90, bottom=90, left=110, right=110)
        p = cell.paragraphs[0]
        add_runs(p, txt, font=F_HEAD, size=9, color=WHITE, bold=True)
        p.paragraph_format.space_after = Pt(0)
    for idx, (titulo, fazer, entrega) in enumerate(cp.VALIDACAO_ETAPAS, start=1):
        row = table.add_row()
        row_no_split(row)
        bg = WHITE if idx % 2 else BG_LIGHT
        cells = row.cells
        for i, w in enumerate(widths):
            cells[i].width = Cm(w)
            cell_shade(cells[i], bg)
            cell_borders(cells[i], bottom=(6, LINE), top=None, left=None, right=None)
            cell_margins(cells[i], top=85, bottom=85, left=110, right=110)
        p = cell_par(cells[0])
        r = p.add_run("%d. " % idx)
        r.font.name = F_HEAD
        r.font.size = Pt(9.3)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL)
        add_runs(p, titulo, font=F_HEAD, size=9.3, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        p = cell_par(cells[1])
        add_runs(p, fazer, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        p = cell_par(cells[2])
        add_runs(p, entrega, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15

    h2(doc, "6.2 Regras para as entrevistas")
    bullets(doc, cp.REGRAS_ENTREVISTA, size=10)

    h2(doc, "6.3 Perguntas para as entrevistas")
    new_par(
        doc,
        "O roteiro abaixo pode ser lido literalmente. As perguntas do bloco D só aparecem depois que o "
        "problema e o custo atual já foram entendidos.",
        size=10,
    )
    for titulo, perguntas in cp.PERGUNTAS_GRUPOS:
        h3(doc, titulo)
        for i, q in enumerate(perguntas, start=1):
            numbered(doc, i, q, size=9.8)

    h2(doc, "6.4 Ficha de registro de cada entrevista")
    table = make_table(doc, [4.4, 12.0])
    for campo, desc in cp.FICHA_ENTREVISTA:
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(4.4)
        right.width = Cm(12.0)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=80, bottom=80, left=130, right=110)
        cell_margins(right, top=80, bottom=80, left=150, right=110)
        p = cell_par(left)
        add_runs(p, campo, font=F_HEAD, size=9, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p = cell_par(right)
        add_runs(p, desc, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)

    h2(doc, "6.5 Como escolher as três finalistas")
    new_par(
        doc,
        "Depois das entrevistas, a equipe se reúne por no máximo uma hora e aplica os critérios abaixo. "
        "A decisão fica registrada por escrito — com a razão de cada escolha — antes de qualquer código.",
        size=10,
    )
    bullets(doc, cp.FINALISTAS_CRITERIOS, size=10)


def build_execucao(doc):
    h1(doc, "7.", "Plano de execução do MVP", new_page=True)
    new_par(doc, cp.EXECUCAO_INTRO, size=10.5)

    h2(doc, "7.1 Metodologia em sete etapas")
    for etapa in cp.EXECUCAO_ETAPAS:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        keep_next(p)
        r = p.add_run(etapa["titulo"])
        r.font.name = F_HEAD
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = rgb(NAVY)
        r2 = p.add_run("   " + etapa["duracao"])
        r2.font.name = F_BODY
        r2.font.size = Pt(9)
        r2.font.italic = True
        r2.font.color.rgb = rgb(TEAL_DK)
        par_border(p, "bottom", sz=6, color=LINE, space=3)

        new_par(doc, etapa["objetivo"], size=10, space_after=5)
        bullets(doc, etapa["atividades"], size=9.8)
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(0.3)
        r = p.add_run("Entregável: ")
        r.font.name = F_BODY
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = rgb(TEAL_DK)
        add_runs(p, etapa["entregavel"], font=F_BODY, size=9.5, color=INK, italic=True)

    h2(doc, "7.2 Divisão de papéis em três pessoas")
    table = make_table(doc, [4.8, 11.6])
    for papel, desc in cp.PAPELS:
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(4.8)
        right.width = Cm(11.6)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=85, bottom=85, left=130, right=110)
        cell_margins(right, top=85, bottom=85, left=150, right=110)
        p = cell_par(left)
        add_runs(p, papel, font=F_HEAD, size=9, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        p = cell_par(right)
        add_runs(p, desc, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15

    h2(doc, "7.3 Cronograma de referência")
    new_par(
        doc,
        "As durações abaixo são orientativas e devem ser ajustadas à janela real da competição. A ordem "
        "não muda: validação antes de escopo, escopo antes de arquitetura e código antes de polimento.",
        size=10,
    )
    widths = [5.0, 3.0, 8.4]
    table = make_table(doc, widths, rows=1, borders=False)
    hdr = table.rows[0]
    row_repeat_header(hdr)
    row_no_split(hdr)
    for i, txt in enumerate(["Etapa", "Duração", "Sinal de saída"]):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        cell_shade(cell, NAVY)
        cell_borders(cell, top=None, bottom=None, left=None, right=None)
        cell_margins(cell, top=90, bottom=90, left=110, right=110)
        p = cell.paragraphs[0]
        add_runs(p, txt, font=F_HEAD, size=9, color=WHITE, bold=True)
        p.paragraph_format.space_after = Pt(0)
    for idx, (etapa, dur, saida) in enumerate(cp.CRONOGRAMA):
        row = table.add_row()
        row_no_split(row)
        bg = WHITE if idx % 2 == 0 else BG_LIGHT
        cells = row.cells
        for i, w in enumerate(widths):
            cells[i].width = Cm(w)
            cell_shade(cells[i], bg)
            cell_borders(cells[i], bottom=(6, LINE), top=None, left=None, right=None)
            cell_margins(cells[i], top=80, bottom=80, left=110, right=110)
        p = cell_par(cells[0])
        add_runs(p, etapa, font=F_BODY, size=9.3, color=NAVY, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p = cell_par(cells[1])
        add_runs(p, dur, font=F_BODY, size=9.3, color=TEAL_DK, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p = cell_par(cells[2])
        add_runs(p, saida, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12

    h2(doc, "7.4 Critérios de “pronto”")
    bullets(doc, cp.CRITERIOS_PRONTO, size=10)

    h2(doc, "7.5 Riscos do time e como mitigar")
    table = make_table(doc, [4.8, 11.6])
    for risco, mitigacao in cp.RISCOS_TIME:
        row = table.add_row()
        row_no_split(row)
        left, right = row.cells
        left.width = Cm(4.8)
        right.width = Cm(11.6)
        cell_shade(left, BG_LABEL)
        cell_borders(left, bottom=(6, LINE), left=None, right=(6, LINE), top=None)
        cell_borders(right, bottom=(6, LINE), left=None, right=None, top=None)
        cell_margins(left, top=80, bottom=80, left=130, right=110)
        cell_margins(right, top=80, bottom=80, left=150, right=110)
        p = cell_par(left)
        add_runs(p, risco, font=F_HEAD, size=9, color=RED_BAD, bold=True)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.12
        p = cell_par(right)
        add_runs(p, mitigacao, font=F_BODY, size=9.3, color=INK)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15


def build_conclusao(doc):
    h1(doc, "8.", "Conclusão", new_page=True)
    for txt in cp.CONCLUSAO:
        new_par(doc, txt, size=10.5)

    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    table.columns[0].width = Cm(CONTENT_W)
    cell = table.rows[0].cells[0]
    cell.width = Cm(CONTENT_W)
    cell_shade(cell, BG_LIGHT)
    cell_borders(cell, left=(24, TEAL), top=None, bottom=None, right=None)
    cell_margins(cell, top=130, bottom=130, left=170, right=170)
    p = cell.paragraphs[0]
    add_runs(p, "Antes de escrever a primeira linha de código", font=F_HEAD, size=10.5,
             color=NAVY, bold=True)
    p.paragraph_format.space_after = Pt(6)
    for item in cp.CHECKLIST_FINAL:
        bullet(cell, item, size=9.6, indent=0.55, space_after=3)
    if cell.paragraphs:
        cell.paragraphs[-1].paragraph_format.space_after = Pt(0)

    new_par(
        doc,
        "Escolhido o problema, escolhido o cliente e escrito o escopo, o time pode programar com "
        "consciência do que está provando. Boa competição — e boa validação.",
        size=10.5, italic=True, color=MUTED, space_before=10,
    )


# ---------------------------------------------------------------- main


def build(path_saida):
    doc = Document()
    build_styles(doc)

    # capa
    cover_section = doc.sections[0]
    build_cover(doc, cover_section)

    # corpo
    body_section = doc.add_section(WD_SECTION.NEW_PAGE)
    setup_body_section(body_section)

    add_toc(doc)

    build_intro(doc)
    build_trilhas(doc)
    build_fichas(doc)
    build_comparativo(doc)
    build_prioridades(doc)
    build_validacao(doc)
    build_execucao(doc)
    build_conclusao(doc)

    props = doc.core_properties
    props.title = "Banco de Ideias de MVPs — Hack Brasil 2026"
    props.subject = "14 ideias de produtos para as 7 trilhas da competição"
    props.author = "Equipe Hack Brasil 2026"
    props.keywords = "MVP, Hack Brasil 2026, startups, inovação, trilhas"
    props.comments = (
        "Documento de trabalho. Avaliações e preços são hipóteses a validar, "
        "não resultados de pesquisa de mercado."
    )
    props.category = "Documento de trabalho"

    doc.save(path_saida)
    return path_saida


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "documento.docx"
    print("Gerado:", build(out))
