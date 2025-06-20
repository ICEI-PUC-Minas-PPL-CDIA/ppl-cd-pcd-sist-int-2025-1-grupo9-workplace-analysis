# Brazilian Workplace Analysis


**Lucca Favilla Campos de Paula, lfcpaula@sga.pucminas.br**

**Caio Soares Fernandes, caio.fernandes.925312@sga.pucminas.br**

**Davi Miguel Almeida da Silva, davi.miguel@sga.pucminas.br**

**João Lucas Garcia Oliveira, joao.oliveira.1387367@sga.pucminas.br**

**Gabriel Lucas de Carvalho Santos, gabriel.santos1524775@sga.pucminas.br**

---



Professores:

**Prof. Hugo Bastos de Paula**

**Prof. Hayala Nepomuceno Curto**

---



_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---



##	Resumo

O projeto Brazilian Workplace Analysis tem como foco combater o etarismo no mercado de trabalho, utilizando tecnologias de inteligência artificial para analisar e interpretar dados socioeconômicos e laborais. O sistema busca identificar desafios enfrentados por trabalhadores seniores (acima de 50 anos), como dificuldades de recolocação, disparidades salariais e barreiras à inclusão. O objetivo principal é criar uma plataforma que processe grandes volumes de dados, gerando insights e recomendações para empresas e gestores públicos, com o intuito de fomentar práticas mais justas e inclusivas.

A solução integra informações de fontes como a PNAD Contínua (IBGE), Rais (Ministério do Trabalho) e estudos acadêmicos, aplicando técnicas de machine learning para detectar padrões de desigualdade e propor ações efetivas, como políticas de inclusão e programas de capacitação. O público-alvo inclui organizações privadas, governos, pesquisadores e entidades da sociedade civil.

Em resumo, o Brazilian Workplace Analysis não apenas mapeia as desigualdades relacionadas ao etarismo no ambiente laboral, mas também oferece ferramentas práticas para transformar esses espaços, utilizando análise de dados e inteligência artificial para promover equidade e inclusão de forma eficiente e embasada.

---



## Sumário

