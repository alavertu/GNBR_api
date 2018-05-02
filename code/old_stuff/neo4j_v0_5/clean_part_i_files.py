# GNBR_clean_part_i_files.py
# Written: 04/26/18
# Last updated: 04/26/18
"""
This code parses and cleans the raw part-i files of the GNBR network.
"""

import gzip
import sys
import numpy as np
from gnbr_parse_utils import *

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Error: wrong number of arguments, check usage statement below:\n")
        print("USAGE: python GNBR_2_csv.py <path/to/part-i-file.txt.gz> <path/to/cleaned-outfile.csv.gz>")
        exit()

        if '-i-' in sys.argv[1]:
            clean_predicates( sys.argv[1], sys.argv[2] )

        elif '-ii-' in sys.arv[1]:
            clean_entities_and_sentences( sys.argv[1], sys.argv[2] )

# Check input and print usage if number of arguments is invalid
def clean_predicates(path_to_part_i_file, path_to_cleaned_out_file)
    # Assign input file paths to their variables
    themeFile = path_to_part_i_file
    outFile = path_to_cleaned_out_file

    # Open buffer to out csv file
    out_parti_CSV=open_csv(outFile)

    with open(themeFile, "r") as themeIn:

        # Extract raw header from the part-i file
        raw_header = themeIn.readline().strip().split("\t")
        
        # Reformat header for compliance with neo4j
        parti_header = ["path"] + [x.lower().replace(" ", "_").replace('.ind', '_ind') + ':float' for x in raw_header[1:]]

        # Write header to file
        out_parti_CSV.writerow(parti_header)
        
        for line in themeIn.readlines():
            info = line.strip().split("\t")
            out_parti_CSV.writerow(info)