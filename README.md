[English Version](https://github.com/diegomiranda02/juris-graph-insights/blob/main/README.md)

# Análise de Dados em Grafo com Python na Área do Direito

## Introdução

A área do Direito recentemente vem utilizando tecnologias e metodologias avançadas para auxiliar advogados, juízes e profissionais da área jurídica a tomarem decisões mais informadas e orientadas a dados. Com o crescente volume de dados disponíveis, a análise de dados em grafo tornou-se uma ferramenta importante para entender as relações complexas entre processos, decisões, advogados, partes do processo, artigos, leis, parágrafos e alíneas.

Ao incorporar juízes, processos, decisões e advogados no modelo de banco de dados gráfico, torna-se possível capturar as relações entre elementos legislativos e entidades legais envolvidas na interpretação, aplicação e representação da lei. Esse modelo estendido permite a navegação não apenas na hierarquia legislativa, mas também nos vários atores jurídicos e suas ações relacionadas a artigos, parágrafos ou alíneas específicas da lei. 

 Neste artigo, exploraremos como o Python pode ser uma ferramenta valiosa para acessar e analisar dados de uma base de dados em grafo e demonstrar o potencial dessa abordagem na área do Direito, utilizando como exemplo hipotético um escritório de advocacia fazendo uso dessas análises e aplicando nas tomadas de decisões.

## Exemplos que serão implementados neste artigo, em Python

Vamos explorar quatro exemplos práticos de como essa análise pode ser aplicada na área de Direito Ambiental, mas vale destacar que os mesmos conceitos podem ser expandidos para outras áreas do Direito, como tributário, previdenciário, cível, entre outras.

* **Perfil do Juiz e suas bases legais:**

    Suponha que um advogado recebeu um processo na área de Direito Ambiental e quer traçar o perfil do juiz responsável pelo caso. Com a análise de grafos, podemos identificar quais dispositivos legais esse juiz mais se baseia em suas decisões na área ambiental. O advogado pode analisar as decisões anteriores do juiz, identificando as leis, artigos e jurisprudências mais frequentemente citados nas sentenças.

* **Análise "What If" - Simulação de cenários:**

    Imagine que uma nova lei sobre regulação ambiental está em discussão no poder legislativo, e algumas alterações serão feitas nos artigos, parágrafos e alíneas de uma lei já existente. Neste cenário, o advogado pode utilizar a análise de grafos para responder perguntas como: "Quais processos que estou responsável poderão ser impactados com a alteração da lei ambiental atual?". Através da simulação de cenários, o advogado pode antecipar possíveis desdobramentos jurídicos e preparar-se para tais mudanças.

* **Impactos da alteração da lei no escritório de advocacia:**

    Em uma perspectiva de escritório de advocacia, é importante entender como a alteração da lei ambiental pode afetar os processos em andamento. Com a análise de grafos, o escritório pode mapear os processos que estão sendo conduzidos e identificar quais deles poderão ter impactos com a mudança na legislação ambiental. Isso permitirá que o escritório tome medidas preventivas ou de ajuste em casos específicos.

* **Identificação das leis e parágrafos mais relevantes:**

    Outra aplicação da análise de grafos é a determinação de quais leis e parágrafos têm maior impacto nas decisões judiciais associadas aos processos do escritório. Identificando essas leis e parágrafos mais relevantes, o escritório pode orientar seus advogados de forma mais efetiva, priorizando o estudo e a compreensão desses elementos chave do sistema jurídico.


Em todas as implementações, será apresentada a visualização gráfica da rede de conexões. A visualização das conexões permitirá que os advogados e o escritório de advocacia visualizem as redes de conexões entre as leis, decisões judiciais, dispositivos legais, e demais elementos relevantes. Essa visualização auxiliará na compreensão das relações entre os nós, possibilitando uma análise mais aprofundada e estratégica dos casos.


## O que são Bancos de Dados em Grafo?

Bancos de dados em grafo são estruturas que armazenam e representam dados usando nós e arestas para modelar as relações entre eles. Os nós representam entidades e as arestas representam as conexões ou relações entre essas entidades. Esse modelo é altamente eficiente para representar e acessar dados complexos com muitas interconexões (ORACLE).


## Modelagem de Dados Jurídicos em Grafo

Para demonstrar o potencial da análise de dados em grafo na área do Direito, podemos modelar um conjunto de dados comumente encontrado em escritórios de advocacia. Suponhamos que temos informações sobre processos judiciais, advogados, partes envolvidas, decisões, leis, artigos, parágrafos e alíneas. Vamos estruturar os dados em nós e arestas:

1. Nós (representam um conjuntos de informações sobre diferentes coisas: como pessoas, objetos ou até mesmo conceitos):

    * **Processos**
    * **Advogados**
    * **Juízes**
    * **Partes**
    * **Decisões Judiciais**
    * **Leis**
    * **Artigos**
    * **Parágrafos**
    * **Alíneas**

2. Arestas (são as conexões que mostram como os nós estão relacionados entre si). Abaixo uma descrição das conexões e da representação em um banco de dados em grafo:

    * **Relação entre juízes e decisões judiciais:** (JUIZ)-[PROFERE]->(DECISAO_JUDICIAL) - Um juiz profere uma decisão judicial.

    * **Relação entre decisões judiciais e leis:** (DECISAO_JUDICIAL)-[FAZ_REFERENCIA_A]->(LEI) - Uma decisão judicial faz referência a uma ou mais leis.

    * **Relação entre decisões judiciais e artigos:** (DECISAO_JUDICIAL)-[FAZ_REFERENCIA_AO]->(ARTIGO) - Uma decisão judicial faz referência a um ou mais artigos.

    * **Relação entre decisões judiciais e parágrafos:** (DECISAO_JUDICIAL)-[FAZ_REFERENCIA_AO]->(PARAGRAFO) - Uma decisão judicial faz referência a um ou mais parágrafos.

    * **Relação entre decisões judiciais e alíneas:** (DECISAO_JUDICIAL)-[FAZ_REFERENCIA_A]->(ALINEA) - Uma decisão judicial faz referência a uma ou mais alíneas.

    * **Relação entre lei e artigos:** (LEI)-[POSSUI_ARTIGO]->(ARTIGO) - Uma lei possui vários artigos.

    * **Relação entre artigos e parágrafos:** (ARTIGO)-[POSSUI_PARAGRAFO]->(PARAGRAFO) - Um artigo possui um ou mais parágrafos.

    * **Relação entre parágrafos e alíneas:** (PARAGRAFO)-[POSSUI_ALINEA]->(ALINEA) - Um parágrafo tem uma ou várias alíneas.

    * **Relação entre decisões judiciais e processos:** (DECISAO_JUDICIAL)-[PERTENCE_AO_PROCESSO]->(PROCESSO) - Uma decisão judicial pertence a um processo.

    * **Relação entre advogados e processos:** (ADVOGADO)-[ENVOLVIDO_EM]->(PROCESSO) - Um advogado está envolvido em um processo.

    * **Relação entre partes e processos:** (PARTE)-[ENVOLVIDA_EM]->(PROCESSO) - Uma parte está envolvida em um processo.

Os nós são representados entre parênteses () e as arestas são representadas entre colchetes [].

Como o objetivo do artigo é apresentar de forma mais simples e didática o potencial da análise de grafos em um escritório de advocacia, seguiremos com as relações acima descritas, porém há a possibilidade de representar interconexões de diferentes formas.

A imagem abaixo mostra um exemplo da representação gráfica dos nós e das arestas em um banco de dados orientado a grafo:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/graph_visualization_example.png?raw=true)


