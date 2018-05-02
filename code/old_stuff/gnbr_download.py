#!/usr/bin/python3

urls=[
    # 'https://zenodo.org/record/1134693/files/part-i-chemical-disease-path-theme-distributions.txt',
    'https://zenodo.org/record/1134693/files/part-i-chemical-gene-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-i-gene-disease-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-i-gene-gene-path-theme-distributions.txt',
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt',
    'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt'
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt   ',
    # 'https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt'
]

import_dir = '~/neo4j/import'

from urllib.request import FancyURLopener
import os.path
import gzip
import shutil
import sys
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class CustomHeaderURLOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

url_opener = CustomHeaderURLOpener()

def filepath( filename ):
    return import_dir+'/'+filename    


if __name__ == '__main__':

    import_dir = os.path.expanduser( import_dir )

    os.system('mkdir -p %s' % import_dir )
    print('Downloading to directory: '+import_dir )

    files = []
    for url in urls:
        txt = url.split('/')[-1]
        gz = txt.replace('.txt', '.gz')
        files.append((url, gz, txt))

    for url, gz, txt in files:
        if os.path.isfile( filepath(gz) ) or os.path.isfile( filepath(txt) ):
            continue
        print('Downloading', txt, 'from', url)
        url_opener.retrieve( url, filepath(txt) )

    for url, gz, txt in files:
        if os.path.isfile( filepath(gz) ):
            continue
        print('Zipping', gz)
        with open( filepath(txt), 'rb') as f_in, gzip.open( filepath(gz), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)