import gzip
import sys

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 4:
	print("Error: wrong number of arguments, check usage statement below:\n")
	print("USAGE: python GNBR_2_csv.py <path/to/part-i-file> <path/to/part-ii-file> <path/to/flattened-graph-outfile.csv>")
	exit()

# assign input files to their variables
themeFile = sys.argv[1]
depPathFile = sys.argv[2]
outFile = sys.argv[3]


# Create a dictionary of the dependency paths (key) and their theme score vectors (value)
depDict = dict()
with gzip.open(themeFile, "rt") as themeIn:
    depDict["header"] = themeIn.readline().strip().split("\t")
    for line in themeIn.readlines():
        info = line.strip().split("\t")
        depDict[info[0]] = info[1:]

# Create the output header for the themes
outThemeHeader = [x.lower().replace(" ", "_") for x in depDict["header"]][1:]

# Create the output header for the dependency graph data
header = ["PMID","sentence_number","first_entity_name",
          "first_entity_name_loc_char","second_entity_name","second_entity_name_loc_char",
          "first_entity_name_raw", "second_entity_name_raw","first_entity_db_id", "second_entity_db_id",
          "first_entity_type", "second_entity_type", "dependency_path","sentence_tokenized", "tax_id"] + outThemeHeader

# Generate the output final output file as we iterate of the part-ii file
netOut = dict()
with open(outFile, "w+") as outCsv:
    outCsv.write(",".join(header)+ "\n")
    with gzip.open(depPathFile, "rt") as dpathIn:
        i = 0
        for line in dpathIn.readlines():
            info = line.strip().split("\t")
            # Omit entry if either entity is missing an identifier
            if info[8] == "null" or info[9] == "null":
                continue

            # Strip tax id from genes and store separately
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

            # Get theme vector for the dependency graph
            dpKey = info[12].lower()
            info = info + [species]
            if dpKey in depDict:
                info = info + depDict.get(dpKey)
            else:
                print("ERROR: MISSING ENTRY")

            # Write joined file values to file
            outCsv.write(",".join('"{0}"'.format(x) for x in info) + "\n")







