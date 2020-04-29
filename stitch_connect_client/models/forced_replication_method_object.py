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


class ForcedReplicationMethodObject(object):
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
    openapi_types = {"reason": "str", "replication_method": "str"}

    attribute_map = {"reason": "reason", "replication_method": "replication-method"}

    def __init__(
        self, reason=None, replication_method=None, local_vars_configuration=None
    ):  # noqa: E501
        """ForcedReplicationMethodObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reason = None
        self._replication_method = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if replication_method is not None:
            self.replication_method = replication_method

    @property
    def reason(self):
        """Gets the reason of this ForcedReplicationMethodObject.  # noqa: E501

        The reason for the forced Replication Method  # noqa: E501

        :return: The reason of this ForcedReplicationMethodObject.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ForcedReplicationMethodObject.

        The reason for the forced Replication Method  # noqa: E501

        :param reason: The reason of this ForcedReplicationMethodObject.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def replication_method(self):
        """Gets the replication_method of this ForcedReplicationMethodObject.  # noqa: E501

        Indicates which Replication Method is required for the stream. Possible values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication.   # noqa: E501

        :return: The replication_method of this ForcedReplicationMethodObject.  # noqa: E501
        :rtype: str
        """
        return self._replication_method

    @replication_method.setter
    def replication_method(self, replication_method):
        """Sets the replication_method of this ForcedReplicationMethodObject.

        Indicates which Replication Method is required for the stream. Possible values are: FULL_TABLE - The stream is using Full Table Replication INCREMENTAL - The stream is using Key-based Incremental Replication LOG_BASED - The stream is using Log-based Incremental Replication.   # noqa: E501

        :param replication_method: The replication_method of this ForcedReplicationMethodObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["FULL_TABLE", "INCREMENTAL", "LOG_BASED"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and replication_method not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `replication_method` ({0}), must be one of {1}".format(  # noqa: E501
                    replication_method, allowed_values
                )
            )

        self._replication_method = replication_method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, ForcedReplicationMethodObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForcedReplicationMethodObject):
            return True

        return self.to_dict() != other.to_dict()
