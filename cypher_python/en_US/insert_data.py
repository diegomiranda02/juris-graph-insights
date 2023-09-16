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

# Loading Judicial Decisions
def load_judicial_decisions(dataframe):
    [create_node("judicial_decision" + str(row["decision_id"]), "JudicialDecision", {"id": "judicial_decision" + str(row["decision_id"]), "decision_number": row["decision_number"], "decision_content": row["decision_content"]}) for _, row in dataframe.iterrows()]

# Loading Cases
def load_cases(dataframe):
    [create_node("case" +  str(row["case_id"]), "Case", {"id": "case" +  str(row["case_id"]), "case_number": row["case_number"], "area_of_law": row["area_of_law"]}) for _, row in dataframe.iterrows()]

# Loading Attorneys
def load_attorneys(dataframe):
    [create_node("attorney" +  str(row["attorney_id"]), "Attorney", {"id": "attorney" +  str(row["attorney_id"]), "attorney_name": row["attorney_name"]}) for _, row in dataframe.iterrows()]

# Loading Parties
def load_parties(dataframe):
    [create_node("party" +  str(row["party_id"]), "Party", {"id": "party" +  str(row["party_id"]), "party_type": row["party_type"], "party_name": row["party_name"]}) for _, row in dataframe.iterrows()]

# Loading Judges
def load_judges(dataframe):
    [create_node("judge" + str(row["judge_id"]), "Judge", {"id": "judge" + str(row["judge_id"]), "judge_name": row["judge_name"]}) for _, row in dataframe.iterrows()]

# Loading Acts
def load_acts(dataframe):
    [create_node("act" +  str(row["act_id"]), "Act", {"id": "act" +  str(row["act_id"]), "act_number": row["act_number"]}) for _, row in dataframe.iterrows()]

# Loading Chapters
def load_chapters(dataframe):
    [create_node("chapter" +  str(row["chapter_id"]), "Chapter", {"id": "chapter" +  str(row["chapter_id"]), "chapter_number": row["chapter_number"], "chapter_content": row["chapter_content"]}) for _, row in dataframe.iterrows()]

# Loading Section
def load_sections(dataframe):
    [create_node("section" +  str(row["section_id"]), "Section", {"id": "section" +  str(row["section_id"]), "section_number": row["section_number"], "section_content": row["section_content"]}) for _, row in dataframe.iterrows()]

# Loading Subsection
def load_subsections(dataframe):
    [create_node("subsection" +  str(row["subsection_id"]), "Subsection", {"id": "subsection" +  str(row["subsection_id"]), "subsection_number": row["subsection_number"], "subsection_content": row["subsection_content"]}) for _, row in dataframe.iterrows()]

########################################################
# Read data files
########################################################

DATA_DIR = './data/en_US/'

def load_data(file_path, load_function):
    df = pd.read_csv(file_path)
    load_function(df)

load_data(DATA_DIR + "decisions.csv", load_judicial_decisions)
load_data(DATA_DIR + "cases.csv", load_cases)
load_data(DATA_DIR + "attorneys.csv", load_attorneys)
load_data(DATA_DIR + "parties.csv", load_parties)
load_data(DATA_DIR + "judges.csv", load_judges)
load_data(DATA_DIR + "acts.csv", load_acts)
load_data(DATA_DIR + "chapters.csv", load_chapters)
load_data(DATA_DIR + "sections.csv", load_sections)
load_data(DATA_DIR + "subsections.csv", load_subsections)


#########################################################
# Creating the relationships
#########################################################

# (JUDGE)-[MAKES]->(JUDICIAL_DECISION)
# Randomly assinging one decision to a judge. It will be usefull to scale the records and test the perfomance with large data.

def create_relationships_judge_decision():
    for i in range(500):
        create_relationship("judge" + str(random.randint(1, 15)), "MAKES", "judicial_decision" + str(i))

# (JUDICIAL_DECISION)-[REFERENCES]->(ACT)
# Randomly assinging one law to a decision. It will be usefull to scale the records and test the perfomance with large data.

