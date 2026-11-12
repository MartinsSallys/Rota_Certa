# -*- coding: utf-8 -*-
"""Atualiza o sumário (campo TOC) do DOCX via API UNO do LibreOffice e exporta o PDF."""

import os
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue

PORT = 2002


def prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def start_listener():
    proc = subprocess.Popen(
        [
            "soffice", "--headless", "--norestore", "--nofirststartwizard",
            "--nolockcheck",
            '--accept=socket,host=127.0.0.1,port=%d;urp;' % PORT,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    for _ in range(60):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext" % PORT
            )
            return proc, ctx
        except Exception:
            time.sleep(0.5)
    proc.terminate()
    raise RuntimeError("Não foi possível conectar ao LibreOffice headless.")


def main(docx_in, docx_out, pdf_out):
    proc, ctx = start_listener()
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    url = uno.systemPathToFileUrl(os.path.abspath(docx_in))
    doc = desktop.loadComponentFromURL(
        url, "_blank", 0,
        (prop("Hidden", True), prop("UpdateDocMode", 3), prop("ReadOnly", False)),
    )
    if doc is None:
        proc.terminate()
        raise RuntimeError("Falha ao abrir o documento.")

    indexes = doc.getDocumentIndexes()
    atualizados = []
    for i in range(indexes.getCount()):
        idx = indexes.getByIndex(i)
        try:
            title = idx.getTitle()
        except Exception:
            title = "?"
        idx.update()
        atualizados.append(title or "Sumário")
    print("Índices atualizados:", atualizados or "(nenhum)")

    # grava o DOCX com o sumário já preenchido
    if os.path.abspath(docx_out) != os.path.abspath(docx_in):
        doc.storeToURL(
            uno.systemPathToFileUrl(os.path.abspath(docx_out)),
            (prop("FilterName", "MS Word 2007 XML"), prop("Overwrite", True)),
        )
    else:
        doc.store()

    # exporta o PDF a partir do mesmo estado em memória
    doc.storeToURL(
        uno.systemPathToFileUrl(os.path.abspath(pdf_out)),
        (prop("FilterName", "writer_pdf_Export"), prop("Overwrite", True)),
    )
    doc.close(False)
    time.sleep(1)
    proc.terminate()
    try:
        proc.wait(timeout=15)
    except Exception:
        proc.kill()
    print("DOCX:", docx_out)
    print("PDF :", pdf_out)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("uso: atualizar_exportar.py entrada.docx saida.docx saida.pdf")
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
