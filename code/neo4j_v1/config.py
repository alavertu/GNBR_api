part_ii_header = [
    "pmid", "loc", 
    "subj_name", "subj_loc", 
    "obj_name", "obj_loc",
    "subj_name_raw", "obj_name_raw", 
    "subj_id", "obj_id", 
    "subj_type", "obj_type", 
    "path", "text"
]

entities = { 
	header : [':ID(Entity-ID)', 'name', ':LABEL'],
	subj_fields : ['subj_id', 'subj_name', 'subj_type'],
	obj_fields : ['obj_id', 'obj_name', 'obj_type']
}

sentences = {
	header : [':ID(Sentence-ID)', 'pmid', 'loc', 'text'],
	id_fields : ['text']
}

predicates = {
	header : [':ID(Path-ID)', ':LABEL'],
	id_fields : ['path'],
	label_fields : ['subj_type', 'obj_type']
}

statements = {
	header : [":START_ID(Entity-ID)", ":END_ID(Entity-ID)"]
}

in_sentence = {
	header : [':START(Entity-ID)','raw_string', ':END(Sentence-ID)'],
	subj_id : ['subj_id', 'subj_name_raw'],
	obj_id : ['obj_id', 'obj_name_raw']
	sentence_id : ['text']
}

has_predicate = {
	header = [':START_ID(Sentence-ID)', 'path',':END_ID(Path-ID)'],
	predicate_type : ['subj_type', 'obj_type'],
	predicate_id : ['path'],
	sentence_id : ['text']
}