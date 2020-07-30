# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class SourceReportCard(object):
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
        "current_step": "int",
        "details": "ConnectionDetails",
        "steps": "list[ConnectionStep]",
        "type": "str",
    }

    attribute_map = {
        "current_step": "current_step",
        "details": "details",
        "steps": "steps",
        "type": "type",
    }

    def __init__(
        self,
        current_step=None,
        details=None,
        steps=None,
        type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SourceReportCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_step = None
        self._details = None
        self._steps = None
        self._type = None
        self.discriminator = None

        if current_step is not None:
            self.current_step = current_step
        if details is not None:
            self.details = details
        if steps is not None:
            self.steps = steps
        if type is not None:
            self.type = type

    @property
    def current_step(self):
        """Gets the current_step of this SourceReportCard.  # noqa: E501

        The index (in the steps array) of the current step needed to configure the data source.   # noqa: E501

        :return: The current_step of this SourceReportCard.  # noqa: E501
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step):
        """Sets the current_step of this SourceReportCard.

        The index (in the steps array) of the current step needed to configure the data source.   # noqa: E501

        :param current_step: The current_step of this SourceReportCard.  # noqa: E501
        :type: int
        """

        self._current_step = current_step

    @property
    def details(self):
        """Gets the details of this SourceReportCard.  # noqa: E501


        :return: The details of this SourceReportCard.  # noqa: E501
        :rtype: ConnectionDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SourceReportCard.


        :param details: The details of this SourceReportCard.  # noqa: E501
        :type: ConnectionDetails
        """

        self._details = details

    @property
    def steps(self):
        """Gets the steps of this SourceReportCard.  # noqa: E501

        A sequential list of Connection Step objects required to complete configuration for the connection type.   # noqa: E501

        :return: The steps of this SourceReportCard.  # noqa: E501
        :rtype: list[ConnectionStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this SourceReportCard.

        A sequential list of Connection Step objects required to complete configuration for the connection type.   # noqa: E501

        :param steps: The steps of this SourceReportCard.  # noqa: E501
        :type: list[ConnectionStep]
        """

        self._steps = steps

    @property
    def type(self):
        """Gets the type of this SourceReportCard.  # noqa: E501

        The connection type. Ex: platform.mysql or platform.hubspot   # noqa: E501

        :return: The type of this SourceReportCard.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceReportCard.

        The connection type. Ex: platform.mysql or platform.hubspot   # noqa: E501

        :param type: The type of this SourceReportCard.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SourceReportCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceReportCard):
            return True

        return self.to_dict() != other.to_dict()
