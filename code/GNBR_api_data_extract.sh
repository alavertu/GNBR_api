base_data="../data"

mkdir -p ${base_data}"/GNBR"
GNBR_dir=${base_data}"/GNBR"

mkdir -p ${base_data}"/GNBR_extracted"
GNBR_extracted_dir=${base_data}"/GNBR_extracted"


gunzip -c ${GNBR_dir}/part-i-chemical-disease-path-theme-distributions.txt.gz > ${GNBR_extracted_dir}/part-i-chemical-disease-path-theme-distributions.txt

gunzip -c ${GNBR_dir}/part-i-chemical-gene-path-theme-distributions.txt.gz > ${GNBR_extracted_dir}/part-i-chemical-gene-path-theme-distributions.txt

gunzip -c ${GNBR_dir}/part-i-gene-disease-path-theme-distributions.txt.gz > ${GNBR_extracted_dir}/part-i-gene-disease-path-theme-distributions.txt

gunzip -c ${GNBR_dir}/part-i-gene-gene-path-theme-distributions.txt.gz > ${GNBR_extracted_dir}/part-i-gene-gene-path-theme-distributions.txt

gunzip -c ${GNBR_dir}/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt.gz > ${GNBR_extracted_dir}/part-ii-dependency-paths-chemical-disease-sorted-with-themes.txt

gunzip -c ${GNBR_dir}/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt.gz > ${GNBR_extracted_dir}/part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt

gunzip -c ${GNBR_dir}/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt.gz > ${GNBR_extracted_dir}/part-ii-dependency-paths-gene-disease-sorted-with-themes.txt

gunzip -c ${GNBR_dir}/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt.gz > ${GNBR_extracted_dir}/part-ii-dependency-paths-gene-gene-sorted-with-themes.txt

