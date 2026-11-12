# -*- coding: utf-8 -*-
"""Conteúdo das sete trilhas, das 14 fichas de ideias, do comparativo e das prioridades."""

TRILHAS = [
    {
        "n": 1,
        "nome": "Meio ambiente e economia verde",
        "cor": "1E9E5A",
        "contexto": (
            "Reduzir consumo de recursos, organizar destinação de resíduos e criar valor a partir da "
            "circularidade — com soluções pequenas, mensuráveis e que cabem na rotina de pequenos negócios."
        ),
    },
    {
        "n": 2,
        "nome": "Cultura e economia criativa",
        "cor": "D6336C",
        "contexto": (
            "Apoiar quem produz cultura com ferramentas de gestão e vendas simples, respeitando a lógica "
            "de projetos financiados por editais, patrocínios e venda direta de peças e experiências."
        ),
    },
    {
        "n": 3,
        "nome": "Acesso à educação",
        "cor": "2F6FED",
        "contexto": (
            "Ampliar oportunidades conectando estudantes a apoio de aprendizagem e a primeiras experiências "
            "de trabalho, com atenção especial à proteção de dados de menores de idade."
        ),
    },
    {
        "n": 4,
        "nome": "Saúde e bem-estar",
        "cor": "E03131",
        "contexto": (
            "Melhorar a rotina de cuidado com ferramentas que reduzem perdas, faltas e falhas de "
            "acompanhamento — sempre com atenção redobrada a privacidade, segurança e regulamentação."
        ),
    },
    {
        "n": 5,
        "nome": "Pagamentos e finanças",
        "cor": "7048E8",
        "contexto": (
            "Dar previsibilidade ao caixa de quem vive de venda diária, organizando conciliação, crédito "
            "de curto prazo e controle do que entra e do que ainda não foi recebido."
        ),
    },
    {
        "n": 6,
        "nome": "Cibersegurança",
        "cor": "0B7285",
        "contexto": (
            "Tornar a segurança prática acessível a empresas que não têm time especializado, com "
            "diagnóstico acionável e conscientização — sempre mediante autorização e dentro da lei."
        ),
    },
    {
        "n": 7,
        "nome": "Logística e automação",
        "cor": "E8590C",
        "contexto": (
            "Ganhar tempo e reduzir custo na última milha com automação proporcional ao porte da operação, "
            "sem exigir integração pesada nem frota dedicada de tecnologia."
        ),
    },
]

