# -*- coding: utf-8 -*-
"""Conteúdo do briefing do produto RotaCerta (Hack Brasil 2026)."""

META = {
    "evento": "HACK BRASIL 2026",
    "versao": "Versão 1.0 · 11 de novembro de 2026 · Documento de trabalho da equipe",
    "tagline": "Planeje, otimize, execute e acompanhe as entregas do seu negócio.",
    "descricao_capa": (
        "Plataforma B2B de otimização e gerenciamento de rotas de entrega para pequenos "
        "negócios: cadastre entregas, importe pedidos por planilha, otimize rotas, "
        "distribua entre motoristas e acompanhe o resultado de cada parada."
    ),
    "aviso_capa": (
        "Hipóteses de mercado, escopo e cronograma sujeitas a validação — "
        "este documento não é pesquisa de mercado."
    ),
}

COMO_LER = {
    "titulo": "Como ler este documento",
    "texto": (
        "Este briefing reúne o entendimento atual da equipe sobre o RotaCerta: problema, "
        "público, concorrência, produto, tecnologia, cronograma e riscos. Tudo o que envolve "
        "cliente, dor, tamanho de mercado e diferenciais está marcado como hipótese — nada "
        "disso foi validado em pesquisa ainda. O objetivo do documento é alinhar a equipe e "
        "orientar as próximas decisões, não apresentar conclusões definitivas."
    ),
}

# ------------------------------------------------------------------ 1. contexto
CONTEXTO = {
    "paragrafos": [
        (
            "O RotaCerta é uma plataforma B2B de otimização e gerenciamento de rotas de "
            "entrega criada para pequenos negócios que operam com entregadores próprios ou "
            "contratados. A proposta é substituir o planejamento manual das entregas por um "
            "fluxo simples e guiado: cadastrar ou importar os pedidos do dia, geocodificar os "
            "endereços, otimizar as rotas automaticamente, distribuir as entregas entre os "
            "motoristas e acompanhar o resultado de cada parada até a conclusão."
        ),
        (
            "O produto se organiza em torno de um ciclo operacional completo. O responsável "
            "pelo negócio importa os pedidos (por cadastro manual ou planilha CSV), o sistema "
            "localiza os endereços no mapa, calcula as melhores rotas, divide o trabalho entre "
            "os entregadores e devolve um painel com o que foi planejado e o que foi "
            "efetivamente entregue. O entregador, por sua vez, acessa a própria rota pelo "
            "celular e atualiza o status de cada parada em campo."
        ),
        (
            "O objetivo é reduzir o trabalho manual de planejamento, melhorar a organização "
            "logística do dia a dia e fornecer informações operacionais — entregas pendentes, "
            "concluídas e não realizadas — a quem responde pelo negócio. Em uma competição de "
            "prazo curto, o RotaCerta existe para provar que esse ciclo completo é viável e "
            "útil para o perfil de pequeno negócio, não para entregar todas as funcionalidades "
            "de um sistema logístico maduro."
        ),
    ],
}

FLUXO_TITULO = "Fluxo do produto — do pedido à entrega concluída"
FLUXO = [
    "Cadastro e\nimportação CSV",
    "Geocodificação\ndos endereços",
    "Otimização e\ndistribuição",
    "Rotas visíveis\nno mapa",
    "Execução no\ncelular do entregador",
    "Status e\ndashboard",
]

# ------------------------------------------------------------------ 2. público
PUBLICO_INTRO = (
    "O foco inicial são pequenos negócios que já contam com entregadores próprios ou "
    "contratados e que planejam as rotas do dia de forma artesanal. Os segmentos abaixo "
    "foram escolhidos por proximidade com essa rotina — todos concentram entregas em uma "
    "área urbana e mantêm uma equipe pequena de campo."
)

