# -*- coding: utf-8 -*-
"""Conteúdo da introdução, do plano de validação, do plano de execução e da conclusão."""

AVISO = {
    "titulo": "Aviso de leitura",
    "texto": (
        "Este é um documento de trabalho de equipe. Todas as avaliações de potencial, complexidade, "
        "monetização e prazo são hipóteses construídas para orientar a escolha entre as ideias — não são "
        "resultados de pesquisa de mercado, não representam dados verificados e não devem ser usadas em "
        "materiais comerciais como se fossem fatos. Nenhum preço, estatística ou concorrente foi assumido "
        "como verdade. Tudo o que envolve cliente, preço, canal e regulação precisa ser validado em "
        "entrevistas reais antes do desenvolvimento."
    ),
}

INTRODUCAO = {
    "paragrafos": [
        (
            "O Hack Brasil 2026 é uma oportunidade rara de transformar um problema observado na vida real "
            "em um produto testável em poucos dias. Este banco de ideias reúne 14 propostas distribuídas "
            "nas sete trilhas da competição, escritas para serem debatidas por uma equipe pequena que precisa "
            "escolher bem: o tempo investido em uma ideia certa vale mais do que qualquer otimização técnica "
            "aplicada a uma ideia errada."
        ),
        (
            "O objetivo do material é duplo. Primeiro, oferecer um ponto de partida estruturado: cada ideia "
            "vem com problema, público, escopo de MVP, monetização hipotética, riscos e um caminho de "
            "validação, para que a equipe não comece do zero em branco. Segundo, tornar a comparação honesta: "
            "as fichas explicitam o que fica de fora da primeira versão e o que ainda precisa ser provado, "
            "evitando que uma boa descrição de produto esconda uma hipótese comercial frágil."
        ),
        (
            "As 14 ideias foram filtradas por cinco critérios. Eles não garantem sucesso — servem para "
            "eliminar rapidamente propostas que exigiriam tempo, cliente ou tecnologia acima do alcance de "
            "uma equipe enxuta durante a competição."
        ),
    ],
    "criterios": [
        {
            "titulo": "Resolver problemas reais",
            "texto": (
                "O problema precisa existir hoje, ser perceptível na rotina de alguém e ter consequência "
                "concreta — dinheiro perdido, tempo desperdiçado, risco assumido ou oportunidade "
                "desperdiçada. Ideias que apenas parecem úteis, sem dor declarada por quem vive o problema, "
                "foram descartadas."
            ),
        },
        {
            "titulo": "Ter um MVP tecnicamente viável para uma equipe pequena",
            "texto": (
                "Três pessoas, prazo curto e escopo limitado: a primeira versão precisa caber em um punhado "
                "de telas e um banco de dados, sem depender de hardware complexo, integrações pesadas ou "
                "infraestrutura que só equipe grande sustenta. Exceções conscientes estão marcadas como tal."
            ),
        },
        {
            "titulo": "Possuir público-alvo identificável",
            "texto": (
                "É preciso ser possível apontar quem é o comprador, onde ele está e como conversar com ele "
                "na primeira semana — lojistas na rua, consultórios na esquina, cooperativas do bairro, "
                "consultores de TI conhecidos. Sem público acessível, não há como validar."
            ),
        },
        {
            "titulo": "Ter potencial de monetização",
            "texto": (
                "O comprador precisa perder algo mensurável com o problema ou já gastar dinheiro com uma "
                "solução imperfeita — planilha, caderno, terceirizado, hora do funcionário. Isso abre espaço "
                "para um modelo de receita plausível, ainda que o preço em si seja hipótese a validar."
            ),
        },
        {
            "titulo": "Poder evoluir depois da competição",
            "texto": (
                "A ideia precisa ter caminho natural de crescimento: mais módulos, mais clientes do mesmo "
                "perfil, receita recorrente ou dados que melhorem o produto. Um experimento que morre com a "
                "demonstração não sustenta uma startup."
            ),
        },
    ],
    "como_usar": [
        "Seção 2 — panorama rápido das sete trilhas e das duas ideias de cada uma.",
        "Seção 3 — ficha detalhada de cada uma das 14 ideias, com escopo e fora de escopo.",
        "Seção 4 — tabela comparativa para cortar opções com critérios uniformes.",
        "Seção 5 — aprofundamento das cinco ideias consideradas prioritárias para investigação.",
        "Seção 6 — roteiro e perguntas para validar com potenciais clientes antes de programar.",
        "Seção 7 — método de execução do MVP para uma equipe de três pessoas.",
        "Seção 8 — reflexão final sobre escolher o problema antes da tecnologia.",
    ],
    "nao_e": (
        "Este documento não é pesquisa de mercado, estudo de concorrência ou plano de negócios. É um "
        "material de decisão interna: serve para escolher três ideias, conversar com clientes reais e "
        "construir o menor produto capaz de provar (ou derrubar) a hipótese central."
    ),
}

