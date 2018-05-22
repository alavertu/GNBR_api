import connexion
import six

from swagger_server.database import neo4j
from swagger_server.models.gnbr_edge import GnbrEdge  # noqa: E501
from swagger_server.models.gnbr_subgraph import GnbrSubgraph  # noqa: E501
from swagger_server.models.gnbr_association import GnbrAssociation
from swagger_server.models.id_mapping import IdMapping  # noqa: E501
from swagger_server import util


def get_edge(entity1, entity2):  # noqa: E501
    """Query for an edge

    Query for edges connecting two entities within GNBR # noqa: E501

    :param entity1: GNBR-ID for first entity
    :type entity1: str
    :param entity2: GNBR-ID for second entity
    :type entity2: str

    :rtype: GnbrEdge
    """
    q = """
    MATCH p=(m)--(n)
    WHERE m.id={entity1} AND n.id={entity2}
    RETURN relationships(p)
    LIMIT 1
    """

    results = neo4j.run(query=q, param={"entity1" : entity1,"entity2" : entity2})

    gnbr_edge = GNBR_edge()
    # do something with results[0]
    ######
    """
    Typical d in result would look like:
    {
      "first_entity_name_loc_char": "1428,1431",
      "a-.ind": 0,
      "first_entity_type": "Chemical",
      "o.ind": 0,
      "second_entity_name_raw": "Myc",
      "sentence_number": "9",
      "e+.ind": 0,
      "first_entity_name": "TSA",
      "dependency_path": "presence|nmod|START_ENTITY END_ENTITY|nmod|presence",
      "a+.ind": 0,
      "b": 164,
      "first_entity_name_raw": "TSA",
      "e": 639,
      "e+": 56,
      "k.ind": 0,
      "z.ind": 0,
      "b.ind": 0,
      "e-": 66,
      "a+": 47,
      "k": 536,
      "a-": 38,
      "second_entity_type": "Gene",
      "tax_id": "9606",
      "n": 100,
      "o": 154,
      "second_entity_name_loc_char": "1405,1408",
      "e-.ind": 0,
      "e.ind": 0,
      "sentence_tokenized": "TSA treatment induced a similar epidermal phenotype to activation of Myc , and activation of Myc in the presence of TSA resulted in massive stimulation of terminal differentiation .",
      "z": 18,
      "n.ind": 0,
      "PMID": "17712411",
      "second_entity_name": "Myc"
    }


    """
    return gnbr_edge
    # return 'do some magic!'


def get_identifier(searchString, limit=None):  # noqa: E501
    """Find GNBR identifier

    Searches entities within GNBR for a matching ID, based on input string # noqa: E501

    :param searchString: pass a search string to find matching identifiers
    :type searchString: str
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: IdMapping
    """

    ###### NOTE: THIS INFORMATION SHOULD PROBABLY BE FOUND USING THE PUBTATOR DICTIONARIES (SIMPLE LOOKUP) ########
    q = """
    MATCH (m)
    WHERE m.formatted contains {searchString}
    RETURN (m)
    LIMIT 25
    """
    results = neo4j.run(query=q, param={"searchString" : searchString})

    subgraph = GnbrSubgraph()
    for d in results:
        id_mapping = IdMapping()
        ## Add some subgraph!!!
        # TODO!!


    """
    example node output looks like:
    {
  "raw": "ace|acetylcholinesterase|acetylcholinesterase enzyme|ach-e|ache|ache-r|anti-acetylcholinesterase|as-ache|mache",
  "formatted": "ace|acetylcholinesterase|acetylcholinesterase_enzyme|ach-e|ache|ache-r|anti-acetylcholinesterase|as-ache|mache",
  "id": "11423"
    }

    """
    return subgraph



def get_node_neighbors(entity1):  # noqa: E501
    """Get all neighbors of a particular node

    Query node to get all nodes connected by at least one edge to the input node within GNBR # noqa: E501

    :param entity1: GNBR-ID for first entity
    :type entity1: str

    :rtype: GnbrSubgraph
    """
    q = """
    MATCH p=(n)--(m) 
    WHERE m.id = {entity1}
    RETURN relationships(p)
    LIMIT 25
    """


    results = neo4j.run(query=q, param={"entity1" : entity1})

    subgraph = GnbrSubgraph()
    for d in results:
        gnbr_edge = GNBR_edge()
        ## Add some subgraph!!!
        # TODO!!
    return subgraph


def get_subgraph(seedNodes):  # noqa: E501
    """Get a GNBR subgraph

    Query a list of nodes to get the GNBR subgraph induced by those nodes # noqa: E501

    :param seedNodes: gnbrIDs for subgraph
    :type seedNodes: List[str]

    :rtype: GnbrSubgraph
    """



    q = """
    MATCH (n) WHERE n.id IN {seedNodes}
    MATCH p=(n)--(m) 
    WHERE m.id IN  {seedNodes}
    RETURN relationships(p)
    LIMIT 25

    """


    results = neo4j.run(query=q, param={"seedNodes" : seedNodes})

    subgraph = GnbrSubgraph()
    for d in results:
        gnbr_edge = GNBR_edge()
        ## Add some subgraph!!!
        # TODO!!
    return subgraph


    # return 'do some magic!'
