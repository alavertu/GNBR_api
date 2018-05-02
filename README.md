## GNBR API

This directory contains code for creating the api for the Global Network of Biomedical Relationships derived from text (GNBR). The original data can be found here (https://zenodo.org/record/1134693#.WqQe1GbVSL9), this api was setup using version 3 of the resource.

## PREQUISITES
Install neo4j (https://neo4j.com/download/other-releases/#releases) OR

Install docker (https://docs.docker.com/install/)

TO setup the GNBR neo4j instance, follow through instructions in the `neo4j_gnbr_setup.sh` file, pay careful attention to directory structure. 

## Running with Docker

Use [Docker Compose](https://docs.docker.com/compose/) to build and run the application. Before using compose in the project, you should first copy the configuration file:

```
cp docker-compose.yaml-template docker-compose.yaml
```

The host machines `NEO4J_AUTH` environment variable is passed into the docker containers.  If it is not set then it will default to neo4j/password.  You can also directly modify the default password (plus Docker port redirections, etc.) in this 'docker-compose.yaml' file.  

Once ready to build, type the following into the terminal:

```
export NEO4J_AUTH=neo4j/<password>  # if you wish to change your default password
cd GNBR_api
docker-compose build
docker-compose up
```

> **Note:** If you don't wish to set a password, you can simply set NEO4J_AUTH=none. You can control which ports, if any at all, are exposed with the `docker-compose.yaml` file.

The Neo4j container's data, import, logs, and config directories will be mounted on the host machine at `$HOME/neo4j`. All the data in the database, including the username and password, will persist in the `$HOME/neo4j/data` directory over multiple runs of the container.

> **Note:** If the docker-compose commands are is giving you trouble, try running them as the system administrator with the `sudo` command. Remember, though, that if you are running  your commands as 'sudo', then depending on how your Linux instance configures sudo, in some cases, $HOME may actually be '/root' or it may otherwise still be in your normal user home. This may consequences for data importation (see below)

The Neo4j browser user interface at http://localhost:7474. You can open your browser with these addresses to see these applications in action. You wont see much until you load data into the database, though.

Before loading the data, you first turn off the docker container (from within the GNBR_api directory):



## Loading Data

This script must be run with version 3 of python, in the terminal run `python --version` to check your version. If you will not be using this script you will need to manually fix TSV headers in some of the data files.

```
cd GNBR_beacon/neo4j/
python3 ./download_gnbr.sh # if you don't already have data downloaded
python3 ./migrate.sh
```

Warning: The download script will create a directory in which to place the GNBR files.  Modify the variable `GNBR_DIR` to change the download location.  Similarly, the migrate scripts creates drirectories in which to stage the data for import (`$PATH_TO_NEO_DATA/import/`), store logs (`$PATH_TO_NEO_DATA/logs`), and place the neo4j database (`$PATH_TO_NEO_DATA/data`).  Also make sure that the location of the GNBR data stored in the `GNBR_DIR` variable matched that in the download script.  Edit the scripts to configure the file locations as you see fit.

To import that data into neo4j, enter the command into the terminal:
```
./docker_neo4j_import.sh
```