VALIDACAO_INTRO = (
    "Nenhuma das 14 ideias deve ir para o código sem antes passar por conversas reais com quem vive o "
    "problema. O roteiro abaixo foi desenhado para ser cumprido por uma equipe pequena, em poucos dias, com "
    "custo baixo e resultado comparável entre as ideias: mesmo número de entrevistas, mesmas perguntas, "
    "mesmo formato de registro. O objetivo não é validar a ideia que a equipe gosta — é descobrir qual das "
    "hipóteses resiste ao contato com a realidade."
)

VALIDACAO_ETAPAS = [
    (
        "Selecionar três ideias finalistas",
        "Usar a tabela comparativa e a discussão da equipe para reduzir de 14 para 3. Priorizar: dor "
        "relatada com facilidade, acesso rápido a clientes, execução dentro do tempo da competição e "
        "menor dependência externa (hardware, dois lados de rede, aprovação regulatória).",
        "Uma folha com as três ideias escolhidas e a razão de cada escolha.",
    ),
    (
        "Identificar ao menos cinco potenciais clientes por ideia",
        "Montar a lista com nome, negócio, cargo, telefone ou WhatsApp e onde encontrar. Usar rua, feira, "
        "redes sociais, associações de comerciantes, contadores, consultórios e conhecidos em comum.",
        "15 contatos mapeados, com pelo menos 10 deles efetivamente abordados.",
    ),
    (
        "Entrevistar essas pessoas",
        "Conversas de 20 a 30 minutos sobre o problema: como é a rotina, quando aconteceu pela última vez, "
        "como resolvem hoje e quanto custa essa dificuldade em dinheiro e tempo. Registrar tudo em ficha "
        "padronizada, com as frases do entrevistado.",
        "Fichas de entrevista preenchidas, com ao menos uma citação literal por conversa.",
    ),
    (
        "Descobrir se já pagam por alguma solução",
        "Perguntar o que já compraram (sistema, planilha paga, terceirizado, hora de funcionário), quanto "
        "custa, por que continuaram ou cancelaram. Se não pagam nada, entender o que fariam em vez de pagar.",
        "Hipótese de preço ancorada em um valor que o cliente já reconhece como gasto.",
    ),
    (
        "Apresentar uma proposta de MVP",
        "Uma página: o que o produto faz em uma frase, três telas principais, prazo de entrega do piloto "
        "e preço do piloto. Mostrar apenas ao final da conversa, depois de ouvir o problema.",
        "Proposta única, escrita, igual para todos os entrevistados daquela ideia.",
    ),
    (
        "Buscar o primeiro cliente de piloto",
        "Pedir compromisso explícito: testar por 30 dias ou pagar um valor simbólico. E-mail ou mensagem "
        "de confirmação vale como acordo. Definir junto o critério de sucesso (o que precisará ser verdade "
        "para continuar).",
        "Um piloto com nome de cliente, data inicial e critério de sucesso acordado.",
    ),
]

