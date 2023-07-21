from neo4j import GraphDatabase
import pandas as pd
import random
import numpy as np

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"  # Replace with your Neo4j username
password = "12345678"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

#############################################
# Define a function to create nodes
#############################################

def create_node(node_label, node_type, node_properties):
    
    #Connect to the database and create a session
    with driver.session() as session:
        session.execute_write(_create_node, node_label, node_type, node_properties)

########################################################################
# Private method to create the query and execute the transaction
########################################################################

def _create_node(tx, 
                 node_label, 
                 node_type, 
                 node_properties):

    # The properties of the node in a dictionary format
    properties_string = ', '.join(f'{key}: ${key}' for key in node_properties.keys())
    # Create the query to execute
    query = f"CREATE ({node_label}:{node_type} {{{properties_string}}})"
    # Assign the parameters
    parameters = {**node_properties}
    # Run the query
    tx.run(query, **parameters)


######################################################
# Define a function to create a relationship
######################################################

def create_relationship(from_node_id, 
                        relationship_type, 
                        to_node_id, 
                        direction="UNIDIRECTIONAL", 
                        relationship_properties=None):
    
    with driver.session() as session:
        session.execute_write(_create_relationship, 
                              from_node_id, 
                              relationship_type, 
                              to_node_id, direction, 
                              relationship_properties)
    
######################################################
# Private method to create the query and execute the transaction
######################################################
def _create_relationship(tx, 
                         from_node_id, 
                         relationship_type, 
                         to_node_id, 
                         direction, 
                         relationship_properties):
    
    if direction == "BIDIRECTIONAL":
        relationship_clause = "<-[r:%s]->" % relationship_type
    else:
        relationship_clause = "-[r:%s]->" % relationship_type

    properties_clause = ""
    if relationship_properties:
        properties_clause = " SET r += $properties"

    query = (
        "MATCH (from {id: '%s'}), (to {id: '%s'}) "
        "CREATE (from)%s(to)%s"
    ) % (from_node_id, 
         to_node_id, 
         relationship_clause, 
         properties_clause)

    parameters = {
        "properties": relationship_properties,
    }

    tx.run(query, **parameters)

###################################################################################
# Using list comprehension to load the data in Neo4J
###################################################################################

# Loading Decisoes Judiciais
def load_decisoes(dataframe):
    [create_node("decisaoJudicial" + str(row["id"]), "DecisaoJudicial", {"id": "decisaoJudicial" + str(row["id"]), "numero": row["numero"], "resumo": row["resumo"], "conteudo": row["conteudo"]}) for _, row in dataframe.iterrows()]

# Loading Processos
def load_processos(dataframe):
    [create_node("processo" +  str(row["numero"]), "Processo", {"id": "processo" +  str(row["numero"]), "numero": row["numero"], "titulo": row["titulo"], "tipo_de_direito": row["tipo_de_direito"]}) for _, row in dataframe.iterrows()]

# Loading Advogados
def load_advogados(dataframe):
    [create_node("advogado" +  str(row["registro_OAB"]), "Advogado", {"id": "advogado" +  str(row["registro_OAB"]), "registro_OAB": row["registro_OAB"], "nome": row["nome"]}) for _, row in dataframe.iterrows()]

# Loading Partes
def load_partes(dataframe):
    [create_node("parte" +  str(row["documento"]), "Parte", {"id": "parte" +  str(row["documento"]), "documento": row["documento"], "tipo_documento": row["tipo_documento"], "tipo_parte": row["tipo_parte"], "nome": row["nome"], "endereco": row["endereco"]}) for _, row in dataframe.iterrows()]

# Loading Juizes
def load_juizes(dataframe):
    [create_node("juiz" + str(row["cpf"]), "Juiz", {"id": "juiz" + str(row["id"]), "nome": row["nome"], "cpf": row["cpf"], "tribunal": row["tribunal"]}) for _, row in dataframe.iterrows()]

# Loading Leis
def load_leis(dataframe):
    [create_node("lei" +  str(row["numero"]), "Lei", {"id": "lei" +  str(row["numero"]), "numero": row["numero"], "titulo": row["titulo"]}) for _, row in dataframe.iterrows()]

# Loading Artigos
def load_artigos(dataframe):
    [create_node("artigo" +  str(row["id"]), "Artigo", {"id": "artigo" +  str(row["id"]), "numero": row["numero"], "conteudo": row["conteudo"]}) for _, row in dataframe.iterrows()]

# Loading Paragrafos
def load_paragrafos(dataframe):
    [create_node("paragrafo" +  str(row["id"]), "Paragrafo", {"id": "paragrafo" +  str(row["id"]), "numero": row["numero"], "conteudo": row["conteudo"]}) for _, row in dataframe.iterrows()]

