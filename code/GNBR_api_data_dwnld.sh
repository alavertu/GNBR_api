# Download GNBR theme data and entity mappings

wget https://zenodo.org/record/1134693/files/part-i-chemical-disease-path-theme-distributions.txt

wget https://zenodo.org/record/1134693/files/part-i-chemical-gene-path-theme-distributions.txt

wget https://zenodo.org/record/1134693/files/part-i-gene-disease-path-theme-distributions.txt

wget https://zenodo.org/record/1134693/files/part-i-gene-gene-path-theme-distributions.txt

wget https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt

wget https://zenodo.org/record/1134693/files/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt

wget https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt

wget https://zenodo.org/record/1134693/files/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt 


# Download CTD data

wget "https://catalystresearch.io/product_downloads?token=&productCode=ctd&fileURL=%2Freports%2FCTD_chemicals.csv.gz&referrer=&sourceURL=http%3A%2F%2Fctd.mdibl.org%2Fdownloads%2F&redirect=http%3A%2F%2Fctd.mdibl.org%2Freports%2FCTD_chemicals.csv.gz" -O CTD_chemicals.csv.gz

wget "https://catalystresearch.io/product_downloads?token=&productCode=ctd&fileURL=%2Freports%2FCTD_diseases.csv.gz&referrer=&sourceURL=http%3A%2F%2Fctd.mdibl.org%2Fdownloads%2F&redirect=http%3A%2F%2Fctd.mdibl.org%2Freports%2FCTD_diseases.csv.gz" -O CTD_diseases.csv.gz

# Download pubtator data for mapping raw strings back to their IDs
wget "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator/chemical2pubtator.gz" -O chemical2pubtator.gz

wget "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator/disease2pubtator.gz" -O disease2pubtator.gz

wget "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator/gene2pubtator.gz" -O gene2pubtator.gz
