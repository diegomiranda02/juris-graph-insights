[Versão em Português](https://github.com/diegomiranda02/juris-graph-insights/blob/main/README_portugues.md)

# Analyzing Graph Data Using Python in the Legal Field

## Introduction

The legal field has been incorporating advanced technologies and methodologies to aid lawyers, judges, and legal professionals in making informed and data-driven decisions. With the growing amount of data available, graph data analysis has become a crucial tool for comprehending the intricate relationships between cases, decisions, judges, attorneys, involved parties, acts, chapters, sections, and subsections.

By including judges, cases, decisions, and attorneys in the graph database model, it becomes feasible to depict the connections among legislative components and legal entities involved in interpreting, applying, and representing the law. This enhanced model allows for navigation not only within the legislative hierarchy but also among different legal actors and their activities related to specific sections and subsections of the act.

In this article, we will explore how Python can be a valuable tool for accessing and analyzing data from a graph database and demonstrate the potential of this approach in the field of Law, using a hypothetical example of a law firm utilizing these analyses and applying them in decision-making processes.

## This article will showcase examples implemented in Python

We can examine four useful instances of how this analysis can apply to Environmental Law. It's important to note that these same concepts can also be applied to other areas of law, including but not limited to tax law, social security law, and civil law.

* **Judge Profile and Their Legal Foundation:**

    Imagine a scenario where an attorney receives a case related to Environmental Law and wishes to understand the judge assigned to the case. By utilizing graph analysis, we can determine which legal provisions the judge frequently references in their environmental decisions. This enables the attorney to review the judge's past decisions and identify the most commonly cited sections and subsections in their decisions.

* **"What If" Analysis - Scenario Simulation:**

    Imagine being an attorney who is presented with a new environmental regulation law under discussion in the legislative branch. This proposed law will modify the current law by altering its chapters, sections, and subsections. Utilizing graph analysis, the attorney can address significant inquiries such as, "What will be the impact of the changes to the existing environmental law on the cases I am handling?" Through simulating various scenarios, the attorney can predict possible legal outcomes and be equipped for any adjustments that may occur.

* **Impacts of the Amendment to the Law on a Law Firm's Cases:**

    From a law firm's perspective, it is important to understand how the amendment to environmental law can affect ongoing cases. With graph analysis, the firm can map the ongoing cases and identify which of them may be impacted by the change in environmental legislation. This will enable the firm to take preventive or adjustment measures in specific cases.

* **Identification of the most relevant sections and subsections:**

    Another application of graph analysis is determining which sections and subsections have the greatest impact on the judicial decisions associated with the law firm's cases. By identifying these most relevant sections and subsections, the firm can guide its attorneys more effectively, prioritizing the study and understanding of these elements.


In all implementations, a graphical visualization of the network of connections will be presented. The visualization of connections will allow the attorneys and the law firm to see the networks of connections between acts, judicial decisions, legal provisions, and other relevant elements. This visualization will aid in understanding the relationships between nodes, enabling a more in-depth and strategic analysis of the cases.


## What are Graph Databases?

Graph databases are structures that store and represent data using nodes and edges to model the relationships between them. Nodes represent entities, and edges represent the connections or relationships between these entities. This model is highly efficient for representing and accessing complex data with many interconnections (ORACLE).


## Modeling Legal Data in Graphs

To demonstrate the potential of graph data analysis in the field of Law, we can model a dataset commonly found in law firms. Let's assume we have information about legal cases, attorneys, involved parties, decisions, judges, acts, chapters, sections, and subsections. We will structure the data into nodes and edges:

1. Nodes (representing sets of information about different things, such as people, objects, or even concepts):

    * **Cases**
    * **Attorneys**
    * **Judges**
    * **Parties**
    * **Judicial Decisions**
    * **Acts**
    * **Chapters**
    * **Sections**
    * **Subsections**

2. Edges (are the connections that show how the nodes are related to each other). Below is a description of the connections and their representation in a graph database:

    * **Relationship between Judges and Judicial Decisions:** (JUDGE)-[MAKES]->(JUDICIAL_DECISION)- This relationship indicates that a judge (or judges) is responsible for making judicial decisions.

    * **Relationship between Judicial Decisions and Cases:** (JUDICIAL_DECISION)-[BELONGS_TO_CASE]->(CASE)- This relationship indicates that a judicial decision is associated with a specific legal case.

    * **Relationship between Attorneys and Cases:** (ATTORNEY)-[REPRESENTS]->(CASE)- This relationship connects the attorneys to the case they are handling.

    * **Relationship between Parties and Cases:** (PARTY)-[INVOLVED_IN]->(CASE)- This relationship shows that a party (e.g., plaintiff, defendant) is involved in a specific case. It connects the parties to the cases in which they are participants.

    * **Relationship between Judicial Decisions and Acts, Chapters, Section, and Subsections:** (JUDICIAL_DECISION)-[REFERENCES]->(ACT), (JUDICIAL_DECISION)-[REFERENCES]->(CHAPTER), (JUDICIAL_DECISION)-[REFERENCES]->(SECTION) and (JUDICIAL_DECISION)-[REFERENCES]->(SUBSECTION) - Judicial decisions are connected to various legislative acts through different relationships. These relationships help establish clear references within the law. The first relationship means that the decision references the entire legislative act, indicating a reliance on or a broader connection to the entire legal framework. The second relationship specifies that the decision references a particular chapter within the legislative act, offering a more focused context. The third relationship means that the decision references a specific section, highlighting the reliance on or relevance to that particular section of the law. To provide even more detail, the model can include subsections, which connect the judicial decision to specific legal details within a section of the legislative act. These relationships allow for a comprehensive and organized representation of legal references in judicial decisions.

    * **Relationship between Acts, Chapters, Sections, and Subsections:** (ACT)-[CONTAINS]->(CHAPTER), (CHAPTER)-[CONTAINS]->(SECTION), and (SECTION)-[CONTAINS]->(SUBSECTION). These relationships represent the hierarchical structure of legal acts, with acts containing chapters, chapters containing sections, and sections containing subsections. While it's important to note that not all acts adhere to this exact structure, this article aims to demonstrate the potential of graph analysis in the legal context. By modeling legal entities and their interactions within a graph, this approach offers a possible framework for understanding, visualizing, and analyzing legal processes and relationships.


Nodes are represented in parentheses () and edges are represented in square brackets [].

As this article aims to present the potential of graph analysis in a law firm in a simpler and didactic way, we will continue with the relationships described above. However, there is the possibility of representing interconnections in different ways.

The image below shows an example of the graphical representation of nodes and edges in a graph database:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/en_US/graph_visualization_example.png?raw=true)