SEGMENTOS = [
    ("Depósitos de materiais de construção",
     "Entregas pesadas e recorrentes por bairro, com endereços muitas vezes informados de forma incompleta."),
    ("Distribuidoras de bebidas e alimentos",
     "Alto volume diário, rota fixa de comércios de bairro e forte pressão por prazo."),
    ("Farmácias",
     "Entregas sensíveis a prazo, com pedidos por telefone e entrega da receita em casa do cliente."),
    ("Pequenos e-commerces",
     "Pedidos vindos de marketplaces e redes sociais, montados em planilha antes da saída."),
    ("Lojas de bairro",
     "Balcão, WhatsApp e telefone geram entregas do dia que precisam ser organizadas na hora."),
    ("Pequenas transportadoras",
     "Operações locais com poucos motoristas e cobertura de uma cidade ou região."),
]

PERFIL_HIPOTESE = {
    "titulo": "Hipótese de segmentação — não é dado comprovado",
    "texto": (
        "Os números abaixo são a hipótese de trabalho da equipe para dimensionar o MVP: "
        "1 a 5 entregadores, aproximadamente 10 a 80 entregas por dia e operação "
        "concentrada em uma cidade ou região. Não existem pesquisas nem estatísticas "
        "sustentando esses valores — eles precisam ser confrontados em conversas com "
        "comerciantes reais antes de virar premissa de produto ou de negócio."
    ),
}

PERFIL_LINHAS = [
    ("Entregadores", "1 a 5 por operação"),
    ("Entregas por dia", "≈ 10 a 80 (hipótese)"),
    ("Cobertura", "Uma cidade ou região metropolitana"),
    ("Planejamento atual", "Hipótese: planilha, caderno ou WhatsApp"),
    ("Decisor", "Hipótese: o próprio dono ou responsável pela operação"),
]

# ------------------------------------------------------------------ 3. problema
PROBLEMA_INTRO = (
    "Os problemas abaixo são hipóteses levantadas a partir da observação de rotinas de "
    "entrega e de conversas informais. Nenhum deles foi ainda validado em pesquisa com "
    "amostra relevante — a equipe precisa conversar com comerciantes para confirmar a "
    "existência e a intensidade de cada dor antes de tratar qualquer uma delas como certa."
)

PROBLEMAS = [
    ("Organização manual das entregas",
     "O planejamento do dia é montado em planilha ou caderno, com risco de duplicidade, "
     "esquecimento e retrabalho a cada alteração de último minuto."),
    ("Deslocamentos desnecessários",
     "Sem cálculo de sequência, as paradas são visitadas em ordem de chegada do pedido, "
     "gerando voltas e travessias repetidas pela mesma região."),
    ("Distribuição inadequada dos pedidos",
     "A divisão do trabalho entre entregadores é feita por intuição, o que pode sobrecarregar "
     "um motorista enquanto outro roda com poucas paradas."),
    ("Falta de acompanhamento das entregas",
     "Enquanto os motoristas estão na rua, não há visão centralizada do que já saiu, o que "
     "está em trânsito e o que ainda não começou."),
    ("Dificuldade de identificar entregas não realizadas",
     "Ao final do dia, saber o que faltou depende de perguntar um a um — a informação "
     "costuma chegar tarde e sem registro confiável."),
    ("Ausência de indicadores operacionais",
     "Sem histórico estruturado, não é possível comparar dias, medir tempo por parada nem "
     "identificar gargalos recorrentes da operação."),
]

PROBLEMA_AVISO = {
    "titulo": "Validação pendente",
    "texto": (
        "A equipe não conduziu pesquisas, não obteve estatísticas e não validou comercialmente "
        "nessas dores. Antes de priorizar funcionalidades ou argumentar valor em uma "
        "apresentação, é necessário entrevistar comerciantes do perfil-alvo e checar quais "
        "desses problemas aparecem com frequência, qual é a intensidade de cada um e quanto "
        "tempo ou dinheiro eles custam hoje."
    ),
}

# ------------------------------------------------------------------ 4. concorrentes
CONC_INTRO = (
    "A análise abaixo é uma leitura inicial a partir dos sites oficiais e de fontes "
    "públicas consultadas em novembro de 2026. Ela descreve posicionamento e "
    "funcionalidades conhecidas de cada solução — não é estudo exaustivo de mercado e "
    "não substitui uma avaliação detalhada de preços, contratos e limites de uso."
)

