# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class Metadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'breadcrumb': 'list[str]',
        'metadata_object': 'MetadataObject'
    }

    attribute_map = {
        'breadcrumb': 'breadcrumb',
        'metadata_object': 'metadata-object'
    }

    def __init__(self, breadcrumb=None, metadata_object=None, local_vars_configuration=None):  # noqa: E501
        """Metadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._breadcrumb = None
        self._metadata_object = None
        self.discriminator = None

        if breadcrumb is not None:
            self.breadcrumb = breadcrumb
        if metadata_object is not None:
            self.metadata_object = metadata_object

    @property
    def breadcrumb(self):
        """Gets the breadcrumb of this Metadata.  # noqa: E501

        An array of strings describing a path into the schema. For example: A value of [] refers to the entire schema, or stream A value of [\"properties\", \"<FIELD_NAME>\"] refers to the properties.<FIELD_NAME> portion of the schema. For example: [\"properties\", \"id\"] would refer to a field named `id`   # noqa: E501

        :return: The breadcrumb of this Metadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._breadcrumb

    @breadcrumb.setter
    def breadcrumb(self, breadcrumb):
        """Sets the breadcrumb of this Metadata.

        An array of strings describing a path into the schema. For example: A value of [] refers to the entire schema, or stream A value of [\"properties\", \"<FIELD_NAME>\"] refers to the properties.<FIELD_NAME> portion of the schema. For example: [\"properties\", \"id\"] would refer to a field named `id`   # noqa: E501

        :param breadcrumb: The breadcrumb of this Metadata.  # noqa: E501
        :type: list[str]
        """

        self._breadcrumb = breadcrumb

    @property
    def metadata_object(self):
        """Gets the metadata_object of this Metadata.  # noqa: E501


        :return: The metadata_object of this Metadata.  # noqa: E501
        :rtype: MetadataObject
        """
        return self._metadata_object

    @metadata_object.setter
    def metadata_object(self, metadata_object):
        """Sets the metadata_object of this Metadata.


        :param metadata_object: The metadata_object of this Metadata.  # noqa: E501
        :type: MetadataObject
        """

        self._metadata_object = metadata_object

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Metadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Metadata):
            return True

        return self.to_dict() != other.to_dict()