__

## Data Used in This Article

The project was developed with the aim to facilitate the rapid generation of fictitious data for testing and demonstrations. Therefore, data related to attorneys, judicial decisions, parties, cases, judges, acts, chapters, sections, and subsections were created sequentially and randomly. This approach allows the system to be quickly populated with information to verify its functionality and perform performance tests.

However, it is important to note that this data structure is flexible and can be easily adapted to represent real data. Simply modify the fields and attributes of the entities to reflect the real information that will be inserted. For example, to replace fictitious data with real data, just replace the names and information in the .csv files with real names and information of attorneys, judicial decisions, parties, etc.

The files containing the data are organized in the "data/en_US/" folder of the system.
In the "cypher_python/en_US/" folder, there are three Python scripts that facilitate data manipulation:

"insert_data.py": This script is responsible for inserting data into the entities of the graph database. When executed, it uses the predefined sequential data to populate the database.

"delete_data.py": The second script is responsible for deleting all existing data in the graph database. This allows restarting the system with clean data for new tests or the insertion of real data.

"query_data.py": Finally, the third script is used to perform queries on the data. It allows retrieving specific information about the entities in the database, enabling the verification of generated results.
__

## Development Environment Setup

1. Install Docker: Visit the official website (https://docs.docker.com/get-docker/) and follow the instructions to install Docker on your system.

2. Install Neo4J with Docker: Visit the official website (https://neo4j.com/docs/operations-manual/current/docker/introduction/#docker-image) and follow the instructions to install the Neo4J graph database server with Docker.

3. Install Git: Install Git from the official website (https://git-scm.com/downloads).

4. Anaconda: Install the Anaconda software from the official website (https://www.anaconda.com/download).

5. Clone the project from the GitHub repository:

- Open a terminal or command prompt
- Navigate to the directory where you want to clone the project
- Execute the following command to clone the project:

``` 
git clone https://github.com/diegomiranda02/juris-graph-insights.git
```
Once the download is complete, navigate to the project directory:

```
cd <diretorio_do_projeto>
```

6. Create an environment to run the project with the following command:

```bash
conda create -f config/environment.yaml
conda activate neo4j-project
```

7. Access the Neo4J database server by visiting http://localhost:7474/ to verify if the installation is correct.

8. Modify the database password in the following sections of the 'insert_data.py,' 'delete_data.py,' and 'query_data.py' scripts

```
username = CHANGE_USERNAME # Replace with your Neo4j username
password = CHANGE_PASSWORD # Replace with your Neo4j password
```

9. Generate the database data:

```python
python cypher_python/en_US/insert_data.py
```

10. To delete the database data, execute the following command:

```python
python cypher_python/en_US/delete_data.py
```

11. To query the database data:

```python
python cypher_python/en_US/query_data.py
```
__

## Examples of Implementations

### Example 1: Which laws does a specific judge rely on in their decisions in environmental law cases?

For this example, 'judge 3' and the cases in the field of environmental law will be considered.

```cypher
    MATCH (j:Judge {judge_name: 'judge 3'})-[:MAKES]->(d:JudicialDecision)-[:REFERENCES]->(a:Act)
    MATCH (c:Case)<-[:BELONGS_TO_CASE]-(d)
    WHERE (c.area_of_law = 'Environmental Law')
    RETURN a.act_number
```

This Cypher query is used to retrieve specific information related to a judge named 'judge 3' and their involvement in judicial decisions that reference acts, with a filter applied to cases falling under the area of law 'Environmental Law'. 

1. MATCH (j:Judge {judge_name: 'judge 3'})-[:MAKES]->(d:JudicialDecision)-[:REFERENCES]->(a:Act): This part of the query starts by matching a node labeled as 'Judge' (represented by j) where the judge's name is 'judge 3'. It then follows an outgoing relationship labeled as 'MAKES' to find associated 'JudicialDecision' nodes (represented by d). From these decisions, it continues with an outgoing relationship labeled as 'REFERENCES' to find associated 'Act' nodes (represented by a).

2. MATCH (c:Case)<-[:BELONGS_TO_CASE]-(d): In this part of the query, it matches 'Case' nodes (represented by c) connected by an incoming relationship labeled as 'BELONGS_TO_CASE' to the previously matched 'JudicialDecision' nodes (d). This part of the query identifies the cases associated with these decisions.

3. WHERE (c.area_of_law = 'Environmental Law'): This is a conditional statement that filters the cases to include only those where the 'area_of_law' property is equal to 'Environmental Law'. It narrows down the results to cases specifically related to environmental law.

4. RETURN a.act_number: Finally, the query returns the 'act_number' property of the 'Act' nodes (a) that were referenced in the judicial decisions made by 'judge 3' and are associated with cases falling under environmental law.


Below is a figure representing the connections:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/en_US/act_a_judge_rely_on_decisions.png?raw=true)

___

### Example 2: What is the potential impact of the current environmental law amendment on the cases where a specific lawyer is acting as responsible?

For this example, 'chapter 2' and the cases in the field of environmental law will be considered.

```cypher
MATCH (c:Case {area_of_law: "Environmental Law"})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(ch:Chapter {chapter_number: 'chapter 2'})
MATCH (attorney:Attorney)-[:REPRESENTS]->(c)
RETURN c.case_number as Number, c.area_of_law as Area_of_Law, attorney.attorney_name as Attorney
```

This Cypher query is used to retrieve specific information related to cases in the field of "Environmental Law" that involve judicial decisions referring to "Chapter 2" and the attorneys representing those cases.

1. MATCH (c:Case {area_of_law: "Environmental Law"})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(ch:Chapter {chapter_number: 'chapter 2'}): This part of the query starts by matching 'Case' nodes (represented by c) where the 'area_of_law' property is equal to "Environmental Law." This identifies cases within the environmental law field. It then uses an incoming relationship labeled as 'BELONGS_TO_CASE' to find associated 'JudicialDecision' nodes (represented by jd) related to these cases. From these decisions, it continues with an outgoing relationship labeled as 'REFERENCES' to find associated 'Chapter' nodes (represented by ch) with a 'chapter_number' property of 'chapter 2'. This identifies cases within environmental law that reference Chapter 2.

2. MATCH (attorney:Attorney)-[:REPRESENTS]->(c): In this part of the query, it matches 'Attorney' nodes (represented by attorney) who are connected by an outgoing relationship labeled as 'REPRESENTS' to the previously matched 'Case' nodes (c). This identifies the attorneys representing these cases.

3. RETURN c.case_number as Number, c.area_of_law as Area_of_Law: Finally, the query returns the 'case_number' and 'area_of_law' properties of the 'Case' nodes (c) that meet the specified criteria. The aliasing (Number and Area_of_Law) is used to provide more meaningful column headers in the query result.

Below is the figure representing the connections:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/en_US/cases_affected_by_chapter_change.png?raw=true)

___

### Example 3: Which cases being handled in the law firm may be impacted by the current Environmental Act amendment?

For this example, Act Number 1 and the cases in the field of environmental law will be considered.

```cypher
MATCH (c:Case {area_of_law: "Environmental Law"})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(act:Act {act_number: 'act 1'})
RETURN c, act, jd
```

This Cypher query is used to retrieve specific information related to cases in the field of "Environmental Law" that involve judicial decisions referencing "Act 1.

1. MATCH (c:Case {area_of_law: "Environmental Law"})<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)-[:REFERENCES]->(act:Act {act_number: 'act 1'}): This part of the query begins by matching 'Case' nodes (represented by c) where the 'area_of_law' property is equal to "Environmental Law." This filters cases specifically within the environmental law field. It then follows an incoming relationship labeled as 'BELONGS_TO_CASE' to find associated 'JudicialDecision' nodes (represented by jd) connected to these cases. From these judicial decisions, it proceeds with an outgoing relationship labeled as 'REFERENCES' to identify 'Act' nodes (represented by act) with an 'act_number' property set to 'act 1'. This narrows the focus to cases within environmental law that reference Act 1.

2. RETURN c, act, jd: Finally, the query returns the matched nodes and relationships: c represents the 'Case' nodes, the act represents the 'Act' nodes referencing "Act 1" and jd represents the 'JudicialDecision' nodes associated with these cases and references to Act 1.

Below is the figure representing the connections:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/en_US/amended_act_that_may_impact_cases.png?raw=true)

