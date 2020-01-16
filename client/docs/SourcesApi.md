# stitch_connect_client.SourcesApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source**](SourcesApi.md#create_source) | **POST** /v4/sources | Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 
[**delete_source**](SourcesApi.md#delete_source) | **DELETE** /v4/sources/{source_id} | Deletes an existing data source.
[**get_last_connection_check**](SourcesApi.md#get_last_connection_check) | **GET** /v4/sources/{source_id}/last-connection-check | Retrieves the last connection check for a source by the source’s unique identifier. 
[**get_source**](SourcesApi.md#get_source) | **GET** /v4/sources/{source_id} | Retrieves a previously created data source by its unique identifier. This endpoint can be used to retrieve an active, paused, or deleted source. 
[**get_sources**](SourcesApi.md#get_sources) | **GET** /v4/sources | Lists the sources for an account, including active, paused, and deleted sources. 
[**start_replication**](SourcesApi.md#start_replication) | **POST** /v4/sources/{source_id}/sync | Manually starts a replication job for a source using the source’s unique identifier. 
[**update_source**](SourcesApi.md#update_source) | **PUT** /v4/sources/{source_id} | Updates an existing data source.


# **create_source**
> Source create_source(create_source_body)

Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 

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
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))
create_source_body = stitch_connect_client.CreateSourceBody() # CreateSourceBody | Request body to create a new source

try:
    # Creates a source object, which is the first step in setting up a new data source. After the source object is created, additional configuration steps must be completed. 
    api_response = api_instance.create_source(create_source_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->create_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_source_body** | [**CreateSourceBody**](CreateSourceBody.md)| Request body to create a new source | 

### Return type

[**Source**](Source.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created new source |  -  |
**400** | Cron expressions can’t specify both a day-of-week and day-of-month  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> delete_source(source_id)

Deletes an existing data source.

### Example

```python
from __future__ import print_function
import time
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = stitch_connect_client.SourcesApi()
source_id = 'source_id_example' # str | The ID of the source

try:
    # Deletes an existing data source.
    api_instance.delete_source(source_id)
except ApiException as e:
    print("Exception when calling SourcesApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_connection_check**
> ConnectionCheck get_last_connection_check(source_id)

Retrieves the last connection check for a source by the source’s unique identifier. 

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
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source

try:
    # Retrieves the last connection check for a source by the source’s unique identifier. 
    api_response = api_instance.get_last_connection_check(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_last_connection_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

[**ConnectionCheck**](ConnectionCheck.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved last connection check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source**
> get_source(source_id)

Retrieves a previously created data source by its unique identifier. This endpoint can be used to retrieve an active, paused, or deleted source. 

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
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source

try:
    # Retrieves a previously created data source by its unique identifier. This endpoint can be used to retrieve an active, paused, or deleted source. 
    api_instance.get_source(source_id)
except ApiException as e:
    print("Exception when calling SourcesApi->get_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sources**
> list[Source] get_sources()

Lists the sources for an account, including active, paused, and deleted sources. 

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
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))

try:
    # Lists the sources for an account, including active, paused, and deleted sources. 
    api_response = api_instance.get_sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->get_sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Source]**](Source.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of source objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> ErrorObject start_replication(source_id)

Manually starts a replication job for a source using the source’s unique identifier. 

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
api_instance = stitch_connect_client.SourcesApi(stitch_connect_client.ApiClient(configuration))
source_id = 'source_id_example' # str | The ID of the source

try:
    # Manually starts a replication job for a source using the source’s unique identifier. 
    api_response = api_instance.start_replication(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourcesApi->start_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 

### Return type

[**ErrorObject**](ErrorObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replication job already in progress |  -  |
**400** | Source has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> update_source(source_id, update_source_body)

Updates an existing data source.

### Example

```python
from __future__ import print_function
import time
import stitch_connect_client
from stitch_connect_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = stitch_connect_client.SourcesApi()
source_id = 'source_id_example' # str | The ID of the source
update_source_body = stitch_connect_client.UpdateSourceBody() # UpdateSourceBody | Request body for updating a source

try:
    # Updates an existing data source.
    api_instance.update_source(source_id, update_source_body)
except ApiException as e:
    print("Exception when calling SourcesApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source | 
 **update_source_body** | [**UpdateSourceBody**](UpdateSourceBody.md)| Request body for updating a source | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