IDEIAS = [
    # ------------------------------------------------------------------ 1
    {
        "num": 1,
        "nome": "EcoConsumo",
        "tagline": "Controle de água e energia para pequenos negócios",
        "trilha": 1,
        "descricao": (
            "Aplicativo web simples que reúne contas de água e energia de um pequeno negócio, mostra o "
            "consumo mês a mês, compara períodos e avisa quando o consumo foge do padrão — permitindo agir "
            "antes que a conta feche alta."
        ),
        "problema": (
            "Padarias, restaurantes, lavanderias e academias pequenas recebem contas altas de água e energia "
            "sem conseguir apontar a causa: não há histórico comparável, nenhum registro de equipamento novo "
            "ou de horário de pico e nenhum alerta de possível vazamento ou equipamento esquecido ligado. O "
            "resultado é custo fixo tratado como 'o preço que é', sem margem real de economia."
        ),
        "publico": (
            "Donos e gestores de pequenos comércios e serviços cuja conta de energia ou água é um dos maiores "
            "custos variáveis: padarias, restaurantes, barbearias, salões, lavanderias, academias de bairro, "
            "escritórios pequenos e clínicas."
        ),
        "como_funciona": (
            "O cliente cadastra o negócio e informa mensalmente os dados da conta (valor, consumo e vencimento) "
            "por digitação ou pelo envio da foto/PDF da conta. A plataforma organiza a série histórica, calcula "
            "medias e desvios, registra eventos que justificam picos (máquina nova, reforma, ponto aberto mais "
            "horas) e gera um painel com comparativo entre meses, custo acumulado e três recomendações práticas "
            "no fechamento de cada ciclo."
        ),
        "mvp": [
            "Cadastro do negócio, da distribuidora e das contas de água/energia.",
            "Lançamento mensal de consumo e valor, com histórico completo por conta.",
            "Painel com consumo, custo, comparativo mês a mês e meta definida pelo usuário.",
            "Alerta simples quando o consumo fica acima de um percentual configurável da média.",
            "Relatório mensal exportável (PDF) com três recomendações de economia.",
        ],
        "fora": [
            "Integração automática com distribuidoras, medição remota ou leitura inteligente.",
            "Sensores, medidores IoT e leitura em tempo real do consumo.",
            "Certificação de energia renovável, crédito de carbono e relatórios de sustentabilidade.",
            "App nativo para iOS/Android e notificações por push.",
            "Módulo de gestão completa de contas a pagar e boletos.",
        ],
        "tecnologias": [
            "Web app responsivo (React ou Vue) com API em Node.js ou Python (FastAPI/Django).",
            "Banco relacional (PostgreSQL) ou SQLite para o MVP.",
            "Envio de relatório por e-mail (fila de mensagens transacionais).",
            "OCR opcional para leitura de foto/PDF de conta em versão posterior.",
            "Hospedagem em nuvem de baixo custo com backup diário.",
        ],
        "quem_pagaria": (
            "O dono ou gestor do pequeno negócio, porque a economia obtida é direta no caixa. Canais "
            "secundários a testar: contadores, associações de comerciantes e fornecedores de energia, que "
            "poderiam indicar a ferramenta como serviço de valor agregado (canal a validar)."
        ),
        "monetizacao": (
            "Assinatura mensal por unidade, com plano gratuito limitado (1 unidade e histórico curto) e plano "
            "pago liberando histórico completo, alertas, relatórios e múltiplas contas. O preço exato é hipótese "
            "que precisa ser validada por entrevistas e por teste de disposição a pagar."
        ),
        "diferenciais": (
            "Foco no pequeno negócio — as ferramentas existentes de gestão de energia atendem grandes "
            "consumidores ou o consumidor doméstico. Não exige instalação de nada e entrega valor já no "
            "primeiro mês de uso."
        ),
        "riscos": (
            "O lançamento manual cria atrito e pode gerar abandono; sem integração automática, dados podem "
            "ficar desatualizados. A economia real depende de ação do cliente, então o produto precisa conduzir "
            "a recomendação até a prática. Risco comercial: a conta de energia é percebida como custo fixo, o "
            "que exige demonstração clara de retorno."
        ),
        "validacao": [
            "Entrevistar 10 donos de pequenos negócios: quanto pagam por mês, se já tentaram controlar e como (planilha, caderno, nada).",
            "Perguntar se algum episódio de conta anormal ficou sem explicação e quanto custou.",
            "Oferecer cadastro gratuito e pedir o registro de dois meses de conta reais, medindo quem efetivamente volta a lançar.",
            "Testar se o relatório mensal gera alguma ação concreta (troca de equipamento, ajuste de rotina).",
        ],
        "ressalvas": (
            "Nenhuma exigência regulatória específica no escopo. Dados de consumo são dados do negócio; "
            "informe finalidade e guarda dos dados conforme a LGPD e evite prometer economia garantida em "
            "materiais comerciais."
        ),
    },
    # ------------------------------------------------------------------ 2
    {
        "num": 2,
        "nome": "ReCiclo",
        "tagline": "Gestão de resíduos e conexão entre empresas e coletores",
        "trilha": 1,
        "descricao": (
            "Plataforma que publica a oferta de recicláveis de empresas e comércios, conecta quem tem resíduo "
            "a quem coleta, agenda retiradas e mantém o histórico de destinação com relatório mensal exportável."
        ),
        "problema": (
            "Pequenos negócios geram papel, plástico, vidro e metal todos os dias e, sem canal organizado, "
            "acabam misturando ou descartando no destino errado. De outro lado, cooperativas e catadores não "
            "sabem antecipadamente onde há volume disponível e percorrem a cidade sem rota definida. Quem "
            "precisa comprovar destinação de resíduos não dispõe de registro simples e auditável."
        ),
        "publico": (
            "Lado da oferta: comércios, indústrias pequenas, escritórios, condomínios e escolas que geram "
            "recicláveis em volume regular. Lado da coleta: cooperativas, grupos de catadores e empresas de "
            "coleta seletiva da região."
        ),
        "como_funciona": (
            "A empresa publica uma oferta com tipo de resíduo, volume estimado, endereço e janela de "
            "disponibilidade. Coletores cadastrados visualizam ofertas próximas e propõem retirada. Combinada "
            "a retirada, o sistema registra o evento e emite um comprovante simples, que se acumula em um "
            "histórico mensal exportável. O pareamento de oferta e coleta é assistido por filtros simples, sem "
            "algoritmo complexo no MVP."
        ),
        "mvp": [
            "Cadastro e verificação básica de dois perfis: empresa geradora e coletor/cooperativa.",
            "Publicação de oferta com tipo, volume, endereço e período de disponibilidade.",
            "Busca de ofertas por bairro/região e solicitação de retirada.",
            "Agendamento combinado entre as partes, com notificação por e-mail.",
            "Comprovante de retirada e histórico mensal por empresa (PDF/planilha).",
        ],
        "fora": [
            "Marketplace financeiro com preço por quilo e pagamento entre as partes.",
            "Rastreamento em tempo real, telemática e otimização de rota de coleta.",
            "Certificação oficial de destinação, laudos e integração com obrigações legais estaduais.",
            "Logística própria, esteiras, balanças conectadas e aplicativo nativo.",
            "Gestão de resíduos perigosos ou hospitalares (fora do escopo inicial).",
        ],
        "tecnologias": [
            "Web responsivo com comportamento de aplicativo (PWA) para uso em campo.",
            "Backend em Node.js ou Python com banco relacional (PostgreSQL).",
            "Mapas com biblioteca aberta (Leaflet + OpenStreetMap) para busca por região.",
            "Notificações por e-mail e, se validado, mensagens via API oficial de WhatsApp.",
            "Upload de fotos simples para evidenciar volume e destino.",
        ],
        "quem_pagaria": (
            "A empresa geradora de resíduos, que precisa se desfazer do material e pode precisar de registro. "
            "A cooperativa tende ao lado gratuito para que a rede cresça (hipótese a validar). "
            "Canal possível: associações comerciais e gestores ambientais de condomínios."
        ),
        "monetizacao": (
            "Assinatura mensal por empresa, com volume de retiradas e relatórios liberados conforme o plano, "
            "e cadastro gratuito para coletores. Alternativa a testar: pacote de retiradas avulsas para "
            "empresas esporádicas. Preço e plano ideal são hipóteses a validar."
        ),
        "diferenciais": (
            "Resolve o problema dos dois lados ao mesmo tempo e dá atenção a pequenos volumes, que grandes "
            "operadores de logística reversa ignoram. O histórico exportável transforma descarte comum em "
            "registro utilizável em relatórios internos."
        ),
        "riscos": (
            "Depende de efeito de rede: só funciona com oferta e coleta ativas na mesma região. A "
            "comprovação gerada pelo produto não deve ser apresentada como documento de validade legal — "
            "risco de expectativa incorreta. Há custo operacional real: cada retirada exige logística de "
            "alguém. Começar por um bairro ou um segmento é mais realista do que abrir a cidade inteira."
        ),
        "validacao": [
            "Mapear 10 empresas geradoras e 5 cooperativas/coletores em uma mesma região.",
            "Perguntar como o descarte acontece hoje, quem paga pelo descarte e se alguém já pediu comprovação.",
            "Levantar custos com os coletores: quanto custa hoje a coleta por bairro e qual volume torna a viagem viável.",
            "Rodar um piloto manual: combinar manualmente 15 retiradas antes de construir pareamento automático.",
        ],
        "ressalvas": (
            "Resíduos comuns estão fora de escopo; ampliar para perigosos ou sanitários exige estrutura e "
            "conformidade legal própria. Registre consentimento dos participantes e não colete dados pessoais "
            "além do necessário (LGPD)."
        ),
    },
    # ------------------------------------------------------------------ 3
    {
        "num": 3,
        "nome": "CulturaGestor",
        "tagline": "Gestão financeira e operacional de projetos culturais",
        "trilha": 2,
        "descricao": (
            "Ferramenta de organização financeira por projeto para produções culturais: reúne edital, "
            "patrocínio, venda de ingressos e custos em um só lugar, mostra quanto do orçamento foi executado "
            "e gera relatório de prestação de contas em poucos cliques."
        ),
        "problema": (
            "Quem produz cultura atravessa fontes de recurso distintas — recurso de edital com prestação de "
            "contas específica, patrocínio com contrapartida e receita de bilheteria ou merchandising — e "
            "controla tudo em planilhas montadas às pressas. No fim do projeto, refazer o relatório consome "
            "dias e ninguém sabe, em tempo real, se o projeto fecha no azul."
        ),
        "publico": (
            "Produtores independentes, coletivos culturais, gestores de projetos de música, teatro, dança, "
            "artes visuais e arte urbana, pequenas produtoras de eventos e lideranças de ocupações culturais "
            "que executam orçamento com fontes combinadas."
        ),
        "como_funciona": (
            "O usuário cria um projeto, informa as fontes de recurso e o orçamento aprovado, e registra "
            "entradas e saídas vinculadas a cada fonte e categoria. A ferramenta calcula saldo, execução do "
            "orçamento por rubrica e projeção simples de fechamento, e monta um relatório em PDF/planilha "
            "organizado por exigência de prestação de contas, pronto para envio a financiador ou patrocinador."
        ),
        "mvp": [
            "Cadastro de projeto, período e fontes de recurso (edital, patrocínio, receita própria).",
            "Lançamento de entradas e saídas com categoria, fonte e comprovante anexado.",
            "Painel de saldo, execução por rubrica e comparação entre orçado e realizado.",
            "Alerta quando uma rubrica se aproxima do limite aprovado.",
            "Relatório de prestação de contas exportável (PDF e planilha).",
        ],
        "fora": [
            "Emissão de nota fiscal, assinatura digital de convênios e contabilidade.",
            "Integração automática com bancos, PIX e cartões.",
            "Gestão de elenco, escalas, ingressos e crachás.",
            "CRM de patrocinadores, captação de recursos e gestão de editais.",
            "Plataforma de inscrição de festivais e venda de ingressos.",
        ],
        "tecnologias": [
            "Web app (Next.js ou Vue) com API em Node.js ou Python.",
            "Banco relacional (PostgreSQL) com histórico de lançamentos por projeto.",
            "Autenticação simples com perfis (produtor, financiador somente leitura).",
            "Geração de PDF no servidor e exportação de planilhas.",
            "Anexo de comprovantes em armazenamento de objetos de baixo custo.",
        ],
        "quem_pagaria": (
            "O produtor ou gestor do projeto, e em segundo plano produtoras com vários projetos simultâneos. "
            "Centros culturais e secretarias que apoiam projetos podem ser canal de venda (hipótese a validar)."
        ),
        "monetizacao": (
            "Assinatura mensal por projeto ativo ou por conta do produtor, com plano gratuito de um projeto e "
            "histórico limitado. Reforço de valor: pacote de relatórios de prestação de contas. Disposição a "
            "pagar e valor do plano precisam ser validados."
        ),
        "diferenciais": (
            "Fala a linguagem de edital e prestação de contas, não é um financeiro genérico. Resolve a dor "
            "que aparece no fim do projeto — o relatório — em vez de exigir disciplina contábil permanente."
        ),
        "riscos": (
            "Sazonalidade: projetos terminam e clientes cancelam, elevando a troca de base. Nicho com baixa "
            "disposição histórica de pagar por software. Concorrência real é a planilha gratuita e o gestor "
            "financeiro de quem já tem contador. Risco de prometer conformidade com regras de editais "
            "diversos — o produto organiza dados, não substitui parecer contábil."
        ),
        "validacao": [
            "Entrevistar 8 a 10 produtores e pedir para ver a planilha real do projeto em execução.",
            "Perguntar quanto tempo levou o último relatório de prestação de contas e o que gerou retrabalho.",
            "Oferecer configurar gratuitamente o controle do projeto que estão executando agora.",
            "Medir se voltam a usar semanalmente e se pagariam pelo relatório automático.",
        ],
        "ressalvas": (
            "Não emitir documentos com valor fiscal ou contábil. Ao anexar comprovantes, trate-os como dados "
            "sensíveis do projeto: acesso restrito, armazenamento protegido e descarte previsto (LGPD)."
        ),
    },
    # ------------------------------------------------------------------ 4
    {
        "num": 4,
        "nome": "FeitoAqui",
        "tagline": "Vitrine e gestão de vendas para artesãos",
        "trilha": 2,
        "descricao": (
            "Vitrine com link único e painel de pedidos para artesãos: cadastro de peças com fotos, recebimento "
            "de pedidos pelo site, acompanhamento de status e histórico de vendas — no lugar de catálogo perdido "
            "em conversas de WhatsApp."
        ),
        "problema": (
            "Artesãos vendem pelo Instagram e por conversas individuais: pedidos se perdem em mensagens, o "
            "estoque de peças únicas não é controlado, não há catálogo com preço atualizado e o cliente final "
            "não tem como comprar sem trocar dez mensagens. Montar loja própria, com domínio, pagamento e "
            "frete, é caro e complexo demais para quem produz e vende sozinho."
        ),
        "publico": (
            "Artesãos e pequenos produtores de economia criativa — cerâmica, tecelagem, marcenaria, joalheria "
            "autoral, bordado, sinalização e estamparia manual — que vendem em feiras, por redes sociais e por "
            "indicação."
        ),
        "como_funciona": (
            "O artesão cadastra suas peças com fotos, preço, variações e quantidade disponível. A plataforma "
            "publica uma vitrine em link único, compartilhável na bio de redes sociais. O cliente monta o "
            "pedido pelo site e o artesão recebe a confirmação para alinhar entrega e pagamento pelo canal que "
            "já usa hoje. Cada pedido ganha status (recebido, em produção, enviado, entregue) e o painel "
            "consolida o mês."
        ),
        "mvp": [
            "Cadastro de produtos com fotos, preço, descrição e estoque (peça única incluída).",
            "Vitrine pública com link único e identidade simples do artesão.",
            "Pedido pelo site com confirmação manual do vendedor.",
            "Gestão de status do pedido e lista de clientes que compraram.",
            "Painel de vendas do mês com exportação de dados.",
        ],
        "fora": [
            "Checkout com processamento de cartão e PIX integrado no primeiro release.",
            "Marketplace multivendedor, curadoria e vitrine coletiva.",
            "Cálculo automático de frete e integração com transportadoras.",
            "Emissão de nota fiscal e integração tributária.",
            "App nativo, domínio próprio com SEO avançado e mídia paga.",
        ],
        "tecnologias": [
            "Web responsivo com gerador de vitrine (Next.js/Astro + backend leve).",
            "Banco relacional (PostgreSQL) e armazenamento de imagens (objeto/CDN).",
            "Notificações por e-mail; mensagens por API oficial de WhatsApp apenas se validadas.",
            "Pagamento de hospedagem de baixo custo; site estático + API para reduzir custo.",
            "Painel administrativo simples com autenticação.",
        ],
        "quem_pagaria": (
            "O próprio artesão, diretamente impactado por vendas perdidas e tempo gasto respondendo. "
            "Canais a testar: associações de artesãos, feiras, casas de artesanato e incubadoras de economia "
            "criativa."
        ),
        "monetizacao": (
            "Assinatura mensal acessível com plano gratuito limitado (número de produtos e marca d'água na "
            "vitrine) e plano pago liberando domínio do link, relatórios e pedidos ilimitados. Taxa por venda "
            "é alternativa a testar. Ambas são hipóteses."
        ),
        "diferenciais": (
            "Pensado para peça única e para o fluxo real do artesão, que é a conversa por mensagem: a "
            "vitrine organiza, mas não obriga abandonar o canal em que já vende."
        ),
        "riscos": (
            "Disposição a pagar historicamente baixa e abandono rápido quando o cadastro exige esforço. "
            "Concorrência não é só software: Instagram, marketplaces e grupos de WhatsApp são gratuitos. O "
            "produto depende de o artesão fotografar bem — incluir guia simples de fotografia melhora "
            "adensamento."
        ),
        "validacao": [
            "Entrevistar 10 artesãos em feiras e grupos online, perguntando como é o dia de uma venda hoje.",
            "Perguntar quantos pedidos já se perderam e quanto isso significou em dinheiro.",
            "Oferecer montar a vitrine deles de graça e medir quem acessa, compartilha e recebe pedido.",
            "Testar disposição a pagar com preço simbólico por 30 dias.",
        ],
        "ressalvas": (
            "Dados de clientes finais são dados pessoais (LGPD): informe uso e retenção. Não processar "
            "pagamento no MVP evita obrigações de arranjo de pagamento — se for incluído depois, exigirá "
            "parceiro regulado."
        ),
    },
    # ------------------------------------------------------------------ 5
    {
        "num": 5,
        "nome": "Aprendi",
        "tagline": "Diagnóstico de dificuldades de aprendizagem",
        "trilha": 3,
        "descricao": (
            "Instrumento digital de triagem para educadores: aplica roteiros curtos de atividades, organiza "
            "resultados por área de aprendizagem e devolve relatório por aluno e por turma, indicando padrões "
            "de dificuldade e caminhos de apoio pedagógico."
        ),
        "problema": (
            "Professores percebem quando um aluno 'não acompanha', mas raramente dispõem de instrumento rápido "
            "e padronizado para identificar onde a dificuldade se concentra — leitura, escrita, raciocínio "
            "lógico, atenção — e como registrar isso para a coordenação e para a família. A triagem hoje é "
            "subjetiva, feita com o tempo que sobra, e o encaminhamento acontece tarde."
        ),
        "publico": (
            "Professores e coordenadores pedagógicos de escolas públicas e particulares do ensino fundamental, "
            "escolas em tempo integral, redes pequenas, tutores e projetos de reforço escolar. O decisor da "
            "compra é a coordenação ou a direção."
        ),
        "como_funciona": (
            "O professor cadastra a turma com identificadores pseudonimizados e aplica um roteiro digital curto "
            "por área. As respostas são pontuadas por critérios definidos com especialistas e resultam em um "
            "relatório por aluno (áreas com desempenho abaixo do esperado, evidências) e por turma (mapa de "
            "dificuldades recorrentes). O relatório sugere estratégias pedagógicas e sinaliza quando cabe "
            "encaminhamento para avaliação profissional — o produto nunca se apresenta como diagnóstico "
            "clínico."
        ),
        "mvp": [
            "Cadastro de escola, turma e alunos com identificador (seudônimo), sem nome completo na análise.",
            "Aplicação de um a dois roteiros curtos por área, no navegador do laboratório ou sala.",
            "Relatório por aluno e por turma, exportável em PDF, em linguagem para educador.",
            "Painel do professor com histórico e progresso ao longo do tempo.",
            "Registro de consentimento dos responsáveis e política de retenção/eliminação de dados.",
        ],
        "fora": [
            "Plataforma de ensino, aulas, exercícios e correção automática por inteligência artificial.",
            "Testes psicológicos ou psicopedagógicos validados e qualquer alegação de diagnóstico clínico.",
            "Prontuário, laudos, integração com sistemas de saúde e armazenamento de dados clínicos.",
            "Aplicativo para famílias, notificações automáticas e gamificação robusta.",
            "Gestão escolar completa (diários, frequência, notas).",
        ],
        "tecnologias": [
            "Web responsivo com modo de aplicação offline básico (funcionar em sala com conexão instável).",
            "Backend (Python/Django ou Node) com banco relacional, criptografia em repouso e minimização de dados.",
            "Autenticação de professor, controle de acesso por escola e trilha de auditoria de consulta.",
            "Geração de relatórios PDF e exportação anonimizada para a coordenação.",
            "Hospedagem com backup criptografado e logs de acesso.",
        ],
        "quem_pagaria": (
            "A escola ou rede de ensino, por assinatura por turma ou por escola, decidida pela coordenação ou "
            "direção. Tutores e projetos sociais educacionais são compradores secundários. A família não é "
            "compradora no modelo inicial."
        ),
        "monetizacao": (
            "Assinatura por escola ou por turma ativa, com plano piloto gratuito limitado em número de "
            "aplicações. Pacote de implantação com treinamento curto pode fazer parte do preço — hipótese a "
            "validar. Não cobrar de famílias."
        ),
        "diferenciais": (
            "Ferramenta de triagem prática para o professor, não mais um app de estudo: entrega relatório "
            "acionável em minutos e organiza o histórico da turma, algo que a observação solta não faz."
        ),
        "riscos": (
            "Alta sensibilidade: dados de crianças exigem consentimento do responsável, minimização, finalidade "
            "clara e guarda controlada (LGPD). Produto pode ser mal interpretado como diagnóstico médico ou "
            "psicológico — comunicação precisa ser precisa e constante. Exige validação pedagógica por "
            "especialistas antes de qualquer uso real. Adesão depende de apoio da direção e de tempo do "
            "professor."
        ),
        "validacao": [
            "Entrevistar 10 professores e coordenadores: como identificam dificuldade hoje e o que fazem com isso.",
            "Perguntar que instrumentos já usam (observação, provas, escalas prontas) e o que falta neles.",
            "Investigar se existe orçamento e quem decide a compra de material pedagógico na escola.",
            "Construir o roteiro com um psicopedagogo ou professor especialista antes de escrever código.",
            "Validar o consentimento e o fluxo de dados com a direção antes de aplicar com alunos reais.",
        ],
        "ressalvas": (
            "Dados de menores de idade e de aprendizagem: consentimento dos responsáveis, minimização, "
            "pseudonimização, retenção limitada e sem compartilhamento com terceiros. Nenhuma alegação de "
            "diagnóstico clínico; sempre recomendar avaliação profissional quando indicado. Submissão a "
            "políticas escolares e a normas de proteção de dados aplicáveis é pré-condição de uso."
        ),
    },
    # ------------------------------------------------------------------ 6
    {
        "num": 6,
        "nome": "ConectaEstágio",
        "tagline": "Conexão entre estudantes e pequenos negócios",
        "trilha": 3,
        "descricao": (
            "Mercado hiperlocal de oportunidades: pequenos negócios publicam vagas de estágio, aprendizagem e "
            "primeiro emprego; estudantes da região se candidatam com perfil simples; a empresa acompanha "
            "candidaturas em um painel direto, sem processo de RH pesado."
        ),
        "problema": (
            "Pequenos negócios precisam de apoio em atendimento, administrativo, vendas ou marketing, mas não "
            "têm departamento de RH: a vaga é publicada em rede social, some em 24 horas e as candidaturas se "
            "perdem nos comentários ou no WhatsApp. Do outro lado, estudantes não encontram oportunidades "
            "locais — os portais genéricos priorizam vagas grandes e a busca por bairro é inexistente."
        ),
        "publico": (
            "Lado da oferta: comércios, serviços, clínicas e escritórios com 1 a 50 funcionários na região. "
            "Lado da procura: estudantes do ensino médio, técnico e inicial da graduação em busca de estágio, "
            "aprendizagem ou primeiro emprego. Canais de apoio: escolas e secretarias de educação."
        ),
        "como_funciona": (
            "A empresa cadastra a vaga com atividades, jornada, valor oferecido, bairro e período. O estudante "
            "monta um perfil enxuto (objetivo, disponibilidade, estudos, contato) e se candidata em um clique. "
            "A empresa recebe as candidaturas organizadas em painel, filtra e agenda conversa; o status da vaga "
            "é acompanhado até o encerramento."
        ),
        "mvp": [
            "Cadastro simples de empresa e de estudante, com verificação básica de e-mail.",
            "Publicação de vaga com filtros por bairro, tipo de atividade e período.",
            "Candidatura em um clique e painel de candidaturas com status.",
            "Notificação por e-mail em cada etapa (nova candidatura, vaga encerrada).",
            "Histórico de vagas publicadas e taxa de resposta da empresa.",
        ],
        "fora": [
            "Contrato digital, assinatura eletrônica e gestão documental de estágio.",
            "Vídeo-entrevista, seleção por inteligência artificial e triagem automatizada.",
            "Sistema de folha, ponto, escala e integração com escolas.",
            "Feed social, mensagens instantâneas no app e gamificação.",
            "Verificação de antecedentes e checagem de documentação de menores.",
        ],
        "tecnologias": [
            "Web responsivo (React/Vue) com API em Node.js ou Python.",
            "Banco relacional com busca por proximidade simples (PostgreSQL).",
            "Autenticação com perfis (empresa, estudante) e verificação de e-mail.",
            "E-mails transacionais (fila de envio) para notificações.",
            "Painel administrativo leve e exportação de candidaturas.",
        ],
        "quem_pagaria": (
            "O pequeno negócio, que economiza tempo de divulgação e triagem. Canais secundários: escolas, "
            "secretarias de educação e programas de aprendizagem que poderiam licenciar a plataforma para "
            "turmas inteiras (hipótese a validar)."
        ),
        "monetizacao": (
            "Publicação gratuita com destaque pago por vaga e/ou assinatura mensal por empresa com vagas "
            "ilimitadas. Licença institucional para escolas é caminho alternativo. Qual modelo prevalece é "
            "hipótese a validar com entrevistas."
        ),
        "diferenciais": (
            "Hiperlocal e proporcional: atende a vaga de três horas por semana que não sobrevive em portal "
            "grande, com fluxo que o dono do negócio consegue usar sem treinamento."
        ),
        "riscos": (
            "Efeito de rede obrigatório: sem estudantes não há vaga interessante e vice-versa. Responsabilidade "
            "legal com menores de idade (consentimento de responsáveis, adequação de atividades e jornada) "
            "precisa ser endereçada desde o início. Concorrência de grupos de WhatsApp de bairro, que são "
            "gratuitos e já funcionam."
        ),
        "validacao": [
            "Entrevistar 5 pequenos empresários (como publicam vaga hoje, quanto tempo consomem) e 5 estudantes (onde procuram).",
            "Perguntar se já pagaram por divulgação de vaga e quanto.",
            "Publicar 10 vagas manualmente (piloto manual) e medir quantas candidaturas chegam em duas semanas.",
            "Verificar com a escola qual o caminho de consentimento para estudantes menores de idade.",
        ],
        "ressalvas": (
            "Dados de menores exigem consentimento de responsáveis e minimização (LGPD). Não intermediar "
            "contratação informal ou irregular: o produto publica e organiza, não formaliza vínculo. "
            "Informações de vaga devem ser verificadas para evitar anúncios enganosos."
        ),
    },
    # ------------------------------------------------------------------ 7
    {
        "num": 7,
        "nome": "FrioGuard",
        "tagline": "Monitoramento de temperatura de geladeiras e câmaras frias com sensores e funcionamento local",
        "trilha": 4,
        "descricao": (
            "Sensor de temperatura com alarme local e histórico exportável, feito para geladeiras comerciais e "
            "câmaras frias: avisa quando a temperatura sai da faixa, registra tudo automaticamente e continua "
            "funcionando mesmo sem internet."
        ),
        "problema": (
            "Mercados, açougues, restaurantes, farmácias, laboratórios e postos de vacina dependem de "
            "equipamentos de refrigeração que falham sem aviso — porta mal fechada, compressor no fim da vida, "
            "corte de energia. O resultado é produto estragado, perda financeira direta e, em casos de cadeia "
            "fria, risco sanitário. O registro de temperatura ainda é feito à mão, quando é feito, e não alerta "
            "ninguém quando tudo dá errado às 3 da manhã."
        ),
        "publico": (
            "Estabelecimentos com um a dez equipamentos de refrigeração: mercados e minimercados, açougues, "
            "restaurantes e lanchonetes com câmara fria, farmácias e drogarias, laboratórios clínicos, "
            "postos de vacina, clínicas e padarias."
        ),
        "como_funciona": (
            "Um módulo com sensor instalado dentro do equipamento mede a temperatura em intervalos curtos e "
            "mostra o valor atual em display local. Se a leitura sai da faixa configurável por tempo "
            "suficiente, dispara alarme sonoro no local e notificação por e-mail/SMS para o responsável. O "
            "histórico fica guardado no próprio aparelho (cartão de memória) e pode ser exportado para "
            "qualquer computador em CSV/PDF, formando registro contínuo sem anotação manual. Tudo funciona "
            "offline: a internet apenas habilita a notificação remota e a visualização no painel."
        ),
        "mvp": [
            "Um dispositivo com sensor confiável, display local e gravação contínua em memória local.",
            "Faixa de temperatura e tempo de tolerância configuráveis por equipamento.",
            "Alarme sonoro local e notificação por e-mail/SMS quando a faixa é violada.",
            "Painel simples (web) com leitura atual, histórico e exportação CSV/PDF.",
            "Cadastro de estabelecimento, equipamentos e responsáveis pelos alertas.",
        ],
        "fora": [
            "Previsão de falha por inteligência artificial e manutenção preditiva do compressor.",
            "Painel corporativo multi-unidades, integração com ERP e telemática de frota.",
            "Medição de umidade, gás refrigerante e abertura de porta por sensor adicional.",
            "Certificação formal de instrumento de medição e assinatura de conformidade sanitária.",
            "Aplicativo nativo e assinatura que exige conexão permanente com a nuvem.",
        ],
        "tecnologias": [
            "Hardware de baixo custo: microcontrolador com Wi-Fi (ex.: família ESP32) e sensor digitais (ex.: DS18B20 ou equivalente).",
            "Firmware em C/C++ (Arduino/ESP-IDF) com gravação local, display e política de alerta com atraso.",
            "Backend leve (Python/Node) para histórico e envio de alertas; armazenamento local como base.",
            "Painel web responsivo; gateway de SMS/e-mail para notificação remota.",
            "Impressão/embalagem simples e modo de instalação por fita/adesivo em geladeira.",
        ],
        "quem_pagaria": (
            "O dono do estabelecimento, cuja perda evitada paga o equipamento com folga (hipótese a validar). "
            "Frigoríficos e distribuidores que atendem pequenos pontos podem ser canal de venda de kit."
        ),
        "monetizacao": (
            "Venda do kit (hardware + licença) com assinatura mensal de monitoramento e suporte, ou kit "
            "vendido com assinatura incluída no primeiro ano. Planos por número de sensores/equipamentos. "
            "Preço, margem de hardware e disposição a pagar são hipóteses centrais a validar."
        ),
        "diferenciais": (
            "Funciona localmente, sem depender de internet — decisão crucial para galpão e madrugada. "
            "Registro automático substitui a anotação em papel e pode ser mostrado a fornecedor ou auditor em "
            "minutos. Custo muito abaixo de soluções industriais de monitoramento."
        ),
        "riscos": (
            "Hardware é mais difícil que software: fiabilidade, calibração, custo de produção, estoque e "
            "suporte técnico pesam. Concorrência com sistemas profissionais de refrigeração, mais caros, mas "
            "já instalados. Não afirmar conformidade sanitária ou validade legal do registro sem revisão "
            "específica. Alerta perdido por canal de mensagem falho é falha crítica do produto — alarme local "
            "é o que garante o mínimo."
        ),
        "validacao": [
            "Entrevistar 8 a 10 estabelecimentos: já perderam produto por temperatura? Quanto? Como registram hoje?",
            "Perguntar se alguém já pediu esse registro (fornecedor, auditoria, vigilância) e em que formato.",
            "Verificar se existe orçamento para segurança do frio e quem decide a compra.",
            "Montar um protótipo funcional e deixar duas semanas em geladeira real, comparando com o registro manual.",
        ],
        "ressalvas": (
            "Não usar o produto como prova de conformidade sanitária sem revisão de especialista e adequação à "
            "norma aplicável; a comunicação deve ser de 'monitoramento e alerta'. Dados de sensores são do "
            "estabelecimento — informe coleta e retenção (LGPD quando houver contato de responsável). Validar "
            "requisitos específicos para cadeia fria de imunobiológicos antes de atuar nesse segmento."
        ),
    },
    # ------------------------------------------------------------------ 8
    {
        "num": 8,
        "nome": "AgendaViva",
        "tagline": "Redução de faltas em consultas e gestão de horários cancelados",
        "trilha": 4,
        "descricao": (
            "Agenda simples com lembrete automático e lista de espera inteligente: confirma a consulta em um "
            "clique, avisa os pacientes da fila quando abre vaga e mostra ao consultório quantos horários se "
            "perdem por falta e cancelamento de última hora."
        ),
        "problema": (
            "Consultórios e clínicas pequenas perdem receita e tempo com faltas: confirmar por telefone consome "
            "horas da recepção, cancelamento de última hora deixa a agenda furada e quem está na fila não é "
            "avisado. Em profissões com agenda de 20 a 30 atendimentos por dia, poucas faltas por semana já "
            "representam perda relevante — e o horário vazio não é recuperável."
        ),
        "publico": (
            "Consultórios e clínicas com um a quatro profissionais: dentistas, psicólogos, fisioterapeutas, "
            "nutricionistas, dermatologistas, médicos de família e pequenas clínicas multidisciplinares que "
            "agendam por telefone ou WhatsApp. Em paralelo, unidades de serviço que funcionam por horário "
            "marcado (estética, laboratórios de coleta) são público adjacente."
        ),
        "como_funciona": (
            "A agenda é cadastrada por profissional e horário. Ao marcar, o paciente informa contato e recebe "
            "lembrete automático com confirmação em um clique. Quem não confirma é avisado novamente; "
            "cancelamentos liberam a vaga, que é oferecida automaticamente à lista de espera em ordem. O "
            "painel mostra ocupação, faltas e horários vagos, e permite exportar a lista do dia."
        ),
        "mvp": [
            "Cadastro de profissionais, horários e agenda por dia.",
            "Registro de agendamento com dados mínimos do paciente (nome, contato, procedimento).",
            "Lembrete automático por e-mail ou SMS com confirmação em um clique.",
            "Lista de espera com oferta automática de vaga liberada.",
            "Painel com taxa de faltas, ocupação e histórico mensal exportável.",
        ],
        "fora": [
            "Prontuário, histórico clínico e qualquer armazenamento de informação de saúde.",
            "Faturamento de convênios, emissão de nota fiscal e caixa.",
            "Telemedicina, videochamada e sala virtual.",
            "Multi-clínica corporativo, escala de equipe grande e integração com sistemas hospitalares.",
            "Aplicativo nativo para pacientes e reagendamento por inteligência artificial.",
        ],
        "tecnologias": [
            "Web responsivo (paciente acessa por link; profissional pelo painel).",
            "API em Node.js ou Python com banco relacional e controle de acesso por profissional.",
            "Gateway de SMS/e-mail transacional para lembretes; API oficial de WhatsApp Business se validada (custo por conversa).",
            "Fila de mensagens para garantir envio e retentativa de lembretes.",
            "Relatórios simples em PDF e exportação de dados.",
        ],
        "quem_pagaria": (
            "O profissional ou a clínica, direta e mensalmente: cada falta evitada custa menos que a "
            "assinatura (hipótese a validar). Quem decide é o dono do consultório ou o gestor da clínica "
            "pequena."
        ),
        "monetizacao": (
            "Assinatura mensal por profissional ou por agenda ativa, com período piloto gratuito de 30 dias. "
            "Canal premium (mensagens via API oficial) pode custar adicional, já que tem custo por mensagem. "
            "Preço precisa ser calibrado contra a perda média de faltas relatada em entrevistas."
        ),
        "diferenciais": (
            "Fecha o ciclo do no-show: lembrete, confirmação, reoferta da vaga e métrica — em vez de apenas "
            "mandar mensagem. Simples o bastante para um consultório de uma pessoa, sem treinamento."
        ),
        "riscos": (
            "Dados de saúde: mesmo sem prontuário, agendamento revela relação com serviço de saúde; exige "
            "minimização, consentimento para mensagens e segurança de acesso (LGPD). Custo e dependência de "
            "canais oficiais de mensagem podem corroer margem. Paciente pode não confirmar — o efeito depende "
            "de frequência e canal certo. Concorrência com agendas embutidas em sistemas de agendamento e "
            "portais de booking."
        ),
        "validacao": [
            "Entrevistar 8 a 10 profissionais: taxa estimada de faltas, tempo gasto confirmando, o que já tentaram.",
            "Perguntar quanto vale, para eles, um horário vazio e se já calcularam perda no mês.",
            "Oferecer piloto gratuito de lembretes por 30 dias e medir taxa de faltas antes e depois.",
            "Custar o envio real de mensagens (e-mail, SMS, WhatsApp oficial) para não prometer preço impossível.",
        ],
        "ressalvas": (
            "Não armazenar conteúdo clínico: apenas dados de agendamento necessários. Consentimento para "
            "mensagens, acesso restrito por profissional, retenção definida e eliminação sob pedido (LGPD). "
            "Comunicação jamais deve sugerir acompanhamento clínico automatizado. Validar regras de arquivos e "
            "documentos do paciente se o produto evoluir."
        ),
    },
    # ------------------------------------------------------------------ 9
    {
        "num": 9,
        "nome": "PixConcilia",
        "tagline": "Conciliação financeira de vendas e extratos para pequenos negócios",
        "trilha": 5,
        "descricao": (
            "Ferramenta que cruza o extrato bancário com as vendas do dia e mostra, em minutos, o que bateu, o "
            "que está pendente e o que divergiu — substituindo a conciliação manual em planilha de lojas que "
            "recebem por Pix, cartão, dinheiro e boleto."
        ),
        "problema": (
            "Quem vive de venda diária recebe por vários meios ao mesmo tempo. No fechamento do caixa, nada "
            "bate: o Pix aparece sem identificação, o cartão entra parcelado e com taxa descontada, o dinheiro "
            "fica no registrador e a maquininha tem prazo próprio. A conciliação vira planilha arrastada à "
            "mão, cheia de erro e sempre adiada — e o dinheiro que 'some' entre vendas e extrato só é "
            "descoberto no mês seguinte."
        ),
        "publico": (
            "Pequenos comerciantes e prestadores com movimentação diária e múltiplos meios de recebimento: "
            "mercadinhos, lojas, restaurantes, barbearias, salões, oficinas, farmácias de bairro, padarias e "
            "profissionais que faturam por Pix e cartão."
        ),
        "como_funciona": (
            "O usuário importa o extrato bancário (OFX ou CSV) e, opcionalmente, o relatório de vendas da "
            "maquininha ou o registro de vendas do dia. A plataforma tenta casar cada lançamento com sua venda "
            "correspondente por valor, data e referência; o que casa entra como conciliado e o que diverge vai "
            "para uma fila de revisão com sugestão. O painel mostra o fechamento do dia e do mês, as "
            "divergências abertas e exporta o consolidado para o contador."
        ),
        "mvp": [
            "Importação de extrato em OFX/CSV e de relatório de vendas (ou lançamento manual do dia).",
            "Casamento automático por regras determinísticas (valor, data, identificador) com sugestão de pareamento.",
            "Fila de divergências com decisão manual (conciliar, marcar como taxa, ignorar).",
            "Fechamento diário e mensal com visão por meio de pagamento.",
            "Relatório consolidado exportável (PDF/planilha) para o contador.",
        ],
        "fora": [
            "Integração bancária automática via Open Finance (fase futura, exige consentimento do cliente).",
            "Emissão de nota fiscal, gestão de estoque e ERP.",
            "Antecipação de recebíveis, crédito, empréstimo e cartão próprio.",
            "Múltiplas lojas, hierarquia corporativa e consolidação de rede.",
            "Previsão de caixa por inteligência artificial e categorização automática por aprendizado de máquina.",
        ],
        "tecnologias": [
            "Web app com API em Python ou TypeScript (Node), banco relacional (PostgreSQL).",
            "Parsers de OFX/CSV e regras de pareamento documentadas e testadas.",
            "Autenticação forte (senha forte + segundo fator), criptografia em trânsito e em repouso.",
            "Exportação PDF/CSV e importação assistida com pré-visualização antes de confirmar.",
            "Backup diário e registro de auditoria de alterações.",
        ],
        "quem_pagaria": (
            "O dono do pequeno negócio, que paga hoje em horas perdidas e em dinheiro que some entre vendas e "
            "extrato. Contadores e escritórios de contabilidade são canal valioso: atendem vários clientes "
            "com o mesmo problema (canal a validar)."
        ),
        "monetizacao": (
            "Assinatura mensal com planos por volume de lançamentos, acompanhada de teste gratuito limitado. "
            "Plano para contadores com múltiplos clientes é extensão natural. Preço e formato são hipóteses: "
            "validar quanto vale a hora do lojista e quanto ele já gasta em solução (inclusive planilha e "
            "tempo do filho/funcionário)."
        ),
        "diferenciais": (
            "Feito para o caixa brasileiro de pequeno negócio — Pix, maquininha, taxa e prazo — e não é um "
            "ERP. Mostra divergências com revisão humana no comando, o que gera confiança: o sistema não "
            "inventa lançamento."
        ),
        "riscos": (
            "Lida com dados financeiros sensíveis: falha de segurança ou vazamento encerra a confiança do "
            "produto — exigência máxima de proteção e transparência. Concorrência de planilhas gratuitas e de "
            "recursos de conciliação embutidos em sistemas de gestão. Pareamento imperfeito gera desconfiança; a "
            "fila de revisão precisa ser rápida e clara. Formato de extrato varia entre bancos — suporte "
            "contínuo a formatos é manutenção real."
        ),
        "validacao": [
            "Entrevistar 8 a 10 lojistas e 2 a 3 contadores: quanto tempo leva a conciliação e que erros já aconteceram.",
            "Perguntar se já pagaram por solução (sistema, assinatura, terceirizado) e quanto.",
            "Oferecer conciliar um mês real de extrato de graça e apresentar as divergências encontradas.",
            "Medir tempo economizado e testar disposição a pagar com preço simbólico por um trimestre.",
        ],
        "ressalvas": (
            "Dados financeiros exigem proteção reforçada: criptografia, controle de acesso, auditoria e "
            "minimização (LGPD). Não ter acesso a conta bancária do cliente no MVP — apenas arquivos "
            "importados. Nunca prometer detecção de fraude ou conciliação 100% automática."
        ),
    },
    # ------------------------------------------------------------------ 10
    {
        "num": 10,
        "nome": "FiadoControl",
        "tagline": "Gestão de vendas a prazo para pequenos comerciantes",
        "trilha": 5,
        "descricao": (
            "O caderno de fiado, digital: registra quem deve, quanto e até quando, avisa vencimento e atraso, "
            "guarda o histórico de cada cliente e mostra quanto dinheiro do mês ainda está na rua."
        ),
        "problema": (
            "Em lojas de bairro, parte relevante do faturamento sai fiado. O controle vive no caderno, na "
            "memória do lojista ou na bagunça de papéis: vencimento esquecido vira perda, cobrança acontece "
            "quando o cliente aparece de novo e não há histórico confiável para decidir se um cliente ainda "
            "pode comprar a prazo. O prejuízo do fiado é normalmente aceito como 'parte do negócio'."
        ),
        "publico": (
            "Comércios de bairro que vendem a prazo: mercearias, mercadinhos, açougues, lojas de material de "
            "construção, lojas de eletro/móveis pequenos, farmácias de confiança e atacadistas regionais que "
            "atendem lojistas vizinhos."
        ),
        "como_funciona": (
            "O lojista cadastra o cliente com dados mínimos e registra a venda a prazo (valor, itens, "
            "parcelas e vencimento). A ferramenta calcula o que está em aberto, avisa vencendo e atrasado, "
            "gera mensagem de cobrança pronta para o canal que o lojista já usa e mantém histórico por cliente "
            "com saldo e comportamento de pagamento. No fechamento do mês, mostra total a receber, total "
            "recebido e perda estimada."
        ),
        "mvp": [
            "Cadastro de cliente (nome, contato e observações mínimas).",
            "Registro de venda a prazo com valor, vencimento e parcelas.",
            "Painel de em aberto, vencendo e atrasado, com total geral.",
            "Lembrete de vencimento e mensagem de cobrança pronta para copiar e enviar.",
            "Histórico por cliente e relatório mensal de recebido e perdido.",
        ],
        "fora": [
            "Consulta a bureaus de crédito, scoring e restrição cadastral.",
            "Cobrança automática em massa por SMS/WhatsApp sem consentimento.",
            "Parcelamento por cartão, empréstimo e intermediação de crédito.",
            "Emissão de nota fiscal, contrato digital com assinatura e venda online.",
            "Gestão de estoque e caixa completo da loja.",
        ],
        "tecnologias": [
            "Web responsivo/PWA que funciona bem no celular do lojista, inclusive com conexão instável.",
            "Backend leve (Node/Python) com banco relacional e autenticação simples.",
            "Notificações por e-mail; mensagens por API oficial de WhatsApp apenas se o custo compensar.",
            "Modo offline com sincronização básica (fica em loja sem sinal).",
            "Exportação de relatório em PDF/planilha.",
        ],
        "quem_pagaria": (
            "O dono da loja, diretamente afetado pela perda. Testar com microempreendedores que já assumem o "
            "fiado como custo pode revelar maior disposição a pagar do que o lojista que nunca perdeu nada "
            "(canal a validar)."
        ),
        "monetizacao": (
            "Assinatura mensal única e baixa, com plano gratuito limitado a número de clientes ou vendas. "
            "Preço calibrado contra o prejuízo mensal relatado em entrevista. Hipótese a validar — não há "
            "referência de mercado assumida neste documento."
        ),
        "diferenciais": (
            "Cadastro digital simples, feito para quem vende fiado de verdade: em dois toques a venda está "
            "registrada no balcão, sem planilha e sem sistema de gestão."
        ),
        "riscos": (
            "Disposição a pagar baixa e concorrência com caderno, WhatsApp e memória. Dados de clientes "
            "terceiros exigem cuidado com LGPD (finalidade, retenção e segurança). A ferramenta organiza a "
            "cobrança, mas não elimina inadimplência: prometer recuperação de dívida seria enganoso. Parte do "
            "fiado é informal — comunicar que o controle é interno e do lojista evita resistência."
        ),
        "validacao": [
            "Entrevistar 10 lojistas: quanto está em aberto hoje, quanto já perderam, como cobram.",
            "Perguntar se já deixaram de vender a prazo por não lembrar do saldo do cliente.",
            "Oferecer registrar todo o fiado atual no aplicativo de graça e acompanhar uso por duas semanas.",
            "Medir se voltam a lançar depois da primeira semana — o caderno só perde se o digital for mais rápido.",
        ],
        "ressalvas": (
            "Dados pessoais de clientes (nome, contato, histórico de compra) só para a finalidade declarada, "
            "com acesso restrito ao lojista e retenção definida (LGPD). Não registrar dívida como crédito "
            "formal, não emitir documentos com valor legal e não realizar cobrança sem consentimento."
        ),
    },
    # ------------------------------------------------------------------ 11
    {
        "num": 11,
        "nome": "AtaqueLab",
        "tagline": "Simulações autorizadas de phishing e conscientização de funcionários",
        "trilha": 6,
        "descricao": (
            "Plataforma de treinamento por campanha controlada: com autorização documentada da empresa, envia "
            "simulações realistas de phishing para os próprios funcionários, mede quem caiu, entrega treinamento "
            "curto direcionado e acompanha a evolução mês a mês."
        ),
        "problema": (
            "Pequenas empresas treinam segurança de forma genérica — ou não treinam — e não sabem quantos "
            "funcionários clicariam em um e-mail falso. Phishing continua sendo a porta de entrada mais "
            "comum de incidentes, mas soluções de conscientização são vendidas em pacotes complexos, em "
            "inglês, pensados para grandes empresas. Quem cuida de TI numa empresa de 40 pessoas não tem "
            "tempo nem ferramenta para isso."
        ),
        "publico": (
            "Empresas de 10 a 200 funcionários sem time de segurança dedicado: comércio, serviços, indústria "
            "leve, clínicas, escritórios de advocacia e contabilidade, agências e e-commerces. Decisor: dono, "
            "sócio ou responsável administrativo de TI."
        ),
        "como_funciona": (
            "A empresa assina termo de autorização registrado na plataforma e define a campanha: remetente, "
            "modelo de e-mail (fatura falsa, RH, senha expirando), público e período. Os e-mails são enviados "
            "para os próprios funcionários; a plataforma registra abertura, clique e relatório voluntário do "
            "usuário, sempre em ambiente controlado. Quem 'caiu' recebe treinamento de três a cinco minutos; "
            "a liderança vê painel com evolução por setor e relatório mensal. Nenhum dado de terceiro é "
            "coletado e nenhuma página de destino falsa captura informações reais."
        ),
        "mvp": [
            "Cadastro da empresa com registro de autorização assinada (termo versionado e guardado).",
            "Dois a três modelos de campanha prontos em português, com dificuldade crescente.",
            "Envio controlado de e-mails com rastreamento de abertura, clique e relatório voluntário.",
            "Landing page segura de simulação, que não coleta dados e explica o resultado ao usuário clicar.",
            "Painel de métricas por campanha e por setor, com microtreinamento direcionado.",
        ],
        "fora": [
            "Pentest de rede, aplicações ou infraestrutura e qualquer exploração real.",
            "Engenharia social por telefone, SMS ou WhatsApp em escala.",
            "Monitoramento 24/7, resposta a incidentes e operação de SOC.",
            "Certificações, auditorias formais e laudos de conformidade.",
            "Plataforma completa de cursos com trilhas, vídeos e certificados.",
        ],
        "tecnologias": [
            "Backend com envio de e-mail transacional próprio, com SPF/DKIM/DMARC bem configurados (ver DomínioSeguro).",
            "Landing pages isoladas em domínio próprio, sem captura de dados, com apenas rastreamento de evento.",
            "Painel web com autenticação forte, controle de acesso por papel e trilha de auditoria.",
            "Banco de dados com criptografia em repouso e segregação por cliente.",
            "Infraestrutura dedicada da simulação, separada de qualquer sistema do cliente.",
        ],
        "quem_pagaria": (
            "O responsável administrativo ou dono da empresa, que enxerga risco e custo de incidente. "
            "Consultores e MSPs (empresas de TI terceirizada) podem revender para sua carteira — canal com "
            "potencial a validar."
        ),
        "monetizacao": (
            "Assinatura mensal por empresa ou por usuário treinado, com pacote anual de campanhas. Plano "
            "para parceiros de TI com múltiplas empresas. Preço é hipótese: validar contra o custo percebido "
            "de um incidente e contra o orçamento real de treinamento dessas empresas."
        ),
        "diferenciais": (
            "Feito para empresas pequenas: campanha pronta em minutos, relatório em português e preço "
            "proporcional ao porte. A autorização documentada e a página segura de simulação são parte do "
            "produto, não um adendo jurídico."
        ),
        "riscos": (
            "Risco ético e legal é o risco número um: simulação sem autorização escrita pode configurar "
            "ilícito; o termo, a finalidade e os dados precisam estar claros (LGPD e legislação aplicável). "
            "Campanha mal comunicada gera desconfiança interna ou pânico — comunicação com a empresa antes do "
            "envio é obrigatória. Envio depende de e-mail confiável: domínio mal configurado prejudica "
            "entregabilidade. O produto deve ser vendido como treinamento, nunca como 'ataque'."
        ),
        "validacao": [
            "Entrevistar 8 a 10 responsáveis por TI/administração: já tiveram incidente? Treinam equipe? Quanto gastam?",
            "Perguntar quem decide e qual o orçamento anual existente para segurança/treinamento.",
            "Oferecer uma campanha piloto gratuita mediante termo de autorização assinado.",
            "Medir taxa de clique, percepção de valor e intenção de contratar continuidade.",
        ],
        "ressalvas": (
            "Autorização escrita e específica é pré-condição de qualquer campanha; sem ela, nada é enviado. "
            "Nunca coletar credenciais, documentos ou dados de terceiros; a simulação só registra eventos de "
            "interação. Manter finalidade, minimização e retenção definidas (LGPD). Não realizar varreduras, "
            "invasões ou qualquer ação fora do ambiente autorizado da própria empresa cliente."
        ),
    },
    # ------------------------------------------------------------------ 12
    {
        "num": 12,
        "nome": "DomínioSeguro",
        "tagline": "Diagnóstico de segurança de e-mail empresarial, verificando SPF, DKIM e DMARC",
        "trilha": 6,
        "descricao": (
            "Auditoria automática da configuração de e-mail de um domínio: verifica SPF, DKIM e DMARC, explica "
            "em português o que está errado, gera os registros sugeridos e monitora mudanças com alerta "
            "periódico."
        ),
        "problema": (
            "A maioria das empresas pequenas envia e-mail sem SPF, DKIM ou DMARC corretamente configurados: "
            "mensagens caem em spam, e pior, qualquer pessoa pode forjar o remetente e usar o nome da empresa "
            "para golpes, porque não há política que impeça. Donos e gestores não sabem que isso existe, não "
            "têm quem verifique e só descobrem quando o cliente recebe um e-mail falso em nome deles."
        ),
        "publico": (
            "Empresas com domínio próprio de qualquer porte — PMEs, e-commerces, clínicas, agências, "
            "escritórios —, além de prestadores e consultores de TI que atendem várias empresas e precisam "
            "diagnóstico rápido para sua carteira (canal com forte potencial)."
        ),
        "como_funciona": (
            "O usuário informa o domínio. A plataforma consulta os registros DNS públicos, avalia a presença "
            "e a qualidade de SPF e DMARC (política, alinhamento, endereço de relatório), tenta identificar "
            "DKIM quando exposto, e devolve um diagnóstico com nota, riscos em linguagem simples e passo a "
            "passo de correção com os registros prontos para colar no painel do provedor. Em seguida, verifica "
            "o domínio semanalmente, registra mudanças e avisa por e-mail quando algo se deteriora ou é "
            "corrigido."
        ),
        "mvp": [
            "Consulta DNS de SPF, DKIM (quando identificável) e DMARC com análise de política e alinhamento.",
            "Diagnóstico em linguagem simples com nota, gravidade e recomendação priorizada.",
            "Geração de registros sugeridos, incluindo política DMARC progressiva e endereço de relatório.",
            "Verificação agendada com histórico de mudanças e alerta por e-mail.",
            "Exportação do relatório em PDF para apresentar à gestão ou ao cliente.",
        ],
        "fora": [
            "Bloqueio de phishing em tempo real e filtragem de e-mail.",
            "Caça a golpes, takedown, remoção de páginas e monitoramento de marca.",
            "Varredura de vazamento de dados, gestão de senhas e antivírus.",
            "Simulação de phishing (ver AtaqueLab) e treinamento de equipe.",
            "API corporativa, white-label completo e integração com painéis de provedores.",
        ],
        "tecnologias": [
            "Consultas DNS (UDP ou DNS-over-HTTPS) com parser próprio de registros SPF/DMARC.",
            "Backend em Python ou Node com agendador de verificações e armazenamento de histórico.",
            "Painel web responsivo com autenticação e cadastro de domínios monitorados.",
            "Fila de e-mails para alertas e geração de PDF de relatório.",
            "Opção futura de webhook/API para parceiros revenderem o monitoramento.",
        ],
        "quem_pagaria": (
            "O dono ou responsável de TI da empresa — e, com mais força, o consultor ou MSP que atende várias "
            "empresas e quer diagnóstico recorrente para sua carteira (hipótese a validar)."
        ),
        "monetizacao": (
            "Diagnóstico pontual gratuito (funil de entrada) e assinatura de monitoramento por domínio, com "
            "plano para consultores que gerenciam múltiplos domínios e emitem relatórios para clientes. "
            "Preço e formato do plano de parceiro são hipóteses a validar."
        ),
        "diferenciais": (
            "Resultado imediato e acionável em minutos, sem instalar nada e em português claro. O relatório "
            "com passo a passo leva o leigo até a correção. Excelente objeto de demonstração: pode-se "
            "diagnosticar um domínio real na apresentação e mostrar o problema encontrado."
        ),
        "riscos": (
            "Relatório detalhado só deve ser divulgado ao responsável pelo domínio — validar propriedade ou "
            "consentimento antes de expor falhas (risco de expor terceiros). Concorrência com verificadores "
            "gratuitos de DNS: o diferencial é monitoramento, relatório e canal de revenda, o que precisa ser "
            "comprovado. DNS tem propagação lenta: atrasos geram falsos negativos e frustração se não forem "
            "explicados."
        ),
        "validacao": [
            "Testar o diagnóstico com 10 domínios de empresas conhecidas, compartilhando o resultado apenas com o responsável autorizado.",
            "Entrevistar donos: já sofreram sequestro de e-mail, spam no nome da empresa ou golpe clonado?",
            "Entrevistar 3 a 5 consultores de TI: quanto tempo gastam diagnosticando, se pagariam por monitoramento da carteira.",
            "Oferecer monitoramento gratuito por 30 dias e medir retenção e intenção de contratar.",
        ],
        "ressalvas": (
            "Trabalha apenas com DNS público e com autorização do responsável pelo domínio. Não intercepta, "
            "não lê e não armazena conteúdo de e-mails — apenas registros técnicos. Divulgação de falha a "
            "terceiros sem autorização deve ser evitada; o diagnóstico é entregue ao dono do domínio. Dados de "
            "conta seguem a LGPD."
        ),
    },
    # ------------------------------------------------------------------ 13
    {
        "num": 13,
        "nome": "RotaCerta",
        "tagline": "Otimização de rotas de entrega",
        "trilha": 7,
        "descricao": (
            "Montagem automática da rota do dia para operações pequenas: o lojista informa as entregas, a "
            "ferramenta calcula a melhor ordem, envia para o entregador e registra o resultado de cada parada."
        ),
        "problema": (
            "Pequenos comércios e entregadores montam a rota 'de cabeça' ou no mapa do celular, parada por "
            "parada. Em operações com dez a trinta entregas por dia, isso significa deslocamento a mais, "
            "combustível queimado, atraso em entrega que exige janela e cliente insatisfeito. Ferramentas "
            "profissionais de roteirização são caras, complexas e exigem integração com sistemas que a loja "
            "nem tem."
        ),
        "publico": (
            "Operações com um a três veículos ou motos: lojas de bairro com entrega própria, e-commerces "
            "pequenos, pizzarias e restaurantes, farmácias de entrega, hortifruti, flores e móveis sob encomenda."
        ),
        "como_funciona": (
            "O usuário lança ou importa as entregas do dia (endereço, nome, janela desejada), escolhe o "
            "veículo e a capacidade, e o sistema gera a sequência de paradas com estimativa de tempo e "
            "distância. A rota é compartilhada com o entregador por link, que a abre no aplicativo de "
            "navegação de sua preferência. Cada parada é marcada como entregue ou não entregue com observação "
            "e o painel consolida km, tempo e pendências do dia."
        ),
        "mvp": [
            "Lançamento manual ou por planilha das paradas do dia, com validação simples de endereço.",
            "Cálculo da rota otimizada com limite de paradas, capacidade e janela de horário.",
            "Sequência de paradas com estimativa de tempo e compartilhamento por link.",
            "Abertura direta em app de navegação (deep link para Google Maps/Waze).",
            "Registro de entrega/pendência e relatório diário de km e tempo por entregador.",
        ],
        "fora": [
            "Gestão de frota, telemática, GPS em tempo real e rastreio do veículo.",
            "Rastreio para o cliente final com mapa ao vivo e notificação de chegada.",
            "Alocação automática de pedidos de marketplaces e integração com ERPs.",
            "Múltiplos depósitos, veículos terceirizados e roteirização com janelas complexas de grande escala.",
            "App nativo offline completo e gestão de combustível/custos de frota.",
        ],
        "tecnologias": [
            "Backend em Python ou Node com serviço de roteirização: algoritmo próprio + distância por estrada.",
            "Motor de rota open source auto-hospedado (ex.: OSRM/Valhalla) ou API de mapas comercial (validar custo).",
            "Banco com suporte geográfico (PostGIS) e geocodificação de endereços.",
            "PWA do entregador e painel do lojista, ambos responsivos.",
            "Deep links para apps de navegação e exportação da rota em formato de lista.",
        ],
        "quem_pagaria": (
            "O lojista ou gestor de entrega, que enxerga economia direta em km, tempo e atraso. Suscetível a "
            "conversão por demonstração: mostra-se a rota de amanhã e compara com a montada à mão."
        ),
        "monetizacao": (
            "Assinatura mensal por operação, com planos pelo número de rotas diárias ou de entregadores, e "
            "teste gratuito limitado. Preço é hipótese: calibrar contra o custo de combustível e tempo "
            "economizados relatados em entrevistas."
        ),
        "diferenciais": (
            "Proporcional a uma operação de duas motos: sem implantação pesada, sem integração obrigatória e "
            "com foco na realidade brasileira (bairro, referência, WhatsApp e app de navegação do entregador)."
        ),
        "riscos": (
            "Qualidade do resultado depende da qualidade do endereço digitado: endereço incompleto gera rota "
            "ruim e frustração — resolver com validação e apoio na digitação. Custo de API de mapa pode corroer "
            "margem; mitigação com motor open source. Concorrência gratuita: 'montar no Google Maps' resolve "
            "paradas poucas — diferenciar com muitas paradas, janelas e comprovante de entrega."
        ),
        "validacao": [
            "Acompanhar 3 a 5 operações reais: quantas paradas por dia, quanto tempo montam rota, km por mês.",
            "Oferecer montar a rota do dia seguinte de graça e comparar tempo e distância com o método atual.",
            "Medir quanto a operação economizaria em km/tempo e perguntar quanto pagaria por isso.",
            "Testar precisão de geocodificação nos bairros alvo antes de prometer ganho de tempo.",
        ],
        "ressalvas": (
            "Dados de clientes que recebem entrega (endereço, nome) são pessoais: usar apenas para a rota, "
            "restringir acesso ao entregador e eliminar após o prazo definido (LGPD). Não prometer ganho "
            "percentual de tempo sem medição real com a operação do cliente."
        ),
    },
    # ------------------------------------------------------------------ 14
    {
        "num": 14,
        "nome": "EntregaCheck",
        "tagline": "Comprovante digital e acompanhamento de entregas",
        "trilha": 7,
        "descricao": (
            "Confirmação de entrega pelo celular do entregador: foto e registro do recebedor, comprovante "
            "digital enviado ao cliente e histórico de cada pedido, encerrando a discussão de 'não recebi'."
        ),
        "problema": (
            "Entrega sem comprovante gera retrabalho: o cliente diz que não recebeu, não há como provar, o "
            "lojista refaz a entrega ou assume o prejuízo. No papel, comprovante se perde e não há como "
            "consultar. E o cliente, por outro lado, não tem notícia nenhuma até ligar para a loja — o que "
            "gera chamados de WhatsApp ocupando o tempo de quem vende."
        ),
        "publico": (
            "Lojas e e-commerces pequenos com entrega própria: mercados de bairro, farmácias, restaurantes, "
            "hortifruti, floriculturas, lojas de brinquedos e eletro pequenos — operações com poucos "
            "entregadores e volume diário."
        ),
        "como_funciona": (
            "A loja registra os pedidos do dia (manual ou por planilha) e envia a lista ao entregador. No "
            "celular, o entregador marca cada parada como entregue com foto opcional, nome de quem recebeu e "
            "observação. O sistema gera o comprovante digital e envia ao cliente por e-mail ou SMS, junto "
            "com link público para acompanhar o status. Tudo fica em histórico pesquisável, com pendências em "
            "destaque para a loja resolver no mesmo dia."
        ),
        "mvp": [
            "Cadastro de pedidos por lote (manual ou importação de planilha).",
            "Tela do entregador com status: saiu para entrega, entregue, não entregue (com motivo).",
            "Comprovante com foto/nome do recebedor e envio automático ao cliente.",
            "Link público de acompanhamento simples por pedido (status e horário).",
            "Histórico de entregas, pendências e relatório diário.",
        ],
        "fora": [
            "Roteirização e otimização de rota (ver RotaCerta).",
            "Rastreio em tempo real por GPS do entregador e mapa ao vivo para o cliente.",
            "Pagamento na entrega (PDV mobile), cobrança e conciliação.",
            "Integração com marketplaces, ERPs e sistemas de gestão da loja.",
            "Assinatura digital com valor jurídico, white-label e aplicativo nativo offline completo.",
        ],
        "tecnologias": [
            "PWA do entregador (funciona no navegador, sem necessidade de loja de aplicativos).",
            "Backend em Node/Python com banco relacional e fila de mensagens.",
            "Armazenamento de fotos em objeto/CDN com acesso restrito e expiração definida.",
            "Envio de e-mail/SMS ao cliente e geração de comprovante em PDF.",
            "Fila offline básica: pendências salvas localmente e sincronizadas ao reconectar (escopo a decidir).",
        ],
        "quem_pagaria": (
            "O dono da loja ou o responsável pela operação de entrega, que já calcula prejuízo por entrega "
            "não confirmada e tempo gasto respondendo cliente. Hipótese de venda por assinatura mensal."
        ),
        "monetizacao": (
            "Assinatura mensal por loja com plano por volume de entregas, e plano gratuito limitado a um "
            "número pequeno de comprovantes. Preço é hipótese a validar contra o custo de uma entrega "
            "repetida."
        ),
        "diferenciais": (
            "Comprovante com foto em minutos, sem app nativo e sem treinamento: o entregador já tem um "
            "celular e um navegador. Resolve uma dor antiga com uma tela."
        ),
        "riscos": (
            "Privacidade: foto do local ou do cliente pode captar pessoas; pedir consentimento do recebedor e "
            "minimizar imagem é o caminho (LGPD). Adesão do entregador é crítica — se ele não registrar, o "
            "produto não existe; manter o fluxo em três toques. Conectividade ruim exige fila offline, o que "
            "amplia escopo. Concorrência com rastreio já embutido em transportadoras e marketplaces."
        ),
        "validacao": [
            "Entrevistar 8 lojas/entregadores: quantos 'não recebi' por mês e quanto custa cada um.",
            "Perguntar como comprovam hoje e quanto tempo respondendo cliente por WhatsApp.",
            "Oferecer duas semanas de comprovante digital grátis para a rota completa.",
            "Medir percentual de entregas registradas pelo entregador — abaixo de 90% o fluxo precisa simplificar.",
        ],
        "ressalvas": (
            "Captura de imagem de pessoas exige consentimento e finalidade clara; evitar registro de rosto e "
            "reter fotos por prazo curto (LGPD). Não prometer prova judicial ou valor jurídico do comprovante. "
            "Dados de cliente final usados apenas para o envio do comprovante."
        ),
    },
]

