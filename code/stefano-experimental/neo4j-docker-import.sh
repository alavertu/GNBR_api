docker run \
	--env=NEO4J_dbms.directories.import=/import \
	--env=NEO4J_dbms_memory_heap_maxSize=5G \
	--volume=$HOME/neo4j/import:/import \
	--volume=$HOME/neo4j/data:/data neo4j:latest \
	/var/lib/neo4j/bin/neo4j-admin \
		import --nodes:Path \
		/import/part-i-chemical-gene-path-theme-distributions-fixed.txt \
		--nodes "/import/entities.txt" \
		--nodes:Sentence "/import/headers2.txt,/import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" \
		--relationships:IN_SENTENCE "/import/headers3.txt,/import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" \
		--relationships:HAS_TREE "/import/headers4.txt,/import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" \
		--delimiter='TAB' --database=graph.db \
		--ignore-duplicate-nodes=true \
		--ignore-missing-nodes=true --max-memory=16G
