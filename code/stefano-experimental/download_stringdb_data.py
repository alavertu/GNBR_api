#!/usr/bin/python3

urls=[
    # 'https://zenodo.org/record/1134693/files/part-i-chemical-disease-path-theme-distributions.txt',
    'https://zenodo.org/record/1134693/files/part-i-chemical-gene-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-i-gene-disease-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-i-gene-gene-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt',
    'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt'
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt   ',
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt'
]

part_ii_file_header = [
    'pubmed_id', 'loc', 'subj_tag', 'subj_loc', 'obj_tag', 'obj_loc', 'subj_txt', 'obj_txt', 
    'subj_id', 'obj_id', 'subj_type', 'obj_type', 'path', 'text'
]   

import_dir = '~/neo4j/import'

from urllib.request import FancyURLopener
import os.path
import gzip
import shutil
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class CustomHeaderURLOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

url_opener = CustomHeaderURLOpener()

def filepath( filename ):
    return import_dir+'/'+filename    

# def field_switcher(x):
#     return {'path':'path:ID'
#     }.get(x, x.replace('.ind','_ind') + ':float')

if __name__ == '__main__':

    import_dir = os.path.expanduser( import_dir )

    os.system('mkdir -p %s' % import_dir )
    print('Downloading to directory: '+import_dir )

    files = []
    for url in urls:
        txt = url.split('/')[-1]
        gz = txt.replace('.txt', '.gz')
        files.append((url, gz, txt))

    for url, gz, txt in files:
        if os.path.isfile( filepath(gz) ) or os.path.isfile( filepath(txt) ):
            continue
        print('Downloading', txt, 'from', url)
        url_opener.retrieve( url, filepath(txt) )

    for url, gz, txt in files:
        if os.path.isfile( filepath(gz) ):
            continue
        print('Zipping', gz)
        with open( filepath(txt), 'rb') as f_in, gzip.open( filepath(gz), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    for url, gz, txt in files:
        cleantxt = txt.replace('.txt', '-clean.gz')
        if os.path.isfile( filepath(cleantxt) ):
            continue
        print('Cleaning',gz)
        with gzip.open( filepath(gz), 'rt') as f_in, gzip.open( filepath(cleantxt), 'wt' ) as f_out:
            if '-i-' in txt:
                    header = f_in.readline()
                    fixed_header = header.replace('path', 'path:ID').replace('.ind', '_ind:float')
                    f_out.write(fixed_header)
                    f_in.seek(0)
                    for line in f_in.readlines()[1:]:
                        f_out.write(line)
            elif '-ii-' in txt:
                    f_out.write( '\t'.join(part_ii_file_header) + '\n' )
                    for line in f_in.readlines():
                        info = line.split('\t')
                        if info[8] == "null" or info[9] == "null":
                            continue
                        if ";" in info[8] or ";" in info[9]:
                            continue
                        f_out.write( re.sub(r'\(Tax:[^)]*\)', '', line) )


"""
Subroutines for cleaning files
"""



# def fix_part_i_header( header_line ):
#     fields = [i.strip() for i in header_line.split('\t')]
#     return = '\t'.join([header_fixer(field) for field in headers]) + '\n'

# def fix_part_i_line( line ):
#     lines = line.split('\t')
#     return lines[0] + '\t'.join( map(float,lines[1:]) ) + '\n'

                # subj, obj, sentence = extract_entities(line)
                # rels = extract_relations(line)
                # if 'null' in subj or 'null' in obj:
                #     continue
                # check_write(subj, duplicated, bfile)
                # check_write(obj, duplicated, bfile)
                # check_write(sentence, duplicated, sfile)
                # [check_write(i, relations, rfile) for i in rels]

                # if obj not in entities:
                #     h.write( '\t'.join(obj) + '\n' ) 
                #     entities.add(obj)
                # if sentence not in sentences:
                #     pass
                # if 


"""
Subroutines for cleaning files
"""

# def path_header(x):
#     return {'path':'path:ID'
#     }.get(x, x.replace('.ind','_ind') + ':float')

# def fix_part_i_header( header_line ):
#     headers = [i.strip() for i in header_line.split('\t')]
#     return = '\t'.join([path_header(i) for i in headers]) + '\n'

# def fix_line( line ):
#     lines = line.split('\t')
#     return lines[0] + '\t'.join( map(float,lines[1:]) ) + '\n'

# def extract_entities( line, header ):
#     lines = line.split('\t')
#     row = dict( zip( header,  lines) )
#     subj = tuple( row['subj_id'], row['subj_type'] )
#     obj = tuple( row['obj_id'], row['obj_type'] )
#     sentence = tuple( row['text'], row['pubmed_id'] )
#     return subj, obj, sentence

# def extract_relations( line, header):
#     lines = line.split('\t')
#     row = dict( zip( header,  lines) )
#     subj_sentence = tuple(row['subj_id'], row['text'])
#     obj_sentence = tuple(row['obj_id'], row['text'])
#     sentence_path = tuple(row['text'], row['path'])
#     return subj_sentence, obj_sentence, sentence_path

# def check_write( concept, dupes, filehandle ):
#     if concept not in dupes:
#         dupes.add(concept)
#         filehandle.write( '\t'.join(concept) + '\n' )