## Preparação do ambiente de desenvolvimento

1. Instalar Docker: Visite o site oficial (https://docs.docker.com/get-docker/) e siga as instruções para instalar o Docker no seu sistema.

2. Instalar Neo4J com Docker: Visite o site oficial https://neo4j.com/docs/operations-manual/current/docker/introduction/#docker-image e siga as instruções para instalar o servidor de banco de dados em grafo Neo4J com Docker.

3. Instalar Git: Instalar o Git do site oficial (https://git-scm.com/downloads).

4. Anaconda: Instalar o software Anaconda do site oficial (https://www.anaconda.com/download).

5. Clone o projeto do repositório do GitHub:

- Abra um terminal ou prompt de comando
- Mude o diretório para o qual você clonou o projeto.
- Execute o seguinte comando para clonar o projeto:

``` 
git clone https://github.com/diegomiranda02/juris-graph-insights.git
```
Uma vez que o download foi finalizado, mude para o diretório do projeto:

```
cd <diretorio_do_projeto>
```

5. Crie um ambiente para executar o projeto com o seguinte comando:

```bash
conda create -f config/environment.yaml
conda activate neo4j-project
```

6. Acesso o servidor do banco de dados Neo4J acessando http://localhost:7474/ para verificar se a instalação está correta.

7. Gerar os dados do banco:
```python
python cypher_python/insert_data.py
```

8. Para deletar os dados do banco execute o seguindo comando:
```python
python cypher_python/delete_data.py
```

9. Para consultar os dados do banco:
```python
python cypher_python/query_data.py
```

## Implementações dos exemplos

### Exemplo 1: Quais leis determinado juíz se baseia nas suas decisões dos processos na área do Direito Ambiental?

Para esse exemplo será considerado o 'juiz 3'e os processo na área de Direito Ambiental. 

```cypher
    MATCH (j:Juiz {nome: 'juiz 3'})-[:PROFERE]->(d:DecisaoJudicial)-[:FAZ_REFERENCIA_A]->(l:Lei) 
    MATCH (p:Processo)<-[:PERTENCE_AO_PROCESSO]-(d)
    WHERE (p.tipo_de_direito = 'Direito Ambiental')
    RETURN l.titulo
```

Esta consulta em linguagem Cypher busca recuperar os títulos das Leis referenciadas por Decisões Judiciais proferidas pelo Juiz de nome "juiz 3" em Processos do tipo "Direito Ambiental".

1. MATCH (j:Juiz {nome: 'juiz 3'})-[:PROFERE]->(d:DecisaoJudicial)-[:FAZ_REFERENCIA_A]->(l:Lei): Realiza uma correspondência para encontrar os nós que representam o Juiz de nome "juiz 3" (identificado pela variável 'j'), as Decisões Judiciais (identificadas pela variável 'd') proferidas por esse Juiz e as Leis (identificadas pela variável 'l') referenciadas por essas Decisões Judiciais.

2. MATCH (p:Processo)<-[:PERTENCE_AO_PROCESSO]-(d): Continuando a consulta, realiza uma correspondência para encontrar os nós que representam os Processos (identificados pela variável 'p') associados às Decisões Judiciais encontradas na correspondência anterior.

3. WHERE (p.tipo_de_direito = 'Direito Ambiental'): Define uma condição (WHERE) para filtrar apenas os Processos cujo tipo de direito seja "Direito Ambiental".

4. RETURN l.titulo: Retorna os títulos (l.titulo) das Leis que foram referenciadas pelas Decisões Judiciais proferidas pelo Juiz de nome "juiz 3" em Processos do tipo "Direito Ambiental".


Abaixo a figura representando as conexões:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/leis_que_o_juiz_3_mais_se_baseia.png?raw=true)

___

### Exemplo 2: Quais processos que determinado advogado está responsável poderão ter impactos com a alteração da lei ambiental atual?

Para esse exemplo será considerado o 'artigo 40' e os processo na área de Direito Ambiental. 

```cypher
MATCH (p:Processo {tipo_de_direito: "Direito Ambiental"})<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)-[:FAZ_REFERENCIA_AO]->(art:Artigo {numero: "artigo 40"}) 
MATCH (adv:Advogado)-[:ENVOLVIDO_EM]->(p)
RETURN p.numero as Número, p.titulo as Título, p.tipo_de_direito as Tipo_do_Direito
```

Esta consulta em linguagem Cypher busca as informações sobre os Processos do tipo "Direito Ambiental" que têm Decisões Judiciais relacionadas a um Artigo específico de número "artigo 40". Além disso, a consulta também recupera os Advogados envolvidos nesses Processos.

1. MATCH (p:Processo {tipo_de_direito: "Direito Ambiental"})<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)-[:FAZ_REFERENCIA_AO]->(art:Artigo {numero: "artigo 40"}): Realiza uma correspondência para encontrar os nós que representam os Processos (identificados pela variável 'p') do tipo "Direito Ambiental" e suas Decisões Judiciais associadas (identificadas pela variável 'dj'), que por sua vez estão relacionadas a um Artigo específico de número "artigo 40" (identificado pela variável 'art').

2. MATCH (adv:Advogado)-[:ENVOLVIDO_EM]->(p): Continuando a consulta, realiza uma correspondência para encontrar os Advogados (identificados pela variável 'adv') que estão envolvidos nos Processos (mantidos com a variável 'p') encontrados na correspondência anterior.

3. RETURN p.numero as Número, p.titulo as Título, p.tipo_de_direito as Tipo_do_Direito: Retorna os números, títulos e tipos de direito dos Processos ('p') que foram encontrados na primeira correspondência da consulta. A consulta também recupera os Advogados envolvidos nos Processos para fins de análise adicional.

Abaixo a figura representando as conexões:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/processos_impactados_por_mudanca_de_artigo.png?raw=true)