___

### Example 4: Determine which sections and subsections have the greatest impact on judicial decisions associated with the law firm's cases.

```cypher
MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)
MATCH (jd)-[:REFERENCES]->(section:Section)
MATCH (jd)-[:REFERENCES]->(subsection:Subsection)
RETURN c, jd, section, subsection
```

The Cypher query you provided is used to retrieve data from a graph database where legal cases (represented as nodes labeled "Case") are related to judicial decisions (labeled "JudicialDecision"). These judicial decisions, in turn, reference sections and subsections of some legal text.

1. MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision): This part of the query finds pairs of nodes where a "Case" node (labeled as 'c') is connected to a "JudicialDecision" node (labeled as 'jd') using a relationship labeled "BELONGS_TO_CASE." This relationship represents that a judicial decision belongs to a specific legal case.

2. MATCH (jd)-[:REFERENCES]->(section:Section): In this part of the query, it continues from the previous match and finds nodes connected to the "JudicialDecision" nodes. Specifically, it looks for nodes labeled "Section" (labeled as 'section') that are connected to the "JudicialDecision" nodes via a relationship labeled "REFERENCES." This suggests that the judicial decision references a legal section.

3. MATCH (jd)-[:REFERENCES]->(subsection:Subsection): Similarly, this part of the query continues from the previous match and finds nodes labeled "Subsection" (labeled as 'subsection') that are connected to the same "JudicialDecision" nodes via a relationship labeled "REFERENCES." This represents that the judicial decision also references a legal subsection.

