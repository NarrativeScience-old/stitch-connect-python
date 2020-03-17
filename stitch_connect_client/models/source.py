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


class Source(object):
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
        "id": "int",
        "created_at": "str",
        "deleted_at": "str",
        "display_name": "str",
        "name": "str",
        "paused_at": "str",
        "properties": "SourceFormProperties",
        "report_card": "SourceReportCard",
        "stitch_client_id": "int",
        "system_paused_at": "str",
        "type": "str",
        "updated_at": "str",
    }

    attribute_map = {
        "id": "id",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "display_name": "display_name",
        "name": "name",
        "paused_at": "paused_at",
        "properties": "properties",
        "report_card": "report_card",
        "stitch_client_id": "stitch_client_id",
        "system_paused_at": "system_paused_at",
        "type": "type",
        "updated_at": "updated_at",
    }

    def __init__(
        self,
        id=None,
        created_at=None,
        deleted_at=None,
        display_name=None,
        name=None,
        paused_at=None,
        properties=None,
        report_card=None,
        stitch_client_id=None,
        system_paused_at=None,
        type=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._deleted_at = None
        self._display_name = None
        self._name = None
        self._paused_at = None
        self._properties = None
        self._report_card = None
        self._stitch_client_id = None
        self._system_paused_at = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name
        if paused_at is not None:
            self.paused_at = paused_at
        if properties is not None:
            self.properties = properties
        if report_card is not None:
            self.report_card = report_card
        if stitch_client_id is not None:
            self.stitch_client_id = stitch_client_id
        if system_paused_at is not None:
            self.system_paused_at = system_paused_at
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Source.  # noqa: E501

        The unique identifier for this source.  # noqa: E501

        :return: The id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Source.

        The unique identifier for this source.  # noqa: E501

        :param id: The id of this Source.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Source.  # noqa: E501

        The time at which the source object was created.  # noqa: E501

        :return: The created_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Source.

        The time at which the source object was created.  # noqa: E501

        :param created_at: The created_at of this Source.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Source.  # noqa: E501

        The time at which the source object was deleted.  # noqa: E501

        :return: The deleted_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Source.

        The time at which the source object was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this Source.  # noqa: E501
        :type: str
        """

        self._deleted_at = deleted_at

    @property
    def display_name(self):
        """Gets the display_name of this Source.  # noqa: E501

        The display name of the source connection.  # noqa: E501

        :return: The display_name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Source.

        The display name of the source connection.  # noqa: E501

        :param display_name: The display_name of this Source.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this Source.  # noqa: E501

        The name of the source connection, dynamically generated from `display_name`. The `name` corresponds to the destination schema name that the data from this source will be loaded into. Names must: - Contain only lowercase alphanumerics and underscores - Be unique within each Stitch client account   # noqa: E501

        :return: The name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Source.

        The name of the source connection, dynamically generated from `display_name`. The `name` corresponds to the destination schema name that the data from this source will be loaded into. Names must: - Contain only lowercase alphanumerics and underscores - Be unique within each Stitch client account   # noqa: E501

        :param name: The name of this Source.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def paused_at(self):
        """Gets the paused_at of this Source.  # noqa: E501

        If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be `null`.   # noqa: E501

        :return: The paused_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._paused_at

    @paused_at.setter
    def paused_at(self, paused_at):
        """Sets the paused_at of this Source.

        If the connection was paused by the user, the time the pause began. Otherwise, or if the connection is active, this will be `null`.   # noqa: E501

        :param paused_at: The paused_at of this Source.  # noqa: E501
        :type: str
        """

        self._paused_at = paused_at

    @property
    def properties(self):
        """Gets the properties of this Source.  # noqa: E501


        :return: The properties of this Source.  # noqa: E501
        :rtype: SourceFormProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Source.


        :param properties: The properties of this Source.  # noqa: E501
        :type: SourceFormProperties
        """

        self._properties = properties

    @property
    def report_card(self):
        """Gets the report_card of this Source.  # noqa: E501


        :return: The report_card of this Source.  # noqa: E501
        :rtype: SourceReportCard
        """
        return self._report_card

    @report_card.setter
    def report_card(self, report_card):
        """Sets the report_card of this Source.


        :param report_card: The report_card of this Source.  # noqa: E501
        :type: SourceReportCard
        """

        self._report_card = report_card

    @property
    def stitch_client_id(self):
        """Gets the stitch_client_id of this Source.  # noqa: E501

        The ID of the Stitch client account.  # noqa: E501

        :return: The stitch_client_id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._stitch_client_id

    @stitch_client_id.setter
    def stitch_client_id(self, stitch_client_id):
        """Sets the stitch_client_id of this Source.

        The ID of the Stitch client account.  # noqa: E501

        :param stitch_client_id: The stitch_client_id of this Source.  # noqa: E501
        :type: int
        """

        self._stitch_client_id = stitch_client_id

    @property
    def system_paused_at(self):
        """Gets the system_paused_at of this Source.  # noqa: E501

        If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null.   # noqa: E501

        :return: The system_paused_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._system_paused_at

    @system_paused_at.setter
    def system_paused_at(self, system_paused_at):
        """Sets the system_paused_at of this Source.

        If the connection was paused by the system, the time the pause began. Otherwise, or if the connection is active, this will be null.   # noqa: E501

        :param system_paused_at: The system_paused_at of this Source.  # noqa: E501
        :type: str
        """

        self._system_paused_at = system_paused_at

    @property
    def type(self):
        """Gets the type of this Source.  # noqa: E501

        The source type.  # noqa: E501

        :return: The type of this Source.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Source.

        The source type.  # noqa: E501

        :param type: The type of this Source.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Source.  # noqa: E501

        The time at which the object was last updated.  # noqa: E501

        :return: The updated_at of this Source.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Source.

        The time at which the object was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Source.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
