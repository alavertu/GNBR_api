# GNBR_clean_part_ii_files.py
# Written: 04/26/18
# Last updated: 04/26/18
"""
This code parses and cleans the raw part-ii files of the GNBR network.
"""

import gzip
import sys
import numpy as np
from gnbr_parse_utils import *

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 3:
	print("Error: wrong number of arguments, check usage statement below:\n")
	print("USAGE: python GNBR_2_csv.py <path/to/part-ii-file.gz> <path/to/cleaned-outfile.csv.gz>")
	exit()

# Assign input file paths to their variables
depPathFile = sys.argv[1]
outFile = sys.argv[2]

# Default file header for the part-ii files
part_ii_header = [
    "pmid", "loc", 
    "subj_name", "subj_loc", 
    "obj_name", "obj_loc",
    "subj_name_raw", "obj_name_raw", 
    "subj_id", "obj_id", 
    "subj_type", "obj_type", "species",
    "path", "text"
    ] 

# Open buffer to out csv file
out_partii_CSV=open_csv(outFile)

# Write header to file
out_partii_CSV.writerow(part_ii_header)

# Iterate over file lines and clean the data
with gzip.open(depPathFile, "rt") as dpathIn:
    for line in dpathIn.readlines():
        info = line.strip().split("\t")

        # Omit entry if either entity is missing an identifier
        if info[8] == "null" or info[9] == "null":
            continue

        # GNBR uses ";" to mark unresolved entities, so we exclude these from our cleaned data
        if ";" in info[8] or ";" in info[9]:
                continue

        if "gene" in depPathFile:
            # Prepend ncbigene prefix to genes, for data provinence 
            if "MESH:" not in info[8]:
                info[8] = "ncbigene:" + info[8]
            if "MESH:" not in info[9]:
                info[9] = "ncbigene:" + info[9]
            
            # Get species used in the study
            if "(Tax:" in info[9]:
                temp = info[9].split("(")
                info[9] = temp[0]
                species = temp[1].strip("Tax:").strip(")")

            if "(Tax:" in info[8]:
                temp = info[8].split("(")
                info[8] = temp[0]
                species = temp[1].strip("Tax:").strip(")")
                
            else:
                species = "9606"
        else:
            species = "9606"
        # Convert dependency paths to lowercase to make them consistent with part-i files
        info[12] = info[12].lower()

        # Add in species as separate column
        info = info[:13] + [species] + info[13:]

        # Write cleaned line to file
        out_partii_CSV.writerow(info)

