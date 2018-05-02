output_headers = {
	'concept': ['uri:ID(Entity-ID)', ':LABEL', 'name'],
	'sentence': [':ID(Sentence-ID)' , ':IGNORE', 'pmid', 'loc', 'text'],
	'predicate': [':ID(Path-ID)', ':LABEL'],
	'statement': [':START_ID(Entity-ID)', ':END_ID(Entity-ID)'],
	'in_sentence': [':START_ID(Entity-ID)', ':END_ID(Sentence-ID)', ':IGNORE', 'text'],
	'has_predicate': [':START_ID(Sentence-ID)', ':END_ID(Path-ID)', ':IGNORE', 'path'],
}

subj_id, subj_label, subj_props = ['subj_id'], ['subj_type'], ['subj_name']
obj_id, obj_label, obj_props = ['obj_id'], ['obj_type'], ['obj_name'] 
sentence_id, sentence_label, sentence_props = ['text'], ['pmid'], ['pmid', 'loc', 'text'] 
predicate_id, predicate_label, predicate_props = ['path'], ['subj_type', 'obj_type'], ['replace_w_part_i_header'] 

subj_in_sentence_props, obj_in_sentence_props = ['subj_name_raw'], ['obj_name_raw']
has_predicate_props = ['path']
statement_props = ['replace_w_part_i_header']


entity_files = ['concepts.csv.gz', 'sentences.csv.gz']
predicates_file = 'predicates.csv.gz'
relation_files = ['in_sentence.csv.gz', 'has_predicate.csv.gz']
statements_file = 'statements.csv.gz'

import_dir = '/Users/srensi/Documents/GitHub/GNBR_api/data/GNBR/'
export_dir = '/Users/srensi/Documents/GitHub/GNBR_api/data/neo4j/import/'

# concepts_header = ['uri:ID(Entity-ID)', ':LABEL', 'name']
# sentences_header = [':ID(Sentence-ID)' , ':IGNORE', 'pmid', 'loc', 'text']
# predicates_header = [':ID(Path-ID)', ':LABEL']

# statements_header = [':START_ID(Entity-ID)', ':END_ID(Entity-ID)', ':IGNORE']
# in_sentence_header = [':START_ID(Entity-ID)', ':END_ID(Sentence-ID)', ':IGNORE', 'text']
# has_predicate_header = [':START_ID(Sentence-ID)', ':END_ID(Path-ID)', ':IGNORE', 'path']

