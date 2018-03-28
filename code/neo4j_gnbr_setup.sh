# Process to set up GNBR neo4j instance
# PREREQUISITES
# neo4j should be installed in a directory at the same level as code/, the subdirectoris of neo4j/ must include bin/ and data/ etc

# current directory should be in GNBR_api/code

# RELATIONSHIP FILES
# add theme information (combine part-i and part-ii) and then save as csv formate (relationship csv files)
mkdir -p ../data/GNBR_processed
python GNBR_2_csv_neo4j.py ../data/GNBR/part-i-chemical-disease-path-theme-distributions.txt.gz ../data/GNBR/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt.gz ../data/GNBR_processed/chem_dis_rel_header.csv ../data/GNBR_processed/chem_dis_rel.csv
python GNBR_2_csv_neo4j.py ../data/GNBR/part-i-chemical-gene-path-theme-distributions.txt.gz ../data/GNBR/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt.gz ../data/GNBR_processed/chem_gene_rel_header.csv ../data/GNBR_processed/chem_gene_rel.csv
python GNBR_2_csv_neo4j.py ../data/GNBR/part-i-gene-disease-path-theme-distributions.txt.gz ../data/GNBR/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt.gz ../data/GNBR_processed/gene_dis_rel_header.csv ../data/GNBR_processed/gene_dis_rel.csv
python GNBR_2_csv_neo4j.py ../data/GNBR/part-i-gene-gene-path-theme-distributions.txt.gz ../data/GNBR/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt.gz ../data/GNBR_processed/gene_gene_rel_header.csv ../data/GNBR_processed/gene_gene_rel.csv
# preprocess_neo4j_gnbr_rel.py basically stores file paths and rewrites headers (a little redundant, but basically manual step)
python preprocess_neo4j_gnbr_rel.py 


# NODE FILES 
# create unique node files based on id, from the newly created rel files
python preprocess_neo4j_gnbr_nodes.py


# Directory to GNBR_api/
cd ..

# DATABASE CREATION
# create neo4j database
neo4j/bin/neo4j-admin import --nodes:Gene "data/GNBR_processed/genes.csv" --nodes:Chemical "data/GNBR_processed/chemicals.csv"  --nodes:Disease "data/GNBR_processed/diseases.csv" --relationships:CHEMICAL_DISEASE "data/GNBR_processed/chem_dis_rel_header.csv,data/GNBR_processed/chem_dis_rel.csv" --relationships:CHEMICAL_GENE "data/GNBR_processed/chem_gene_rel_header.csv,data/GNBR_processed/chem_gene_rel.csv" --relationships:GENE_DISEASE "data/GNBR_processed/gene_dis_rel_header.csv,data/GNBR_processed/gene_dis_rel.csv" --relationships:GENE_GENE "data/GNBR_processed/gene_gene_rel_header.csv,data/GNBR_processed/gene_gene_rel.csv" --ignore-missing-nodes True --array-delimiter "|" 


# # TESTING
# # start console
# neo4j/bin/neo4j console