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