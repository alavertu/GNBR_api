#!/usr/bin/env python3


#### UNCOMMENT OUT WHEN RUNNING SERVER
# import connexion
# from swagger_server import encoder

import gzip
import shutil
import os
from collections import defaultdict

data_dir = os.path.abspath('../../../data')
print(data_dir)


def get_id_mappings(file_name, mentions2ID=None, ID2mentions=None):
	"""
	get the mention to ID (one-to-one) and ID to mention  (one to many) dictionaries 
	from putator data of genes, chemicals, and diseases
	INPUT: 
		file_name = .gz file from pubtator
		mentions2ID = (opt) one-to-one dictionary mapping mentions (str) to IDs (str) either MESH ID (for disease and chemical) or NCBI_gene for gene
		ID2mentions = (opt) one-to-many distory mapping ID (str) to mentions (list of str)
	OUPUT:
		mentions2ID - updated with file info
		ID2mentions 
	"""
	file = os.path.join(data_dir, file_name)
	if mentions2ID is None:
		mentions2ID = {} 
	if ID2mentions is None:
		ID2mentions = defaultdict(list)

	with gzip.open(file, 'rb') as f:
		headings = f.readline().decode('utf8')
		# print(headings) #PMID	meshID or NCBI_GENE	Mentions	Resource
		headings = headings.strip().split('\t')
		for i, line in enumerate(f):
			line_arr = line.decode('utf8').strip().split('\t')
			ID = line_arr[1]
			mentions_arr = line_arr[2].split("|")
			for mention in mentions_arr:
				mentions2ID[mention] = ID
				ID2mentions[ID].append(mention)

			# ####DEBUG
			# if i > 100:
			# 	break
	return mentions2ID, ID2mentions



def main():
	mentions2ID, ID2mentions = get_id_mappings('pubtator/disease2pubtator.gz')
	mentions2ID, ID2mentions = get_id_mappings('pubtator/gene2pubtator.gz', mentions2ID, ID2mentions)
	mentions2ID, ID2mentions = get_id_mappings('pubtator/chemical2pubtator.gz', mentions2ID, ID2mentions)

	# #### UNCOMMENT OUT WHEN RUNNING SERVER
	# app = connexion.App(__name__, specification_dir='./swagger/')
	# app.app.json_encoder = encoder.JSONEncoder
	# app.add_api('swagger.yaml', arguments={'title': 'GNBR'})
	# app.run(port=8080)


if __name__ == '__main__':
	main()
	