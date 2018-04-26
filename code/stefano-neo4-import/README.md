This directory contains scripts for processing GNBR files and conditioning data for neo4j command line import.  Each script generates a data file for concepts (entity, sentence, dependency path) and relations (E predicate E, E in_setence S, S has_path P). A more compact version of the database can be generated using only the the entities and predicates.

Note that the scripts currently loop over all part-i and part-ii files in the import directory.
