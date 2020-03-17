# stitch_connect_client.StreamsApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stream_schema**](StreamsApi.md#get_stream_schema) | **GET** /v4/sources/{source_id}/streams/{stream_id} | Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.
[**get_streams**](StreamsApi.md#get_streams) | **GET** /v4/sources/{source_id}/streams | Lists the available streams for a source.
[**update_stream_metadata**](StreamsApi.md#update_stream_metadata) | **PUT** /v4/sources/{source_id}/streams/metadata | Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.


# **get_stream_schema**
> StreamSchema get_stream_schema(source_id, stream_id)

Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint
configuration = stitch_connect_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = stitch_connect_client.StreamsApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source
stream_id = 'stream_id_example' # str | The ID of the source

try:
    # Retrieves the schema for a source’s stream by the source and stream’s unique identifiers.
    api_response = api_instance.get_stream_schema(source_id, stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_stream_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source |
 **stream_id** | **str**| The ID of the source |

### Return type

[**StreamSchema**](StreamSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema for a stream object |  -  |
**400** | Invalid stream ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_streams**
> list[Stream] get_streams(source_id)

Lists the available streams for a source.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint
configuration = stitch_connect_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = stitch_connect_client.StreamsApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source

try:
    # Lists the available streams for a source.
    api_response = api_instance.get_streams(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StreamsApi->get_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source |

### Return type

[**list[Stream]**](Stream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stream objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stream_metadata**
> update_stream_metadata(source_id, streams_update_list)

Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint
configuration = stitch_connect_client.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.stitchdata.com
configuration.host = "https://api.stitchdata.com"
# Create an instance of the API class
api_instance = stitch_connect_client.StreamsApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source
streams_update_list = stitch_connect_client.StreamsUpdateList() # StreamsUpdateList | Array of streams to update metadata for

try:
    # Updates the metadata for streams and fields. This endpoint is used to define the metadata properties returned in the Stream Schema object’s non-discoverable-metadata-keys property.
    api_instance.update_stream_metadata(source_id, streams_update_list)
except ApiException as e:
    print("Exception when calling StreamsApi->update_stream_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source |
 **streams_update_list** | [**StreamsUpdateList**](StreamsUpdateList.md)| Array of streams to update metadata for |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated stream metadata |  -  |
**400** | Request body is missing streams, breadcrumb, and/or metadata properties  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