# Colunas: facilidade de desenvolvimento | potencial comercial | complexidade técnica |
#          necessidade de hardware/integrações externas
COMPARATIVO = {
    1:  ("Alta",   "Média", "Baixa",  "Baixa"),
    2:  ("Média",  "Média", "Média",  "Baixa"),
    3:  ("Alta",   "Média", "Baixa",  "Baixa"),
    4:  ("Alta",   "Média", "Baixa",  "Baixa"),
    5:  ("Média",  "Média", "Média",  "Baixa"),
    6:  ("Média",  "Média", "Média",  "Baixa"),
    7:  ("Baixa",  "Alta",  "Alta",   "Alta"),
    8:  ("Média",  "Alta",  "Média",  "Média"),
    9:  ("Média",  "Alta",  "Média",  "Média"),
    10: ("Alta",   "Média", "Baixa",  "Baixa"),
    11: ("Média",  "Média", "Média",  "Média"),
    12: ("Alta",   "Alta",  "Média",  "Média"),
    13: ("Média",  "Alta",  "Média",  "Alta"),
    14: ("Média",  "Média", "Média",  "Média"),
}

LEGENDA_COMPARATIVO = [
    ("Facilidade de desenvolvimento do MVP",
     "Alta = é possível entregar um uso real com poucas telas e sem integração pesada; "
     "Média = exige integrações ou regras de negócio relevantes; "
     "Baixa = há hardware, validação especial ou dependência externa forte que alonga o ciclo."),
    ("Potencial comercial",
     "Alta = dor com perda financeira direta, comprador claro e pagamento já existente no mercado; "
     "Média = comprador identificado, porém disposição a pagar a confirmar; "
     "Baixa = valor percebido incipiente ou decisão de compra muito difícil de alcançar."),
    ("Complexidade técnica",
     "Baixa = CRUD, painel e relatório; Média = regras de negócio, pareamento ou mensageria; "
     "Alta = hardware, embarcado, tempo real ou dependência crítica de serviço externo."),
    ("Necessidade de hardware ou integrações externas",
     "Baixa = roda apenas com navegador e banco de dados; Média = depende de API de terceiro, canal de "
     "mensagem, DNS ou serviço de mapa; Alta = exige hardware próprio ou serviço externo essencial ao produto."),
]

