import time
import gzip
import sys
import csv
import os
import config
import numpy as np
from models import Entity, Relation

class Statement(Relation):
    def __init__(self, enty1, enty2, props, header):
        super().__init__(enty1, enty2, props, header)
        self._data = dict()

    def update(self, line):
        uid = self.fetch_id(line)
        props = self.fetch_properties(line)
        if uid in self._data.keys():
            self._data[uid] = np.add( self._data[uid], props )#np.array(list(map(float, props))) )
        else:
            self._data[uid] = props #np.array(list(map(float, props)))

    def fetch_statements(self):
        return [ tuple(uid) + tuple(props) for uid, props in self._data.items() ]


def write_entity(entity, line, file):
    if not entity.duplicated(line):
        entity_out = entity.fetch_entity(line)
        file.writerow(entity_out)

def write_relation(relation, line, file):
    if not relation.duplicated(line):
        relation_out = relation.fetch_relation(line)
        file.writerow(relation_out)

# Handy subroutines
def in_path( filename ):
    return config.import_dir+filename 

def out_path( filename ):
    return config.export_dir+filename 

def open_out_csv(name, delimiter=','):
    return csv.writer(gzip.open('{}'.format(name), 'wt'), doublequote=True, delimiter=delimiter, escapechar='\\')

def open_in_csv(name, delimiter=','):
    return csv.reader(gzip.open('{}'.format(name), 'rt'), doublequote=True, delimiter=delimiter, escapechar='\\')


"""
Main program
"""
def format_db_files(part_i_files, part_ii_files):
    # print(part_ii_files)
    concept_out, sentence_out = [open_out_csv(out_path(filename)) for filename in config.entity_files]
    concept_out.writerow(config.output_headers['concept'])
    sentence_out.writerow(config.output_headers['sentence'])

    in_sentence_out, has_predicate_out = [open_out_csv(out_path(filename)) for filename in config.relation_files]
    in_sentence_out.writerow(config.output_headers['in_sentence'])
    has_predicate_out.writerow(config.output_headers['has_predicate'])

    i = 0
    for part_i_file, part_ii_file in zip( sorted(part_i_files, reverse=True), sorted(part_ii_files, reverse=True) ):
        print(part_i_file, part_ii_file)
        start_time = time.time()


        predicate_out = open_out_csv( out_path(config.predicates_file.replace('.csv','%i.csv'%i)) )
        statement_out = open_out_csv( out_path(config.statements_file.replace('.csv','%i.csv'%i)) )

        i = i + 1
        in_csv = open_in_csv( in_path(part_i_file) )
        part_i_header = next(in_csv)[1:]
        statements_header = config.output_headers['statement'] + part_i_header
        predicates_header = config.output_headers['predicate'] + part_i_header
        statement_out.writerow( statements_header )
        predicate_out.writerow( predicates_header )
        predicates = dict()
        for line in in_csv:
            predicates[line[0]] = np.array(list(map(float,line[1:])))
        print("finished processing ", part_i_file, time.time() - start_time)
    # Generate the output final output file as we iterate of the part-ii file
        in_csv = open_in_csv(in_path(part_ii_file)) 
        header = next(in_csv) + part_i_header

        # Instantiate entity parser objects for each entity type
        subj = Entity(
            ids=config.subj_id, labels=config.subj_label, props=config.subj_props, 
            header=header
            )
        obj = Entity(
            ids=config.obj_id, labels=config.obj_label, props=config.obj_props, 
            header=header)
        sentence = Entity(
            ids=config.sentence_id, labels=config.sentence_label, props=config.sentence_props, 
            header=header
            )
        predicate = Entity(
            ids=config.predicate_id, labels=config.predicate_label, props=part_i_header, 
            header=header
            )

        # Instantiate relationship(s) parser objects for each relationship type
        subj_in_sentence = Relation(
            enty1=subj, enty2=sentence, props=config.subj_in_sentence_props, 
            header=header
            )
        obj_in_sentence = Relation(
            enty1=obj, enty2=sentence, props=config.obj_in_sentence_props, 
            header=header
            )
        sentence_has_predicate = Relation(
            enty1=sentence, enty2=predicate, props=config.has_predicate_props, 
            header=header
            )
        statement = Statement(
            enty1=subj, enty2=obj, props=part_i_header, 
            header=header
            )
        print("started processing ", part_ii_file, time.time() - start_time)
        q = 0
        for line in in_csv:
            key = line[13]
            info = line + list(predicates[key])
            # statement.update(info)
            write_entity(subj, info, concept_out)
            write_entity(obj, info, concept_out)            
            # write_entity(sentence, info, sentence_out)
            # write_entity(predicate, info, predicate_out)
            # write_relation(subj_in_sentence, info, in_sentence_out)
            # write_relation(obj_in_sentence, info, in_sentence_out)
            # write_relation(sentence_has_predicate, info, has_predicate_out)
            q = q + 1

            if q%100000 == 0:
                print("%i loops "%q, time.time() - start_time)

        print("finished processing ", part_ii_file, time.time() - start_time)
        # for line in statement.fetch_statements():
            # statement_out.writerow(line)
        # print("finished loop ", time.time() - start_time)
        exit()

if __name__ == '__main__':
    # Check input and print usage if number of arguments is invalid
    if len(sys.argv) != 1:
        print("Error: wrong number of arguments, check usage statement below:\n")
        print("USAGE: python GNBR_2_csv.py")
        exit()
    # Assign input files to their variables
    part_i_files  = [f for f in os.listdir(config.import_dir) if '-i-' in f]
    part_ii_files = [f for f in os.listdir(config.import_dir) if '-ii-' in f]
    # print(part_ii_files)
    format_db_files(part_i_files, part_ii_files)
