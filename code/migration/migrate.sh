# Process to set up GNBR neo4j instance
# PREREQUISITES
# Neo4j should be running in a docker instance.  

# Current directory should be in GNBR_api/code/stefano-neo4j-import

# Make neo4j directories.
mkdir -p ../../data/neo4j/import/ ../../data/neo4j/data/ ../../data/neo4j/logs/

# Generate concepts files.
python3 entities.py ../../data/GNBR/ ../../data/neo4j/import/entities.csv.gz 
python3 sentences.py ../../data/GNBR/ ../../data/neo4j/import/sentences.csv.gz 
python3 path.py ../../data/GNBR/ ../../data/neo4j/import/paths.csv.gz 

# Generate relationships files
python3 statements.py ../../data/GNBR/ ../../data/neo4j/import/statements.csv.gz 
python3 in_sentence.py ../../data/GNBR/ ../../data/neo4j/import/in_sentence.csv.gz 
python3 has_path.py ../../data/GNBR/ ../../data/neo4j/import/has_path.csv.gz 

# docker run --env=NEO4J_dbms.directories.import=/import --env=NEO4J_dbms_memory_heap_maxSize=5G --volume=$HOME/Documents/Github/GNBR_api/data/neo4j/import:/import --volume=$HOME/Documents/Github/GNBR_api/data/neo4j/data:/data neo4j:latest /var/lib/neo4j/bin/neo4j-admin import --nodes:Entity=/import/entities.csv --nodes:Sentence=/import/sentences.csv --nodes:Path=/import/paths_0.csv --nodes:Path=/import/paths_1.csv --nodes:Path=/import/paths_2.csv --nodes:Path=/import/paths_3.csv --relationships:IN_SENTENCE=/import/in_sentence.csv --relationships:HAS_PATH=/import/has_path.csv --relationships:STATEMENT=/import/statements_0.csv --relationships:STATEMENT=/import/statements_1.csv --relationships:STATEMENT=/import/statements_2.csv --relationships:STATEMENT=/import/statements_3.csv --database=graph.db

# Test import
#docker run --env=NEO4J_dbms.directories.import=/import --env=NEO4J_dbms_memory_heap_maxSize=5G --volume=$HOME/Documents/Github/GNBR_api/data/neo4j/import:/import --volume=$HOME/Documents/Github/GNBR_api/data/neo4j/data:/data neo4j:latest /var/lib/neo4j/bin/neo4j-admin import --nodes: /import/entities.csv --relationships:STATEMENT=/import/statements_0.csv --relationships:STATEMENT=/import/statements_1.csv --relationships:STATEMENT=/import/statements_2.csv --relationships:STATEMENT=/import/statements_3.csv --database=graph.db