CONCORRENTES = [
    {
        "nome": "RoutEasy",
        "origem": "Brasil",
        "posicao": (
            "Plataforma brasileira de roteirização e gestão de entregas para empresas de "
            "porte médio e grande, com clientes em varejo, marketplaces e transportadoras."
        ),
        "funcs": (
            "Roteirização com restrições (janelas horárias, capacidade, sequenciamento), "
            "gestão de entregas com comprovação de entrega (POD), automação de atribuição de "
            "pedidos, aplicativo para motoristas, API/webhooks e módulo de indicadores."
        ),
        "preco": "Sob consulta (demonstração comercial)",
    },
    {
        "nome": "Cobli",
        "origem": "Brasil",
        "posicao": (
            "Plataforma de gestão de frotas com foco em telemetria, segurança e "
            "conformidade — não é, na essência, uma ferramenta de planejamento de rotas "
            "para pequenos comércios."
        ),
        "funcs": (
            "Rastreamento veicular, telemetria e videotelemetria, identificação de motorista, "
            "gestão de manutenção e gastos, relatórios e roteirização integrada à operação "
            "de frota."
        ),
        "preco": "Sob consulta (teste disponível)",
    },
    {
        "nome": "Routific",
        "origem": "Canadá",
        "posicao": (
            "Software de planejamento de rotas e gestão de entregas para pequenos e médios "
            "negócios que entregam com motoristas próprios — o concorrente mais próximo do "
            "perfil que o RotaCerta imagina atender."
        ),
        "funcs": (
            "Otimização de rotas com janelas de horário e capacidade, aplicativo gratuito do "
            "motorista, rastreamento em tempo real, comprovação de entrega, notificações por "
            "e-mail, importação de pedidos e API de otimização."
        ),
        "preco": (
            "Plano gratuito até 100 pedidos/mês; US$ 150/mês até 1.000 pedidos, com "
            "cobrança por pedido acima disso (tabela pública em dólares)"
        ),
    },
    {
        "nome": "Onfleet",
        "origem": "Estados Unidos",
        "posicao": (
            "Plataforma de orquestração de última milha para operações de entrega em "
            "diversos portes, com forte apelo em experiência do motorista e comunicação "
            "com o cliente final."
        ),
        "funcs": (
            "Despacho e otimização de rotas com machine learning, aplicativos nativos de "
            "motorista (iOS e Android), comprovação de entrega, notificações por SMS, "
            "rastreamento em tempo real, portal do cliente e relatórios de desempenho."
        ),
        "preco": "Sob consulta (teste disponível)",
    },
    {
        "nome": "4LogOS",
        "origem": "Brasil",
        "posicao": (
            "Plataforma cloud-native de gestão logística integrada, voltada a distribuidores, "
            "indústria, e-commerce, transportadoras e operadores 3PL — escopo muito além do "
            "que um pequeno negócio precisa para começar."
        ),
        "funcs": (
            "WMS (armazém), TMS (transportes, com roteirização, fretes e status de entrega), "
            "YMS, OMS, ERP e módulo fiscal na mesma plataforma, com integração a ERPs do "
            "mercado e aplicativo móvel."
        ),
        "preco": (
            "Planos publicados a partir de R$ 4.990/mês, com implantação a partir de "
            "R$ 5 mil (valores do site oficial)"
        ),
    },
]

CONC_TABELA_COLS = [2.5, 4.5, 6.6, 2.8]

