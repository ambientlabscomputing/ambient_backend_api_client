# ambient_backend_api_client.UnimplementedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_events_event_get**](UnimplementedApi.md#create_event_events_event_get) | **GET** /events/event | Create Event
[**create_event_label_events_event_label_get**](UnimplementedApi.md#create_event_label_events_event_label_get) | **GET** /events/event_label | Create Event Label
[**create_event_template_events_event_template_get**](UnimplementedApi.md#create_event_template_events_event_template_get) | **GET** /events/event_template | Create Event Template


# **create_event_events_event_get**
> object create_event_events_event_get(event)

Create Event

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.event import Event
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.UnimplementedApi(api_client)
    event = ambient_backend_api_client.Event() # Event | 

    try:
        # Create Event
        api_response = await api_instance.create_event_events_event_get(event)
        print("The response of UnimplementedApi->create_event_events_event_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnimplementedApi->create_event_events_event_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**Event**](Event.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_label_events_event_label_get**
> object create_event_label_events_event_label_get(event_label)

Create Event Label

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.event_label import EventLabel
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.UnimplementedApi(api_client)
    event_label = ambient_backend_api_client.EventLabel() # EventLabel | 

    try:
        # Create Event Label
        api_response = await api_instance.create_event_label_events_event_label_get(event_label)
        print("The response of UnimplementedApi->create_event_label_events_event_label_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnimplementedApi->create_event_label_events_event_label_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_label** | [**EventLabel**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_template_events_event_template_get**
> object create_event_template_events_event_template_get(event_template)

Create Event Template

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.event_template import EventTemplate
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.UnimplementedApi(api_client)
    event_template = ambient_backend_api_client.EventTemplate() # EventTemplate | 

    try:
        # Create Event Template
        api_response = await api_instance.create_event_template_events_event_template_get(event_template)
        print("The response of UnimplementedApi->create_event_template_events_event_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnimplementedApi->create_event_template_events_event_template_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_template** | [**EventTemplate**](EventTemplate.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

