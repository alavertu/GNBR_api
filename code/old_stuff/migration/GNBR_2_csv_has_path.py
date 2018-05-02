import time
import hashlib
import gzip
import sys
import csv
import os

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 3:
	print("Error: wrong number of arguments, check usage statement below:\n")
	print("USAGE: python GNBR_2_csv.py <path/to/part-ii-files> <path/to/outfile.csv>")
	exit()


# Define input and output headers
header = [
    "pmid", "loc", 
    "subj_name", "subj_loc", 
    "obj_name", "obj_loc",
    "subj_name_raw", "obj_name_raw", 
    "subj_id", "obj_id", 
    "subj_type", "obj_type", 
    "path", "text"
    ] 
out_header = [':START_ID(Sentence-ID)',':END_ID(Path-ID)']

# Handy subroutines
def filepath( filename ):
    return import_dir+'/'+filename 

def hash_md5(array):
    return hashlib.md5( ''.join(array).encode() ).hexdigest()

def open_csv(name, delimiter=','):
    return csv.writer(gzip.open('{}'.format(name), 'wt'), doublequote=True, delimiter=delimiter, escapechar='\\')

def get_fields(line, fields, header):
    extractor = dict( zip(header, line) )
    return [extractor[i] for i in fields]


# Get file info from arguments
import_dir = sys.argv[1]
depPathFiles = [f for f in os.listdir(import_dir) if '-ii-' in f]
outFile = sys.argv[2]

# Open output file and write header
start_time = time.time()
outCSV = open_csv(outFile)  
netOut = set()
outCSV.writerow(out_header)

# Loop over input files and stream output
for depPathFile in depPathFiles:
    print('processing', depPathFile)
    with gzip.open( filepath(depPathFile) , "rb" ) as dpathIn:
        for line in dpathIn.readlines():
            try:
                info = line.decode('utf-8').strip().split("\t")
                # Omit entry if either entity is missing an identifier
                if info[8] == "null" or info[9] == "null":
                    continue

                # Normalize path because different cases in part i and part ii
                info[-2] = info[-2].lower()
                path = info[-2]

                # Use md5 hashes of path|type1|type2 and sentence text as ids  
                types = sorted(get_fields(info, ['subj_type', 'obj_type'], header))
                path_id = hash_md5( get_fields(info, ['path'], header) + types )
                sentence_id = hash_md5( get_fields( info, ['text'], header ) )

                # Output sentence_id and path_id
                out = tuple( [sentence_id, path_id] )
                if out not in netOut:
                    outCSV.writerow(out)
                    netOut.add(out)
            except:
                print(':( ...', info)
                raise

    print("finished processing ", depPathFile, time.time() - start_time)

print('wrote', outFile)
