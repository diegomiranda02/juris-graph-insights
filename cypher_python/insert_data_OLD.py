from neo4j import GraphDatabase

# Establish a connection to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"  # Replace with your Neo4j username
password = "12345678"  # Replace with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(username, password))

# Define a function to create nodes
def create_node(node_label, node_type, node_properties):

    #Connect to the database and create a session
    with driver.session() as session:
        session.execute_write(_create_node, node_label, node_type, node_properties)

# Private method to create the query and execute the transaction
def _create_node(tx, node_label, node_type, node_properties):

    # The properties of the node in a dictionary format
    properties_string = ', '.join(f'{key}: ${key}' for key in node_properties.keys())

    # Create the query to execute
    query = f"CREATE ({node_label}:{node_type} {{{properties_string}}})"

    # Assign the parameters
    parameters = {**node_properties}

    # Run the query
    tx.run(query, **parameters)


# Define a function to create a relationship
def create_relationship(from_node_id, relationship_type, to_node_id, direction="UNIDIRECTIONAL", relationship_properties=None):
    with driver.session() as session:
        session.execute_write(_create_relationship, from_node_id, relationship_type, to_node_id, direction, relationship_properties)

def _create_relationship(tx, from_node_id, relationship_type, to_node_id, direction, relationship_properties):
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
    ) % (from_node_id, to_node_id, relationship_clause, properties_clause)

    parameters = {
        "properties": relationship_properties,
    }

    tx.run(query, **parameters)


# Create Categories
create_node("smartphones","Category", {"id": "smartphones", "title": "Smartphones"})
create_node("notebooks", "Category", {"id": "notebooks","title": "Notebooks"})
create_node("cameras", "Category", {"id": "cameras","title": "Cameras"})

# Smartphones
create_node("sony_xperia_z22","Product", {"id": "sony_xperia_z22","title": "Sony Experia Z22", "price": 765.00, "shippability": True, "availability": True})
create_node("sony_galaxy_s8","Product", {"id": "sony_galaxy_s8","title": "Samsung Galaxy S8", "price": 784.00, "shippability": True, "availability": True})
create_node("sony_xperia_xa1","Product", {"id": "sony_xperia_xa1","title": "Sony Experia XA1 Dual G3112", "price": 229.50, "shippability": True, "availability": False})
create_node("iphone_8","Product", {"id": "iphone_8","title": "Apple iPhone 8 Plus 64GB", "price": 874.20, "shippability": True, "availability": False})
create_node("xiaomi_mi_mix_2","Product", {"id": "xiaomi_mi_mix_2","title": "Xiaomi Mi Mix 2", "price": 420.87, "shippability": True, "availability": True})
create_node("huawei_p8","Product", {"id": "huawei_p8","title": "Huawei P8 Lite", "price": 191.00, "shippability": True, "availability": True})


# Create the Relationship between Product and Category
create_relationship("sony_xperia_z22", "IS_IN", "smartphones")
create_relationship("sony_galaxy_s8", "IS_IN", "smartphones")
create_relationship("sony_xperia_xa1", "IS_IN", "smartphones")
create_relationship("iphone_8", "IS_IN", "smartphones")
create_relationship("xiaomi_mi_mix_2", "IS_IN", "smartphones")
create_relationship("huawei_p8", "IS_IN", "smartphones")

# Notebooks
create_node("acer_swift_3","Product", {"id": "acer_swift_3", "title": "Acer Swift 3 SF314-51-34TX", "price": 595.00, "shippability": True, "availability": False})
create_node("hp_pro_book","Product", {"id": "hp_pro_book","title": "HP ProBook 440 G4", "price": 771.30, "shippability": True, "availability": True})
create_node("dell_inspiron_15","Product", {"id": "dell_inspiron_15","title": "Dell Inspiron 15 7577", "price": 1477.50, "shippability": True, "availability": False})
create_node("apple_macbook","Product", {"id": "apple_macbook","title": "Apple MacBook A1534 12' Rose Gold", "price": 1293.00, "shippability": False, "availability": False})

# Create the Relationship between Product and Category
create_relationship("acer_swift_3", "IS_IN", "notebooks")
create_relationship("hp_pro_book", "IS_IN", "notebooks")
create_relationship("dell_inspiron_15", "IS_IN", "notebooks")
create_relationship("apple_macbook", "IS_IN", "notebooks")

# Cameras
create_node("canon_eos_6d","Product", {"id": "canon_eos_6d","title": "Canon EOS 6D Mark II Body", "price": 1794.00, "shippability": True, "availability": False})
create_node("nikon_d7500","Product", {"id": "nikon_d7500","title": "Nikon D7500 Kit 18-105mm VR'", "price": 1612.35, "shippability": True, "availability": True})

# Create the Relationship between Product and Category
create_relationship("canon_eos_6d", "IS_IN", "cameras")
create_relationship("nikon_d7500", "IS_IN", "cameras")

# Create Customers
create_node("joe","Customer", {"id": "joe","name": "Joe Baxton", "email": "joeee_baxton@example.com", "age":25})
create_node("daniel","Customer", {"id": "daniel","name": "Daniel Johnston", "email": "dan_j@example.com", "age":31})
create_node("alex","Customer", {"id": "alex","name": "Alex McGyver", "email": "mcgalex@example.com", "age":22})
create_node("alisson","Customer", {"id": "alisson","name": "Allison York", "email": "ally_york1@example.com", "age":24})

# Create the Relationship between Product and Category
create_relationship("joe", "VIEWED", "nikon_d7500", relationship_properties={"views_count": 15})
create_relationship("joe", "ADDED_TO_WISH_LIST", "iphone_8")
create_relationship("joe", "BOUGHT", "apple_macbook")

create_relationship("daniel", "VIEWED", "sony_xperia_z22", relationship_properties={"views_count": 10})
create_relationship("daniel", "VIEWED", "dell_inspiron_15", relationship_properties={"views_count": 20})
create_relationship("daniel", "ADDED_TO_WISH_LIST", "dell_inspiron_15")

create_relationship("alex", "VIEWED", "canon_eos_6d", relationship_properties={"views_count": 20})
create_relationship("alex", "ADDED_TO_WISH_LIST", "sony_xperia_xa1")
create_relationship("alex", "ADDED_TO_WISH_LIST", "nikon_d7500")
create_relationship("alex", "BOUGHT", "xioami_mi_mix_2")

create_relationship("alisson", "ADDED_TO_WISH_LIST", "acer_swift_3")
create_relationship("alisson", "ADDED_TO_WISH_LIST", "hp_pro_book")
create_relationship("alisson", "BOUGHT", "huawei_p8")
create_relationship("alisson", "BOUGHT", "sony_xperia_xa1")


# Close the database connection
driver.close()


