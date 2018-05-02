#!/usr/bin/python3

from urllib.request import FancyURLopener
from clean_gnbr_db import clean_file
import os
import gzip
import shutil
import sys
import re
import ssl

# Zenodo ssl gives FancyURLopener problems so disabled for download
ssl._create_default_https_context = ssl._create_unverified_context

class CustomHeaderURLOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

url_opener = CustomHeaderURLOpener()

def filepath( filename ):
    return import_dir+'/'+filename    

def download_gnbr(list_of_gnbr_urls, path_to_output_dir):
	import_dir = path_to_output_dir
	urls = list_of_gnbr_urls
	import_dir = os.path.expanduser( import_dir )

	os.system('mkdir -p %s' % import_dir )
	print('Downloading to directory: '+import_dir )

	files = []
	for url in urls:
	    txt = url.split('/')[-1]
	    csv = txt.replace('.txt', '.csv.gz')
	    gz = txt.replace('.txt', '.txt.gz')
	    files.append((url, gz, txt, csv))

	for url, gz, txt, csv in files:
		if os.path.isfile( filepath(gz) ) or os.path.isfile( filepath(txt) ) or os.path.isfile( filepath(csv) ):
		    continue
		print('Downloading', txt, 'from', url)
		url_opener.retrieve( url, filepath(txt) )

	# for url, gz, txt, csv in files:
	# 	if os.path.isfile( filepath(gz) ) or os.path.isfile( filepath(csv) ):
	# 	    continue
	# 	print('Zipping', gz)
	# 	with open( filepath(txt), 'r') as f_in, gzip.open( filepath(gz), 'wt') as f_out:
	# 	    shutil.copyfileobj(f_in, f_out)
	# 	os.remove( filepath(txt) )

	# for url, gz, txt, csv in files:
	# 	if os.path.isfile( filepath(csv) ):
	# 		continue
	# 	clean_file( filepath(gz) )
	# 	# os.remove( filepath(gz) )

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("Error: wrong number of arguments, check usage statement below:\n")
		print("USAGE: python gnbr_download <path/to/import-dir>")
		exit()

	import_dir = sys.argv[1]

	urls=[
	'https://zenodo.org/record/1134693/files/part-i-chemical-disease-path-theme-distributions.txt',
	'https://zenodo.org/record/1134693/files/part-i-chemical-gene-path-theme-distributions.txt',
	'https://zenodo.org/record/1134693/files/part-i-gene-disease-path-theme-distributions.txt',
	'https://zenodo.org/record/1134693/files/part-i-gene-gene-path-theme-distributions.txt',
	'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt',
	'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt',
	'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt   ',
	'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt'
	]

	download_gnbr(urls, import_dir)


