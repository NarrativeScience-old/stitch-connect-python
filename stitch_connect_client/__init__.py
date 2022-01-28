# coding: utf-8

# flake8: noqa

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import apis into sdk package
# import ApiClient
# import models into sdk package
from stitch_connect_client.api.destinations_api import DestinationsApi
from stitch_connect_client.api.sources_api import SourcesApi
from stitch_connect_client.api.streams_api import StreamsApi
from stitch_connect_client.api_client import ApiClient
from stitch_connect_client.configuration import Configuration
from stitch_connect_client.exceptions import (
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
from stitch_connect_client.models.azure_destination_form_properties import (
    AzureDestinationFormProperties,
)
from stitch_connect_client.models.connection_check import ConnectionCheck
from stitch_connect_client.models.connection_details import ConnectionDetails
from stitch_connect_client.models.connection_step import ConnectionStep
from stitch_connect_client.models.connection_step_props import ConnectionStepProps
from stitch_connect_client.models.connection_step_props_any_of import (
    ConnectionStepPropsAnyOf,
)
from stitch_connect_client.models.connection_step_props_json_schema import (
    ConnectionStepPropsJsonSchema,
)
from stitch_connect_client.models.create_destination_body import CreateDestinationBody
from stitch_connect_client.models.create_source_body import CreateSourceBody
from stitch_connect_client.models.destination import Destination
from stitch_connect_client.models.destination_form_properties import (
    DestinationFormProperties,
)
from stitch_connect_client.models.destination_report_card import DestinationReportCard
from stitch_connect_client.models.error_object import ErrorObject
from stitch_connect_client.models.error_object_error import ErrorObjectError
from stitch_connect_client.models.field_level_metadata import FieldLevelMetadata
from stitch_connect_client.models.forced_replication_method import (
    ForcedReplicationMethod,
)
from stitch_connect_client.models.forced_replication_method_object import (
    ForcedReplicationMethodObject,
)
from stitch_connect_client.models.google_analytics_source_form_properties import (
    GoogleAnalyticsSourceFormProperties,
)
from stitch_connect_client.models.google_analytics_source_form_properties_report_definitions import (
    GoogleAnalyticsSourceFormPropertiesReportDefinitions,
)
from stitch_connect_client.models.hook_notification import HookNotification
from stitch_connect_client.models.hook_notification_config import HookNotificationConfig
from stitch_connect_client.models.metadata import Metadata
from stitch_connect_client.models.metadata_object import MetadataObject
from stitch_connect_client.models.mixpanel_source_form_properties import (
    MixpanelSourceFormProperties,
)
from stitch_connect_client.models.replication_job import ReplicationJob
from stitch_connect_client.models.s3_destination_form_properties import (
    S3DestinationFormProperties,
)
from stitch_connect_client.models.salesforce_source_form_properties import (
    SalesforceSourceFormProperties,
)
from stitch_connect_client.models.source import Source
from stitch_connect_client.models.source_form_properties import SourceFormProperties
from stitch_connect_client.models.source_report_card import SourceReportCard
from stitch_connect_client.models.stream import Stream
from stitch_connect_client.models.stream_level_metadata import StreamLevelMetadata
from stitch_connect_client.models.stream_schema import StreamSchema
from stitch_connect_client.models.stream_update import StreamUpdate
from stitch_connect_client.models.streams_update_list import StreamsUpdateList
from stitch_connect_client.models.update_source_body import UpdateSourceBody

__version__ = "0.6.1"
