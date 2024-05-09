# ambient_backend_api_client.ServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_service_services_post**](ServicesApi.md#deploy_service_services_post) | **POST** /services | Deploy Service
[**get_service_services_service_id_get**](ServicesApi.md#get_service_services_service_id_get) | **GET** /services/{service_id} | Get Service
[**get_services_services_get**](ServicesApi.md#get_services_services_get) | **GET** /services | Get Services
[**patch_service_services_service_id_patch**](ServicesApi.md#patch_service_services_service_id_patch) | **PATCH** /services/{service_id} | Patch Service


# **deploy_service_services_post**
> PostServiceResponse deploy_service_services_post(service_create)

Deploy Service

Deploy a new service

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.post_service_response import PostServiceResponse
from ambient_backend_api_client.models.service_create import ServiceCreate
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_create = ambient_backend_api_client.ServiceCreate() # ServiceCreate | 

    try:
        # Deploy Service
        api_response = await api_instance.deploy_service_services_post(service_create)
        print("The response of ServicesApi->deploy_service_services_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->deploy_service_services_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create** | [**ServiceCreate**](ServiceCreate.md)|  | 

### Return type

[**PostServiceResponse**](PostServiceResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_services_service_id_get**
> Service get_service_services_service_id_get(service_id)

Get Service

Get a service

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service import Service
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # Get Service
        api_response = await api_instance.get_service_services_service_id_get(service_id)
        print("The response of ServicesApi->get_service_services_service_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_services_service_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**Service**](Service.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_services_get**
> ServiceList get_services_services_get(q=q)

Get Services

Get all services

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service_list import ServiceList
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    q = '' # str |  (optional) (default to '')

    try:
        # Get Services
        api_response = await api_instance.get_services_services_get(q=q)
        print("The response of ServicesApi->get_services_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ServiceList**](ServiceList.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_services_service_id_patch**
> Service patch_service_services_service_id_patch(service_id, body)

Patch Service

Patch a service

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service import Service
from ambient_backend_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ambient_backend_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 'service_id_example' # str | 
    body = None # object | 

    try:
        # Patch Service
        api_response = await api_instance.patch_service_services_service_id_patch(service_id, body)
        print("The response of ServicesApi->patch_service_services_service_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->patch_service_services_service_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Service**](Service.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

