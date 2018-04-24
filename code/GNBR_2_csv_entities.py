import gzip
import sys
import csv

# Check input and print usage if number of arguments is invalid
if len(sys.argv) != 3:
	print("Error: wrong number of arguments, check usage statement below:\n")
	print("USAGE: python GNBR_2_csv.py <path/to/part-ii-file> <path/to/outfile.csv>")
	exit()

def open_csv(name, delimiter=','):
    return csv.writer(open('{}'.format(name), 'w'), doublequote=True, delimiter=delimiter, escapechar='\\')

def get_fields(line, fields, header):
    extractor = dict( zip(header, line) )
    return [extractor[i] for i in fields]

# assign input files to their variables
# themeFile = sys.argv[1]
depPathFile = sys.argv[1]
# outHeaderFile = sys.argv[2]
outFile = sys.argv[2]


print('processing', sys.argv)
# Create a dictionary of the dependency paths (key) and their theme score vectors (value)
# depDict = dict()
# with gzip.open(themeFile, "rb") as themeIn:
#     depDict["header"] = themeIn.readline().decode('utf-8').strip().split("\t")
#     for line in themeIn.readlines():
#         info = line.decode('utf-8').strip().split("\t")
#         depDict[info[0]] = info[1:]

# # Create the output header for the themes
# outThemeHeader = [x.lower().replace(" ", "_") for x in depDict["header"]][1:]
out_header = ['curie:ID(Entity-ID)', 'name', ':LABEL']
# Create the output header for the dependency graph data
header = [
    "pmid", "loc", 
    "subj_name", "subj_loc", 
    "obj_name", "obj_loc",
    "subj_name_raw", "obj_name_raw", 
    "subj_id", "obj_id", 
    "subj_type", "obj_type", 
    "path", "text"
    ] #+ outThemeHeader
# outHeaderCSV = open_csv(outHeaderFile)
# outHeaderCSV.writerow(header)
# print('wrote', outHeaderFile)

# Generate the output final output file as we iterate of the part-ii file
outCSV = open_csv(outFile)
netOut = set()
outCSV.writerow(out_header)
with gzip.open(depPathFile, "rb") as dpathIn:
    i = 0
    for line in dpathIn.readlines():
        try:
            info = line.decode('utf-8').strip().split("\t")
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
            if "gene" in depPathFile:
                if "MESH:" not in info[8]:
                    info[8] = "ncbigene:" + info[8]
                if "MESH:" not in info[9]:
                    info[9] = "ncbigene:" + info[9]

            # Get theme vector for the dependency graph
            # dpKey = info[12].lower()
            # info = info + [species]
            # if dpKey in depDict:
            #     info = info + depDict.get(dpKey)
            # else:
            #     print("ERROR: MISSING ENTRY")

            # Write joined file values to file
            # outCSV.writerow(['"{0}"'.format(x) for x in info])

            subj_out = get_fields( info, ['subj_id', 'subj_name', 'subj_type'], header )
            if subj_out[0] not in netOut:
                outCSV.writerow( subj_out )
                netOut.add( subj_out[0] )

            obj_out = get_fields( info, ['obj_id', 'obj_name', 'obj_type'], header )
            if obj_out[0] not in netOut:
                outCSV.writerow( obj_out )
                netOut.add( obj_out[0] )
            # sentence_out = get_fields( info, ['text', 'pmid', 'loc'], header )
            # outCSV.writerow( info_out )
        except:
            print(':( ...', info)
            raise

print('wrote', outFile)