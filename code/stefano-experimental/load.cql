CREATE CONSTRAINT ON (entity:Entity) ASSERT entity.id IS UNIQUE;
CREATE CONSTRAINT ON (sentence:Sentence) ASSERT sentence.text IS UNIQUE;
CREATE CONSTRAINT ON (path:Path) ASSERT path.path IS UNIQUE;
CREATE INDEX ON :Entity(type);

// ---- Load Actions ---- //

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MERGE (e:Entity {id: row.subj_id})
ON CREATE SET e.type = row.subj_type;

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MERGE (f:Entity {id: row.obj_id})
ON CREATE SET f.type = row.obj_type;

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MERGE (p:Path {path: row.path});

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MERGE (s:Sentence {text:row.text})
ON CREATE SET s.pubmed_id = row.pubmed_id;

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MATCH (e:Entity {id: row.subj_id})
MATCH (s:Sentence {text: row.text})
MERGE (e)-[:ENTITY_IN]->(s);

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MATCH (f:Entity {id: row.obj_id})
MATCH (s:Sentence {text: row.text})
MERGE (f)-[:ENTITY_IN]->(s);

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "FILE:///import/part-ii-dependency-paths-chemical-gene-sorted-with-themes-fixed.txt" AS row FIELDTERMINATOR '\t'
MATCH (s:Sentence {text: row.text})
MATCH (p:Path {path: row.path})
MERGE (s)-[:HAS_PATH]->(p);