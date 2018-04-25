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

# Define input and output headers
out_header = [':ID(Sentence-ID)', 'pmid', 'location', 'text']

header = [
    "pmid", "loc", 
    "subj_name", "subj_loc", 
    "obj_name", "obj_loc",
    "subj_name_raw", "obj_name_raw", 
    "subj_id", "obj_id", 
    "subj_type", "obj_type", 
    "path", "text"
    ] 

# Handy subroutines
def filepath( filename ):
    return import_dir+'/'+filename 

def hash_md5(array):
    return hashlib.md5( ''.join(array).encode() ).hexdigest()

def open_csv(name, delimiter=','):
    return csv.writer(open('{}'.format(name), 'w'), doublequote=True, delimiter=delimiter, escapechar='\\')

def get_fields(line, fields, header):
    extractor = dict( zip(header, line) )
    return [extractor[i] for i in fields]

# Get file info from arguments
import_dir = sys.argv[1]
depPathFiles = [f for f in os.listdir(import_dir) if '-ii-' in f]
outFile = sys.argv[2]

# Generate the output final output file as we iterate of the part-ii file
start_time = time.time()
outCSV = open_csv(outFile)
netOut = set()
outCSV.writerow(out_header)
for depPathFile in depPathFiles:
    print('processing', depPathFile)
    with gzip.open( filepath(depPathFile) , "rb" ) as dpathIn:
        i = 0
        for line in dpathIn.readlines():
            try:
                info = line.decode('utf-8').strip().split("\t")
                # Omit entry if either entity is missing an identifier
                if info[8] == "null" or info[9] == "null":
                    continue
                sentence_id = hash_md5( get_fields( info, ['text'], header ) )
                sentence_info = get_fields( info, ['pmid', 'loc', 'text'], header )
                sentence_out = [sentence_id] + sentence_info
                if sentence_id not in netOut:
                    outCSV.writerow( sentence_out )
                    netOut.add( sentence_id )
                # outCSV.writerow( info_out )
            except:
                print(':( ...', info)
                raise

    print("finished processing ", depPathFile, time.time() - start_time)

print('wrote', outFile)