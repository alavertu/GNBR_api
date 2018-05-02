import time
import gzip
import hashlib
import sys
import csv
import os

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 3:
	print("Error: wrong number of arguments, check usage statement below:\n")
	print("USAGE: python GNBR_2_csv.py <path/to/part-ii-files> <path/to/outfile.csv>")
	exit()

# Define input and output headers.
# header = [
#     "pmid", "loc", 
#     "subj_name", "subj_loc", 
#     "obj_name", "obj_loc",
#     "subj_name_raw", "obj_name_raw", 
#     "subj_id", "obj_id", 
#     "subj_type", "obj_type", 
#     "path", "text"
#     ] 

out_header = [':ID(Entity-ID)', ':LABEL', 'name']


# Handy subroutines
def filepath( filename ):
    return import_dir+'/'+filename 

def open_csv(name, delimiter=','):
    return csv.writer(open('{}'.format(name), 'w'), doublequote=True, delimiter=delimiter, escapechar='\\')

def get_csv(name, delimiter=','):
    return csv.DictReader(open('{}'.format(name), 'r'), doublequote=True, delimiter=delimiter, escapechar='\\')

def hash_md5(array):
    return hashlib.md5( ''.join(array).encode() ).hexdigest()

# Assign input files to their variables
import_dir = sys.argv[1]
depPathFiles = [f for f in os.listdir(import_dir) if '_ii_' in f]
outFile = sys.argv[2]

print('generating ', outFile)
# Generate the output final output file as we iterate of the part-ii file
start_time = time.time()
outCSV = open_csv(outFile)
netOut = set()
outCSV.writerow(out_header)
for depPathFile in depPathFiles:
    # with gzip.open( filepath(depPathFile) , "rb" ) as dpathIn:
    dpathIn = get_csv(filepath(depPathFile))
    # i = 0
    try:
        for line in dpathIn:
            pass
            # print(line['path'], line['text'])
            # info = line.decode('utf-8').strip().split("\t")
            # Output entity 1 info if not duplicate
            # subj_out = [line['subj_id'], line['subj_type'], line['subj_name']]
            # if subj_out[0] not in netOut:
            #     outCSV.writerow( subj_out )
            #     netOut.add( subj_out[0] )

            # # # Output entity 2 info if not duplicate
            # obj_out = [line['obj_id'], line['obj_type'], line['obj_name']]
            # if obj_out[0] not in netOut:
            #     outCSV.writerow( obj_out )
            #     netOut.add( obj_out[0] )
    except:
        print(line)
        # print(':( ...', info)
        raise

print("wrote  ", outFile, time.time() - start_time)