- [Introdução](#introdução)
- [Contextualização](#contextualização)
- [Problema](#problema)
- [Objetivo Geral](#objetivo-geral)
  - [Objetivos Específicos](#objetivos-específicos)
- [Justificativas](#justificativas)
- [Público Alvo](#público-alvo)
- [Análise Exploratória dos dados](#análise-exploratória-dos-dados)
  - [Descrição das bases](#descrição-das-bases)
  - [Atributos relevantes da base de dados](#atributos-relevantes-da-base-de-dados)
    - [State of data Brazil](#state-of-data-brazil)
    - [Base do IPEA](#base-do-ipea)
    - [Base do IBGE](#base-do-ibge)
- [Dicionário de dados Estados do Brasil](#dicionário-de-dados-estados-do-brasil)
  - [Bases unificada](#bases-unificada)
  - [Análise Descritiva das Bases de dados](#análise-descritiva-das-bases-de-dados)
  - [1 Base de dados do IPEA](#1-base-de-dados-do-ipea)
    - [1 Estatística Numéricas](#1-estatísticas-numéricas)
    - [1 Estatísticas Categóricas](#1-estatísticas-categóricas)
  - [2 Base de Dados do IBGE](#2-base-de-dados-do-ibge)
    - [2 Estatística Numéricas](#1-estatísticas-numéricas)
    - [2 Estatísticas Categóricas](#1-estatísticas-categóricas)
  - [3 Base State of Data BR 2023](#3-base-state-of-data-br-2023)
    - [3 Estatísticas Numéricas](#3-estatísticas-numéricas)
    - [3 Estatísticas Categóricas](#3-estatísticas-categóricas)
- [Preparação dos dados ](#preparação-dos-dados)
- [Modelo Random Forest](#modelo-random-forest)
  - [Pergunta orientada a dados](#pergunta-orientada-a-dados)
  - [Por que escolhemos o Random Forest e como ele funciona](#por-que-escolhemos-o-random-forest-e-como-ele-funciona)
    - [Por que Random Forest](#por-que-random-forest)
    - [Como o Random Forest funciona](#como-o-random-forest-funciona)
  - [Indução do modelo](#indução-do-modelo)
  - [Objetivo do modelo](#objetivo-do-modelo)
  - [Comparação com o treinamento do modelo](#comparação-com-o-treinamento-do-modelo)
  - [Avaliação do modelo Random Forest](#avaliação-do-modelo-random-forest)
  - [Interpretação dos resultados](#interpretação-dos-resultados)
  - [Resultados obtidos](#resultados-obtidos)
    - [Relatório de classificação](#relatório-de-classificação)
    - [Interpretação da matriz](#interpretação-da-matriz)
  - [Importância das variáveis](#importância-das-variáveis)
  - [Conclusão](#conclusão)
- [Modelo K-Nearest Neighbors](#modelo-k-nearest-neighbors)
  - [Pergunta orientada a dados](#pergunta-orientada-a-dados)
  - [Por que escolhemos o KNN e como ele funciona](#por-que-escolhemos-o-knn-e-como-ele-funciona)
    - [Por que KNNt](#por-que-knn)
    - [Como o KNN funciona](#como-o-knn-funciona)
  - [Indução do modelo](#indução-do-modelo)
  - [Objetivo do modelo](#objetivo-do-modelo)
  - [Comparação com o treinamento do modelo](#comparação-com-o-treinamento-do-modelo)
  - [Avaliação do modelo KNN](#avaliação-do-modelo-knn)
    - [Relatório de classificação](#relatório-de-classificação)
    - [Interpretação da matriz de confusão](#interpretação-da-matriz-de-confusão)
  - [Importância das variáveis](#importância-das-variáveis)
  - [Conclusão](#conclusão)
- [COMPARAÇÃO GERAL](#comparação-geral)
  - [Desempenho Quantitativo](#desempenho-quantitativo)
  - [Intepretação](#interpretação)
  - [Capacidade de Interpretação](#capacidade-de-interpretação)
  - [Erros Cometidos](#erros-cometidos)
  - [Análise](#análise)
  - [Conclusões Comparativas](#conclusões-comparativas)



##	Introdução

O etarismo, ou discriminação etária, se consolida como um desafio persistente no mercado de trabalho, e o setor de dados não se exime desse problema.

Embora a ciência de dados, análise de dados,e a engenharia de dados apresentem um crescimento exponencial, há uma percepção de que o setor é dominado pelos jovens. Muitos profissionais com idade superior a 55 anos enfrentam barreiras, seja na contratação, ou na progressão na carreira, devido ao estigma de que habilidades tecnológicas estão mais associadas às gerações mais novas.

Além disso, a rápida evolução das ferramentas e linguagens de programação pode fortalecer essa discriminação, criando um ambiente onde se espera que apenas os mais jovens consigam acompanhar as mudanças. No entanto, a diversidade geracional pode ser um grande diferencial competitivo para as empresas, combinando a experiência e a visão estratégica dos profissionais mais seniores com a inovação e o dinamismo dos mais jovens.

 Diante desse contexto, o projeto “Brazilian Workplace Analysis” busca investigar o fundo do impacto do etarismo no mercado de dados, analisando fatores como os desafios enfrentados por profissionais seniores, as tendências de contratação no setor e as soluções possíveis para promover um ambiente mais inclusivo e diverso.



##    Contextualização

O "State of Data 2023" representa a maior base de dados dedicada aos especialistas em ciência de dados no Brasil, permitindo a análise da atual situação da área. Nesse sentido, esta é a quarta edição do panorama, na qual mais de 5.200 profissionais foram entrevistados. Portanto, diversos temas podem ser estudados por meio dessa base, incluindo questões raciais, inclusão de pessoas com deficiência, integração da comunidade LGBT e o tema selecionado para este projeto: o etarismo.

O etarismo no mercado de trabalho é um fenômeno global, mas assume contornos particulares no Brasil. Segundo dados do IBGE (2022), houve um aumento de 56,0% na população acima de 55 anos em relação a 2010; entretanto, o mercado de trabalho aparenta não acompanhar esse crescimento.

De acordo com o IBGE (2024), os trabalhadores acima de 55 anos representam mais de 22% da população economicamente ativa, mas enfrentam dificuldades para se recolocar no mercado após demissões ou transições de carreira. Nesse sentido, o número de trabalhadores nessa faixa etária com carteira assinada está em queda desde 2022, mesmo com o aumento na oferta de empregos. Além disso, estudos mostram que trabalhadores seniores frequentemente recebem salários menores e têm menos oportunidades de ascensão profissional em comparação com colegas mais jovens.

A aplicação de tecnologias como a inteligência artificial e a análise de dados pode oferecer insights valiosos para compreender as barreiras enfrentadas por trabalhadores seniores e propor soluções baseadas em evidências. O projeto Brazilian Workplace Analysis utiliza dados de fontes confiáveis, como a PNAD Contínua, Rais, IPEA e IBGE, para mapear padrões de desigualdade e buscar informações que ajudem a solucionar a desvalorização desses profissionais. Dessa forma, é possível implementar ações práticas para promover a inclusão desses trabalhadores no mercado de trabalho no Brasil.



##    Problema

No setor de dados, o etarismo se torna ainda mais evidente devido a uma rápida evolução das tecnologias e à opinião generalizada de que apenas as gerações mais jovens possuem capacidade de adaptação a essas mudanças. No entanto, essa percepção desconsidera o potencial estratégico dos trabalhadores sênior, que pode contribuir significativamente para o desenvolvimento do setor por meio de sua experiência.

Os esteriótipos como baixa produtividade, vulnerabilidade de saúde e dificuldades em acompanhar a evoluçao tenológica no setor são recorrentes quando indivíduos com idade superior a 55 anos tentam se candidatar ou se recolocar no mercado de trabalho. Fato estes que resultam na negação de oportunidade de emprego, baixa remuneração e consequentemente impacto na saúde financeira dos indivíduos em questão.

 Dessa forma, um estudo aprofundado  se torna essencial para formar um debate amplo sobre a implementação de políticas de inclusão que visem promover a diversidade etária no mercado de trabalho juntamente com o impulsionamento de campanhas de consientização sobre o tema na sociedade.



##    Objetivo geral

Desenvolver um sistema inteligente que examine a influência do etarismo no mercado de dados, averiguando a forma de como a discriminação impacta na contratação, permanência e desenvolvimento dos profissionais mais experientes.

Ademais o estudo busca compreender as causas e consequências referentes a este preconceito, a fim de propor estratégias e soluções  que busquem proporcionar um ambiente de trabalho mais inclusivo, equitativo e diversificado.


###    Objetivos específicos

- **Mapear os principais desafios** enfrentados pelos profissionais seniores, incluindo:  
  - Dificuldades na atualização tecnológica.  
  - Limitações de acesso.  
  - Oportunidades de capacitação.  
  - Obstáculos no crescimento profissional.  

- **Identificar padrões de exclusão etária** no mercado de dados, analisando:  
  - Dados de contratação.  
  - Promoção e desligamento de profissionais de diferentes idades.  

- **Compreender a percepção** de recrutadores e trabalhadores sobre profissionais mais velhos no setor, avaliando:  
  - Quais preconceitos influenciam as decisões de contratação.  

- **Fomentar um debate** amplo sobre políticas de inclusão.  

- **Criar programas de incentivo** à adoção de medidas que promovam a igualdade de oportunidades, independentemente da faixa etária.  



##    Justificativas
O projeto de um sistema inteligente para enfrentar o etarismo no mercado de dados é uma iniciativa essencial para promover a inclusão e a equidade no setor. Profissionais mais experientes frequentemente enfrentam barreiras na busca por oportunidades, e essa solução tecnológica busca reduzir esse preconceito.

O sistema será capaz de identificar padrões de discriminação etária em processos seletivos, utilizando inteligência artificial para analisar dados e sugerir melhorias nos critérios de recrutamento. Também poderá auxiliar empresas na formulação de políticas mais inclusivas, ajudando a valorizar profissionais experientes e sua contribuição ao mercado.

Além disso, a ferramenta poderá oferecer um módulo educacional para conscientizar gestores e recrutadores sobre a importância da diversidade etária, demonstrando seus impactos positivos na inovação e produtividade das equipes.

Esse projeto não apenas combate o etarismo, mas também fortalece um ambiente de trabalho mais justo e diversificado, promovendo a valorização do talento e da experiência independentemente da idade.


##    Público alvo

O projeto Brazilian Workplace Analysis tem como público-alvo empresas, gestores públicos, pesquisadores e organizações da sociedade civil que buscam promover a equidade etária no mercado de trabalho. Esses usuários estão distribuídos em diferentes setores e possuem perfis variados, mas compartilham o interesse em utilizar tecnologia e dados para concretizar a inclusão e acabar com as desigualdades presentes atualmente em diversos setores trabalhistas.


## Análise Exploratória dos Dados
Dicionário de Dados
Aqui está a descrição das bases de dados que serão utilizadas no projeto Brazilian Workplace Analysis, com foco no etarismo no mercado de trabalho. O projeto utilizará duas fontes principais: a State_of_Data_BR_2023 (fonte principal), PNAD Contínua (IBGE) (fonte de enriquecimento) e a Base do IPEA.



### Descrição das Bases

1. State_of_Data_BR_2023
A State_of_Data_BR_2023 é uma pesquisa anual que mapeia o perfil dos profissionais de dados no Brasil. Ela contém informações sobre salários, ferramentas utilizadas, nível de experiência, formação acadêmica, entre outros aspectos.

2. Base do IPEA
O IPEA disponibiliza diversas bases de dados e indicadores socioeconômicos, como o Atlas do Desenvolvimento Humano no Brasil e o Sistema de Indicadores de Percepção Social (SIPS). Essas bases contêm informações sobre emprego, renda, educação e desigualdades regionais.
 
 ### Atributos Relevantes da Base de Dados
 
####**State of Data Brazil**
| Atributo | Tipo | Subtipo | Descrição |
|----------|------|---------|-----------|
| Idade | Numérico | - | Idade exata do respondente |
| Faixa etária | Categórico | Ordinal | Agrupamento por intervalos de idade (ex: 30-34, 35-39, 55+) |
| Gênero | Categórico | Nominal | Identidade de gênero do respondente (Masculino, Feminino, Não-binário, Outro) |
| Cor/Raça/Etnia | Categórico | Nominal | Autodeclaração de raça (Branca, Preta, Amarela, Indígena, Parda) |
| PCD | Categórico | Nominal | Se a pessoa possui deficiência (Sim, Não) |
| Experiência prejudicada | Categórico | Nominal | Se o respondente acredita que sua experiência profissional foi afetada pelo etarismo |
| Motivo da experiência prejudicada | Categórico | Nominal | Razões da discriminação (Idade, Gênero, Raça, Outro) |
| Anos de experiência | Numérico | - | Tempo total de experiência profissional do respondente |
| Área de atuação | Categórico | Nominal | Campo de trabalho (ex: Ciência de Dados, Engenharia de Software, Análise de Dados) |
| Nível de escolaridade | Categórico | Ordinal | Grau acadêmico mais alto concluído (Graduação, Pós-graduação, Mestrado, Doutorado) |
| Salário | Numérico | - | Faixa salarial do respondente |
| Tipo de empresa | Categórico | Nominal | Setor da empresa onde trabalha (Pública, Privada, Startup, Autônomo) |
| Tamanho da empresa | Categórico | Ordinal | Número de funcionários na empresa (Pequena, Média, Grande) |
| Modelo de trabalho | Categórico | Nominal | Modalidade de trabalho (Presencial, Híbrido, Remoto) |
| Satisfação profissional | Categórico | Ordinal | Nível de satisfação do respondente com sua carreira (Baixo, Médio, Alto) |
| Oportunidades de promoção | Categórico | Ordinal | Se o respondente percebe oportunidades de crescimento na empresa (Sim, Não, Raramente) |
| Já sofreu discriminação por idade? | Categórico | Nominal | Se o profissional acima de 55 anos já enfrentou discriminação direta (Sim, Não) |
| Tipo de discriminação por idade | Categórico | Nominal | Formas de discriminação (Dificuldade de contratação, Exclusão em promoções, Comentários depreciativos) |
| Adequação às novas tecnologias | Categórico | Ordinal | Se o profissional sente dificuldades em se adaptar a novas ferramentas e tendências (Nenhuma, Pouca, Média, Alta) |
| Incentivo à diversidade etária na empresa | Categórico | Nominal | Se a empresa promove ações para incluir trabalhadores mais velhos (Sim, Não, Não sei) |
| Planos de aposentadoria e transição de carreira | Categórico | Nominal | Se a empresa oferece suporte para planejamento da aposentadoria e requalificação (Sim, Não) |
| Flexibilidade de trabalho para profissionais 55+ | Categórico | Nominal | Se há opções de trabalho mais flexíveis para trabalhadores mais velhos (Sim, Não) |
| Acesso a treinamentos e capacitações | Categórico | Ordinal | Se a empresa oferece cursos e treinamentos para profissionais mais velhos (Sim, Não, Ocasionalmente) |
| Frequência de atualização profissional | Categórico | Ordinal | Com que frequência o profissional acima de 55 anos realiza cursos ou capacitações (Nunca, Raramente, Algumas vezes, Frequentemente) |
| Barreiras para recolocação profissional | Categórico | Nominal | Principais dificuldades para conseguir um novo emprego (Falta de oportunidades, Exigência de tecnologia, Salário abaixo do esperado) |
| Sentimento de valorização na empresa | Categórico | Ordinal | Se o trabalhador 55+ se sente valorizado no ambiente de trabalho (Muito baixo, Baixo, Médio, Alto, Muito alto) |
| Acesso a mentorias e suporte na empresa | Categórico | Nominal | Se há programas de mentoria ou suporte para trabalhadores mais velhos (Sim, Não) |

#### **Base do IPEA**
| Nome do Atributo | Descrição | Tipo do Atributo | 
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------------| 
| Rendimento médio real.todos trabalhos.efetivo - mais de 60 anos | Média de rendimento financeiro de pessoas com mais de 60 anos em trabalhos efetivos | Numérico | 
| Média de horas trabalhadas.trabalho principal.efetivo - mais de 60 anos | Média de horas trabalhadas por pessoas com mais de 60 anos em seus trabalhos principais | Numérico | | Média de horas trabalhadas.trabalho principal.habitual - mais de 60 anos | Média de horas trabalhadas por pessoas com mais de 60 anos em seus trabalhos habituais | Numérico | 
| Informalidade - mais de 60 anos | Percentual de trabalhadores com mais de 60 anos em empregos informais | Numérico | 
| Taxa de participação - mais de 60 anos | Percentual de pessoas com mais de 60 anos que estão ativamente participando do mercado de trabalho | Numérico |
| Taxa de desemprego - mais de 60 anos | Percentual de pessoas com mais de 60 anos que estão desempregadas | Numérico |
| Taxa de subutilização da força de trabalho - mais de 60 anos | Percentual de pessoas com mais de 60 anos que estão subutilizadas no mercado de trabalho | Numérico |
| Ocupados - mais de 60 anos | Número total de pessoas com mais de 60 anos que estão ocupadas em trabalhos | Numérico |
| Desocupados - mais de 60 anos | Número total de pessoas com mais de 60 anos que estão desempregadas | Numérico | | Fora da força de trabalho - mais de 60 anos | Número total de pessoas com mais de 60 anos que não estão ativamente procurando trabalho | Numérico |

#### Base do IBGE
| Atributo               | Descrição                                      | Tipo de Dado   |
|------------------------|-----------------------------------------------|----------------|
| Empregado - Com carteira de trabalho assinada (2) | Especifica quantos trabalhadores não têm carteira assinada | Numérico     |
| Empregado - Sem carteira de trabalho assinada (3) | Especifica quantos trabalhador não têm carteira assinada   | Numérico     |
| Militar ou funcionário público estatutário        | Indica a o número de trabalhadores em funções públicas     | Numérico     |
| Conta própria                                     | Indica o número de trabalhadores autônomo                  | Numérico     |
| Empregador                                        | Indica o número de trabalhadores em posição de empregador  | Numérico     |



## Dicionário de Dados Estados do Brasil 

### Bases Unificada
| Atributo | Tipo de Dado | Descrição |
|----------|---------------|-----------|
| Idade | Numérico | Idade exata do entrevistado |
| Faixa etária | Categórico (Ordinal) | Faixa de idade (ex: 30-34, 35-39, 55+) |
| Gênero | Categórico (Nominal) | Identidade de gênero do entrevistado |
| Raça/Cor/Etnia | Categórico (Nominal) | Autodeclaração racial ou étnica |
| Pessoa com deficiência (PCD) | Categórico (Nominal) | Indica se a pessoa possui deficiência |
| Experiência profissional (anos) | Numérico | Total de anos de experiência profissional |
| Área de atuação profissional | Categórico (Nominal) | Campo de trabalho (ex: Engenharia, Dados) |
| Escolaridade | Categórico (Ordinal) | Nível educacional mais alto alcançado |
| Salário (faixa ou média) | Numérico | Faixa salarial mensal ou média (individual) |
| Modelo de trabalho | Categórico (Nominal) | Presencial, remoto ou híbrido |
| Tipo de empresa | Categórico (Nominal) | Pública, privada, startup, autônomo |
| Tamanho da empresa | Categórico (Ordinal) | Pequena, média ou grande empresa |
| Vínculo empregatício (classificação IBGE) | Categórico (Nominal) | Ex: com carteira, sem carteira, público, conta própria, empregador |
| Formalidade do emprego | Categórico (Nominal) | Se o trabalho é formal ou informal |
| Satisfação profissional | Categórico (Ordinal) | Nível de satisfação com a carreira |
| Oportunidades de promoção | Categórico (Ordinal) | Percepção sobre chances de crescimento |
| Já sofreu discriminação por idade? | Categórico (Nominal) | Se a pessoa sofreu discriminação direta |
| Tipo de discriminação por idade | Categórico (Nominal) | Forma que a discriminação ocorreu |
| Experiência profissional prejudicada (por etarismo) | Categórico (Nominal) | Se a idade já impactou a carreira |
| Motivo da experiência prejudicada | Categórico (Nominal) | Causa atribuída da discriminação |
| Adequação às novas tecnologias | Categórico (Ordinal) | Dificuldade percebida com tecnologias novas |
| Acesso a treinamentos | Categórico (Ordinal) | Frequência de cursos oferecidos pela empresa |
| Frequência de atualização profissional | Categórico (Ordinal) | Frequência com que o profissional busca capacitação |
| Sentimento de valorização na empresa (55+) | Categórico (Ordinal) | Nível de valorização percebido no trabalho |
| Acesso a mentorias e suporte | Categórico (Nominal) | Se há programas de apoio à carreira |
| Flexibilidade no trabalho (55+) | Categórico (Nominal) | Se há opções de flexibilidade para mais velhos |
| Incentivo à diversidade etária na empresa | Categórico (Nominal) | Se a empresa promove inclusão etária |
| Planos de aposentadoria e transição de carreira | Categórico (Nominal) | Se a empresa oferece suporte para transição ou aposentadoria |
| Barreiras para recolocação profissional | Categórico (Nominal) | Dificuldades enfrentadas para conseguir emprego |
| Rendimento médio (60+) | Numérico | Rendimento médio de pessoas com mais de 60 anos |
| Horas trabalhadas (60+) | Numérico | Média de horas semanais no trabalho principal |
| Informalidade (60+) | Numérico | Percentual de trabalhadores 60+ em empregos informais |
| Participação no mercado (60+) | Numérico | Taxa de participação no mercado de trabalho |
| Taxa de desemprego (60+) | Numérico | Percentual de desempregados com 60+ |
| Subutilização da força de trabalho (60+) | Numérico | Percentual de subutilização entre idosos |
| Ocupados (60+) | Numérico | Número total de trabalhadores 60+ ocupados |
| Desocupados (60+) | Numérico | Número total de trabalhadores 60+ desocupados | 

### Análise Descritiva das Bases de Dados

Este relatório apresenta uma análise descritiva de primeira ordem sobre três bases de dados utilizadas no projeto de ciência de dados **Brazilian Workplace Analysis**, com foco na inclusão e diversidade etária no mercado de trabalho brasileiro.

---

###  1 Base de Dados do IPEA

####  1 Estatísticas Numéricas 

- **Ano**:
  - Média: 2020.50
  - Desvio Padrão: 1.74
  - Mínimo: 2018.0
  - 1º Quartil (25%): 2019.0
  - Mediana (50%): 2020.5
  - 3º Quartil (75%): 2022.0
  - Máximo: 2023.0

- **Informalidade - mais de 60 anos**:
  - Média: 55.08
  - Desvio Padrão: 2.20
  - Mínimo: 50.4
  - 1º Quartil (25%): 54.77
  - Mediana (50%): 55.25
  - 3º Quartil (75%): 56.80
  - Máximo: 57.8

- **Taxa de participação - mais de 60 anos**:
  - Média: 22.68
  - Desvio Padrão: 1.49
  - Mínimo: 19.5
  - 1º Quartil (25%): 21.85
  - Mediana (50%): 23.35
  - 3º Quartil (75%): 23.73
  - Máximo: 24.4

####  1 Estatísticas Categóricas

- **Sigla**:
  - Moda: BR
  - Nº de Categorias Distintas: 1
  - Categoria mais frequente: BR (24)

- **Brasil**:
  - Moda: Brasil
  - Nº de Categorias Distintas: 1
  - Categoria mais frequente: Brasil (24)

---

###  2 Base de Dados do IBGE 

####  2 Estatísticas Numéricas

**Nenhuma variável numérica identificada nesta base.**

####  2 Estatísticas Categóricas

- **Ano**:
  - Moda: 2022
  - Nº de Categorias Distintas: 6
  - Categoria mais frequente: 2022 (6)

- **Unidade da Federação**:
  - Moda: Brasil
  - Nº de Categorias Distintas: 1
  - Categoria mais frequente: Brasil (24)

---

###  3 Base State of Data BR 2023

####  3 Estatísticas Numéricas

- **Senioridade das vagas x Experiência**:
  - Média: 0.18
  - Desvio Padrão: 0.39
  - Mínimo: 0.0
  - 1º Quartil (25%): 0.0
  - Mediana (50%): 0.0
  - 3º Quartil (75%): 0.0
  - Máximo: 1.0

- **Satisfação na empresa atual**:
  - Média: 0.61
  - Desvio Padrão: 0.49
  - Mínimo: 0.0
  - 1º Quartil (25%): 0.0
  - Mediana (50%): 1.0
  - 3º Quartil (75%): 1.0
  - Máximo: 1.0

####  3 Estatísticas Categóricas

- **Faixa idade**:
  - Moda: 25-29
  - Nº de Categorias Distintas: 9
  - Categoria mais frequente: 25-29 (1654)

- **Gênero**:
  - Moda: Masculino
  - Nº de Categorias Distintas: 4
  - Categoria mais frequente: Masculino (3975)

- **Raça/Cor/Etnia**:
  - Moda: Branca
  - Nº de Categorias Distintas: 7
  - Categoria mais frequente: Branca (3414)

---



## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

> - Seleção dos atributos
> - Tratamentos dos valores faltantes ou omissos: remoção, substituição, indução, etc.
> - Tratamento dos valores inconsistentes: conversão, remoção de dados duplicados, remoção ou tratamento de ouliers.
> - Conversão de dados: p. ex. numérico para categórico, categórico para binário, etc.

---



## Modelo Random Forest

### Pergunta orientada a dados

**A idade é um fator que prejudica a experiência profissional dos trabalhadores?**

Este projeto tem como objetivo prever se um profissional sofreu etarismo (discriminação por idade) com base em dados sobre sua situação profissional, nível de escolaridade, políticas de diversidade da empresa, entre outros fatores.

---

### Por que escolhemos o Random Forest e como ele funciona

#### Por que Random Forest

· É um modelo de classificação robusto e de alto desempenho.  
· Trabalha bem com dados tabulares com variáveis numéricas e categóricas.  
· Reduz o risco de overfitting ao combinar várias árvores de decisão (ensemble).  
· Permite interpretar a importância das variáveis.  

#### Como o Random Forest funciona

· Constrói múltiplas árvores de decisão a partir de subconjuntos aleatórios dos dados e das variáveis.  
· Cada árvore faz uma previsão individual, e a classe final é decidida por votação da maioria.  
· Isso aumenta a precisão e a estabilidade das previsões.  

---

### Indução do Modelo

1. A indução teve início com a leitura da base de dados, composta por informações de profissionais relacionadas a características pessoais, trajetória profissional e percepções sobre o ambiente de trabalho.  
2. Em seguida, foram criadas variáveis essenciais para a análise, incluindo a variável “grupo_etário”, classificando profissionais com 50 anos ou mais, e a variável “alvo” que representa o etarismo, construída a partir dos relatos de experiências negativas atribuídas à idade.  
3. Após isso, houve a seleção dos atributos mais relevantes para a modelagem, priorizando variáveis ligadas a políticas de diversidade, programas de valorização profissional, acesso a promoções, adequação tecnológica e outras dimensões organizacionais.  
4. Com os atributos definidos, foi necessário transformar as variáveis categóricas em formato numérico, utilizando técnicas de codificação para que os algoritmos pudessem interpretá-las corretamente.  
5. Devido ao desequilíbrio entre os casos de profissionais que relataram etarismo e os que não relataram, aplicou-se o método SMOTE, que gera amostras sintéticas para equilibrar as classes e evitar o viés do modelo.  
6. A base balanceada foi então dividida em dois subconjuntos: 70% dos dados foram destinados ao treinamento do modelo, e os 30% restantes, ao final, garantindo uma avaliação justa do desempenho.  
7. O modelo escolhido para a etapa de treinamento foi o RandomForestClassifier, que combina várias árvores de decisão para obter melhores resultados em problemas com múltiplas variáveis.  
8. A etapa de otimização dos hiperparâmetros foi realizada utilizando o GridSearchCV, que testou combinações de parâmetros para encontrar a configuração que oferecesse o melhor desempenho do modelo.  
9. O desempenho do modelo foi avaliado com métricas como acurácia, precisão, recall, F1-score e matriz de confusão, possibilitando uma análise quantitativa da sua eficácia em classificar corretamente os casos de etarismo.  
10. Por fim, foram analisadas as árvores que compõem o modelo e a importância atribuída a cada variável, permitindo interpretar quais fatores mais influenciaram nas decisões do algoritmo e fornecendo insights sobre os elementos mais associados à discriminação etária no ambiente de trabalho.  

---

### Objetivo do Modelo

O objetivo do modelo é prever se um profissional sofreu etarismo, com base em variáveis relacionadas à sua experiência de trabalho, cultura organizacional e suporte ao desenvolvimento contínuo.

---

### Comparação com o treinamento do modelo

Para avaliar a capacidade de generalização do modelo, comparamos a acurácia nos dados de treinamento com os dados finais. Essa análise permite verificar possíveis problemas de overfitting ou underfitting.

A acurácia do modelo Random Forest nos conjuntos de treinamento foi: 0,80 e no modelo final: 0,77. Isso indica que o modelo teve bom desempenho nos dados em que foi treinado, com diferença controlada entre treino e teste. O modelo demonstrou capacidade de generalizar sem se ajustar excessivamente aos dados de treinamento.

![image](https://github.com/user-attachments/assets/f8f464e1-077d-4018-a916-26104a39d3b3)


[Código do Modelo 1](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/src/Modelo%201/First%20Model%20(Code).py)

[Código da comparação Modelo 1](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/src/Modelo%201/First%20Model%20Training%20x%20Final%20(Code).py)

---

### Avaliação do Modelo Random Forest

**Acurácia no treinamento:** 0.80  
**Acurácia final:** 0.77  

Essa diferença indica uma generalização saudável, sem indícios fortes de overfitting.

---

### Interpretação dos resultados

A análise dos valores de acurácia obtidos permite as seguintes conclusões:

· Acurácia no treinamento: 0.80  
· Acurácia final: 0.77  
· A diferença entre treino e o modelo final está dentro do esperado, indicando boa generalização.  
· O modelo tem desempenho equilibrado na identificação tanto de casos de etarismo quanto de não etarismo, com F1-score médio de 0.77.

---

### Resultados obtidos

**Acurácia final:** 0.77  

#### Relatório de classificação

| Classe             | Precisão | Recall | F1-score | Suporte |
|--------------------|----------|--------|----------|---------|
| Sem Etarismo (0)   | 0.77     | 0.75   | 0.76     | 945     |
| Com Etarismo (1)   | 0.76     | 0.79   | 0.77     | 966     |
| Média Macro        | 0.77     | 0.77   | 0.77     | 1911    |
| Média Ponderada    | 0.77     | 0.77   | 0.77     | 1911    |

#### Interpretação da matriz:

· 708 acertos em identificar corretamente casos sem etarismo.  
· 759 acertos na identificação de casos com etarismo.  
· 237 falsos positivos: pessoas sem etarismo classificadas incorretamente como vítimas.  
· 207 falsos negativos: pessoas com etarismo não reconhecidas pelo modelo.  

---

### Importância das variáveis

As variáveis mais relevantes para o modelo foram:

1. sentimento_de_valorização_na_empresa  
2. incentivo_à_diversidade_etária_na_empresa  
3. barreiras_para_recolocação_profissional  
4. adequação_às_novas_tecnologias  
5. satisfação_profissional  

Essas variáveis demonstram o papel da cultura organizacional, valorização interna e suporte à atualização contínua na percepção de etarismo no ambiente de trabalho.

---

### Conclusão

  O modelo Random Forest demonstrou desempenho satisfatório na tarefa de identificar percepções de etarismo entre profissionais com 50 anos ou mais. Com uma acurácia de 80% no conjunto de treinamento e 77% no modelo final, observou-se um leve overfitting, mas ainda dentro de um nível aceitável, indicando que o modelo consegue se adaptar bem aos novos dados e corrigir valores falsos.  
  A escolha do Random Forest foi um acerto, pois trata-se de um algoritmo robusto, capaz de lidar com variáveis categóricas e numéricas, além  de identificar padrões complexos sem exigir ajustes extensivos. Sua estrutura baseada em múltiplas árvores permite avaliar a importância de cada variável na tomada de decisão, o que contribuiu diretamente para a interpretação dos resultados. A análise da importância das variáveis revelou que fatores organizacionais, como políticas de diversidade etária, planos de carreira e satisfação profissional, tiveram peso significativo na predição da percepção de etarismo, o que reforça a relevância dessas dimensões na sociedade.  
  Dessa forma, o modelo respondeu positivamente à pergunta central do estudo, ao conseguir mapear, com base em dados objetivos, os principais fatores associados à percepção de discriminação por idade e confirmar as desigualdades enfrentadas por esse grupo. O modelo se mostra útil como uma ferramenta complementar para apoiar diagnósticos organizacionais, orientar políticas de diversidade e fomentar ambientes corporativos mais inclusivos para profissionais com idade avançada.

---



## Modelo K-Nearest Neighbors

### Pergunta orientada a dados

**É possível concluir que fatores como carreira profissional, oportunidades de emprego e inclusão são afetadas pelo etarismo**

Este projeto tem como objetivo prever se um profissional sofreu etarismo (discriminação por idade) com base em variáveis sobre sua experiência de trabalho, características pessoais e políticas organizacionais, como satisfação profissional, incentivo à diversidade e acesso a tecnologias. Além disso, busca analisar como a idade impactou em múltiplos fatores de histórico profissional desse grupo.

---

### Por que escolhemos o KNN e como ele funciona

#### Por que KNN

- É um modelo simples e eficaz para tarefas de classificação.
- Não assume distribuições estatísticas específicas.
- Ideal para casos com estruturas de decisão baseadas em similaridade.
- Fácil de interpretar e ajustar, com apenas um parâmetro principal (número de vizinhos, K).

#### Como o KNN funciona

- O modelo armazena todos os dados de treinamento.
- Para prever a classe de uma nova amostra, calcula a distância entre ela e todas as instâncias conhecidas (normalmente distância euclidiana).
- A classe é atribuída com base na maioria entre os **K vizinhos mais próximos**.
- Um valor de K mais baixo tende a overfitting; valores altos favorecem a generalização.

---

### Indução do Modelo

1. O primeiro passo consistiu na seleção dos dados relevantes. A base original foi filtrada para incluir apenas profissionais com 50 anos ou mais, por ser o grupo-alvo da investigação sobre etarismo. A análise foca especificamente nas experiências dessa faixa etária no mercado de trabalho. Após o filtro, foram eliminadas linhas com valores ausentes nas colunas selecionadas, garantindo consistência e completude para a modelagem.
2. A variável preditiva central foi definida como já_sofreu_discriminação_por_idade?, uma coluna binária baseada nas respostas auto referidas dos participantes sobre se já tiveram sua experiência profissional negativamente afetada por conta da idade. Essa variável passou a representar a classe a ser prevista pelo modelo — 1 para “sim” (sofreu etarismo) e 0 para “não”.
3. Foram escolhidas 16 variáveis consideradas potencialmente associadas à experiência de etarismo, abrangendo aspectos pessoais (idade, gênero, cor/raça), profissionais (área de atuação, anos de experiência, salário), organizacionais (tipo e tamanho da empresa) e culturais (incentivo à diversidade, planos de transição de carreira, adequação tecnológica, satisfação e promoções). A curadoria visou garantir amplitude e relevância para o fenômeno investigado.
4. Para tornar os dados compatíveis com algoritmos de aprendizado de máquina, todas as variáveis categóricas foram convertidas para o formato numérico utilizando codificação one-hot. Isso permitiu representar categorias como "gênero" ou "tipo de empresa" por meio de variáveis binárias, possibilitando o cálculo de distâncias entre amostras — essencial no modelo KNN.
5. O número de casos de profissionais que sofreram etarismo era diferente do número de casos que não sofreram, o que poderia enviesar o modelo. Para corrigir isso, foi utilizado o método SMOTE (Synthetic Minority Oversampling Technique), que gera exemplos sintéticos da classe minoritária com base na distribuição dos dados, resultando em um conjunto de dados balanceados.
6. Após o balanceamento, a base foi dividida em dois subconjuntos: 70% dos dados foram usados para treinar o modelo e 30% foram reservados para avaliação final. Essa separação permitiu validar o desempenho do modelo em dados nunca vistos durante o treinamento, garantindo uma avaliação mais justa da sua capacidade preditiva..
7. Como o modelo KNN baseia suas decisões em cálculos de distância, foi necessário padronizar as variáveis numéricas para que todas tivessem média zero e desvio padrão igual a um. Sem essa etapa, variáveis com valores mais altos teriam influência desproporcional na decisão do algoritmo.
8. Foram testados diferentes valores para o parâmetro K, que define o número de vizinhos mais próximos a serem considerados na classificação. Os valores de K de 1 a 5 foram avaliados, comparando os resultados de acurácia tanto no conjunto de treinamento quanto no conjunto final. O melhor desempenho geral foi obtido com K=3, que apresentou equilíbrio entre precisão e generalização.
9. Com o modelo treinado, ele foi aplicado ao conjunto final para avaliar sua capacidade de prever corretamente os casos de etarismo. As métricas utilizadas incluíram acurácia, precisão, recall, F1-score e matriz de confusão. Essa análise permitiu compreender tanto a qualidade geral do modelo quanto os tipos de erros cometidos (falsos positivos e falsos negativos), fornecendo subsídios para interpretações mais aprofundadas sobre os fatores associados à discriminação por idade.

---

### Objetivo do Modelo

Prever se um profissional com 50 anos ou mais sofreu etarismo com base em variáveis relacionadas à sua vivência profissional, políticas organizacionais e satisfação com o ambiente de trabalho.

---

### Comparação com o treinamento do modelo

| K | Acurácia (Treinamento) | Acurácia (Final) |
|---|-------------------------|------------------|
| 1 | 0.92                    | 0.87             |
| 2 | 0.88                    | 0.88             |
| 3 | 0.91                    | 0.89             |
| 4 | 0.89                    | 0.88             |
| 5 | 0.88                    | 0.87             |

**Melhor valor de K: 3**

- Acurácia no treinamento: **91%**  
- Acurácia no modelo final: **89%**

Essa diferença mínima indica que o modelo generalizou bem, sem sinais relevantes de overfitting.

![image](https://github.com/user-attachments/assets/13230f6a-69ef-4553-ae46-603d8634c93f)


[Código do Modelo 2](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/src/Modelo%202/Second%20Model%20(Code).py)

[Código da comparação Modelo 2](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/src/Modelo%202/Second%20Model%20Training%20x%20Final%20(Code).py)

---

### Avaliação do Modelo KNN 
(K=3)

- **Acurácia no conjunto final**: **0.89**

#### Relatório de Classificação

| Classe             | Precisão | Recall | F1-score |
|--------------------|----------|--------|----------|
| Sem Etarismo (0)   | 0.83     | 1.00   | 0.91     |
| Com Etarismo (1)   | 1.00     | 0.74   | 0.85     |

- **Precisão média**: 0.91  
- **Recall médio**: 0.87  
- **F1-score médio**: 0.88

---

### Interpretação da Matriz de Confusão

![image](https://github.com/user-attachments/assets/827f1562-bcb8-4fef-b417-3c4f89881d02)


| Classe Real \ Prevista | Previsto Não | Previsto Sim |
|------------------------|--------------|---------------|
| **Sem Etarismo (0)**   | 35           | 0             |
| **Com Etarismo (1)**   | 7            | 20            |

- **35 acertos** na identificação correta de profissionais que **não sofreram etarismo**.
- **20 acertos** ao identificar corretamente quem **sofreu etarismo**.
- **7 falsos negativos**: casos reais de etarismo que o modelo não identificou.
- **0 falsos positivos**: nenhum erro ao prever indevidamente etarismo onde não houve.

---

### Importância das variáveis

Embora o KNN não forneça uma medida direta de importância de variáveis, a seleção criteriosa foi essencial. As variáveis que mais contribuíram para o desempenho do modelo incluem:

1. `satisfação_profissional`  
2. `incentivo_à_diversidade_etária_na_empresa`  
3. `adequação_às_novas_tecnologias`  
4. `planos_de_aposentadoria_e_transição_de_carreira`  
5. `nível_de_escolaridade`

Esses fatores reforçam a influência do ambiente organizacional e das políticas inclusivas na percepção de etarismo.

---

### Conclusão

  O modelo KNN com K=3 apresentou desempenho preciso em sua tarefa: “É possível concluir que fatores como carreira profissional, oportunidades de emprego e inclusão são afetados pelo etarismo”, abrangendo todos os trabalhadores da amostra com mais de 50 anos. Com uma acurácia de 91% no treinamento e 89% no modelo final, os resultados indicam que o modelo conseguiu um valor de apenas 2% de overfitting. Além disso, o modelo se mostrou especialmente eficiente na identificação de profissionais que não sofreram etarismo, apresentando apenas 7 casos de falsos negativos e nenhum caso de falso positivo, além de um recall equilibrado. 
	Com base nos dados obtidos pelo modelo, é possível inferir que quase 43,5% dos trabalhadores com idade avançada na base do state of data, considerando os falsos negativos, tiveram sua experiência prejudicada. Caso aplicado em uma escala nacional, dos 13.454.522 trabalhadores com mais de 50 anos de acordo com o RAIS, aproximadamente 5.852.717 sofreram algum tipo de desvantagem relacionada ao etarismo. Esses dados revelam regresso no cenário profissional Brasileiro, na qual uma parcela significativa da população sofre desvantagens no mercado de trabalho, prejudicando a vida de milhões de pessoas e indiretamente a economia do país, uma vez que fatores como esse desmotivam os trabalhadores e diminuem sua produtividade. Além disso essa porcentagem representa apenas profissionais da área de tecnologia, um dos setores mais igualitárias, portanto áreas que são historicamente mais desiguais podem apresentar porcentagens maiores que 50% para os profissionais anciões, que acabam sendo marginalizados em muitos ambientes de trbaalho.
	Em síntese, a escolha do KNN foi a melhor para o tamanho da amostra e o objetivo exploratório do estudo. Apesar de sua simplicidade estrutural, o modelo não necessita de ajustes complexos ou mecanismos internos de regularização além do SMOTE. o modelo KNN respondeu de forma favorável acerca da pergunta central orientada a dados do nosso estudo, identificando com eficácia os elementos mais associados à percepção de discriminação por idade, além de concluir que a idade elevada impacta significativamente a experiência profissionais dos trabalhadores mais velhos. Com isso,os dados obtidos nesse modelo auxiliam no reconhecimento de desigualdades vivenciadas por trabalhadores mais velhos e podendo ser utilizado como uma ferramenta de apoio para empresas que buscam diagnosticar práticas excludentes, promover ambientes mais inclusivos e orientar políticas de diversidade etária de forma fundamentada em dados.

---



## COMPARAÇÃO GERAL

| Aspecto | Random Forest | KNN (K=3) |
|-----------------------------|-----------------------------------------------|--------------------------------------------------|
| Tipo de Modelo | Ensemble (árvores de decisão) | Baseado em instâncias (distância) |
| Justificativa da escolha | Robusto, interpreta variáveis, evita overfitting | Simples, eficaz com dados padronizados |
| Pré-processamento | Codificação + SMOTE | Codificação + padronização + SMOTE |
| Capacidade de Generalização | Moderada (diferença de 4 p.p. entre treino e teste) | Alta (diferença de 2 p.p.) |
| Overfitting | Leve, detectado e corrigido | Praticamente inexistente |
| Importância das Variáveis | Fornecida diretamente | Não fornecida diretamente (implícita na escolha) |
| Complexidade Computacional | Alta (várias árvores) | Baixa a média (simples, mas exige muitos cálculos de distância) |
| Interpretação de Resultados | Boa (importância de variáveis, árvores acessíveis) | Limitada (sem explicabilidade interna) |

---

### Desempenho Quantitativo

| Métrica | Random Forest | KNN (K=3) |
|----------------|----------------|-----------|
| Acurácia Treino| 0.81 | 0.91 |
| Acurácia Final | 0.77 | 0.89 |
| Precisão (0) | 0.77 | 0.83 |
| Precisão (1) | 0.76 | 1.00 |
| Recall (0) | 0.75 | 1.00 |
| Recall (1) | 0.79 | 0.74 |
| F1-score (0) | 0.76 | 0.91 |
| F1-score (1) | 0.77 | 0.85 |

### Interpretação

- O KNN superou o Random Forest em acurácia geral (0.89 vs 0.77).
- O Random Forest foi melhor em recall da classe minoritária (etarismo) (0.79 vs 0.74), mostrando mais sensibilidade aos casos de discriminação.
- O KNN teve F1-scores mais equilibrados e precisos, especialmente pela ausência de falsos positivos.

---

### Capacidade de Interpretação

| Elemento | Random Forest | KNN |
|--------------------------|-----------------------------------------|-------------------------------------------|
| Importância das variáveis| Clara, extraída diretamente | Indireta, inferida via seleção inicial |
| Variáveis mais influentes| Sentimento de valorização, diversidade, recolocação | Satisfação, diversidade, tecnologia |
| Explicabilidade do modelo| Alta (árvores e scores) | Baixa (modelo de caixa preta de instâncias) |

---

### Erros Cometidos

| Tipo de erro | Random Forest | KNN (K=3) |
|------------------|----------------|-----------|
| Falsos positivos | 237 | 0 |
| Falsos negativos | 207 | 7 |

### Análise

- Random Forest cometeu mais falsos positivos, o que pode indicar um viés mais "cauteloso" em detectar etarismo, mesmo quando não há.
- KNN teve mais falsos negativos, ou seja, deixou de identificar alguns casos reais de etarismo — o que é crítico do ponto de vista social e de inclusão.

---

### Conclusões Comparativas

| Critério | Vencedor / Destaque |
|-------------------------------------------|------------------------------------------------------|
| Acurácia Geral | KNN (0.89) |
| Sensibilidade a Etarismo (Recall 1) | Random Forest (0.79) |
| Balanceamento entre Precisão e Recall | KNN (F1 médio mais alto) |
| Explicabilidade e Insight | Random Forest (importância de variáveis interpretável) |
| Simplicidade de Implementação | KNN |
| Robustez contra ruído/dados sintéticos | KNN (menos afetado por overfitting) |

---



## Conclusão

A pesquisa realizada pelo projeto Brazilian Workplace Analysis evidencia, de forma quantitativa e qualitativa, a existência e os impactos do etarismo no mercado de dados brasileiro. Utilizando duas abordagens de aprendizado de máquina — Random Forest e K-Nearest Neighbors (KNN) — foi possível diagnosticar padrões discriminatórios relacionados à idade, especialmente entre profissionais com 50 anos ou mais.

O modelo Random Forest mostrou-se eficaz na identificação de casos de etarismo, com uma acurácia final de 77% e destaque para sua capacidade de sensibilidade à classe minoritária, ou seja, à detecção de trabalhadores que relataram discriminação por idade. Por outro lado, o modelo KNN (K=3) obteve uma acurácia superior, de 89%, e demonstrou grande equilíbrio entre precisão e recall, com especial destaque para a ausência de falsos positivos, embora tenha apresentado mais falsos negativos.

A análise das variáveis mais influentes em ambos os modelos revelou um padrão comum: a cultura organizacional tem peso significativo na percepção de etarismo. Elementos como satisfação profissional, políticas de diversidade etária, adequação às novas tecnologias e barreiras para recolocação foram recorrentes, mostrando que o preconceito etário vai além da idade em si e se manifesta no ambiente e nas práticas institucionais.

Além do desempenho técnico dos modelos, os resultados mostram que aproximadamente 43,5% dos profissionais seniores da base analisada relataram experiências de etarismo. Extrapolando para o cenário nacional, mais de 5,8 milhões de brasileiros com mais de 50 anos podem estar enfrentando desvantagens profissionais por conta da idade — uma estatística alarmante, especialmente se considerarmos que o setor de tecnologia tende a ser mais progressista que outros setores do mercado.

Do ponto de vista da análise de riscos, o estudo revela implicações críticas tanto para as empresas quanto para o mercado de trabalho em geral. Ignorar o etarismo representa um risco reputacional, social e econômico. Organizações que perpetuam práticas discriminatórias podem sofrer perda de talentos experientes, aumento de rotatividade e queda na produtividade. Além disso, há risco jurídico, especialmente em contextos onde ações afirmativas ou leis antidiscriminatórias são mais rigorosas. Do lado técnico, o uso de algoritmos também exige cautela: um modelo com alto recall pode cometer falsos positivos e gerar decisões injustas; um modelo com baixo recall pode invisibilizar vítimas reais. Por isso, o uso responsável da inteligência artificial, com revisão humana e validação ética, é indispensável.

Diante disso, o projeto demonstra que modelos de inteligência artificial podem e devem ser usados como ferramentas de diagnóstico social, fornecendo suporte objetivo à formulação de políticas públicas, práticas de RH e ações institucionais mais justas. Tanto o Random Forest quanto o KNN mostraram ser modelos viáveis e úteis nesse contexto, e sua aplicação pode servir de base para auditorias automatizadas, sistemas de triagem de processos seletivos ou ferramentas de monitoramento de clima organizacional, com foco em equidade etária.

Portanto, o estudo não apenas comprova a existência do etarismo no mercado de dados, mas também oferece caminhos práticos, baseados em dados, para combatê-lo e promover um ambiente profissional mais inclusivo e igualitário.

---



## Referências Bibliográficas

[1] Kaggle: *State of Data Brazil-2023*, o mapeamento mais completo do mercado brasileiro de dados [Data Hackers + Bain]. Disponível em: [https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023/data](https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-2023/data). Acesso em: 05 mar. 2025.

[2] IBGE. *Síntese de Indicadores Sociais – Uma análise das condições de vida da população brasileira*. Rio de Janeiro: Instituto Brasileiro de Geografia e Estatística, 2025. Disponível em: [https://www.ibge.gov.br/estatisticas/sociais/trabalho/9221-sintese-de-indicadores-sociais.html](https://www.ibge.gov.br/estatisticas/sociais/trabalho/9221-sintese-de-indicadores-sociais.html). Acesso em: 20 mar. 2025.

[3] IPEA. *Ipeadata – Conjunto de Microdados*. Brasília: Instituto de Pesquisa Econômica Aplicada, 2025. Disponível em: [https://www.ipeadata.gov.br/Default.aspx](https://www.ipeadata.gov.br/Default.aspx). Acesso em: 20 mar. 2025.

[4] OpenAI. *ChatGPT (GPT-4) - Inteligência artificial generativa*. São Francisco: OpenAI, 2023. Disponível em: [https://chat.openai.com/](https://chat.openai.com/). Acesso em: 05 mar. 2025.

---



## Apêndice

- [Imagem da Análise Exploratória de Dados](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/tree/main/assets/results)
- [Resultados do Modelo 1]
  - [Árvores do Modelo 1](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/assets/models/1st%20model/Results%20of%20First%20Model%20(Image).md)
  - [Matriz de Confusão Modelo 1](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/assets/models/1st%20model/Confusion%20Matrix%20Model%201%20(Image).md)
- [Resultados do Modelo 2]
  - [Matriz de Confusão Modelo 2](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo9-workplace-analysis/blob/main/assets/models/2nd%20model/Confusion%20Matrix%20Model%202%20(Image).md)
- [Link do Vídeo]()

---
