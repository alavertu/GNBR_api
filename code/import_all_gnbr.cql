// enforce uniqueness for curies //

CREATE CONSTRAINT ON (disease:Disease) ASSERT disease.id IS UNIQUE;
CREATE CONSTRAINT ON (chem:Chemical) ASSERT chem.id IS UNIQUE;
CREATE CONSTRAINT ON (gene:Gene) ASSERT gene.id IS UNIQUE;

// Chemical-Disease Imports //

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "file:///chem-disease-neo4j-import.csv" AS line
MERGE (c:Chemical {id: line.entity1})
MERGE (d:Disease {id: line.entity2})
MERGE (c)-[:treats {score: line.t, flag: line.`t.ind`}]->(d)
MERGE (c)-[:inhibits {score: line.c, flag: line.`c.ind`}]->(d)
MERGE (c)-[:has_side_effect {score: line.sa, flag: line.`sa.ind`}]->(d)
MERGE (c)-[:prevents {score: line.pr, flag: line.`pr.ind`}]->(d)
MERGE (c)-[:alleviates {score: line.pa, flag: line.`pa.ind`}]->(d)
MERGE (c)-[:pathogenic {score: line.j, flag: line.`j.ind`}]->(d)
MERGE (c)<-[:biomarker {score: line.mp, flag: line.`mp.ind`}]-(d)

// Chemical-Gene Imports //

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "file:///chem-gene-neo4j-import.csv" AS line
MERGE (c:Chemical {id: line.entity1})
MERGE (g:Gene {id: line.entity2})
MERGE (c)-[:agonist {score: line.`a+`, flag: line.`a+.ind`}]->(g)
MERGE (c)-[:antagonist {score: line.`a-`, flag: line.`a-.ind`}]->(g)
MERGE (c)-[:binds {score: line.b, flag: line.`b.ind`}]->(g)
MERGE (c)-[:increase_expr {score: line.`e+`, flag: line.`e+.ind`}]->(g)
MERGE (c)-[:decrease_expr {score: line.`e-`, flag: line.`e-.ind`}]->(g)
MERGE (c)-[:inhibits {score: line.n, flag: line.`n.ind`}]->(g)
MERGE (c)<-[:transports {score: line.o, flag: line.`o.ind`}]-(g)
MERGE (c)<-[:metabolizes {score: line.k, flag: line.`k.ind`}]-(g)
MERGE (c)<-[:enzyme_act {score: line.z, flag: line.`z.ind`}]-(g)

// Gene-Disease Imports //

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "file:///gene-disease-neo4j-import.csv" AS line
MERGE (g:Gene {id: line.entity1})
MERGE (d:Disease {id: line.entity2})
MERGE (g)-[:causes {score: line.u, flag: line.`u.ind`}]->(d)
MERGE (g)-[:affects {score: line.ud, flag: line.`ud.ind`}]->(d)
MERGE (g)-[:drug_target {score: line.d, flag: line.`d.ind`}]->(d)
MERGE (g)-[:pathogenic {score: line.j, flag: line.`j.ind`}]->(d)
MERGE (g)-[:therapeutic {score: line.te, flag: line.`te.ind`}]->(d)
MERGE (g)-[:risk {score: line.y, flag: line.`y.ind`}]->(d)
MERGE (g)-[:progression {score: line.g, flag: line.`g.ind`}]->(d)
MERGE (g)<-[:biomarker {score: line.md, flag: line.`md.ind`}]-(d)
MERGE (g)<-[:overexpession {score: line.x, flag: line.`x.ind`}]-(d)
MERGE (g)<-[:misregulation {score: line.l, flag: line.`l.ind`}]-(d)

// Gene-Gene Imports //

USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM "file:///gene-gene-neo4j-import.csv" AS line
MERGE (c:Gene {id: line.entity1})
MERGE (g:Gene {id: line.entity2})

MERGE (c)-[:binds {score: line.b, flag: line.`b.ind`}]->(g)
MERGE (c)-[:increases_resp {score: line.w, flag: line.`w.ind`}]->(g)
MERGE (c)-[:activates {score: line.`v+`, flag: line.`v+.ind`}]->(g)
MERGE (c)-[:increases_expr {score: line.`e+`, flag: line.`e+.ind`}]->(g)
MERGE (c)-[:affects {score: line.e, flag: line.`e.ind`}]->(g)
MERGE (c)-[:signals {score: line.i, flag: line.`i.ind`}]->(g)
MERGE (c)-[:same_as {score: line.h, flag: line.`h.ind`}]->(g)
MERGE (c)<-[:regulates {score: line.rg, flag: line.`rg.ind`}]->(g)
MERGE (c)<-[:produces {score: line.q, flag: line.`q.ind`}]->(g)
