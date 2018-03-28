import json, sys, os, csv
from os.path import join
import shutil
import time


#################################################
############# DEFINE PATHS ######################
#################################################
DATA_DIR='../data/GNBR_extracted'

PROCESSED_DIR = '../data/GNBR_processed'
if not os.path.isdir(PROCESSED_DIR):
    os.mkdirs(PROCESSED_DIR)
print("data dir: ",DATA_DIR)
print("processed data dir: ",PROCESSED_DIR)

# note the header for each of these files is:
## pubmed_id   sentence_num    entity_a_formatted  entity_a_loc    entity_b_formatted  entity_b_loc    entity_a_raw    entity_b_raw    entity_a_id entity_b_id entity_a_type   entity_b_type   rel_path    rel_sentence

# chem_dis_file = join(DATA_DIR, 'part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt')
# chem_gene_file = join(DATA_DIR, 'part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt')
# gene_dis_file = join(DATA_DIR, 'part-ii-dependency-paths-gene-disease-sorted-with-themes.txt')
# gene_gene_file = join(DATA_DIR, 'part-ii-dependency-paths-gene-gene-sorted-with-themes.txt')
# test_file = join(DATA_DIR, 'part-ii-chem-gene-test.txt')


# use the newly extracted relationship files

chem_dis_file = join(PROCESSED_DIR, 'chem_dis_rel.csv')
chem_gene_file = join(PROCESSED_DIR, 'chem_gene_rel.csv')
gene_dis_file = join(PROCESSED_DIR, 'gene_dis_rel.csv')
gene_gene_file = join(PROCESSED_DIR, 'gene_gene_rel.csv')
test_file = join(PROCESSED_DIR, 'part-ii-chem-gene-test.txt')


# def clean(x):
#     #neo4j-import doesn't support: multiline (coming soon), quotes next to each other and escape quotes with '\""'
#     return x.replace('\n','').replace('\r','').replace('\\','').replace('"','')

#################################################
############# CREATING NODE FILES ###############
# Need to extract unique nodes from the gnbr files
# nodes = genes, chemicals, and diseases
#################################################

def open_csv(name, out_dir=PROCESSED_DIR, delimiter=','):
    return csv.writer(open('{}.csv'.format(name), 'w'), doublequote=True, delimiter=delimiter, escapechar='\\')


genes = open_csv(join(PROCESSED_DIR, 'genes'),delimiter=',')
diseases = open_csv(join(PROCESSED_DIR, 'diseases'),delimiter=',')
chemicals = open_csv(join(PROCESSED_DIR, 'chemicals'),delimiter=',')


genes.writerow([':ID(Gene)', 'raw', 'id',':LABEL'])
diseases.writerow([':ID(Disease)', 'raw', 'id',':LABEL'])
chemicals.writerow([':ID(Chemical)', 'raw', 'id',':LABEL'])


#################################################
############# CREATE NODE FILES #################
#################################################

genes_dict = {}
diseases_dict = {}
chemicals_dict = {}

def process_file(file, genes_dict, diseases_dict, chemicals_dict):
    # take in path to file and add the genes to the set 
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader((line.replace('\0','') for line in f), doublequote=True, escapechar='\\')
        for i, line_arr in enumerate(reader):
            # print(line)
            # # line = line.decode('utf-8')
            # line = line.strip()
            try:
                # line_arr = line.split(',')
                # print(line)
                pubmed_id, sentence_num, a_formatted, a_loc, b_formatted, b_loc, a_raw, b_raw, a_id, b_id, a_type, b_type, rel_path, rel_sentence = line_arr[:14]
                # print(a_formatted, a_raw, a_id, a_type)
                # pubmed_id, sentence_num, a_formatted, a_loc, b_formatted, b_loc, a_raw, b_raw, a_id, b_id, a_type, b_type, rel_path, rel_sentence = line.split('\t')
                if a_type == 'Gene':
                    genes_dict[a_formatted] = [a_formatted, a_raw, a_id, a_type]
                elif a_type == 'Disease':
                    diseases_dict[a_formatted] = [a_formatted, a_raw, a_id, a_type]
                elif a_type == 'Chemical':
                    chemicals_dict[a_formatted] = [a_formatted, a_raw, a_id, a_type]

                if b_type == 'Gene':
                    genes_dict[b_formatted] = [b_formatted, b_raw, b_id, b_type]
                elif b_type == 'Disease':
                    diseases_dict[b_formatted] = [b_formatted, b_raw, b_id, b_type]
                elif b_type == 'Chemical':
                    chemicals_dict[b_formatted] = [b_formatted, b_raw, b_id, b_type]

            except Exception as e:
                print('x',e)
                if i and i % 5000 == 0:
                    print('.',end='')
                if i and i % 1000000 == 0:
                    print(i)
            # #DEBUG
            # if i > 100:
            #     break
        return genes_dict, diseases_dict, chemicals_dict