___

### Exemplo 3: Quais processos que estão sendo conduzidos aqui no escritório poderão ter impactos com a alteração da lei ambiental atual?

Para esse exemplo será considerada a lei de número 8 e os processo na área de Direito Ambiental. 

```cypher
MATCH (p:Processo {tipo_de_direito: "Direito Ambiental"})<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)-[:FAZ_REFERENCIA_A]->(lei:Lei {numero: 8}) 
RETURN p,lei,dj
```

Esta consulta em linguagem Cypher busca recuperar os Processos do tipo "Direito Ambiental" que têm Decisões Judiciais associadas a uma Lei específica de número 8.

1. MATCH (p:Processo {tipo_de_direito: "Direito Ambiental"})<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)-[:FAZ_REFERENCIA_A]->(lei:Lei {numero: 8}): Realiza uma correspondência para encontrar os nós que representam os Processos (identificados pela variável 'p') do tipo "Direito Ambiental" e suas Decisões Judiciais associadas (identificadas pela variável 'dj'), que por sua vez estão relacionadas a uma Lei específica de número 8 (identificada pela variável 'lei').

2. RETURN p, lei, dj: Retorna os nós dos Processos ('p'), da Lei específica ('lei') e das Decisões Judiciais ('dj') que foram encontrados na correspondência anterior da consulta.

