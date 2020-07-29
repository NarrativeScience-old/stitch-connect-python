# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from stitch_connect_client.configuration import Configuration


class MixpanelSourceFormProperties(object):
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
        "anchor_time": "str",
        "api_secret": "str",
        "attribution_window": "str",
        "cron_expression": "str",
        "date_window_size": "str",
        "frequency_in_minutes": "str",
        "project_timezone": "str",
        "select_properties_by_default": "str",
        "start_date": "str",
    }

    attribute_map = {
        "anchor_time": "anchor_time",
        "api_secret": "api_secret",
        "attribution_window": "attribution_window",
        "cron_expression": "cron_expression",
        "date_window_size": "date_window_size",
        "frequency_in_minutes": "frequency_in_minutes",
        "project_timezone": "project_timezone",
        "select_properties_by_default": "select_properties_by_default",
        "start_date": "start_date",
    }

    def __init__(
        self,
        anchor_time=None,
        api_secret=None,
        attribution_window=None,
        cron_expression=None,
        date_window_size=None,
        frequency_in_minutes=None,
        project_timezone=None,
        select_properties_by_default=None,
        start_date=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """MixpanelSourceFormProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anchor_time = None
        self._api_secret = None
        self._attribution_window = None
        self._cron_expression = None
        self._date_window_size = None
        self._frequency_in_minutes = None
        self._project_timezone = None
        self._select_properties_by_default = None
        self._start_date = None
        self.discriminator = None

        if anchor_time is not None:
            self.anchor_time = anchor_time
        self.api_secret = api_secret
        self.attribution_window = attribution_window
        if cron_expression is not None:
            self.cron_expression = cron_expression
        self.date_window_size = date_window_size
        if frequency_in_minutes is not None:
            self.frequency_in_minutes = frequency_in_minutes
        self.project_timezone = project_timezone
        if select_properties_by_default is not None:
            self.select_properties_by_default = select_properties_by_default
        self.start_date = start_date

    @property
    def anchor_time(self):
        """Gets the anchor_time of this MixpanelSourceFormProperties.  # noqa: E501

        Defines the time that frequency_in_minutes is \"anchored\" to, which Stitch will use to create the integration's replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.   # noqa: E501

        :return: The anchor_time of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._anchor_time

    @anchor_time.setter
    def anchor_time(self, anchor_time):
        """Sets the anchor_time of this MixpanelSourceFormProperties.

        Defines the time that frequency_in_minutes is \"anchored\" to, which Stitch will use to create the integration's replication schedule. In Stitch, this is referred to as Anchor Scheduling. This field must contain an ISO 8601-compliant date. Note: When Stitch stores this value, it will be in UTC. You should provide this value in UTC to ensure the desired anchor time is retained. For example: You want to create a schedule that is anchored to 1:00PM EST and runs every 6 hours (360 minutes). To do this, you can set anchor_time to something like 2018-04-30T17:00:00Z and frequency_in_minutes to 360. This means jobs would run at 23:00:00, 05:00:00, 11:00:00, and so on.   # noqa: E501

        :param anchor_time: The anchor_time of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """

        self._anchor_time = anchor_time

    @property
    def api_secret(self):
        """Gets the api_secret of this MixpanelSourceFormProperties.  # noqa: E501

        The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.   # noqa: E501

        :return: The api_secret of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this MixpanelSourceFormProperties.

        The API secret of your project in your Mixpanel account. Refer to the Mixpanel documentation for instructions on obtaining this information.   # noqa: E501

        :param api_secret: The api_secret of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and api_secret is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `api_secret`, must not be `None`"
            )  # noqa: E501

        self._api_secret = api_secret

    @property
    def attribution_window(self):
        """Gets the attribution_window of this MixpanelSourceFormProperties.  # noqa: E501

        Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel's default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.   # noqa: E501

        :return: The attribution_window of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._attribution_window

    @attribution_window.setter
    def attribution_window(self, attribution_window):
        """Sets the attribution_window of this MixpanelSourceFormProperties.

        Defines the number, in days, Stitch should use as an attribution window. To ensure your Mixpanel and Stitch settings align, we recommend using the same attribution window in Stitch that you use in Mixpanel. Mixpanel's default attribution window is five days (5). Refer to the Mixpanel documentation for more information about attribution windows for this integration.   # noqa: E501

        :param attribution_window: The attribution_window of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and attribution_window is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `attribution_window`, must not be `None`"
            )  # noqa: E501

        self._attribution_window = attribution_window

    @property
    def cron_expression(self):
        """Gets the cron_expression of this MixpanelSourceFormProperties.  # noqa: E501

        Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source's default frequency_in_minutes value (60).   # noqa: E501

        :return: The cron_expression of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this MixpanelSourceFormProperties.

        Note: Advanced Scheduling using Cron is not yet supported for this source. A value may be submitted for this property if the account is on an Enterprise plan, but Stitch will not use the expression submitted. A valid Quartz cron expression representing the replication schedule for the integration. Refer to the Advanced Scheduling documentation for more info. Note: If neither a cron_expression or frequency_in_minutes property is provided, Stitch will use the source's default frequency_in_minutes value (60).   # noqa: E501

        :param cron_expression: The cron_expression of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """

        self._cron_expression = cron_expression

    @property
    def date_window_size(self):
        """Gets the date_window_size of this MixpanelSourceFormProperties.  # noqa: E501

        Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.   # noqa: E501

        :return: The date_window_size of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._date_window_size

    @date_window_size.setter
    def date_window_size(self, date_window_size):
        """Sets the date_window_size of this MixpanelSourceFormProperties.

        Defines the number, in days, for a date looping window for the export, funnel, and revenue tables. Date looping will return records whose from_date and to_date fall between the number of days in the defined window size. Note: If your project has large volumes of events, you may want to set the number of days to 14, 7, or even to 1 or 2 days.   # noqa: E501

        :param date_window_size: The date_window_size of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and date_window_size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `date_window_size`, must not be `None`"
            )  # noqa: E501

        self._date_window_size = date_window_size

    @property
    def frequency_in_minutes(self):
        """Gets the frequency_in_minutes of this MixpanelSourceFormProperties.  # noqa: E501

        Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440   # noqa: E501

        :return: The frequency_in_minutes of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._frequency_in_minutes

    @frequency_in_minutes.setter
    def frequency_in_minutes(self, frequency_in_minutes):
        """Sets the frequency_in_minutes of this MixpanelSourceFormProperties.

        Defines how often, in minutes, Stitch should attempt to replicate data from Google Analytics. Accepted values are: - 30 - 60 - 360 - 720 - 1440   # noqa: E501

        :param frequency_in_minutes: The frequency_in_minutes of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """

        self._frequency_in_minutes = frequency_in_minutes

    @property
    def project_timezone(self):
        """Gets the project_timezone of this MixpanelSourceFormProperties.  # noqa: E501

        The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console   # noqa: E501

        :return: The project_timezone of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._project_timezone

    @project_timezone.setter
    def project_timezone(self, project_timezone):
        """Sets the project_timezone of this MixpanelSourceFormProperties.

        The timezone in which your date-time fields are stored for your project. You can find your project timezone in the project settings in the Mixpanel console   # noqa: E501

        :param project_timezone: The project_timezone of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and project_timezone is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project_timezone`, must not be `None`"
            )  # noqa: E501

        self._project_timezone = project_timezone

    @property
    def select_properties_by_default(self):
        """Gets the select_properties_by_default of this MixpanelSourceFormProperties.  # noqa: E501

        A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables' records. If set to false, new properties will be ignored.   # noqa: E501

        :return: The select_properties_by_default of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._select_properties_by_default

    @select_properties_by_default.setter
    def select_properties_by_default(self, select_properties_by_default):
        """Sets the select_properties_by_default of this MixpanelSourceFormProperties.

        A configuration parameter - the only accepted values are true and false. When set to true, this parameter captures new properties in the events and engage tables' records. If set to false, new properties will be ignored.   # noqa: E501

        :param select_properties_by_default: The select_properties_by_default of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """

        self._select_properties_by_default = select_properties_by_default

    @property
    def start_date(self):
        """Gets the start_date of this MixpanelSourceFormProperties.  # noqa: E501

        The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z   # noqa: E501

        :return: The start_date of this MixpanelSourceFormProperties.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this MixpanelSourceFormProperties.

        The date from which Stitch should begin replicating data from Salesforce. Data from this date forward will be replicated. This field must contain an ISO 8601-compliant date, and the timestamp must be midnight. For example: 2018-01-01T00:00:00Z   # noqa: E501

        :param start_date: The start_date of this MixpanelSourceFormProperties.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and start_date is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `start_date`, must not be `None`"
            )  # noqa: E501

        self._start_date = start_date

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
        if not isinstance(other, MixpanelSourceFormProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MixpanelSourceFormProperties):
            return True

        return self.to_dict() != other.to_dict()