POSICIONAMENTO = {
    "titulo": "Onde o RotaCerta se posiciona — e onde não entra",
    "texto": (
        "O RotaCerta não pretende competir, inicialmente, com essas plataformas em "
        "quantidade de funcionalidades. A hipótese a investigar é outra: existe espaço "
        "para uma solução de entrada — configuração rápida, interface simples, importação "
        "por planilha e foco em operação de 1 a 5 entregadores — que resolva o ciclo "
        "básico do planejamento do dia sem exigir implantação, integração ou curva de "
        "aprendizado compatíveis com o tamanho do negócio. Confirmar se essa simplificação "
        "é um valor real (e não apenas uma versão incompleta de produto maior) é uma das "
        "principais tarefas de validação da equipe."
    ),
}

# ------------------------------------------------------------------ 5. proposta
PROPOSTA_INTRO = (
    "Os diferenciais abaixo são pretendidos — descrevem o que o produto quer ser, não o "
    "que já é. Cada um precisa ser confrontado com o que os concorrentes oferecem e "
    "validado com potenciais clientes antes de virar argumento de venda ou promessa em "
    "apresentação."
)

DIFERENCIAIS = [
    ("Interface simples",
     "Telas poucas e diretas, pensadas para quem não tem equipe de tecnologia e não quer "
     "treinar o time inteiro para usar a ferramenta."),
    ("Configuração rápida",
     "Do cadastro à primeira rota otimizada em poucos passos, sem implantação longa nem "
     "consultoria obrigatória."),
    ("Importação de entregas por CSV",
     "As planilhas que o negócio já usa viram pedidos no sistema sem digitação item a item."),
    ("Otimização automática de rotas",
     "O sistema define a sequência das paradas e sugere as rotas em segundos, sem cálculo "
     "manual nem conhecimento de algoritmos."),
    ("Distribuição entre motoristas",
     "As entregas do dia são divididas entre os entregadores de forma equilibrada e "
     "visível para o responsável."),
    ("Interface mobile para entregadores",
     "O motorista acessa a própria rota pelo celular, no navegador, sem instalar aplicativo "
     "de loja."),
    ("Atualização do status das entregas",
     "Cada parada é marcada como entregue, pendente ou não realizada em campo, com "
     "registro imediato para o painel."),
    ("Histórico e indicadores operacionais",
     "O responsável consulta o que foi feito no dia e o desempenho acumulado, em vez de "
     "reconstruir o histórico de cabeça."),
]

PROPOSTA_AVISO = {
    "titulo": "Diferenciais sob teste",
    "texto": (
        "Nenhum desses diferenciais está confirmado como vantagem competitiva. Alguns "
        "podem já existir nos concorrentes (a preços ou em pacotes diferentes), outros "
        "podem não ser valorizados pelos comerciantes. A equipe precisa comparar cada "
        "item com as soluções da seção 4 e perguntar aos potenciais clientes o que eles "
        "realmente buscariam numa ferramenta assim."
    ),
}

# ------------------------------------------------------------------ 6. tecnologia
TEC_INTRO = (
    "A arquitetura proposta se organiza em três áreas: o backend, que concentra dados e "
    "regras; o frontend, que entrega a experiência ao planejador e ao entregador; e o "
    "bloco de otimização e geolocalização, que transforma endereços em rotas. As três "
    "se comunicam por uma API REST em JSON."
)

TEC_AREAS = [
    {
        "titulo": "Backend",
        "cor_titulo": "API, dados e regras de negócio",
        "itens": [
            ("Python", "linguagem do backend e do código de integração entre os módulos."),
            ("FastAPI", "framework que expõe a API REST consumida pelas telas e pelo aplicativo web do entregador."),
            ("SQLAlchemy", "mapeamento objeto-relacional: os pedidos, rotas e motoristas do código viram tabelas do banco."),
            ("PostgreSQL", "banco de dados de produção dos pedidos, endereços, rotas, motoristas e status."),
            ("Alembic", "controle de versão do esquema do banco, permitindo evoluir os dados sem perder o que já existe."),
        ],
    },
    {
        "titulo": "Frontend",
        "cor_titulo": "Experiência do planejador e do entregador",
        "itens": [
            ("React", "biblioteca de interface para as telas de cadastro, importação, mapa e dashboard."),
            ("TypeScript", "tipagem estática que reduz erros de integração entre telas e API."),
            ("Tailwind CSS", "estilização utilitária para uma interface limpa e consistente com pouco código de estilo."),
            ("PWA", "aplicativo web instalável: o entregador usa pelo navegador do celular, sem loja de aplicativos."),
        ],
    },
    {
        "titulo": "Otimização e geolocalização",
        "cor_titulo": "Do endereço à rota",
        "itens": [
            ("Google OR-Tools", "solver de otimização que decide a sequência das paradas e a distribuição entre motoristas."),
            ("OpenStreetMap", "base de dados geográfica aberta com ruas e limites usada pelos serviços de mapa."),
            ("OSRM", "serviço de roteamento que calcula distâncias e tempos estimados entre os pontos, pelas ruas."),
            ("Serviço de geocodificação", "converte o endereço digitado ou importado em coordenadas latitude/longitude."),
        ],
    },
]