REGRAS_ENTREVISTA = [
    "Ouvir antes de falar: a ideia só é mencionada nos últimos cinco minutos.",
    "Perguntar sobre comportamento passado, não sobre opinião futura — 'o que você fez' vale mais que 'você compraria?'.",
    "Pedir números mesmo aproximados: quanto tempo, quantas vezes por semana, quanto já perdeu.",
    "Anotar as frases exatas do entrevistado: elas viram texto de produto e argumento de venda.",
    "Nunca apresentar preço antes de entender o custo atual do problema.",
    "Encerrar pedindo indicação de mais duas pessoas com o mesmo problema.",
    "Registrar a conversa na ficha no mesmo dia, antes que a memória suavize os detalhes.",
]

PERGUNTAS_GRUPOS = [
    (
        "A. Sobre o problema e a rotina",
        [
            "Como é o seu dia em relação a [problema da ideia]? Descreva o processo do começo ao fim.",
            "Quando foi a última vez que esse problema aconteceu? O que você fez naquele momento?",
            "Com que frequência acontece — todo dia, toda semana, todo mês?",
            "Quem é a pessoa que mais sofre com isso na sua operação?",
            "O que você já tentou para resolver? Por que parou ou não funcionou?",
            "O que acontece quando o problema não é resolvido: prejuízo, atraso, cliente bravo, risco?",
        ],
    ),
    (
        "B. Sobre a solução atual e o custo da dificuldade",
        [
            "Como você resolve hoje: caderno, planilha, aplicativo, papel, memória, pessoa dedicada?",
            "Quanto tempo por dia ou por semana alguém gasta com isso?",
            "Você chegou a perder dinheiro, produto ou cliente por causa disso no último ano? Quanto, mais ou menos?",
            "Esse custo está em algum lugar do seu orçamento hoje, mesmo que escondido na conta de energia, no estoque ou na hora do funcionário?",
            "Se isso fosse resolvido amanhã, o que mudaria na sua operação?",
        ],
    ),
    (
        "C. Sobre pagamento e alternativas",
        [
            "Você já pagou por alguma solução para isso? Qual, quanto e por quanto tempo?",
            "Por que continuou pagando — ou por que cancelou?",
            "Além de pagar, o que você já investiu de tempo montando sua própria solução?",
            "Quem na sua empresa decide comprar uma ferramenta? Como é esse processo?",
            "Existem alternativas que você já olhou (outro app, terceirizar, contratar alguém)?",
            "Se existisse algo que resolvesse, quanto de tempo ou dinheiro isso precisaria te devolver para valer a pena?",
        ],
    ),
    (
        "D. Sobre a proposta — somente ao final da conversa",
        [
            "Se eu montar isso em [prazo] e te entregar por [preço do piloto], você testaria? Com qual critério?",
            "O que te faria desistir de usar a ferramenta depois de uma semana?",
            "Quem mais você indicaria para eu conversar — alguém com o mesmo problema na cidade?",
            "Posso te mandar uma página de uma tela explicando a proposta para você confirmar por mensagem?",
        ],
    ),
]

FICHA_ENTREVISTA = [
    ("Identificação", "Ideia · Nome do entrevistado · Negócio/cargo · Data · Canal (presencial, telefone, mensagem)"),
    ("Problema relatado", "Frases literais do entrevistado sobre quando e como o problema acontece"),
    ("Como resolve hoje", "Ferramenta, processo e pessoa envolvida atualmente"),
    ("Custo da dificuldade", "Tempo gasto, dinheiro perdido e consequências já vividas"),
    ("Já paga por algo?", "O que paga hoje, quanto, há quanto tempo e por que não trocou"),
    ("Reação à proposta", "O que pareceu convincente, o que gerou dúvida, objeções ouvidas"),
    ("Compromisso obtido", "Piloto pago, piloto gratuito, só indicação ou desinteresse — com data"),
    ("Próximo passo", "O que a equipe se comprometeu a enviar e até quando"),
]

FINALISTAS_CRITERIOS = [
    "Dor relatada com frequência e custo concreto em pelo menos três entrevistas.",
    "Cliente já gasta algo hoje (dinheiro, tempo de funcionário ou solução improvisada cara).",
    "Acesso garantido a pelo menos cinco entrevistados antes de começar a desenvolver.",
    "MVP executável dentro do tempo da competição por quem está no time.",
    "Baixa dependência externa: sem hardware, sem dois lados de rede e sem aprovação regulatória no caminho crítico.",
    "Empate decidido pelo critério humano: qual problema o time consegue sustentar com entusiasmo por semanas.",
]

