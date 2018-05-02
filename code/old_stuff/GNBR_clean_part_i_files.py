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

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 3:
    print("Error: wrong number of arguments, check usage statement below:\n")
    print("USAGE: python GNBR_2_csv.py <path/to/part-i-file.txt> <path/to/cleaned-outfile.csv.gz>")
    exit()

# Assign input file paths to their variables
themeFile = sys.argv[1]
outFile = sys.argv[2]

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