def create_relationships_judicial_decision_act():
    for i in range(500):
        create_relationship("judicial_decision" + str(i), "REFERENCES", "act" + str(random.randint(1, 10)), relationship_properties={"qty_of_references": random.randint(1, 5)})

# (JUDICIAL_DECISION)-[REFERENCES]->(CHAPTER)
# Randomly assinging one article to a decision. It will be usefull to scale the records and test the perfomance with large data.

def create_relationships_judicial_decision_chapter():
    for i in range(500):
        create_relationship("judicial_decision" + str(i), "REFERENCES", "chapter" + str(random.randint(1, 50)), relationship_properties={"qty_of_references": random.randint(1, 5)})

# (JUDICIAL_DECISION)-[REFERENCES]->(SECTION)
# Randomly assinging one paragrafo to a decision. It will be usefull to scale the records and test the perfomance with large data.

def create_relationships_judicial_decision_section():
    for i in range(500):
        create_relationship("judicial_decision" + str(i), "REFERENCES", "section" + str(random.randint(1, 250)), relationship_properties={"qty_of_references": random.randint(1, 5)})

# (JUDICIAL_DECISION)-[REFERENCES]->(SUBSECTION)
# Randomly assinging one alinea to a decision. It will be usefull to scale the records and test the perfomance with large data.

def create_relationships_judicial_decision_subsection():
    for i in range(500):
        create_relationship("judicial_decision" + str(i), "REFERENCES", "subsection" + str(random.randint(1, 500)), relationship_properties={"qty_of_references": random.randint(1, 5)})
    
# (ACT)-[CONTAINS]->(CHAPTER)
# Each law has five articles

def create_relationships_act_chapter():
    count = 1
    for i in range(1,11):
        for j in range(5):
            create_relationship("act" + str(i), "CONTAINS", "chapter" + str(count))
            count += 1

# (CHAPTER)-[CONTAINS]->(SECTION)
# Each article has five paragraphs

def create_relationships_chapter_section():
    count = 1
    for i in range(1,51):
        for j in range(5):
            create_relationship("chapter" + str(i), "CONTAINS", "section" + str(count))
            count += 1

# (SECTION)-[CONTAINS]->(SUBSECTION)
# Each paragraph has two alineas

def create_relationships_section_subsection():
    count = 1
    for i in range(1,251):
        for j in range(2):
            create_relationship("section" + str(i), "CONTAINS", "subsection" + str(count))
            count += 1

# (JUDICIAL_DECISION)-[:BELONGS_TO_CASE]->(CASE)
# Each decision is linked with a process
for i in range(1,501):
    create_relationship("judicial_decision" + str(i), "BELONGS_TO_CASE", "case" + str(i))

# (ATTORNEY)-[REPRESENTS]->(CASE)
# Each attorney has fifty processes
def create_relationships_attorney_case():
    case_count = 1
    for attorney_num in range(1, 11):
        attorney = f"attorney{attorney_num}"
        for _ in range(1, 51):
            case = f"case{case_count}"
            create_relationship(attorney,"REPRESENTS",case)
            case_count += 1



# (PARTY)-[INVOLVED_IN]->(CASE)
# Each part are in 10 processes

def create_relationships_party_case():
    case_count = 1
    for party_num in range(1, 51):
        party = f"party{party_num}"
        for _ in range(1, 11):
            case = f"case{case_count}"
            create_relationship(party,"INVOLVED_IN",case)
            case_count += 1

# Creating relationships among nodes

create_relationships_judge_decision()
create_relationships_judicial_decision_act()
create_relationships_judicial_decision_chapter()
create_relationships_judicial_decision_section()
create_relationships_judicial_decision_subsection()
create_relationships_act_chapter()
create_relationships_chapter_section()
create_relationships_section_subsection()
create_relationships_attorney_case()
create_relationships_party_case()


# Close the database connection
driver.close()
