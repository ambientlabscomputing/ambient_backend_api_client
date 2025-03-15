# ambient_backend_api_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_token_auth_token_mgmt_post**](AuthApi.md#create_new_token_auth_token_mgmt_post) | **POST** /auth/token-mgmt | Create New Token
[**delete_token_auth_token_mgmt_token_id_delete**](AuthApi.md#delete_token_auth_token_mgmt_token_id_delete) | **DELETE** /auth/token-mgmt/{token_id} | Delete Token
[**get_token_auth_token_mgmt_token_id_get**](AuthApi.md#get_token_auth_token_mgmt_token_id_get) | **GET** /auth/token-mgmt/{token_id} | Get Token
[**get_tokens_auth_token_mgmt_get**](AuthApi.md#get_tokens_auth_token_mgmt_get) | **GET** /auth/token-mgmt | Get Tokens
[**handle_token_refresh_auth_token_post**](AuthApi.md#handle_token_refresh_auth_token_post) | **POST** /auth/token | Handle Token Refresh


# **create_new_token_auth_token_mgmt_post**
> Token create_new_token_auth_token_mgmt_post(create_token_request)

Create New Token

Create a token

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.create_token_request import CreateTokenRequest
from ambient_backend_api_client.models.token import Token
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
    api_instance = ambient_backend_api_client.AuthApi(api_client)
    create_token_request = ambient_backend_api_client.CreateTokenRequest() # CreateTokenRequest | 

    try:
        # Create New Token
        api_response = await api_instance.create_new_token_auth_token_mgmt_post(create_token_request)
        print("The response of AuthApi->create_new_token_auth_token_mgmt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_new_token_auth_token_mgmt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_request** | [**CreateTokenRequest**](CreateTokenRequest.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_auth_token_mgmt_token_id_delete**
> object delete_token_auth_token_mgmt_token_id_delete(token_id)

Delete Token

Delete a token

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
    api_instance = ambient_backend_api_client.AuthApi(api_client)
    token_id = 56 # int | 

    try:
        # Delete Token
        api_response = await api_instance.delete_token_auth_token_mgmt_token_id_delete(token_id)
        print("The response of AuthApi->delete_token_auth_token_mgmt_token_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->delete_token_auth_token_mgmt_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

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
**204** | No Content |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_auth_token_mgmt_token_id_get**
> Token get_token_auth_token_mgmt_token_id_get(token_id)

Get Token

Get a token

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.token import Token
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
    api_instance = ambient_backend_api_client.AuthApi(api_client)
    token_id = 56 # int | 

    try:
        # Get Token
        api_response = await api_instance.get_token_auth_token_mgmt_token_id_get(token_id)
        print("The response of AuthApi->get_token_auth_token_mgmt_token_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_token_auth_token_mgmt_token_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**Token**](Token.md)

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

# **get_tokens_auth_token_mgmt_get**
> List[Token] get_tokens_auth_token_mgmt_get(limit=limit, offset=offset, sort=sort, order=order, user_id=user_id, org_id=org_id, node_id=node_id, token_type=token_type, value=value)

Get Tokens

Get tokens

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.token import Token
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
    api_instance = ambient_backend_api_client.AuthApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    sort = 'id' # str |  (optional) (default to 'id')
    order = 'desc' # str |  (optional) (default to 'desc')
    user_id = 0 # int |  (optional) (default to 0)
    org_id = 0 # int |  (optional) (default to 0)
    node_id = 0 # int |  (optional) (default to 0)
    token_type = '' # str |  (optional) (default to '')
    value = '' # str |  (optional) (default to '')

    try:
        # Get Tokens
        api_response = await api_instance.get_tokens_auth_token_mgmt_get(limit=limit, offset=offset, sort=sort, order=order, user_id=user_id, org_id=org_id, node_id=node_id, token_type=token_type, value=value)
        print("The response of AuthApi->get_tokens_auth_token_mgmt_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_tokens_auth_token_mgmt_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**|  | [optional] [default to &#39;id&#39;]
 **order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **user_id** | **int**|  | [optional] [default to 0]
 **org_id** | **int**|  | [optional] [default to 0]
 **node_id** | **int**|  | [optional] [default to 0]
 **token_type** | **str**|  | [optional] [default to &#39;&#39;]
 **value** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[Token]**](Token.md)

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

# **handle_token_refresh_auth_token_post**
> TokenResponse handle_token_refresh_auth_token_post(refresh_token)

Handle Token Refresh

Handle token refresh

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.token_response import TokenResponse
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
    api_instance = ambient_backend_api_client.AuthApi(api_client)
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Handle Token Refresh
        api_response = await api_instance.handle_token_refresh_auth_token_post(refresh_token)
        print("The response of AuthApi->handle_token_refresh_auth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->handle_token_refresh_auth_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

