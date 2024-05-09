# ambient_backend_api_client.PingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_ping_auth_ping_get**](PingApi.md#auth_ping_auth_ping_get) | **GET** /auth_ping | Auth Ping
[**ping_ping_get**](PingApi.md#ping_ping_get) | **GET** /ping | Ping


# **auth_ping_auth_ping_get**
> object auth_ping_auth_ping_get()

Auth Ping

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
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
    api_instance = ambient_backend_api_client.PingApi(api_client)

    try:
        # Auth Ping
        api_response = await api_instance.auth_ping_auth_ping_get()
        print("The response of PingApi->auth_ping_auth_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PingApi->auth_ping_auth_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_ping_get**
> object ping_ping_get()

Ping

### Example


```python
import ambient_backend_api_client
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
    api_instance = ambient_backend_api_client.PingApi(api_client)

    try:
        # Ping
        api_response = await api_instance.ping_ping_get()
        print("The response of PingApi->ping_ping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PingApi->ping_ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

