# coding: utf-8

"""
    GNBR

    This API provides access to the relationships between entities in the global network of biomedical relationships (GNBR) derived from text  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: alavertu@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pprint
import re  # noqa: F401

import six


class GnbrEdge(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'edge_type': 'str',
        'edge_label': 'str',
        'edge_score': 'float',
        'sentence': 'str',
        'pubmed_id': 'str'
    }

    attribute_map = {
        'edge_type': 'edge_type',
        'edge_label': 'edge_label',
        'edge_score': 'edge_score',
        'sentence': 'sentence',
        'pubmed_id': 'pubmed_id'
    }

    def __init__(self, edge_type=None, edge_label=None, edge_score=None, sentence=None, pubmed_id=None):  # noqa: E501
        """GnbrEdge - a model defined in Swagger"""  # noqa: E501

        self._edge_type = None
        self._edge_label = None
        self._edge_score = None
        self._sentence = None
        self._pubmed_id = None
        self.discriminator = None

        self.edge_type = edge_type
        if edge_label is not None:
            self.edge_label = edge_label
        self.edge_score = edge_score
        self.sentence = sentence
        self.pubmed_id = pubmed_id

    @property
    def edge_type(self):
        """Gets the edge_type of this GnbrEdge.  # noqa: E501


        :return: The edge_type of this GnbrEdge.  # noqa: E501
        :rtype: str
        """
        return self._edge_type

    @edge_type.setter
    def edge_type(self, edge_type):
        """Sets the edge_type of this GnbrEdge.


        :param edge_type: The edge_type of this GnbrEdge.  # noqa: E501
        :type: str
        """
        if edge_type is None:
            raise ValueError("Invalid value for `edge_type`, must not be `None`")  # noqa: E501

        self._edge_type = edge_type

    @property
    def edge_label(self):
        """Gets the edge_label of this GnbrEdge.  # noqa: E501


        :return: The edge_label of this GnbrEdge.  # noqa: E501
        :rtype: str
        """
        return self._edge_label

    @edge_label.setter
    def edge_label(self, edge_label):
        """Sets the edge_label of this GnbrEdge.


        :param edge_label: The edge_label of this GnbrEdge.  # noqa: E501
        :type: str
        """

        self._edge_label = edge_label

    @property
    def edge_score(self):
        """Gets the edge_score of this GnbrEdge.  # noqa: E501


        :return: The edge_score of this GnbrEdge.  # noqa: E501
        :rtype: float
        """
        return self._edge_score

    @edge_score.setter
    def edge_score(self, edge_score):
        """Sets the edge_score of this GnbrEdge.


        :param edge_score: The edge_score of this GnbrEdge.  # noqa: E501
        :type: float
        """
        if edge_score is None:
            raise ValueError("Invalid value for `edge_score`, must not be `None`")  # noqa: E501

        self._edge_score = edge_score

    @property
    def sentence(self):
        """Gets the sentence of this GnbrEdge.  # noqa: E501


        :return: The sentence of this GnbrEdge.  # noqa: E501
        :rtype: str
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        """Sets the sentence of this GnbrEdge.


        :param sentence: The sentence of this GnbrEdge.  # noqa: E501
        :type: str
        """
        if sentence is None:
            raise ValueError("Invalid value for `sentence`, must not be `None`")  # noqa: E501

        self._sentence = sentence

    @property
    def pubmed_id(self):
        """Gets the pubmed_id of this GnbrEdge.  # noqa: E501


        :return: The pubmed_id of this GnbrEdge.  # noqa: E501
        :rtype: str
        """
        return self._pubmed_id

    @pubmed_id.setter
    def pubmed_id(self, pubmed_id):
        """Sets the pubmed_id of this GnbrEdge.


        :param pubmed_id: The pubmed_id of this GnbrEdge.  # noqa: E501
        :type: str
        """
        if pubmed_id is None:
            raise ValueError("Invalid value for `pubmed_id`, must not be `None`")  # noqa: E501

        self._pubmed_id = pubmed_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GnbrEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