Abaixo a figura representando as conexões:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/lei_alterada_que_pode_impactar_processos.png?raw=true)

___

### Exemplo 4: Determinar quais leis e parágrafos têm maior impacto em decisões judiciais associadas aos processos do escritório.

```cypher
MATCH (pr:Processo)<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)
MATCH (dj)-[:FAZ_REFERENCIA_A]->(l:Lei)
MATCH (dj)-[:FAZ_REFERENCIA_AO]->(p:Paragrafo)
MATCH (l)-[:POSSUI_ARTIGO]->(art:Artigo)
MATCH (art)-[:POSSUI_PARAGRAFO]->(p)
RETURN l, art, p, dj
```

Esta consulta em linguagem Cypher busca recuperar informações relacionadas às Leis, Artigos, Parágrafos e Decisões Judiciais que estão interconectados em um grafo de dados.

1. MATCH (pr:Processo)<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial): Realiza uma correspondência para encontrar os nós que representam os Processos (identificados pela variável 'pr') e suas Decisões Judiciais associadas (identificadas pela variável 'dj'). O relacionamento "<-[:PERTENCE_AO_PROCESSO]" liga as Decisões Judiciais aos Processos.

2. MATCH (dj)-[:FAZ_REFERENCIA_A]->(l:Lei): Continuando a correspondência anterior, encontra as Leis (identificadas pela variável 'l') que são referenciadas pelas Decisões Judiciais (mantidas com a variável 'dj'). O relacionamento "[:FAZ_REFERENCIA_A]" liga as Decisões Judiciais às Leis.

3. MATCH (dj)-[:FAZ_REFERENCIA_AO]->(p:Paragrafo): Continuando a correspondência anterior, encontra os Parágrafos (identificados pela variável 'p') que são referenciados pelas Decisões Judiciais (mantidas com a variável 'dj'). O relacionamento "[:FAZ_REFERENCIA_AO]" liga as Decisões Judiciais aos Parágrafos.

4. MATCH (l)-[:POSSUI_ARTIGO]->(art:Artigo): Continuando a correspondência, encontra os Artigos (identificados pela variável 'art') associados às Leis (mantidas com a variável 'l'). O relacionamento "[:POSSUI_ARTIGO]" liga as Leis aos Artigos.

5. MATCH (art)-[:POSSUI_PARAGRAFO]->(p): Continuando a correspondência, encontra os Parágrafos (identificados pela variável 'p') associados aos Artigos (mantidos com a variável 'art'). O relacionamento "[:POSSUI_PARAGRAFO]" liga os Artigos aos Parágrafos.

6. RETURN l, art, p, dj: Retorna os nós das Leis ('l'), dos Artigos ('art'), dos Parágrafos ('p') e das Decisões Judiciais ('dj') que foram encontrados nas correspondências anteriores da consulta.


