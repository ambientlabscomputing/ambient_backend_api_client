# ambient_backend_api_client.RequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_notes_to_request_requests_request_id_notes_post**](RequestsApi.md#add_notes_to_request_requests_request_id_notes_post) | **POST** /requests/{request_id}/notes | Add Notes To Request
[**get_request_requests_request_id_get**](RequestsApi.md#get_request_requests_request_id_get) | **GET** /requests/{request_id} | Get Request
[**patch_request_requests_request_id_patch**](RequestsApi.md#patch_request_requests_request_id_patch) | **PATCH** /requests/{request_id} | Patch Request


# **add_notes_to_request_requests_request_id_notes_post**
> Request add_notes_to_request_requests_request_id_notes_post(request_id, notes)

Add Notes To Request

Add notes to a request

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.request import Request
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
    api_instance = ambient_backend_api_client.RequestsApi(api_client)
    request_id = 56 # int | 
    notes = 'notes_example' # str | 

    try:
        # Add Notes To Request
        api_response = await api_instance.add_notes_to_request_requests_request_id_notes_post(request_id, notes)
        print("The response of RequestsApi->add_notes_to_request_requests_request_id_notes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->add_notes_to_request_requests_request_id_notes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 
 **notes** | **str**|  | 

### Return type

[**Request**](Request.md)

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

# **get_request_requests_request_id_get**
> Request get_request_requests_request_id_get(request_id)

Get Request

Get a request

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.request import Request
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
    api_instance = ambient_backend_api_client.RequestsApi(api_client)
    request_id = 56 # int | 

    try:
        # Get Request
        api_response = await api_instance.get_request_requests_request_id_get(request_id)
        print("The response of RequestsApi->get_request_requests_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request_requests_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 

### Return type

[**Request**](Request.md)

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

# **patch_request_requests_request_id_patch**
> Request patch_request_requests_request_id_patch(request_id, body)

Patch Request

Patch a request

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.request import Request
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
    api_instance = ambient_backend_api_client.RequestsApi(api_client)
    request_id = 56 # int | 
    body = None # object | 

    try:
        # Patch Request
        api_response = await api_instance.patch_request_requests_request_id_patch(request_id, body)
        print("The response of RequestsApi->patch_request_requests_request_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->patch_request_requests_request_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**Request**](Request.md)

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

