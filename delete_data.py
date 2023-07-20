from neo4j import GraphDatabase

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

def delete(query: str):
    result = _run_query(query)
    print(result)

delete("MATCH ()-[r]-() DELETE r")
delete("MATCH (n) DELETE n")
