// Top 10 safe and effective drugs for treating FA
match p=(:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(c:Chemical) 
where r.t > 0
return distinct c.uri, c.name, sum(r.t) as eff, sum(r.sa) as safe 
order by 1.0*eff/(safe + 5) desc limit 5

// Look at safety and efficacy sentences for top drug (fludarabine)
match p=(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence)-[:HAS_THEME]-(r:`Chemical|Disease`),
(s)-[:IN_SENTENCE]-(c:Chemical{uri: "MESH:C024352"})
where r.t > 0
return distinct s.text as sentence, sum(r.t) as eff, sum(r.sa) as safe 
order by 1.0*eff/(safe + 5) desc
limit 3

// Safety and efficacy of oxymetholone
match p=(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence),
(c:Chemical{uri: "MESH:D010110"})-[:IN_SENTENCE]-(s),
(s)-[:HAS_THEME]-(r:`Chemical|Disease`)
return distinct 
s.text as sentence, 
sum(r.t) as eff, 
sum(r.sa) as safe 
order by 
1.0*eff/(safe + 5) desc
limit 5
	
// Top 10 safe and effective drugs in 2000
match 
(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence),
(c:Chemical)-[:IN_SENTENCE]-(s),
(d:Document)-[:IN_DOCUMENT]-(s),
(s)-[:HAS_THEME]-(r:`Chemical|Disease`)
where 
d.year < 2001
return distinct 
c.name as name, 
sum(r.t) as eff, 
sum(r.sa) as safe
order by 
1.0*eff/(safe + 5) desc
limit 5

// Top 10 safe and effective drugs in 1990
match 
(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence),
(c:Chemical)-[:IN_SENTENCE]-(s),
(d:Document)-[:IN_DOCUMENT]-(s),
(s)-[:HAS_THEME]-(r:`Chemical|Disease`)
where 
d.year < 1999
return distinct 
c.name as name, 
sum(r.t) as eff, 
sum(r.sa) as safe
order by 
1.0*eff/(safe + 5) desc
limit 5

// Collect string names
match (n:Chemical{uri:"MESH:D005665"})-[r:IN_SENTENCE]-(:Sentence)
return distinct r.raw_string, count (r.raw_string) as num order by num desc limit 5

// Aggregate over predicates for a sentence
match (s:Sentence)-[:HAS_THEME]-(r:`Chemical|Disease`)
where r.sa_ind > 0
return distinct s.text, sum(r.sa) as safe order by safe desc limit 10


// Ehlers Danlos Syndrome Genes
match (rxln1:Gene{uri:"ncbigene:6013"})-[r:STATEMENT]-(gene1:Gene)
with distinct rxln1, gene1,
reduce(accumulator = 0, key IN keys(r) | accumulator + r[key]) as values
with rxln1, gene1, sum(values) as score1
match (gene1)-[r:STATEMENT]-(gene2:Gene)
with distinct rxln1, score1, gene1, gene2, r,
reduce(accumulator = 0, key IN keys(r) | accumulator + r[key]) as values
return distinct gene1.uri, gene2.uri, 
r.b as binds, r.e as aff_expr, r.`e+` as expr_up, 
r.h as same_prot, r.i as inhibits, r.q as aff_prod, 
r.rg as regulates, r.`v+` as activates, r.w as incr_resp, 
score1, sum(values) as score2
order by score1*score2 desc


//
match (c:Chemical {uri: "MESH:C014289"}),(d:Disease {uri:"MESH:D005199"}),
p=shortestpath((c)-[:STATEMENT*..5]-(d))
return p


match (:Disease{uri:"MESH:D007593"})-[r:STATEMENT]-(g:Gene)
with distinct g,
reduce(accumulator = 0, key IN keys(r) | accumulator + r[key]) as values1
match (:Disease{uri:"MESH:C536196"})-[r:STATEMENT]-(g)
return distinct g, values1, 
reduce(accumulator = 0, key IN keys(r) | accumulator + r[key]) as values2
order by value1*values2 desc