ARQUITETURA_TITULO = "Arquitetura simplificada"
ARQUITETURA = [
    ("Frontend — React + TypeScript + Tailwind (PWA)",
     "Telas do planejador · interface mobile do entregador"),
    ("API REST em JSON (HTTPS)", None),
    ("Backend — Python + FastAPI · SQLAlchemy · Alembic",
     "Regras de negócio · importação CSV · orquestração"),
    ("PostgreSQL — dados operacionais", "OR-Tools — otimização de rotas",
     "OSRM + geocodificação — dados de mapa"),
]

ARQUITETURA_LEGENDA = (
    "O frontend consome a API do backend; o backend grava e lê no PostgreSQL, aciona o "
    "OR-Tools para planejar as rotas e consulta o serviço de geocodificação e o OSRM para "
    "transformar endereços em coordenadas e coordenadas em distâncias reais."
)
ARQUITETURA_NOTA = "Arquitetura simplificada — camadas e serviços do MVP"

OTIMIZACAO_VS_ROTEAMENTO = {
    "titulo": "Otimização ≠ roteamento: dois papéis diferentes",
    "esquerda": (
        "**Algoritmo de otimização (Google OR-Tools)** — decide **o quê** e **em que ordem**: "
        "quais entregas entram em cada rota, qual motorista recebe cada parada e em que "
        "sequência a rota é cumprida, respeitando as regras da operação. É o cérebro do "
        "planejamento."
    ),
    "direita": (
        "**Serviço de roteamento (OSRM)** — informa **quanto custa**: a distância e o tempo "
        "estimado de deslocamento entre dois pontos, seguindo as ruas do OpenStreetMap. É a "
        "régua com que o cérebro mede as opções. Sem dados de roteamento confiáveis, a "
        "otimização pode escolher uma sequência que parece boa, mas que parte de premissas "
        "erradas."
    ),
    "rodape": (
        "A qualidade do plano final depende dos dois: o OR-Tools só é tão bom quanto a "
        "matriz de distâncias que recebe do OSRM."
    ),
}

# ------------------------------------------------------------------ 7. equipe
EQUIPE_INTRO = (
    "A equipe possui três integrantes. A divisão abaixo sugere frentes de trabalho para "
    "evitar sobreposição e cobrir todas as partes do MVP — nomes e distribuição final "
    "dependem da experiência real de cada pessoa, que está registrada como decisão "
    "pendente na seção 12."
)

