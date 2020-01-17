# coding: utf-8

"""
    Stitch Connect

    https://www.stitchdata.com/docs/developers/stitch-connect/api  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import stitch_connect_client
from stitch_connect_client.api.streams_api import StreamsApi  # noqa: E501
from stitch_connect_client.rest import ApiException


class TestStreamsApi(unittest.TestCase):
    """StreamsApi unit test stubs"""

    def setUp(self):
        self.api = stitch_connect_client.api.streams_api.StreamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_stream_schema(self):
        """Test case for get_stream_schema

        Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.   # noqa: E501
        """
        pass

    def test_get_streams(self):
        """Test case for get_streams

        Lists the available streams for a source.  # noqa: E501
        """
        pass

    def test_update_stream_metadata(self):
        """Test case for update_stream_metadata

        Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
