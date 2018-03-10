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

from swagger_client.models.gnbr_edge import GnbrEdge  # noqa: F401,E501


class GnbrAssociation(object):
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
        'subject_id': 'str',
        'object_id': 'str',
        'association_score': 'float',
        'associations': 'list[GnbrEdge]'
    }

    attribute_map = {
        'subject_id': 'subject_id',
        'object_id': 'object_id',
        'association_score': 'association_score',
        'associations': 'associations'
    }

    def __init__(self, subject_id=None, object_id=None, association_score=None, associations=None):  # noqa: E501
        """GnbrAssociation - a model defined in Swagger"""  # noqa: E501

        self._subject_id = None
        self._object_id = None
        self._association_score = None
        self._associations = None
        self.discriminator = None

        self.subject_id = subject_id
        self.object_id = object_id
        self.association_score = association_score
        self.associations = associations

    @property
    def subject_id(self):
        """Gets the subject_id of this GnbrAssociation.  # noqa: E501


        :return: The subject_id of this GnbrAssociation.  # noqa: E501
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this GnbrAssociation.


        :param subject_id: The subject_id of this GnbrAssociation.  # noqa: E501
        :type: str
        """
        if subject_id is None:
            raise ValueError("Invalid value for `subject_id`, must not be `None`")  # noqa: E501

        self._subject_id = subject_id

    @property
    def object_id(self):
        """Gets the object_id of this GnbrAssociation.  # noqa: E501


        :return: The object_id of this GnbrAssociation.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this GnbrAssociation.


        :param object_id: The object_id of this GnbrAssociation.  # noqa: E501
        :type: str
        """
        if object_id is None:
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    @property
    def association_score(self):
        """Gets the association_score of this GnbrAssociation.  # noqa: E501


        :return: The association_score of this GnbrAssociation.  # noqa: E501
        :rtype: float
        """
        return self._association_score

    @association_score.setter
    def association_score(self, association_score):
        """Sets the association_score of this GnbrAssociation.


        :param association_score: The association_score of this GnbrAssociation.  # noqa: E501
        :type: float
        """
        if association_score is None:
            raise ValueError("Invalid value for `association_score`, must not be `None`")  # noqa: E501

        self._association_score = association_score

    @property
    def associations(self):
        """Gets the associations of this GnbrAssociation.  # noqa: E501


        :return: The associations of this GnbrAssociation.  # noqa: E501
        :rtype: list[GnbrEdge]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this GnbrAssociation.


        :param associations: The associations of this GnbrAssociation.  # noqa: E501
        :type: list[GnbrEdge]
        """
        if associations is None:
            raise ValueError("Invalid value for `associations`, must not be `None`")  # noqa: E501

        self._associations = associations

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
        if not isinstance(other, GnbrAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
