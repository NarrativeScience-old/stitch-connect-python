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


class S3DestinationFormProperties(object):
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
        "csv_delimiter": "str",
        "output_file_format": "str",
        "s3_bucket": "str",
    }

    attribute_map = {
        "csv_delimiter": "csv_delimiter",
        "output_file_format": "output_file_format",
        "s3_bucket": "s3_bucket",
    }

    def __init__(
        self,
        csv_delimiter=None,
        output_file_format=None,
        s3_bucket=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """S3DestinationFormProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._csv_delimiter = None
        self._output_file_format = None
        self._s3_bucket = None
        self.discriminator = None

        if csv_delimiter is not None:
            self.csv_delimiter = csv_delimiter
        if output_file_format is not None:
            self.output_file_format = output_file_format
        if s3_bucket is not None:
            self.s3_bucket = s3_bucket

    @property
    def csv_delimiter(self):
        """Gets the csv_delimiter of this S3DestinationFormProperties.  # noqa: E501

        csv delimiter character  # noqa: E501

        :return: The csv_delimiter of this S3DestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._csv_delimiter

    @csv_delimiter.setter
    def csv_delimiter(self, csv_delimiter):
        """Sets the csv_delimiter of this S3DestinationFormProperties.

        csv delimiter character  # noqa: E501

        :param csv_delimiter: The csv_delimiter of this S3DestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._csv_delimiter = csv_delimiter

    @property
    def output_file_format(self):
        """Gets the output_file_format of this S3DestinationFormProperties.  # noqa: E501

        Defines the type of file Stitch will write to the bucket. Possible values are: - csv, which will use CSV (.csv) files - jsonl, which will use JSON (.jsonl) files   # noqa: E501

        :return: The output_file_format of this S3DestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._output_file_format

    @output_file_format.setter
    def output_file_format(self, output_file_format):
        """Sets the output_file_format of this S3DestinationFormProperties.

        Defines the type of file Stitch will write to the bucket. Possible values are: - csv, which will use CSV (.csv) files - jsonl, which will use JSON (.jsonl) files   # noqa: E501

        :param output_file_format: The output_file_format of this S3DestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._output_file_format = output_file_format

    @property
    def s3_bucket(self):
        """Gets the s3_bucket of this S3DestinationFormProperties.  # noqa: E501

        The name of the Amazon S3 bucket Stitch will write to.  # noqa: E501

        :return: The s3_bucket of this S3DestinationFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._s3_bucket

    @s3_bucket.setter
    def s3_bucket(self, s3_bucket):
        """Sets the s3_bucket of this S3DestinationFormProperties.

        The name of the Amazon S3 bucket Stitch will write to.  # noqa: E501

        :param s3_bucket: The s3_bucket of this S3DestinationFormProperties.  # noqa: E501
        :type: str
        """

        self._s3_bucket = s3_bucket

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
        if not isinstance(other, S3DestinationFormProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3DestinationFormProperties):
            return True

        return self.to_dict() != other.to_dict()