# Loading Alineas
def load_alineas(dataframe):
    [create_node("alinea" +  str(row["id"]), "Alinea", {"id": "alinea" +  str(row["id"]), "numero": row["numero"], "conteudo": row["conteudo"]}) for _, row in dataframe.iterrows()]

########################################################
# Read data files
########################################################

DATA_DIR = './data_pt_BR/'

def load_data(file_name, load_function):
    df = pd.read_csv(DATA_DIR + file_name)
    load_function(df)

load_data("decisoes.csv", load_decisoes)
load_data("processos.csv", load_processos)
load_data("advogados.csv", load_advogados)
load_data("partes.csv", load_partes)
load_data("juizes.csv", load_juizes)
load_data("leis.csv", load_leis)
load_data("artigos.csv", load_artigos)
load_data("paragrafos.csv", load_paragrafos)
load_data("alineas.csv", load_alineas)


#########################################################
# Creating the relationships
#########################################################

# JUIZ -[PROFERE]-> DECISAO
# Randomly assinging one decision to a judge. It will be usefull to scale the records and test the perfomance with large data.
for i in range(500):
    create_relationship("juiz" + str(random.randint(1, 15)), "PROFERE", "decisaoJudicial" + str(i))

# DECISAO -[FAZ_REFERENCIA_A]-> LEI
# Randomly assinging one law to a decision. It will be usefull to scale the records and test the perfomance with large data.
for i in range(500):
    create_relationship("decisaoJudicial" + str(i), "FAZ_REFERENCIA_A", "lei" + str(random.randint(1, 10)), relationship_properties={"qtd_referencias": random.randint(1, 5)})

# DECISAO -[FAZ_REFERENCIA_AO]-> ARTIGO
# Randomly assinging one article to a decision. It will be usefull to scale the records and test the perfomance with large data.
for i in range(500):
    create_relationship("decisaoJudicial" + str(i), "FAZ_REFERENCIA_AO", "artigo" + str(random.randint(1, 50)), relationship_properties={"qtd_referencias": random.randint(1, 5)})

# DECISAO -[FAZ_REFERENCIA_AO]-> PARAGRAFO
# Randomly assinging one paragrafo to a decision. It will be usefull to scale the records and test the perfomance with large data.
for i in range(500):
    create_relationship("decisaoJudicial" + str(i), "FAZ_REFERENCIA_AO", "paragrafo" + str(random.randint(1, 250)), relationship_properties={"qtd_referencias": random.randint(1, 5)})

# DECISAO -[FAZ_REFERENCIA_A]-> ALINEA
# Randomly assinging one alinea to a decision. It will be usefull to scale the records and test the perfomance with large data.
for i in range(500):
    create_relationship("decisaoJudicial" + str(i), "FAZ_REFERENCIA_A", "alinea" + str(random.randint(1, 500)), relationship_properties={"qtd_referencias": random.randint(1, 5)})
    
# LEI -[POSSUI_ARTIGO]-> ARTIGO
# Each law has five articles
count = 1
for i in range(1,11):
    for j in range(5):
        create_relationship("lei" + str(i), "POSSUI_ARTIGO", "artigo" + str(count))
        count += 1

# ARTIGO -[POSSUI_PARAGRAFO]-> PARAGRAFO
# Each article has five paragraphs
count = 1
for i in range(1,51):
    for j in range(5):
        create_relationship("artigo" + str(i), "POSSUI_PARAGRAFO", "paragrafo" + str(count))
        count += 1

# PARAGRAFO -[POSSUI_ALINEA]-> ALINEA
# Each paragraph has two alineas
count = 1
for i in range(1,251):
    for j in range(2):
        create_relationship("paragrafo" + str(i), "POSSUI_ALINEA", "alinea" + str(count))
        count += 1

# DECISAO_JUDICIAL -[PERTENCE_AO_PROCESSO]-> PROCESSO
# Each decision is linked with a process
for i in range(1,501):
    create_relationship("decisaoJudicial" + str(i), "PERTENCE_AO_PROCESSO", "processo" + str(i))

# ADVOGADO -[ENVOLVIDO_EM]-> PROCESSO
# Each lawyer has fifty processes
def create_relationships_lawyer_process():
    processo_count = 1
    for advogado_num in range(1, 11):
        advogado = f"advogado{advogado_num}"
        for _ in range(1, 51):
            processo = f"processo{processo_count}"
            create_relationship(advogado,"ENVOLVIDO_EM",processo)
            processo_count += 1



# PARTE -[ENVOLVIDA_EM]-> PROCESSO
# Each part are in 10 processes
def create_relationships_part_process():
    processo_count = 1
    for parte_num in range(1, 51):
        parte = f"parte{parte_num}"
        for _ in range(1, 11):
            processo = f"processo{processo_count}"
            create_relationship(parte,"ENVOLVIDA_EM",processo)
            processo_count += 1

create_relationships_lawyer_process()
create_relationships_part_process()


# Close the database connection
driver.close()
