# Installed postgres from conda channels
# postgres=9.6.6
conda activate gnbrAPI

-- #First run only
-- #conda install postgres=9.6.6

-- # For all purposes within this file, the working directory is
-- # the base directory of the GNBR_api repository

-- # First we need to initialize the database in an empty directory
-- mkdir data/database
-- initdb -D data/database/

-- # Start the server
pg_ctl -D data/database/ -l logfile start
-- 
-- # begin interaction session with the server
psql postgres

CREATE DATABASE gnbr_db;

\connect gnbr_db

CREATE TABLE chemical_gene(
	PMID serial NOT NULL,
	sentence_number numeric,
	first_entity_name varchar(500),
	first_entity_name_loc_char varchar(500), 
    second_entity_name varchar(500),
    second_entity_name_loc_char varchar(500),
    first_entity_name_raw varchar(500),
    second_entity_name_raw varchar(500),
    first_entity_db_id varchar(500),
    second_entity_db_id varchar(500),
    first_entity_type varchar(15),
    second_entity_type varchar(15),
    dependency_path varchar(5000),
    sentence_tokenized varchar(5000),
    tax_id varchar(15),
    a_plus numeric,
    a_plus_ind numeric,
    a_neg numeric,
    a_neg_ind numeric,
    b numeric,
    b_ind numeric,
    e_plus numeric,
    e_plus_ind numeric,
    e_neg numeric,
    e_neg_ind numeric,
    e numeric,
    e_ind numeric,
    n numeric,
    n_ind numeric,
    o numeric,
    o_ind numeric,
    k numeric,
    k_ind numeric,
    z numeric,
    z_ind numeric
);
COPY chemical_gene FROM '/Users/alavertu/Desktop/Lab/NCATS_consulting/GNBR_api/data/GNBR/flattened-chemical-gene-sorted-with-themes.csv' DELIMITER ',' CSV HEADER;

-- if you messed up
-- DROP TABLE chemical_gene;

-- # To kill the server
-- kill -INT `head -1 data/database/postmaster.pid`

-- # Run the data base constructor to process the raw GNBR data
-- # into a csv representation that we can load into mySQL

