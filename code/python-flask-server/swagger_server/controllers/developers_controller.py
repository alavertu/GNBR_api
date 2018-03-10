import connexion
import six

from swagger_server.models.gnbr_edge import GnbrEdge  # noqa: E501
from swagger_server.models.gnbr_subgraph import GnbrSubgraph  # noqa: E501
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
    return 'do some magic!'


def get_identifier(searchString, limit=None):  # noqa: E501
    """Find GNBR identifier

    Searches entities within GNBR for a matching ID, based on input string # noqa: E501

    :param searchString: pass a search string to find matching identifiers
    :type searchString: str
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: IdMapping
    """
    return 'do some magic!'


def get_node_neighbors(entity1):  # noqa: E501
    """Get all neighbors of a particular node

    Query node to get all nodes connected by at least one edge to the input node within GNBR # noqa: E501

    :param entity1: GNBR-ID for first entity
    :type entity1: str

    :rtype: GnbrSubgraph
    """
    return 'do some magic!'


def get_subgraph(seedNodes):  # noqa: E501
    """Get a GNBR subgraph

    Query a list of nodes to get the GNBR subgraph induced by those nodes # noqa: E501

    :param seedNodes: gnbrIDs for subgraph
    :type seedNodes: List[str]

    :rtype: GnbrSubgraph
    """
    return 'do some magic!'