EXECUCAO_INTRO = (
    "A metodologia abaixo supõe uma equipe de três pessoas, um prazo curto e um objetivo claro: sair da "
    "competição com um produto funcional, um cliente real testando e uma história defensável. O princípio "
    "que organiza tudo é simples — validar cedo, cortar cedo e entregar em fatias verticais, ou seja, "
    "funcionando de ponta a ponta desde o primeiro dia, em vez de camadas pela metade."
)

EXECUCAO_ETAPAS = [
    {
        "titulo": "1. Pesquisa e validação",
        "duracao": "2 a 3 dias, no início (e contínua)",
        "objetivo": (
            "Escolher o problema com evidência de conversa real, não com preferência do time. Se a equipe "
            "já escolheu a ideia, esta etapa confirma ou derruba a hipótese central antes de qualquer linha "
            "de código."
        ),
        "atividades": [
            "Aplicar o roteiro de entrevistas da seção 6 com cinco a dez pessoas por ideia finalista.",
            "Escrever em uma frase o problema, o comprador e a consequência de não resolvê-lo.",
            "Definir o critério de sucesso do piloto: qual número precisa mudar para o cliente continuar.",
            "Registrar hipótese de preço com base no que o cliente já gasta hoje.",
        ],
        "entregavel": "Resumo de entrevistas (uma página), frase de problema, comprador e critério de sucesso do piloto.",
    },
    {
        "titulo": "2. Definição do escopo",
        "duracao": "1 dia",
        "objetivo": (
            "Converter a hipótese no menor produto capaz de prová-la. Toda ideia nasce grande demais: o "
            "trabalho desta etapa é decidir, por escrito, o que fica de fora."
        ),
        "atividades": [
            "Escrever a história única do usuário: 'Eu quero [resultado] para [motivo]'.",
            "Listar os três fluxos essenciais que precisam funcionar de ponta a ponta.",
            "Listar por escrito tudo que não entrará — a lista 'não vai' é entregável, não enfeite.",
            "Definir critério de pronto para cada item: o que significa estar finalizado.",
            "Cortar novamente: se couber com folga, falta cortar.",
        ],
        "entregavel": "Backlog enxuto (15 a 25 itens) e lista de escopo negado, compartilhada com toda a equipe.",
    },
    {
        "titulo": "3. Arquitetura e tecnologias",
        "duracao": "Meio dia",
        "objetivo": (
            "Escolher a menor stack que a equipe domina, modelar os dados e deixar o caminho de deploy "
            "traçado — sem experimento tecnológico em véspera."
        ),
        "atividades": [
            "Usar tecnologias já conhecidas pelo time: nada de framework novo durante a competição.",
            "Desenhar o modelo de dados em uma página: entidades, relacionamentos e quem é dono de cada dado.",
            "Decidir autenticação, hospedagem, banco e estratégia de backup.",
            "Criar repositório base, ambiente de desenvolvimento e deploy de continuidade desde o primeiro commit.",
            "Preparar base de demonstração com dados realistas e estáveis (nada de tela vazia no pitch).",
        ],
        "entregavel": "Diagrama de arquitetura de uma página, repositório inicial e ambiente publicado por link.",
    },
    {
        "titulo": "4. Desenvolvimento",
        "duracao": "Maior bloco de tempo disponível",
        "objetivo": (
            "Entregar funcionalidade de ponta a ponta, repetidamente. A regra é fatia vertical: dado entrando, "
            "regra aplicando, tela mostrando, resultado saindo — completo."
        ),
        "atividades": [
            "Trabalhar na ordem dos três fluxos essenciais, um por vez, até funcionarem completos.",
            "Integrar no principal a cada dia; nada de branch que fica dias sem fundir.",
            "Manter a base de demonstração sempre populada e utilizável.",
            "Congelar escopo assim que o primeiro fluxo terminar: o restante é refinamento, não nova funcionalidade.",
            "Anotar decisões de produto em um único arquivo do time (por que cortamos, por que fizemos assim).",
        ],
        "entregavel": "Aplicação com os três fluxos principais funcionais, publicada e acessível por link.",
    },
    {
        "titulo": "5. Testes",
        "duracao": "Contínua, desde o primeiro dia",
        "objetivo": (
            "Garantir que a demonstração não morra por um caso simples — e que o produto não exponha dados "
            "ou dependa de condições perfeitas."
        ),
        "atividades": [
            "Roteiro de teste manual por fluxo: caso feliz, dado vazio, dado inválido e repetição do comando.",
            "Testar com três pessoas de fora do time, sem explicação prévia, apenas observando.",
            "Revisão de segurança básica: senhas, controle de acesso, sem dado sensível exposto em tela ou log.",
            "Verificação de privacidade mínima: só coletar o necessário, informar finalidade, prever exclusão.",
            "Registrar defeitos com gravidade e corrigir apenas os críticos e os visíveis na demonstração.",
        ],
        "entregavel": "Lista de defeitos classificada, críticos corrigidos e evidência de três testes com usuários externos.",
    },
    {
        "titulo": "6. Demonstração",
        "duracao": "1 dia, com ensaio",
        "objetivo": (
            "Apresentar o produto com segurança: roteiro curto, dados estáveis e plano B para falha de "
            "internet ou do ambiente."
        ),
        "atividades": [
            "Escrever roteiro de quatro minutos: problema, evidência da validação, produto ao vivo, próximo passo.",
            "Gravar vídeo de contingência de todo o percurso da demonstração.",
            "Popular a base com dados verossímeis e revisar textos da interface.",
            "Ensaio com cronômetro, com alguém do time fingindo ser jurado e perguntando o inesperado.",
        ],
        "entregavel": "Roteiro aprovado, vídeo de contingência e ambiente estável na hora da apresentação.",
    },
    {
        "titulo": "7. Pitch e modelo de negócio",
        "duracao": "Meio dia, após o ensaio",
        "objetivo": (
            "Conectar o produto a um negócio possível, com honestidade sobre o que é fato e o que é hipótese."
        ),
        "atividades": [
            "Narrativa em sete slides: problema, evidência, solução, público, modelo de receita (hipótese), piloto, próximos 90 dias.",
            "Marcar verbalmente o que já foi validado e o que ainda é hipótese — credibilidade nasce do rigor.",
            "Preparar respostas para: tamanho de mercado (sem inventar número), concorrência (planilha e status quo) e custo de aquisição.",
            "Definir o pedido claro ao fim: cliente piloto, investidor ou parceiro.",
        ],
        "entregavel": "Pitch de cinco a sete slides e um pedido explícito ao final da apresentação.",
    },
]

