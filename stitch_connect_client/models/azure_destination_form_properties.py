# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class AzureDestinationFormProperties(object):
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
        "azure_storage_account_token": "str",
        "azure_storage_sas_url": "str",
        "database": "str",
    }

    attribute_map = {
        "azure_storage_account_token": "azure_storage_account_token",
        "azure_storage_sas_url": "azure_storage_sas_url",
        "database": "database",
    }

    def __init__(
        self,
        azure_storage_account_token=None,
        azure_storage_sas_url=None,
        database=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """AzureDestinationFormProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._azure_storage_account_token = None
        self._azure_storage_sas_url = None
        self._database = None
        self.discriminator = None

        if azure_storage_account_token is not None:
            self.azure_storage_account_token = azure_storage_account_token
        if azure_storage_sas_url is not None:
            self.azure_storage_sas_url = azure_storage_sas_url
        if database is not None:
            self.database = database

    @property
    def azure_storage_account_token(self):
        """Gets the azure_storage_account_token of this AzureDestinationFormProperties.  # noqa: E501

        An Azure Storage Access Key. This is used to access Azure Blob Storage, which Stitch uses to stage data for Polybase before loading it into an Azure SQL Data Warehouse destination.   # noqa: E501

        :return: The azure_storage_account_token of this AzureDestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._azure_storage_account_token

    @azure_storage_account_token.setter
    def azure_storage_account_token(self, azure_storage_account_token):
        """Sets the azure_storage_account_token of this AzureDestinationFormProperties.

        An Azure Storage Access Key. This is used to access Azure Blob Storage, which Stitch uses to stage data for Polybase before loading it into an Azure SQL Data Warehouse destination.   # noqa: E501

        :param azure_storage_account_token: The azure_storage_account_token of this AzureDestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._azure_storage_account_token = azure_storage_account_token

    @property
    def azure_storage_sas_url(self):
        """Gets the azure_storage_sas_url of this AzureDestinationFormProperties.  # noqa: E501

        An Azure Blob service Shared Access Signature (SAS) URL, which is used to grant Stitch restricted access to Azure Storage resources. These resources are used to load data into an Azure SQL Data Warehouse destination.   # noqa: E501

        :return: The azure_storage_sas_url of this AzureDestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._azure_storage_sas_url

    @azure_storage_sas_url.setter
    def azure_storage_sas_url(self, azure_storage_sas_url):
        """Sets the azure_storage_sas_url of this AzureDestinationFormProperties.

        An Azure Blob service Shared Access Signature (SAS) URL, which is used to grant Stitch restricted access to Azure Storage resources. These resources are used to load data into an Azure SQL Data Warehouse destination.   # noqa: E501

        :param azure_storage_sas_url: The azure_storage_sas_url of this AzureDestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._azure_storage_sas_url = azure_storage_sas_url

    @property
    def database(self):
        """Gets the database of this AzureDestinationFormProperties.  # noqa: E501

        The name of the logical database to connect to.   # noqa: E501

        :return: The database of this AzureDestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this AzureDestinationFormProperties.

        The name of the logical database to connect to.   # noqa: E501

        :param database: The database of this AzureDestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._database = database

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
        if not isinstance(other, AzureDestinationFormProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureDestinationFormProperties):
            return True

        return self.to_dict() != other.to_dict()
