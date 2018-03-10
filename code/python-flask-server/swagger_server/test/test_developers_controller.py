# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.gnbr_edge import GnbrEdge  # noqa: E501
from swagger_server.models.gnbr_subgraph import GnbrSubgraph  # noqa: E501
from swagger_server.models.id_mapping import IdMapping  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_get_edge(self):
        """Test case for get_edge

        Query for an edge
        """
        query_string = [('entity1', 'entity1_example'),
                        ('entity2', 'entity2_example')]
        response = self.client.open(
            '/NCATS_GNBR/GNBR_API/1.0.0/queryEdge',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_identifier(self):
        """Test case for get_identifier

        Find GNBR identifier
        """
        query_string = [('searchString', 'searchString_example'),
                        ('limit', 10)]
        response = self.client.open(
            '/NCATS_GNBR/GNBR_API/1.0.0/findEntity',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_node_neighbors(self):
        """Test case for get_node_neighbors

        Get all neighbors of a particular node
        """
        query_string = [('entity1', 'entity1_example')]
        response = self.client.open(
            '/NCATS_GNBR/GNBR_API/1.0.0/getNodeNeighbors',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_subgraph(self):
        """Test case for get_subgraph

        Get a GNBR subgraph
        """
        query_string = [('seedNodes', 'seedNodes_example')]
        response = self.client.open(
            '/NCATS_GNBR/GNBR_API/1.0.0/getInducedSubgraph',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
