from neo4j import GraphDatabase
import pandas as pd

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"  # Replace with your Neo4j username
password = "12345678"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

def _run_query(query: str):
    result = None
    with driver.session() as session:
        result = session.run(query)
        records = result.data()
    # Close the database connection
    driver.close()

    return records

def run_query(query: str) -> pd.DataFrame:
    result = _run_query(query)
    df = pd.DataFrame.from_dict(result)

    return df

def print_query_result(title: str, query: str):
    separator = "-" * len(title)
    result = run_query(query)

    print(f"{title}\n{separator}\n{result}\n\n")

# Recuperar as alíneas associadas a um determinado artigo:
title = "Recuperar as alíneas associadas a um determinado artigo"
query = "MATCH (a:Artigo {numero: 'artigo 13'})-[:POSSUI_PARAGRAFO]->(p:Paragrafo)-[:POSSUI_ALINEA]->(al:Alinea) RETURN al.numero as numero_alinea, a.numero as numero_artigo, p.numero as numero_processo"
print_query_result(title, query)

# Todas as decisões judiciais associadas a um determinado processo:
title = "Todas as decisões judiciais associadas a um determinado processo"
query = "MATCH (p:Processo {numero: " + str(11) + "})<-[:PERTENCE_AO_PROCESSO]-(dj:DecisaoJudicial) RETURN dj.numero as numero_da_decisao, p.numero as numero_do_processo"
print_query_result(title, query)

# Todos os advogados envolvidos em um processo específico
title = "Todos os advogados envolvidos em um processo específico"
query = "MATCH (p:Processo {numero: " + str(1) + "})<-[:ENVOLVIDO_EM]-(a:Advogado) RETURN a.nome as nome, a.registro_OAB as registro_OAB"
print_query_result(title, query)

# Todas as partes relacionadas a um um processo específico
title = "Todas as partes relacionadas a um um processo específico"
query = "MATCH (p:Processo {numero: " + str(1) + "})<-[:ENVOLVIDA_EM]-(pa:Parte) RETURN pa.nome as nome_da_parte, p.numero as numero_do_processo"
print_query_result(title, query)

title = "Todas as partes relacionadas a um um processo específico"
query = "MATCH (p:Processo {numero: " + str(57) + "})<-[:ENVOLVIDA_EM]-(pa:Parte) RETURN pa.nome as nome_da_parte, p.numero as numero_do_processo"
print_query_result(title, query)

# Recuperar todas as leis associadas a uma decisão judicial específica
title = "Recuperar todas as leis associadas a uma decisão judicial específica"
query = "MATCH (dj:DecisaoJudicial {numero: 'decisao 123'})-[:FAZ_REFERENCIA_A]->(l:Lei) RETURN dj.numero as decisao, l.numero as numero_da_lei, l.titulo as titulo_da_lei"
print_query_result(title, query)

# Recuperar todos os artigos associados a uma decisão judicial específica
title = "Recuperar todos os artigos associados a uma decisão judicial específica"
query = "MATCH (dj:DecisaoJudicial {numero: 'decisao 123'})-[:FAZ_REFERENCIA_AO]->(a:Artigo) RETURN dj.numero as decisao, a.numero as numero_do_artigo"
print_query_result(title, query)

# Recuperar todos os parágrafos associados a uma decisão judicial específica
title = "Recuperar todos os parágrafos associados a uma decisão judicial específica"
query = "MATCH (dj:DecisaoJudicial {numero: 'decisao 123'})-[:FAZ_REFERENCIA_AO]->(p:Paragrafo) RETURN dj.numero as decisao, p.numero as numero_do_paragrafo"
print_query_result(title, query)

# Recuperar todas as alíneas associadas a uma decisão judicial específica
title = "Recuperar todas as alíneas associadas a uma decisão judicial específica"
query = "MATCH (dj:DecisaoJudicial {numero: 'decisao 123'})-[:FAZ_REFERENCIA_A]->(al:Alinea) RETURN dj.numero as decisao, al.numero as numero_da_alinea"
print_query_result(title, query)

# Quais leis que o 'juiz 3' mais referencia nas suas decisoes sobre direito ambiental?
title = "Quais leis que o 'juiz 3' mais referencia nas suas decisoes sobre direito ambiental?"
query = "MATCH (j:Juiz {nome: 'juiz 3'})-[:PROFERE]->(d:DecisaoJudicial)-[:FAZ_REFERENCIA_A]->(l:Lei) "
query += "MATCH (p:Processo)<-[:PERTENCE_AO_PROCESSO]-(d) " 
query += "WHERE (p.tipo_de_direito = 'Direito Ambiental') "
query += "RETURN l.numero as Lei, j.nome as Juíz, p.numero as Processo "
query += "ORDER BY l.numero"
print_query_result(title, query)

 













