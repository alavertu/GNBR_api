import gzip
import shutil


concepts = ['entity', 'sentence']
relations = ['in_sentence', 'has_graph']
duplicated = {'concepts': set(), 'relations': set()}
entityfile_header = ['curie:ID','type:LABEL']
sentencefile_header = ['text:ID', 'pubmed_id']
relationfile_header = [':START',':END']
	
header = [

    'pubmed_id', 'loc', 'subj_tag', 'subj_loc', 'obj_tag', 'obj_loc', 'subj_txt', 'obj_txt', 
    'subj_id', 'obj_id', 'subj_type', 'obj_type', 'path', 'text'
]	


def filepath( filename ):
    return import_dir+'/'+filename    
if __name__ == '__main__':

    import_dir = os.path.expanduser( import_dir )
    print('Conditioning in directory '+import_dir )
    files = []
    for url in urls:
        txt = url.split('/')[-1]
        gz = txt.replace('.txt', '.gz')
        files.append((gz, txt))

    with gzip.open() as f_in, open() as entities, open() as in_sentence, open() as sentences, open() as has_path:
    	entities.write( '\t'.join(entityfile_header) + '\n' )
    	sentences.write( '\t'.join(sentencefile_header) + '\n' )
    	in_sentence.write('\t'.join(relationfile_header) + '\n')
    	has_path.write('\t'.join(relationfile_header) + '\n')
    	for line in f_in.readlines():
    		subj, obj, sentence = extract_concepts(line)
    		write_concept(subj, entities)
    		write_concept(obj, entities)
    		write_concept(sentence, sentencefile)

    		subj, obj, sentence = extract_relations(line)
    		write_relation(subj, in_sentence)
    		write_relation(obj, in_sentence)
    		write_relation(sentence, has_path)

def extract_concepts( line ):
	lines = line.split('\t')
	info = dict( zip(header, lines) )
	subj = tuple( info['subj_id'], info['subj_type'] )
	obj = tuple( info['obj_id'], info['obj_type'] )
	sentence = tuple( info['text'], info['pubmed_id'] )
	return subj, obj, sentence

def extract_relations( line ):
    lines = line.split('\t')
    info = dict( zip( header,  lines) )
    subj = tuple( info['subj_id'], info['text'] )
    obj = tuple( info['obj_id'], info['text'] )
    sentence = tuple( info['text'], info['path'] )
    return subj, obj, sentence

def write_concept( concept , conceptfile, tag ):
	if concept not in duplicated['concepts']:
		concept_out = '\t'.join(concept) + '\n'
		conceptfile.write(concept_out)

def write_relation( relation, relationfile ):
	if relation not in duplicated['relations']:
		relation_out = '\t'.join(relation) + '\n'
		relationfile.write(concept_out)

