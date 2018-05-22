// Find sentences relating a chemical, gene, and a disease
match p=(:Chemical)-[:IN_SENTENCE]-(s:Sentence),
(s)-[:IN_SENTENCE]-(:Gene),
(s)-[:IN_SENTENCE]-(:Disease) 
return s limit 25

// Find sentences that relate 2 chemicals and a disease
match p=(:Chemical)-[:IN_SENTENCE]-(s:Sentence),
(s)-[:IN_SENTENCE]-(:Chemical),
(s)-[:IN_SENTENCE]-(:Disease) 
return s limit 25


// Fanconi Anemia and TNFa, diseases
match p=(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence), 
(s)-[:IN_SENTENCE]-(g:Gene{uri: "ncbigene:21926"}) 
return p limit 25

// Find Diseases linked to FANCA
match p=(g:Gene{uri:"ncbigene:2175"})-[s:STATEMENT]-(:Disease) 
where s.u_ind >0 return p limit 25

match p=(g:Gene{uri:"ncbigene:2175"})-[s:STATEMENT]-(:Disease) 
where s.u_ind >1000 return p limit 25

match p=(g:Gene{uri:"ncbigene:2175"})-[s:STATEMENT]-(:Disease) 
return p limit 25

// Find Genes linked to FANCA by a disease
match p=(g:Gene{uri:"ncbigene:2175"})-[s:STATEMENT]-(:Disease)-[]-(:Gene) return p limit 25

// Return high confidence sentences about genes that regulate FANCA
match p=(:Gene{uri:"ncbigene:2175"})-[:IN_SENTENCE]-(s:Sentence)-[:HAS_PATH]-(t:`Gene|Gene`),
(s)-[:IN_SENTENCE]-(:Gene) 
where t.rg > 0 
return s,t order by t.rg desc limit 25


// Find causal or pathogenic genes linked to FA (Disease)
match p=(:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(g:Gene) 
where r.u_ind > 0 or r.ud_ind >0  or r.y_ind>0 or r.j_ind>0 
return distinct g

match p=(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence)-[:HAS_PATH]-(r:`Disease|Gene`),
(s)-[:IN_SENTENCE]-(g:Gene) 
where r.u_ind > 0 or r.ud_ind >0  or r.y_ind>0 or r.j_ind>0
return s, r.u order by r.u desc  

// Find top sentences linking procarbazine and FA
match p=(:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence)-[:HAS_PATH]-(r:`Chemical|Disease`),
(s)-[:IN_SENTENCE]-(c:Chemical{uri: "MESH:D003520"}) 
where r.t > 1000
return distinct s.text, r.t order by r.t desc

// Find all diseases treated by lasix with 
match p=(:Chemical{uri:"MESH:D005665"})-[:IN_SENTENCE]-(s:Sentence),
(s)-[:HAS_PATH]-(t:`Chemical|Disease`),
(s)-[:IN_SENTENCE]-(:Disease) where t.t > 1000 return p limit 25



// Find treatment cliques
match p=(d:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(g:Gene) 
where r.te > 1000 or r.d >1000    
with d,r,g
match (c:Chemical)-[s:STATEMENT]-(d),
(c)-[t:STATEMENT]-(g)
where s.t > 1000 or t.e > 1000
return c,g,d, s.t, t.e, r.te, r.d order by s.t + r.te + r.d desc


// Look for clique sentences
match p=(:Chemical{uri: "MESH:D003520"})-[:IN_SENTENCE]-(s:Sentence),
(:Gene{uri: "ncbigene:3569"})-[:IN_SENTENCE]-(s),
(:Disease{uri: "MESH:D005199"})-[:IN_SENTENCE]-(s)
return s

// Find chemical gene sentence
match p=(:Chemical{uri: "MESH:D003520"})-[:IN_SENTENCE]-(s:Sentence),
(:Gene{uri: "ncbigene:3569"})-[:IN_SENTENCE]-(s),
(s)-[:HAS_PATH]-(th:`Chemical|Gene`)
return s, th.e order by th.e desc

// Find Gene disease sentence
match p=(:Gene{uri: "ncbigene:3569"})-[:IN_SENTENCE]-(s),
(:Disease{uri: "MESH:D005199"})-[:IN_SENTENCE]-(s)
(s)-[:HAS_PATH]-(th:`Disease|Gene`)
return s, th.te order by th.te desc


// Collect node property values in a list
match(n)
return
    labels(n) as labels,
    keys(n) as properties,
    reduce(accumulator = [], key IN keys(n) | accumulator + n[key]) as values

// Most informative sentences
match 
(d:Disease{uri:"MESH:D005199"})-[:IN_SENTENCE]-(s:Sentence)
with distinct s
match (e:Entity)-[:IN_SENTENCE]-(s)
with 
distinct s, count(e) as ecount
match (s)-[:HAS_THEME]-(th:Theme)
return s.text, ecount,  reduce(accumulator = 0.0, key IN keys(th) | accumulator + th[key]) as values
order by ecount + log(values) desc limit 5

// Return entity count for sentences related to FA (sorted)
match p=(d:Disease{uri:"MESH:D005199"})-[r:IN_SENTENCE]-(s:Sentence)
with distinct s
match (s)-[:IN_SENTENCE]-(e:Entity)
return 
distinct s, count(e) as ecount order by ecount desc limit 10

// Return sentence count for entities related to FA
match p=(d:Disease{uri:"MESH:D005199"})-[r:IN_SENTENCE]-(s:Sentence),
(s)-[:IN_SENTENCE]-(e:Entity)
return 
distinct e, d, count(s) as scount order by scount desc limit 10

// get gini purity
match p=(d:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(e:Entity)
with e, d, r, reduce(accumulator = 0.0, key IN keys(r) | accumulator + r[key]) as sum
return 
distinct e, d, r, sum,
reduce(accumulator = 0.0, key IN keys(r) | accumulator + (r[key]/sum)^2) as gini
order by sum*gini desc limit 5

// Get sum of theme weights
match p=(d:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(e:Entity)
return 
distinct e, d, 
reduce(accumulator = 0, key IN keys(r) | accumulator + r[key]) as values 
order by values desc limit 5

// Compute frequencies 
match p=(d:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(e:Entity)
with e, d, r, reduce(accumulator = 0.0, key IN keys(r) | accumulator + r[key]) as sum
return 
distinct e, d, sum,
reduce(accumulator = [], key IN keys(r) | accumulator + (r[key]/sum)^2 as values
order by sum desc limit 5

// Get dependency path count for sentences with FA
match p=(d:Disease{uri:"MESH:D005199"})-[r:IN_SENTENCE]-(s:Sentence)
with distinct s
match (s)-[:HAS_PATH]-(th:Path)
return 
distinct s, count(th) as pcount order by pcount desc limit 10

// Get 10 oldest sentences mentioning FA
match (d:Document)-[:IN_DOCUMENT]-(s:Sentence),
(s)-[:IN_SENTENCE]-(:Disease{uri:"MESH:D005199"})
return s.text, d.year order by d.year limit 10

// Get disease for which FA causal genes have therapeutic effect
match p=(:Disease{uri:"MESH:D005199"})-[r:STATEMENT]-(g:Gene) 
where r.u_ind > 0 
with distinct g, r
match p=(d:Disease)-[s:STATEMENT]-(g)
where s.te_ind > 0
return g, d, r.u, s.te order by r.u*s.te desc limit 10

// Get most common string mentions
match (n:Chemical)
with n
match (n)-[r:IN_SENTENCE]-(:Sentence)
return distinct n.name, r.raw_string, count (r.raw_string) as num order by num desc limit 25