# Hack Brasil 2026 — Documentos do Projeto

Repositório de documentos de trabalho da equipe para o Hack Brasil 2026. Todo o conteúdo
é gerado por scripts em Python: o texto fica isolado dos arquivos de renderização, o que
permite editar conteúdo sem mexer no layout (e vice-versa).

## Entregáveis

| Arquivo | Descrição |
|---|---|
| `entregaveis/RotaCerta_Briefing_Produto_MVP.docx` / `.pdf` | Briefing do produto RotaCerta e planejamento do MVP (15 páginas): contexto, público, problema, concorrentes, proposta de valor, tecnologias, equipe, escopo, cronograma, demonstração, riscos e decisões pendentes |
| `entregaveis/Banco_de_Ideias_MVPs_Hack_Brasil_2026.docx` / `.pdf` | Banco de 14 ideias de MVP em 7 trilhas, com comparativo e plano de validação |

## Estrutura

```
.
├── entregaveis/          # documentos finais (DOCX + PDF)
└── scripts/
    ├── gerar_documento.py      # biblioteca de estilos + gerador do Banco de Ideias
    ├── conteudo_ideias.py      # conteúdo (trilhas, ideias, comparativo)
    ├── conteudo_plano.py       # conteúdo (introdução, validação, execução)
    ├── gerar_rotacerta.py      # gerador do briefing RotaCerta
    ├── conteudo_rotacerta.py   # conteúdo do briefing RotaCerta
    └── atualizar_exportar.py   # atualiza sumário (TOC) via LibreOffice e exporta PDF
```

## Requisitos

- Python 3.10+ com `python-docx` (`pip install python-docx`)
- LibreOffice com bindings UNO (`soffice` no PATH; no Debian/Ubuntu: `python3-uno`)
- Fontes **Montserrat** e **Open Sans** instaladas (essenciais para o render do PDF):
  ```bash
  sudo apt install fonts-montserrat fonts-open-sans
  ```

## Como regenerar os documentos

O sumário é um campo do Word que só é resolvido pelo LibreOffice, por isso o processo
tem dois passos: gerar o DOCX e depois atualizar o índice + exportar o PDF.

### Briefing RotaCerta

```bash
python3 scripts/gerar_rotacerta.py /tmp/rotacerta_raw.docx
python3 scripts/atualizar_exportar.py /tmp/rotacerta_raw.docx \
  entregaveis/RotaCerta_Briefing_Produto_MVP.docx \
  entregaveis/RotaCerta_Briefing_Produto_MVP.pdf
```

### Banco de Ideias

```bash
python3 scripts/gerar_documento.py /tmp/ideias_raw.docx
python3 scripts/atualizar_exportar.py /tmp/ideias_raw.docx \
  entregaveis/Banco_de_Ideias_MVPs_Hack_Brasil_2026.docx \
  entregaveis/Banco_de_Ideias_MVPs_Hack_Brasil_2026.pdf
```

> `atualizar_exportar.py` sobe um `soffice --headless` na porta 2002, atualiza o TOC,
> salva o DOCX final e exporta o PDF. Se um LibreOffice estiver aberto, feche-o antes.

## Editar conteúdo vs. layout

- **Texto** (parágrafos, tabelas, listas): edite `conteudo_*.py`. Não há texto solto nos
  geradores — tudo vem dos módulos de conteúdo.
- **Layout** (cores, fontes, diagramas, Gantt, quebras de página): edite
  `gerar_documento.py` (biblioteca compartilhada) ou `gerar_rotacerta.py`.
- **Identidade visual**: constantes em `gerar_documento.py` (`NAVY`, `TEAL`, `F_HEAD`,
  `F_BODY`, `CONTENT_W` etc.).

## Convenções do conteúdo

- Todo número de mercado, preço ou prazo não verificado está marcado como **hipótese**
  ou vem com fonte/data de consulta. Nada de dados inventados.
- Decisões pendentes ficam com linha em branco para preenchimento manual.
- Datas do cronograma conferidas contra o calendário de 2026 (inclui fins de semana).