4. RETURN c, jd, section, subsection: Finally, the query returns the nodes for the legal case ('c'), the judicial decision ('jd'), the section of law ('section'), and the subsection of law ('subsection') that were found in the previous matches. The result of this query will include combinations of these nodes based on the specified relationships and labels.


```cypher
MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision)
MATCH (jd)-[:REFERENCES]->(section:Section)
MATCH (jd)-[:REFERENCES]->(subsection:Subsection)
RETURN section.section_number, subsection.subsection_number, COUNT(DISTINCT jd) AS ImpactOfDecisions
ORDER BY ImpactOfDecisions DESC
```

This Cypher query is designed to retrieve and analyze information related to judicial decisions that reference specific sections and subsections.

1. MATCH (c:Case)<-[:BELONGS_TO_CASE]-(jd:JudicialDecision): This part of the query begins by matching 'Case' nodes (represented by c) connected by an incoming relationship labeled as 'BELONGS_TO_CASE' to 'JudicialDecision' nodes (represented by jd). This identifies cases and their associated judicial decisions.

2. MATCH (jd)-[:REFERENCES]->(section:Section): In the next part, it continues from the matched 'JudicialDecision' nodes (jd) and follows an outgoing relationship labeled as 'REFERENCES' to connect to 'Section' nodes (represented by section). This identifies sections referenced by the judicial decisions.