EQUIPE = [
    {
        "frente": "Backend e banco de dados",
        "resp": (
            "API com FastAPI, modelagem com SQLAlchemy, migrações com Alembic, endpoints de "
            "entregas, motoristas, rotas e status, importação de CSV e integração com o "
            "módulo de otimização."
        ),
        "entregas": [
            "Esquema do banco e API de entregas funcionando",
            "Importação de CSV gravando pedidos válidos",
            "Status de entrega atualizável via API",
        ],
    },
    {
        "frente": "Frontend e experiência do usuário",
        "resp": (
            "Telas do planejador em React com TypeScript e Tailwind — cadastro, importação, "
            "mapa das rotas e dashboard — além da base do PWA e da navegação geral do "
            "produto."
        ),
        "entregas": [
            "Fluxo de cadastro e importação navegável",
            "Visualização das rotas em mapa",
            "Dashboard básico com os indicadores do dia",
        ],
    },
    {
        "frente": "Otimização, geolocalização e testes",
        "resp": (
            "Integração de geocodificação e OSRM, modelagem do problema no OR-Tools, "
            "distribuição entre motoristas, rotas de teste de ponta a ponta e preparação "
            "do roteiro de demonstração."
        ),
        "entregas": [
            "Endereços virando coordenadas com retorno de erro",
            "Rotas otimizadas e distribuídas em tempo útil",
            "Roteiro de demonstração testado de ponta a ponta",
        ],
    },
]

EQUIPE_NOTA = (
    "Nenhum nome foi atribuído a estas frentes e nenhum conhecimento técnico foi presumido "
    "sobre os integrantes: os papéis devem ser confirmados com a equipe na primeira "
    "reunião de planejamento."
)

# ------------------------------------------------------------------ 8. escopo
ESCOPO_INTRO = (
    "O escopo abaixo separa o que precisa existir para o MVP ser demonstrável do que "
    "ficará conscientemente de fora. Qualquer inclusão nova durante o desenvolvimento "
    "exige retirar algo da lista — o prazo não absorve escopo adicional."
)

MVP_DENTRO = [
    ("Cadastro de entregas", "inclusão manual de paradas com endereço e dados básicos"),
    ("Importação CSV", "lote de pedidos a partir de planilha padronizada"),
    ("Geocodificação", "endereços convertidos em coordenadas, com aviso de falha"),
    ("Cadastro de pelo menos dois motoristas", "base para distribuir as rotas"),
    ("Otimização de rotas com OR-Tools", "sequência e agrupamento calculados automaticamente"),
    ("Distribuição de entregas", "paradas divididas entre os motoristas"),
    ("Visualização em mapa", "rotas e paradas desenhadas para o planejador"),
    ("Interface mobile", "rota do entregador no celular via PWA"),
    ("Atualização de status", "marcar entregue, pendente ou não realizada em campo"),
    ("Dashboard básico", "resumo do dia: entregas, pendências e conclusão"),
]

MVP_FORA = [
    ("Pagamentos e assinaturas", "nenhuma cobrança no MVP"),
    ("Rastreamento GPS contínuo", "sem posição do veículo em tempo real"),
    ("Aplicativo Android nativo", "o PWA substitui a loja de aplicativos"),
    ("Integrações com Mercado Livre e Shopee", "importação apenas por CSV"),
    ("IA generativa", "sem chatbots nem geração de conteúdo"),
    ("Gestão avançada de frotas", "sem telemetria, manutenção ou multidoca"),
]

# ------------------------------------------------------------------ 9. cronograma
CRONO_INTRO = (
    "O prazo de desenvolvimento vai de 12 a 30 de novembro de 2026 — 19 dias corridos "
    "para três pessoas. O quadro abaixo é uma estimativa de esforço, não um compromisso "
    "contratado: ele assume escopo congelado, sem dependências externas e com a equipe "
    "trabalhando também nos fins de semana, como é comum em competições."
)

CRONO = [
    ("12–13/11", "Planejamento e arquitetura", 12, 13),
    ("14–17/11", "Backend e banco de dados", 14, 17),
    ("18–20/11", "Geolocalização e otimização", 18, 20),
    ("21–23/11", "Frontend e mapas", 21, 23),
    ("24–26/11", "Interface do entregador", 24, 26),
    ("27–28/11", "Integração e testes", 27, 28),
    ("29–30/11", "Apresentação e ajustes", 29, 30),
]