PAPELS = [
    (
        "Pessoa A — Produto e validação",
        "Conduz entrevistas, decide o escopo, escreve os textos da interface, mantém o backlog e é dona da "
        "narrativa do pitch. Também é a pessoa que segura o relógio: corta escopo quando o tempo aperta.",
    ),
    (
        "Pessoa B — Backend e dados",
        "Modela o banco, escreve a API, faz integrações e importações de arquivo, cuida de autenticação, "
        "proteção de dados e deploy. Responde pela estabilidade do ambiente de demonstração.",
    ),
    (
        "Pessoa C — Interface e demonstração",
        "Constrói as telas, o painel e a base de dados de demonstração, aplica a identidade visual e conduz "
        "o ensaio da demonstração. É também a primeira pessoa a testar cada fluxo entregue.",
    ),
    (
        "Responsabilidades compartilhadas",
        "Teste manual diário, apoio na bancada durante a demonstração, revisão do pitch e decisões de corte "
        "tomadas em conjunto. Em dupla, os papéis se dividem de forma assimétrica: um assume produto + interface, o "
        "outro backend + dados — e os dois validam com cliente.",
    ),
]

CRONOGRAMA = [
    ("Pesquisa e validação", "2 a 3 dias", "Três ideias reduzidas, entrevistas registradas, hipótese de valor escrita"),
    ("Definição do escopo", "1 dia", "Backlog enxuto e lista de escopo negado"),
    ("Arquitetura e tecnologias", "Meio dia", "Modelo de dados, repositório e deploy de continuidade"),
    ("Desenvolvimento", "Maior bloco", "Três fluxos completos funcionando de ponta a ponta"),
    ("Testes", "Contínua", "Críticos corrigidos e três testes com usuários externos"),
    ("Demonstração", "1 dia + ensaio", "Roteiro, vídeo de contingência e ambiente estável"),
    ("Pitch e modelo de negócio", "Meio dia", "Slides finais, hipóteses marcadas e pedido claro"),
]