PRIORIDADES = [
    {
        "num": 9,
        "nome": "PixConcilia",
        "trilha": 5,
        "resumo": "Conciliação de vendas e extrato para pequenos negócios.",
        "por_que": [
            "A dor é financeira, imediata e mensurável: cada hora de conciliação manual e cada real que some "
            "entre vendas e extrato são custo que o lojista já reconhece.",
            "O problema acontece todos os dias e em quase todos os tipos de comércio — base de clientes "
            "potencialmente ampla e fácil de encontrar em qualquer praça.",
            "O MVP dispensa hardware, licença bancária e integração pesada: importar arquivo e casar lançamento "
            "é tecnicamente acessível para uma equipe pequena.",
            "Há caminho de canal natural com contadores, que conhecem a dor e atendem vários compradores de uma vez.",
        ],
        "dificuldades": [
            "Formatos de extrato e relatório variam entre bancos e adquirentes; a manutenção dos parsers é "
            "trabalho contínuo, não tarefa única.",
            "O produto só convence se o pareamento estiver correto: erro de pareamento destrói a confiança mais "
            "rápido do que a falta de recurso.",
            "Dados financeiros exigem padrão alto de segurança; um incidente encerra o produto antes de crescer.",
            "Planilha gratuita e o sistema que o lojista já usa disputam o mesmo espaço — o ganho precisa ser "
            "claramente de tempo, não de funcionalidade.",
        ],
        "caminho": [
            "Mapear 20 lojas de rua e 3 contadores do bairro/região e agendar entrevistas curtas de 15 minutos.",
            "Oferecer conciliar um mês real de extrato de graça e devolver o relatório de divergências em 48 horas.",
            "Usar o próprio relatório como prova de valor: mostrar o tempo gasto e o que ficou pendente.",
            "Converter dois a três lojistas em piloto pago simbólico por 30 dias; preço baixo, compromisso real.",
            "Pedir indicação ativa: 'quem mais na sua rua faz conciliação na mão?' é a porta mais barata de aquisição.",
        ],
    },
    {
        "num": 12,
        "nome": "DomínioSeguro",
        "trilha": 6,
        "resumo": "Diagnóstico de SPF, DKIM e DMARC de e-mail empresarial.",
        "por_que": [
            "Entrega valor em minutos, sem instalação e sem dependência de hardware: o usuário vê o problema "
            "antes mesmo de decidir comprar.",
            "A vulnerabilidade é real e invisível — o domínio da empresa pode estar aberto a sequestro de "
            "remetente sem que ninguém saiba.",
            "Escopo bem delimitado: consultar DNS, analisar e explicar é trabalho técnico contido, adequado ao "
            "tempo de um hackathon e a uma equipe pequena.",
            "Canal de revenda com consultores e MSPs multiplica a força de venda sem custo comercial inicial.",
        ],
        "dificuldades": [
            "Existem verificadores gratuitos de DNS; o produto precisa provar que monitoramento, relatório e "
            "acompanham entram mais do que a consulta avulsa.",
            "Expor falha de terceiros sem autorização é risco — é preciso validar domínio ou consentimento "
            "antes de entregar diagnóstico profundo.",
            "DNS é lento e distribuído: propagação atrasada gera falsos negativos e desconfiança se não for "
            "explicado na interface.",
            "A conversão em pagamento depende de educar o comprador sobre um risco que ele ainda não enxerga.",
        ],
        "caminho": [
            "Diagnosticar 10 domínios de empresas do entorno, com autorização para compartilhar o achado.",
            "Apresentar o relatório em reunião de 10 minutos: problema, risco em reais (golpe no nome da "
            "empresa) e correção passo a passo.",
            "Oferecer monitoramento gratuito por 30 dias para a amostra e pedir continuidade paga no fim.",
            "Abordar 3 a 5 consultores de TI com plano de múltiplos domínios: eles já têm a carteira e a confiança.",
            "Usar o diagnóstico ao vivo na demonstração da competição — é visual, rápido e convincente.",
        ],
    },
    {
        "num": 7,
        "nome": "FrioGuard",
        "trilha": 4,
        "resumo": "Sensor de temperatura com alarme local e registro exportável.",
        "por_que": [
            "A perda é concreta e visível: um dia de câmara parada pode custar mais que o produto inteiro — "
            "o comprador calcula retorno sem precisar de explicação elaborada.",
            "O registro manual de temperatura é obrigação prática que quase ninguém cumpre bem; substituí-lo "
            "automático é ganho imediato.",
            "O diferencial 'funciona sem internet' resolve a objeção número um de tecnologia instalada em "
            "loja e galpão.",
            "Hardware bem-sucedido cria barreira de entrada: quem tem o sensor na parede é difícil de trocar.",
        ],
        "dificuldades": [
            "Hardware multiplica risco: confiabilidade, calibração, custo de peça, produção, estoque e suporte "
            "físico — tudo escala de modo diferente de software.",
            "O prazo de competição é curto para um produto físico; é preciso decidir cedo entre protótipo "
            "funcional limitado e produto pronto demais para ser testado.",
            "Concorrem com sistemas profissionais de refrigeração, mais caros, porém já instalados e com "
            "contrato de manutenção.",
            "Afirmar conformidade sanitária ou validade legal do registro sem revisão especializada expõe a "
            "empresa a risco regulatório.",
        ],
        "caminho": [
            "Entrevistar donos de açougue, mercado e farmácia da região perguntando: já perderam? Quanto? "
            "Como registram hoje?",
            "Montar dois protótipos e deixar instalados por duas semanas em estabelecimento real, com "
            "comparação contra o registro manual.",
            "Devolver ao cliente o relatório daquelas duas semanas: prova concreta de alerta e histórico.",
            "Fechar um piloto com kit emprestado e assinatura simbólica; transformar a perda evitada em "
            "depoimento numérico (com autorização).",
            "Validar cadeia de fornecedores e custo unitário antes de prometer entrega de produto físico.",
        ],
    },
    {
        "num": 8,
        "nome": "AgendaViva",
        "trilha": 4,
        "resumo": "Lembrete, confirmação e lista de espera contra faltas em consultas.",
        "por_que": [
            "O custo da falta é conhecido e recorrente: o profissional sabe quanto vale um horário vazio sem "
            "precisar de estudo para entender.",
            "A venda é consultiva e local — dá para conversar com dez consultórios em uma semana e medir "
            "resposta quase em tempo real.",
            "O MVP é predominantemente software: agenda, lembrete e lista de espera cabem em escopo curto.",
            "Métrica de sucesso objetiva (taxa de faltas antes e depois) facilita demonstrar valor e renovar "
            "assinatura.",
        ],
        "dificuldades": [
            "Custo e dependência de canais de mensagem: e-mail tem baixa taxa de leitura em pacientes e SMS/"
            "WhatsApp oficial têm custo por mensagem que comprime a margem.",
            "Dados de agendamento são sensíveis por contexto: exige disciplina de privacidade desde o primeiro release.",
            "Paciente pode simplesmente não confirmar — o ganho real depende de canal e frequência certos, "
            "que precisam ser descobertos no piloto.",
            "Concorrem com agendas embutidas em sistemas que o consultório talvez já pague.",
        ],
        "caminho": [
            "Mapear 15 consultórios em um raio pequeno e perguntar taxa de faltas e tempo gasto confirmando.",
            "Oferecer 30 dias de lembretes gratuitos com medição de faltas antes e depois.",
            "Devolver o número da comparação ao profissional e propor assinatura mensal com desconto de piloto.",
            "Começar por uma especialidade ou rua inteira para criar densidade de indicação.",
            "Testar canais (e-mail, SMS, WhatsApp) por A/B antes de fixar o modelo de cobrança.",
        ],
    },
    {
        "num": 13,
        "nome": "RotaCerta",
        "trilha": 7,
        "resumo": "Montagem automática da rota de entregas do dia.",
        "por_que": [
            "A economia é direta e contável: quilômetro, hora de entregador e atraso viram número no fim do mês.",
            "Demonstração espetacular: coloca-se a rota montada à mão e a calculada lado a lado na tela — "
            "diferença visível em segundos.",
            "Existem entregas suficientes em qualquer cidade para testar, e o público está fácil de encontrar: "
            "pizzarias, farmácias e lojas de bairro.",
            "MVP factível sem hardware, com motor de rota open source e poucas telas.",
        ],
        "dificuldades": [
            "Endereço mal preenchido degrada o resultado — e em bairro brasileiro a referência pesa mais que "
            "o CEP. Geocodificação precisa de atenção real.",
            "API de mapas comerciais tem custo por chamada que precisa ser planejado; auto-hospedagem exige "
            "manutenção e dados atualizados.",
            "A concorrência barata é o celular: 'montar no Google Maps' resolve rota de cinco paradas. O "
            "produto precisa vencer a partir de dez ou mais.",
            "Ganho de tempo real deve ser medido com a operação do cliente antes de qualquer promessa "
            "comercial.",
        ],
        "caminho": [
            "Acompanhar três a cinco operações por dois dias: contagem de paradas, tempo de montagem e km.",
            "Montar a rota do dia seguinte de graça e comparar com a rota atual, medindo diferença real.",
            "Apresentar o resultado em números ao dono e oferecer piloto pago simbólico por um mês.",
            "Escolher um segmento (pizzaria, farmácia de entrega, hortifruti) para repetir a proposta e "
            "padronizar a venda.",
            "Só depois de validar, investir em rastreio para cliente final e demais funções da lista 'fora do MVP'.",
        ],
    },
]