CRONO_AVISO = {
    "titulo": "Cronograma como estimativa",
    "texto": (
        "Com três pessoas e prazo curto, as frentes se sobrepõem por necessidade: backend "
        "começa antes do fim do planejamento e a integração consome dias que seriam de "
        "polimento. Atenção aos pontos de maior risco — geocodificação de endereços "
        "reais e a integração entre otimização, mapa e aplicativo do entregador. Se algo "
        "precisar ser cortado, o corte deve ser combinado antes, em conjunto, e registrado "
        "neste documento."
    ),
}

# ------------------------------------------------------------------ 10. demonstração
DEMO_CENARIO = {
    "titulo": "Cenário: Distribuidora fictícia de Parnaíba, Piauí",
    "texto": (
        "A demonstração usa uma distribuidora fictícia sediada em Parnaíba (PI), com 20 "
        "entregas do dia e 2 motoristas. Os endereços utilizados são de pontos reais da "
        "cidade, apenas para efeito de demonstração — nenhum dado de cliente real é "
        "necessário. O roteiro abaixo percorre o produto do começo ao fim, na mesma ordem "
        "em que um comerciante usaria."
    ),
}

DEMO_PASSOS = [
    ("Importação dos pedidos",
     "A planilha do dia com as 20 entregas é importada por CSV e os pedidos aparecem na lista."),
    ("Otimização automática",
     "O sistema geocodifica os endereços e aciona o OR-Tools: as rotas são calculadas em segundos."),
    ("Distribuição das entregas",
     "As 20 paradas são divididas entre os 2 motoristas, com carga visível para cada um."),
    ("Visualização das rotas no mapa",
     "O planejador vê as duas rotas desenhadas no mapa, com sequência de paradas."),
    ("Acesso do entregador pelo celular",
     "Um dos motoristas abre a própria rota pelo navegador do celular, em modo PWA."),
    ("Atualização de uma entrega",
     "Em campo, o entregador marca uma parada como concluída — e outra como não realizada."),
    ("Dashboard atualizado",
     "O painel do responsável reflete imediatamente o novo status: concluídas, pendentes e não realizadas."),
]

DEMO_PROVA = {
    "titulo": "O que a demonstração comprova",
    "texto": (
        "Cada passo do roteiro exercita uma funcionalidade essencial do MVP: importação, "
        "geocodificação, otimização, distribuição, mapa, interface mobile e status em tempo "
        "real. Executado de ponta a ponta, sem etapa intermediária forçada, o roteiro "
        "demonstra que o ciclo completo planejado — pedido importado até indicador "
        "atualizado — é funcional na versão inicial do produto. O cenário fictício também "
        "prova o produto em uma operação realista do perfil-alvo: volume pequeno, poucos "
        "entregadores e uma única cidade."
    ),
}

# ------------------------------------------------------------------ 11. riscos
RISCOS_INTRO = (
    "Os riscos abaixo foram identificados pela equipe como os mais prováveis de afetar o "
    "MVP. As estratégias de mitigação são medidas preventivas a serem adotadas desde o "
    "início do desenvolvimento — não garantias de que o risco não ocorrerá."
)

RISCOS = [
    ("Endereços incorretos ou incompletos",
     "Técnico / comercial",
     "Geocodificação com retorno claro de falha, permitindo correção manual de coordenadas; "
     "cenário de demonstração com endereços previamente conferidos."),
    ("Limitações dos serviços de mapas",
     "Técnico",
     "Preferir serviços auto-hospedáveis (OSRM com extrato do OpenStreetMap) e cache de "
     "matrizes de distância; limitar o volume do MVP ao que os serviços comportam."),
    ("Complexidade da otimização",
     "Técnico",
     "Começar com um modelo simples e bem testado (rotas com poucos veículos e sem "
     "restrições exóticas), validar tempo de resposta antes de adicionar restrições."),
    ("Integração entre módulos",
     "Técnico",
     "Contrato de API definido já no planejamento, integração contínua desde as primeiras "
     "semanas e testes de ponta a ponta antes da demonstração."),
    ("Prazo reduzido",
     "Processo",
     "Escopo congelado, priorização diária entre as três frentes e lista prévia do que "
     "será cortado se o cronograma escorregar."),
    ("Falta de validação da demanda",
     "Comercial",
     "Entrevistas com comerciantes antes e durante o desenvolvimento; tratar todo "
     "posicionamento como hipótese até haver retorno de clientes reais."),
]