CRITERIOS_PRONTO = [
    "O fluxo funciona do início ao fim com dados realistas, sem passo manual escondido.",
    "Uma pessoa de fora do time consegue concluir o fluxo sem explicação.",
    "Nenhum defeito crítico conhecido permanece aberto.",
    "O produto está publicado em um link que abre em qualquer navegador.",
    "Existe vídeo de contingência e base de demonstração restaurável.",
    "Nenhuma funcionalidade nova entrou nas últimas 24 horas antes da demonstração.",
]

RISCOS_TIME = [
    ("Escopo grande demais", "Aplicar a regra do corte pela metade: o que é essencial vira metade, o resto entra na lista negada."),
    ("Tecnologia nova", "Proibido usar framework, banco ou serviço que ninguém do time já tenha usado em produção."),
    ("Perfeccionismo de interface", "Usar componentes prontos e uma paleta única; a demonstração valoriza fluxo funcionando, não pixel."),
    ("Validação adiada", "Nenhum código antes de cinco conversas: prazo é curto, conversa é barata e corte é doloroso."),
    ("Dependência de serviço externo", "Prever plano B para API indisponível: arquivo importado, dado de demonstração ou modo manual."),
    ("Integrante bloqueado", "Trabalhar em pares nas tarefas travadas e manter decisão registrada em arquivo único do time."),
    ("Falha na demonstração", "Vídeo ensaiado, dados estáveis e capturas de tela dos momentos críticos sempre à mão."),
]

CONCLUSAO = [
    (
        "Não existe hackathon que recompense melhor decisão do que escolher um problema que já dói. As "
        "14 ideias deste documento são portas de entrada, não respostas: qualquer uma delas pode morrer na "
        "primeira semana de entrevistas, e isso é um resultado bom, porque o custo de aprender isso em uma "
        "conversa de vinte minutos é incomparavelmente menor do que o custo de descobrir em três meses de "
        "desenvolvimento."
    ),
    (
        "A tecnologia é a parte que o time domina; o problema é a parte que só o cliente pode ensinar. Por "
        "isso a ordem importa: primeiro a dor, depois o público, depois o escopo menor possível e só então a "
        "stack. Uma ferramenta medíocre aplicada a um problema urgente sobrevive e melhora; uma obra-prima "
        "técnica aplicada a um inconveniente pequeno encerra o ciclo com uma demonstração bonita e nenhum "
        "segundo uso."
    ),
    (
        "Feche este documento com três decisões escritas: as ideias finalistas, os nomes das pessoas que "
        "serão entrevistadas e o critério de sucesso do piloto. A partir daí, o trabalho deixa de ser "
        "intelectual e passa a ser conversa — e o produto, quando nascer, já saberá para quem existe."
    ),
]

CHECKLIST_FINAL = [
    "A frase do problema foi escrita com palavras de um cliente, não do time?",
    "Pelo menos cinco pessoas já foram entrevistadas sobre esse problema?",
    "Existe um comprador nomeado, acessível na primeira semana?",
    "O cliente já gasta tempo ou dinheiro hoje com essa dificuldade?",
    "A lista de 'o que não entra' está escrita e conhecida por todos?",
    "O MVP foi cortado até caber no tempo real disponível, com folga?",
    "Há um critério de sucesso de piloto definido com antecedência?",
    "Os riscos de segurança, privacidade e regulamentação foram revisados?",
]