3. MATCH (jd)-[:REFERENCES]->(subsection:Subsection): Similarly, this part of the query also follows the 'REFERENCES' relationship from 'JudicialDecision' nodes (jd) to 'Subsection' nodes (represented by subsection). It identifies subsections referenced by the judicial decisions.

4. RETURN section.section_number, subsection.subsection_number, COUNT(DISTINCT jd) AS ImpactOfDecisions: Here, the query specifies what information to return:section.section_number retrieves the section numbers, subsection.subsection_number retrieves the subsection numbers and COUNT(DISTINCT jd) AS ImpactOfDecisions calculates the count of distinct judicial decisions that reference each section and subsection. It also gives this count an alias "ImpactOfDecisions".

5. ORDER BY ImpactOfDecisions DESC: Finally, the query orders the results in descending order based on the count of judicial decisions impacting each section and subsection. This means that the sections and subsections with the most significant impact will appear at the top of the result set.

Below is the figure representing the connections:

![alt text](https://github.com/diegomiranda02/juris-graph-insights/blob/main/images/en_US/sections_and_subsections_with_the_greatest_impact_on_judicial_decisions.png?raw=true)

___

## Conclusion

Graph data analysis using Python in conjunction with graph databases like "Neo4j" offers vast potential in the field of Law. The ability to model and visualize complex relationships between cases, decisions, attorneys, parties, acts, chapters, sections, and subsections allows for a deeper and more informed analysis, enabling the identification of relevant legal precedents and assisting in decision-making. With the proper use of graph analysis, attorneys and law firms can gain valuable insights, make more informed decisions, and be better prepared to tackle the challenges of legal practice in the field of Law. With the ongoing advancement of technology and the increasing amount of available data, graph data analysis will undoubtedly play a pivotal role in the future of Law.

## References

1. ORACLE. Defined graph database. Oracle, 2023. Available at: https://www.oracle.com/br/autonomous-database/what-is-graph-database/#:~:text=Um%20banco%20de%20dados%20de,n%C3%A3o%20est%C3%A3o%20equipados%20a%20fazer. Accessed on: July 21, 2023.