SUCESSO_TITULO = "Critérios de sucesso do MVP"
SUCESSO = [
    "Demonstração completa do fluxo — importação, otimização, mapa, celular e dashboard — "
    "sem etapa intermediária forçada.",
    "As 20 entregas do cenário são otimizadas e distribuídas entre os 2 motoristas em "
    "tempo útil para o uso diário.",
    "Status atualizado em campo reflete no painel do responsável durante a demonstração.",
    "Um usuário não técnico consegue seguir o roteiro da demonstração sem ajuda do "
    "desenvolvedor.",
    "Ao menos 3 conversas com comerciantes do perfil-alvo realizadas até a apresentação, "
    "com registro das perguntas e respostas.",
    "Decisões pendentes da seção 12 respondidas antes do início do desenvolvimento.",
]

VALIDACAO_TITULO = "Validação comercial — perguntas para entrevistas"
VALIDACAO_INTRO = (
    "As perguntas abaixo orientam conversas com comerciantes do perfil-alvo. A meta "
    "inicial da equipe é realizar de 8 a 12 entrevistas curtas, sem vender nada, apenas "
    "ouvir a rotina atual. O objetivo é confirmar quais dores da seção 3 existem de "
    "fato, com que frequência e com que intensidade."
)

VALIDACAO_GRUPOS = [
    ("Rotina atual", [
        "Como você organiza as entregas de hoje? Quem monta a rota e quanto tempo isso leva?",
        "Quais ferramentas são usadas — planilha, caderno, WhatsApp, algum sistema?",
        "Quantas entregas por dia e quantos entregadores trabalham na operação?",
    ]),
    ("Dores percebidas", [
        "O que costuma dar errado no planejamento das entregas da semana?",
        "Já aconteceu de entrega ser esquecida, sair fora de ordem ou voltar sem conclusão? Como você ficou sabendo?",
        "Como você sabe, hoje, se uma entrega foi concluída ou não?",
        "Como os pedidos são divididos entre os entregadores?",
    ]),
    ("Reação à solução", [
        "O que você faria primeiro ao ver uma tela de importação de planilha com as rotas já calculadas?",
        "Quais informações são essenciais para você acompanhar o dia: pendentes, atrasadas, por entregador?",
        "O que te faria testar uma ferramenta assim? E o que te faria desistir dela?",
    ]),
    ("Compra e decisão", [
        "Quem decide a compra de uma ferramenta como essa na sua empresa?",
        "Você já pagou por algum sistema de rotas, gestão ou entrega? Como foi a experiência?",
        "Como você prefere ser abordado para conhecer uma solução nova: presencial, ligação ou WhatsApp?",
    ]),
]

VALIDACAO_NOTA = (
    "Nenhuma resposta deve ser interpretada como validação isolada: o objetivo das "
    "entrevistas é reconhecer padrões entre diferentes comerciantes e registrar, sem "
    "edulcorar, o que descarta a hipótese tanto quanto o que a confirma."
)

# ------------------------------------------------------------------ 12. decisões
DECISOES_INTRO = (
    "As perguntas abaixo estão em aberto e precisam de resposta da equipe antes do "
    "início do desenvolvimento. Nada foi presumido: cada uma terá sua resposta "
    "registrada aqui quando decidida."
)

DECISOES = [
    ("Qual é a experiência técnica dos outros dois integrantes?",
     "Define a divisão real das frentes da seção 7 e o grau de dependência entre elas."),
    ("A equipe confirma React + FastAPI como stack?",
     "A arquitetura da seção 6 assume essa combinação; trocar agora é barato, trocar depois não."),
    ("O HackBrasil exige pitch, demonstração funcional ou ambos?",
     "Define o peso do cronograma entre códigos e preparação de apresentação nos últimos dias."),
]