```cypher
MATCH (pr:Processo)<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial)
MATCH (dj)-[:FAZ_REFERENCIA_A]->(l:Lei)
MATCH (dj)-[:FAZ_REFERENCIA_AO]->(p:Paragrafo)
MATCH (l)-[:POSSUI_ARTIGO]->(art:Artigo)
MATCH (art)-[:POSSUI_PARAGRAFO]->(p)
RETURN l.numero, art.numero, p.numero, COUNT(DISTINCT dj) AS ImpactoDecisoes
ORDER BY ImpactoDecisoes DESC
```

Esta consulta em linguagem Cypher busca determinar o impacto das Leis, Artigos e Parágrafos nas Decisões Judiciais associadas aos Processos em um banco de dados em grafo.

1. MATCH (pr:Processo)<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial): Realiza uma correspondência para encontrar os nós que representam os Processos (identificados pela variável 'pr') e suas Decisões Judiciais associadas (identificadas pela variável 'dj'). O relacionamento "<-[:PERTENCE_AO_PROCESSO]" liga as Decisões Judiciais aos Processos.

2. MATCH (dj)-[:FAZ_REFERENCIA_A]->(l:Lei): Continuando a correspondência, encontra as Leis (identificadas pela variável 'l') referenciadas pelas Decisões Judiciais (mantidas com a variável 'dj'). O relacionamento "[:FAZ_REFERENCIA_A]" liga as Decisões Judiciais às Leis.

3. MATCH (dj)-[:FAZ_REFERENCIA_AO]->(p:Paragrafo): Continuando a correspondência, encontra os Parágrafos (identificados pela variável 'p') referenciados pelas Decisões Judiciais (mantidas com a variável 'dj'). O relacionamento "[:FAZ_REFERENCIA_AO]" liga as Decisões Judiciais aos Parágrafos.

4. MATCH (l)-[:POSSUI_ARTIGO]->(art:Artigo): Continuando a correspondência, encontra os Artigos (identificados pela variável 'art') associados às Leis (mantidas com a variável 'l'). O relacionamento "[:POSSUI_ARTIGO]" liga as Leis aos Artigos.

5. MATCH (art)-[:POSSUI_PARAGRAFO]->(p): Continuando a correspondência, encontra os Parágrafos (identificados pela variável 'p') associados aos Artigos (mantidos com a variável 'art'). O relacionamento "[:POSSUI_PARAGRAFO]" liga os Artigos aos Parágrafos.

6. RETURN l.numero, art.numero, p.numero, COUNT(DISTINCT dj) AS ImpactoDecisoes: Retorna os números das Leis ('l.numero'), dos Artigos ('art.numero'), dos Parágrafos ('p.numero') e calcula o número de Decisões Judiciais distintas associadas a cada combinação de Lei, Artigo e Parágrafo. O resultado é renomeado como 'ImpactoDecisoes'.

7. ORDER BY ImpactoDecisoes DESC: Ordena os resultados em ordem decrescente de acordo com o impacto das Leis, Artigos e Parágrafos nas Decisões Judiciais, permitindo identificar quais têm maior impacto nas Decisões Judiciais associadas aos Processos.

Abaixo a figura representando as conexões:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/leis_e_paragrafos_que_tem_maior_impacto_em_decisoes_judiciais.png?raw=true)

___

## Conclusão

A análise de dados em grafo utilizando Python em conjunto com bancos de dados em grafo, como o "Neo4j", oferece um vasto potencial na área do Direito. A capacidade de modelar e visualizar relações complexas entre processos, decisões, advogados, partes, leis, artigos, parágrafos e alíneas permite uma análise mais profunda e informada, possibilitando a identificação de precedentes jurídicos relevantes e auxiliando na tomada de decisões. Com o uso adequado da análise de grafos, advogados e escritórios de advocacia podem ganhar insights valiosos, tomar decisões mais informadas e estar melhor preparados para enfrentar os desafios da prática jurídica na área do Direito. Com o contínuo avanço da tecnologia e a crescente quantidade de dados disponíveis, a análise de dados em grafo certamente desempenhará um papel fundamental no futuro do Direito.

## Referências

1. ORACLE. Banco de dados de grafos definido. Oracle, 2023. Disponível em: <https://www.oracle.com/br/autonomous-database/what-is-graph-database/#:~:text=Um%20banco%20de%20dados%20de,n%C3%A3o%20est%C3%A3o%20equipados%20a%20fazer>. Acesso em: 21 de jul. de 2023.


