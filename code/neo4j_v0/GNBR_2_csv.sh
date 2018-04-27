#!/bin/bash
python3 GNBR_2_csv_collapsed_depPath.py ~/data/GNBR/part-i-gene-disease-path-theme-distributions.txt.gz ~/data/GNBR/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt.gz ~/data/neo4j_for_import/gene-disease-neo4j-import.csv

python3 GNBR_2_csv_collapsed_depPath.py ~/data/GNBR/part-i-chemical-disease-path-theme-distributions.txt.gz ~/data/GNBR/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt.gz ~/data/neo4j_for_import/chemical-disease-neo4j-import.csv

python3 GNBR_2_csv_collapsed_depPath.py ~/data/GNBR/part-i-chemical-gene-path-theme-distributions.txt.gz ~/data/GNBR/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt.gz ~/data/neo4j_for_import/chemical-gene-neo4j-import.csv

python3 GNBR_2_csv_collapsed_depPath.py ~/data/GNBR/part-i-gene-gene-path-theme-distributions.txt.gz ~/data/GNBR/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt.gz ~/data/neo4j_for_import/gene-gene-neo4j-import.csv
