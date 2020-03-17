# stitch_connect_client.DestinationsApi

All URIs are relative to *https://api.stitchdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_destination**](DestinationsApi.md#create_destination) | **POST** /v4/destinations | Creates a new destination. Only a single destination is supported per Stitch client account.
[**delete_destination**](DestinationsApi.md#delete_destination) | **DELETE** /v4/destinations/{destination_id} | Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection.
[**get_destination_types**](DestinationsApi.md#get_destination_types) | **GET** /v4/destination-types | Retrieves general information about the configuration required for all supported destination types.
[**get_destinations**](DestinationsApi.md#get_destinations) | **GET** /v4/destinations | Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account.
[**update_destination**](DestinationsApi.md#update_destination) | **PUT** /v4/destinations/{destination_id} | Updates an existing destination. Modifications to the type attribute are not supported.


# **create_destination**
> Destination create_destination(create_destination_body)

Creates a new destination. Only a single destination is supported per Stitch client account.

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
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))
create_destination_body = stitch_connect_client.CreateDestinationBody() # CreateDestinationBody | Object containing type and properties of a destination

try:
    # Creates a new destination. Only a single destination is supported per Stitch client account.
    api_response = api_instance.create_destination(create_destination_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationsApi->create_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_destination_body** | [**CreateDestinationBody**](CreateDestinationBody.md)| Object containing type and properties of a destination |

### Return type

[**Destination**](Destination.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created destination |  -  |
**400** | Only a single destination per account is allowed  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination**
> delete_destination(destination_id)

Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection.

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
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))
destination_id = 'destination_id_example' # str | The ID of the destination

try:
    # Deletes an existing destination. Note: Stitch requires a destination to replicate data. Replication will be paused until a new destination is created and has a successful connection.
    api_instance.delete_destination(destination_id)
except ApiException as e:
    print("Exception when calling DestinationsApi->delete_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The ID of the destination |

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
**200** | Destination successfully deleted  |  -  |
**400** | Invalid destination ID  |  -  |
**502** | Destination ID contains illegal characters  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_types**
> list[DestinationReportCard] get_destination_types()

Retrieves general information about the configuration required for all supported destination types.

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
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))

try:
    # Retrieves general information about the configuration required for all supported destination types.
    api_response = api_instance.get_destination_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationsApi->get_destination_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DestinationReportCard]**](DestinationReportCard.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of destination report card objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destinations**
> list[Destination] get_destinations()

Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account.

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
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))

try:
    # Lists the destination currently in use for a Stitch account. Only a single data warehouse is supported per Stitch client account.
    api_response = api_instance.get_destinations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationsApi->get_destinations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Destination]**](Destination.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of destination objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_destination**
> Destination update_destination(destination_id, destination_form_properties)

Updates an existing destination. Modifications to the type attribute are not supported.

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
api_instance = stitch_connect_client.DestinationsApi(stitch_connect_client.ApiClient(configuration))
destination_id = 'destination_id_example' # str | The ID of the destination
destination_form_properties = stitch_connect_client.DestinationFormProperties() # DestinationFormProperties | Object containing properties info

try:
    # Updates an existing destination. Modifications to the type attribute are not supported.
    api_response = api_instance.update_destination(destination_id, destination_form_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DestinationsApi->update_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The ID of the destination |
 **destination_form_properties** | [**DestinationFormProperties**](DestinationFormProperties.md)| Object containing properties info |

### Return type

[**Destination**](Destination.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated destination |  -  |
**400** | Invalid destination ID  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

