import gzip
import sys
import numpy as np

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
        depDict[info[0]] = np.array(list(map(float,info[1:])))


# Create the output header for the themes
outThemeHeader = [x.lower().replace(" ", "_") for x in depDict["header"]][1:]

# Generate the output final output file as we iterate over the part-ii file
netOut = dict()
with gzip.open(depPathFile, "rt") as dpathIn:
    i = 0
    for line in dpathIn.readlines():
        info = line.strip().split("\t")
        # Omit entry if either entity is missing an identifier
        if info[8] == "null" or info[9] == "null":
            continue
        # GNBR uses ";" to mark unresolved entities, so we exclude these from our database`
        if ";" in info[8] or ";" in info[9]:
                continue
        # prepend ncbigene prefix to genes, for data provinence 
        if "gene" in themeFile:
            if "MESH:" not in info[8]:
                info[8] = "ncbigene:" + info[8]
            if "MESH:" not in info[9]:
                info[9] = "ncbigene:" + info[9]
        entity_pair = info[8] + "_" + info[9]
        dpKey = info[12].lower()
        if entity_pair in netOut:
            temp = netOut[entity_pair]
            netOut[entity_pair] = np.add(temp, depDict.get(dpKey))
        else:
            netOut[entity_pair] = depDict.get(dpKey)

# Write the final output to a file
with open(outFile, "w+") as outCsv:
    header = ["entity1", "entity2", "species"] + outThemeHeader
    outCsv.write(",".join(header)+ "\n")
    for key in netOut:
        info = key.split("_")
        # Check if gene study was done in another species, if so note the species
        if "(Tax:" in info[0]:
            temp = info[0].split("(")
            info[0] = temp[0]
            species = temp[1].strip("Tax:").strip(")")
        if "(Tax:" in info[1]:
            temp = info[1].split("(")
            info[1] = temp[0]
            species = temp[1].strip("Tax:").strip(")")   
        else:
            species = "9606"
        info = info + [species] + list(map(int, netOut.get(key).tolist()))
        # Write joined file values to file
        outCsv.write(",".join('"{0}"'.format(x) for x in info) + "\n")







