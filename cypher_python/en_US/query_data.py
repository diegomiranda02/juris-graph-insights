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

# query is used to retrieve specific information related to a judge named 'judge 3' and their involvement in judicial decisions that reference acts, with a filter applied to cases falling under the area of law 'Environmental Law':
title = "query is used to retrieve specific information related to a judge named 'judge 3' and their involvement in judicial decisions that reference acts, with a filter applied to cases falling under the area of law 'Environmental Law'."
query = "MATCH (j:Judge {judge_name: 'judge 3'})-[:MAKES]->(d:JudicialDecision)-[:REFERENCES]->(a:Act) " + \
        "MATCH (c:Case)<-[:BELONGS_TO_CASE]-(d) " + \
        "WHERE (c.area_of_law = 'Environmental Law') " + \
        "RETURN a.act_number"
print_query_result(title, query)

# Query is used to retrieve specific information related to cases in the field of "Environmental Law" that involve judicial decisions referring to "Chapter 2" and the attorneys representing those cases.
title = "Query is used to retrieve specific information related to cases in the field of 'Environmental Law' that involve judicial decisions referring to 'Chapter 2' and the attorneys representing those cases."
query = "MATCH (c:Case {area_of_law: 'Environmental Law'})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(ch:Chapter {chapter_number: 'chapter 2'})" + \
        "MATCH (attorney:Attorney)-[:REPRESENTS]->(c) " + \
        "RETURN c.case_number as Number, c.area_of_law as Area_of_Law, attorney.attorney_name as Attorney"
print_query_result(title, query)

# Query is used to retrieve specific information related to cases in the field of "Environmental Law" that involve judicial decisions referencing "Act 1.
title = "Query is used to retrieve specific information related to cases in the field of 'Environmental Law' that involve judicial decisions referencing 'Act 1.'"
query = "MATCH (c:Case {area_of_law: 'Environmental Law'})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(act:Act {act_number: 'act 1'}) " + \
        "RETURN c, act, jd"
print_query_result(title, query)

# Query you provided is used to retrieve data from a graph database where legal cases (represented as nodes labeled "Case") are related to judicial decisions (labeled "JudicialDecision"). These judicial decisions, in turn, reference sections and subsections of some legal text.
title = "Query you provided is used to retrieve data from a graph database where legal cases (represented as nodes labeled 'Case') are related to judicial decisions (labeled 'JudicialDecision'). These judicial decisions, in turn, reference sections and subsections of some legal text."
query = "MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision) " + \
        "MATCH (jd)-[:REFERENCES]->(section:Section) " + \
        "MATCH (jd)-[:REFERENCES]->(subsection:Subsection) " + \
        "RETURN c, jd, section, subsection"
print_query_result(title, query)

title = "Query is designed to retrieve and analyze information related to judicial decisions that reference specific sections and subsections."
query = "MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision) " + \
        "MATCH (jd)-[:REFERENCES]->(section:Section) " + \
        "MATCH (jd)-[:REFERENCES]->(subsection:Subsection) " + \
        "RETURN section.section_number, subsection.subsection_number, COUNT(DISTINCT jd) AS ImpactOfDecisions " + \
        "ORDER BY ImpactOfDecisions DESC"
print_query_result(title, query)


 