start_time = time.time()
genes_dict, diseases_dict, chemicals_dict = process_file(chem_dis_file, genes_dict, diseases_dict, chemicals_dict)
print("finished processing ", chem_dis_file, time.time() - start_time)
genes_dict, diseases_dict, chemicals_dict = process_file(chem_gene_file, genes_dict, diseases_dict, chemicals_dict)
print("finished processing ", chem_gene_file, time.time() - start_time)
genes_dict, diseases_dict, chemicals_dict = process_file(gene_dis_file, genes_dict, diseases_dict, chemicals_dict)
print("finished processing ", gene_dis_file, time.time() - start_time)
genes_dict, diseases_dict, chemicals_dict = process_file(gene_gene_file, genes_dict, diseases_dict, chemicals_dict)
print("finished processing ", gene_gene_file, time.time() - start_time)
# genes_dict, diseases_dict, chemicals_dict = process_file(test_file, genes_dict, diseases_dict, chemicals_dict)

# writing [name, raw, idx, dtype]
print(len(genes_dict), 'unique genes')
for arr in genes_dict.values():
    genes.writerow(arr)
print(len(diseases_dict), 'unique diseases')
for arr in chemicals_dict.values():
    chemicals.writerow(arr)
print(len(chemicals_dict), 'unique chemicals')
for arr in diseases_dict.values():
    diseases.writerow(arr)

print('finished writing node files')
# #################################################
# ######## CREATE RELATIONSHIP HEADER FILES #######
# #RELATIONSHIP FILES USE THE ORIGINAL GNBR FILES # 
# #################################################
# chem_dis_rel_header = open_csv(join(PROCESSED_DIR,'chem_dis_rel_header'),delimiter='\t')
# # # chem_dis_rel = open_csv('chem_dis_rel')
# chem_gene_rel_header = open_csv(join(PROCESSED_DIR,'chem_gene_rel_header'), delimiter='\t')
# # # chem_gene_rel = open_csv('chem_gene_rel')
# gene_dis_rel_header = open_csv(join(PROCESSED_DIR,'gene_dis_rel_header'), delimiter='\t')
# # # gene_dis_rel = open_csv('gene_dis_rel')
# gene_gene_rel_header = open_csv(join(PROCESSED_DIR,'gene_gene_rel_header'), delimiter='\t')
# # # gene_gene_rel = open_csv('gene_gene_rel')

# chem_dis_rel_header.writerow(['pubmed_id', 'sentence_num', 'start_id:START_ID(Chemical)', ':IGNORE', ':END_ID(Disease)', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', 'path', 'sentence'])
# chem_gene_rel_header.writerow(['pubmed_id', 'sentence_num', 'start_id:START_ID(Chemical)', ':IGNORE', ':END_ID(Gene)', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', 'path', 'sentence'])
# gene_dis_rel_header.writerow(['pubmed_id', 'sentence_num', 'start_id:START_ID(Gene)', ':IGNORE', ':END_ID(Disease)', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', 'path', 'sentence'])
# gene_gene_rel_header.writerow(['pubmed_id', 'sentence_num', 'start_id:START_ID(Gene)', ':IGNORE', ':END_ID(Gene)', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', ':IGNORE', 'path', 'sentence'])
# # gene_dis_rel_header.writerow([':START_ID(Gene)', ':END_ID(Disease)'])
# # gene_gene_rel_header.writerow([':START_ID(Gene)', ':END_ID(Gene)'])



