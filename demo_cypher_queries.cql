match p=(:Chemical)-[:IN_SENTENCE]-(s)-[:IN_SENTENCE]-(:Gene),(s)-[:IN_SENTENCE]-(:Disease) return s limit 25
# loc: 3  pmid: 21792892
match p=(:Chemical)-[:IN_SENTENCE]-(s:Sentence)-[:IN_SENTENCE]-(:Chemical),(s:Sentence)-[:IN_SENTENCE]-(:Disease) return s limit 25