# ambient_backend_api_client.OauthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_device_authorization_oauth_device_authorization_confirm_post**](OauthApi.md#confirm_device_authorization_oauth_device_authorization_confirm_post) | **POST** /oauth/device_authorization/confirm | Confirm Device Authorization
[**confirm_device_authorization_oauth_device_authorization_confirm_post_0**](OauthApi.md#confirm_device_authorization_oauth_device_authorization_confirm_post_0) | **POST** /oauth/device_authorization/confirm | Confirm Device Authorization
[**create_device_authorization_oauth_device_authorization_post**](OauthApi.md#create_device_authorization_oauth_device_authorization_post) | **POST** /oauth/device_authorization | Create Device Authorization
[**create_device_authorization_oauth_device_authorization_post_0**](OauthApi.md#create_device_authorization_oauth_device_authorization_post_0) | **POST** /oauth/device_authorization | Create Device Authorization
[**decode_jwt_oauth_decode_post**](OauthApi.md#decode_jwt_oauth_decode_post) | **POST** /oauth/decode | Decode Jwt
[**decode_jwt_oauth_decode_post_0**](OauthApi.md#decode_jwt_oauth_decode_post_0) | **POST** /oauth/decode | Decode Jwt
[**delete_token_oauth_tokens_token_id_delete**](OauthApi.md#delete_token_oauth_tokens_token_id_delete) | **DELETE** /oauth/tokens/{token_id} | Delete Token
[**delete_token_oauth_tokens_token_id_delete_0**](OauthApi.md#delete_token_oauth_tokens_token_id_delete_0) | **DELETE** /oauth/tokens/{token_id} | Delete Token
[**get_token_oauth_tokens_token_id_get**](OauthApi.md#get_token_oauth_tokens_token_id_get) | **GET** /oauth/tokens/{token_id} | Get Token
[**get_token_oauth_tokens_token_id_get_0**](OauthApi.md#get_token_oauth_tokens_token_id_get_0) | **GET** /oauth/tokens/{token_id} | Get Token
[**get_tokens_oauth_tokens_get**](OauthApi.md#get_tokens_oauth_tokens_get) | **GET** /oauth/tokens | Get Tokens
[**get_tokens_oauth_tokens_get_0**](OauthApi.md#get_tokens_oauth_tokens_get_0) | **GET** /oauth/tokens | Get Tokens
[**handle_token_request_oauth_token_post**](OauthApi.md#handle_token_request_oauth_token_post) | **POST** /oauth/token | Handle Token Request
[**handle_token_request_oauth_token_post_0**](OauthApi.md#handle_token_request_oauth_token_post_0) | **POST** /oauth/token | Handle Token Request
[**register_client_oauth_clients_post**](OauthApi.md#register_client_oauth_clients_post) | **POST** /oauth/clients | Register Client
[**register_client_oauth_clients_post_0**](OauthApi.md#register_client_oauth_clients_post_0) | **POST** /oauth/clients | Register Client


# **confirm_device_authorization_oauth_device_authorization_confirm_post**
> DeviceAuthorization confirm_device_authorization_oauth_device_authorization_confirm_post(user_code, node_id)

Confirm Device Authorization

Confirm device authorization

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.device_authorization import DeviceAuthorization
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    user_code = 'user_code_example' # str | 
    node_id = 56 # int | 

    try:
        # Confirm Device Authorization
        api_response = await api_instance.confirm_device_authorization_oauth_device_authorization_confirm_post(user_code, node_id)
        print("The response of OauthApi->confirm_device_authorization_oauth_device_authorization_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->confirm_device_authorization_oauth_device_authorization_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_code** | **str**|  | 
 **node_id** | **int**|  | 

### Return type

[**DeviceAuthorization**](DeviceAuthorization.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_device_authorization_oauth_device_authorization_confirm_post_0**
> DeviceAuthorization confirm_device_authorization_oauth_device_authorization_confirm_post_0(user_code, node_id)

Confirm Device Authorization

Confirm device authorization

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.device_authorization import DeviceAuthorization
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    user_code = 'user_code_example' # str | 
    node_id = 56 # int | 

    try:
        # Confirm Device Authorization
        api_response = await api_instance.confirm_device_authorization_oauth_device_authorization_confirm_post_0(user_code, node_id)
        print("The response of OauthApi->confirm_device_authorization_oauth_device_authorization_confirm_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->confirm_device_authorization_oauth_device_authorization_confirm_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_code** | **str**|  | 
 **node_id** | **int**|  | 

### Return type

[**DeviceAuthorization**](DeviceAuthorization.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_authorization_oauth_device_authorization_post**
> DeviceAuthorizationRequest create_device_authorization_oauth_device_authorization_post()

Create Device Authorization

Create device authorization

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.device_authorization_request import DeviceAuthorizationRequest
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
    api_instance = ambient_backend_api_client.OauthApi(api_client)

    try:
        # Create Device Authorization
        api_response = await api_instance.create_device_authorization_oauth_device_authorization_post()
        print("The response of OauthApi->create_device_authorization_oauth_device_authorization_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->create_device_authorization_oauth_device_authorization_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceAuthorizationRequest**](DeviceAuthorizationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_authorization_oauth_device_authorization_post_0**
> DeviceAuthorizationRequest create_device_authorization_oauth_device_authorization_post_0()

Create Device Authorization

Create device authorization

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.device_authorization_request import DeviceAuthorizationRequest
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
    api_instance = ambient_backend_api_client.OauthApi(api_client)

    try:
        # Create Device Authorization
        api_response = await api_instance.create_device_authorization_oauth_device_authorization_post_0()
        print("The response of OauthApi->create_device_authorization_oauth_device_authorization_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->create_device_authorization_oauth_device_authorization_post_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceAuthorizationRequest**](DeviceAuthorizationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_jwt_oauth_decode_post**
> JWTClaims decode_jwt_oauth_decode_post()

Decode Jwt

Decode JWT

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.jwt_claims import JWTClaims
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)

    try:
        # Decode Jwt
        api_response = await api_instance.decode_jwt_oauth_decode_post()
        print("The response of OauthApi->decode_jwt_oauth_decode_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->decode_jwt_oauth_decode_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JWTClaims**](JWTClaims.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_jwt_oauth_decode_post_0**
> JWTClaims decode_jwt_oauth_decode_post_0()

Decode Jwt

Decode JWT

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.jwt_claims import JWTClaims
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)

    try:
        # Decode Jwt
        api_response = await api_instance.decode_jwt_oauth_decode_post_0()
        print("The response of OauthApi->decode_jwt_oauth_decode_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->decode_jwt_oauth_decode_post_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JWTClaims**](JWTClaims.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_oauth_tokens_token_id_delete**
> object delete_token_oauth_tokens_token_id_delete(token_id)

Delete Token

Delete token by ID

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_id = 56 # int | 

    try:
        # Delete Token
        api_response = await api_instance.delete_token_oauth_tokens_token_id_delete(token_id)
        print("The response of OauthApi->delete_token_oauth_tokens_token_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->delete_token_oauth_tokens_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

# **delete_token_oauth_tokens_token_id_delete_0**
> object delete_token_oauth_tokens_token_id_delete_0(token_id)

Delete Token

Delete token by ID

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_id = 56 # int | 

    try:
        # Delete Token
        api_response = await api_instance.delete_token_oauth_tokens_token_id_delete_0(token_id)
        print("The response of OauthApi->delete_token_oauth_tokens_token_id_delete_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->delete_token_oauth_tokens_token_id_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

# **get_token_oauth_tokens_token_id_get**
> Token get_token_oauth_tokens_token_id_get(token_id)

Get Token

Get token by ID

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_id = 56 # int | 

    try:
        # Get Token
        api_response = await api_instance.get_token_oauth_tokens_token_id_get(token_id)
        print("The response of OauthApi->get_token_oauth_tokens_token_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->get_token_oauth_tokens_token_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**Token**](Token.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_oauth_tokens_token_id_get_0**
> Token get_token_oauth_tokens_token_id_get_0(token_id)

Get Token

Get token by ID

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_id = 56 # int | 

    try:
        # Get Token
        api_response = await api_instance.get_token_oauth_tokens_token_id_get_0(token_id)
        print("The response of OauthApi->get_token_oauth_tokens_token_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->get_token_oauth_tokens_token_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**Token**](Token.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_oauth_tokens_get**
> ListResponseToken get_tokens_oauth_tokens_get(limit=limit, offset=offset, order_by=order_by, order=order, user_id=user_id, org_id=org_id, node_id=node_id, tombstoned=tombstoned, uid=uid, search=search)

Get Tokens

Get all tokens

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_token import ListResponseToken
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'id' # str |  (optional) (default to 'id')
    order = 'desc' # str |  (optional) (default to 'desc')
    user_id = 0 # int |  (optional) (default to 0)
    org_id = 0 # int |  (optional) (default to 0)
    node_id = 56 # int |  (optional)
    tombstoned = True # bool |  (optional)
    uid = 'uid_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Get Tokens
        api_response = await api_instance.get_tokens_oauth_tokens_get(limit=limit, offset=offset, order_by=order_by, order=order, user_id=user_id, org_id=org_id, node_id=node_id, tombstoned=tombstoned, uid=uid, search=search)
        print("The response of OauthApi->get_tokens_oauth_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->get_tokens_oauth_tokens_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]
 **order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **user_id** | **int**|  | [optional] [default to 0]
 **org_id** | **int**|  | [optional] [default to 0]
 **node_id** | **int**|  | [optional] 
 **tombstoned** | **bool**|  | [optional] 
 **uid** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**ListResponseToken**](ListResponseToken.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_oauth_tokens_get_0**
> ListResponseToken get_tokens_oauth_tokens_get_0(limit=limit, offset=offset, order_by=order_by, order=order, user_id=user_id, org_id=org_id, node_id=node_id, tombstoned=tombstoned, uid=uid, search=search)

Get Tokens

Get all tokens

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_token import ListResponseToken
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'id' # str |  (optional) (default to 'id')
    order = 'desc' # str |  (optional) (default to 'desc')
    user_id = 0 # int |  (optional) (default to 0)
    org_id = 0 # int |  (optional) (default to 0)
    node_id = 56 # int |  (optional)
    tombstoned = True # bool |  (optional)
    uid = 'uid_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Get Tokens
        api_response = await api_instance.get_tokens_oauth_tokens_get_0(limit=limit, offset=offset, order_by=order_by, order=order, user_id=user_id, org_id=org_id, node_id=node_id, tombstoned=tombstoned, uid=uid, search=search)
        print("The response of OauthApi->get_tokens_oauth_tokens_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->get_tokens_oauth_tokens_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] [default to &#39;id&#39;]
 **order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **user_id** | **int**|  | [optional] [default to 0]
 **org_id** | **int**|  | [optional] [default to 0]
 **node_id** | **int**|  | [optional] 
 **tombstoned** | **bool**|  | [optional] 
 **uid** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**ListResponseToken**](ListResponseToken.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_token_request_oauth_token_post**
> TokenResponse handle_token_request_oauth_token_post(token_request)

Handle Token Request

Handle OAuth2 token request

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.token_request import TokenRequest
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
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_request = ambient_backend_api_client.TokenRequest() # TokenRequest | 

    try:
        # Handle Token Request
        api_response = await api_instance.handle_token_request_oauth_token_post(token_request)
        print("The response of OauthApi->handle_token_request_oauth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->handle_token_request_oauth_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **handle_token_request_oauth_token_post_0**
> TokenResponse handle_token_request_oauth_token_post_0(token_request)

Handle Token Request

Handle OAuth2 token request

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.token_request import TokenRequest
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
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    token_request = ambient_backend_api_client.TokenRequest() # TokenRequest | 

    try:
        # Handle Token Request
        api_response = await api_instance.handle_token_request_oauth_token_post_0(token_request)
        print("The response of OauthApi->handle_token_request_oauth_token_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->handle_token_request_oauth_token_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **register_client_oauth_clients_post**
> ClientSecret register_client_oauth_clients_post(create_client_secret)

Register Client

Register client

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.client_secret import ClientSecret
from ambient_backend_api_client.models.create_client_secret import CreateClientSecret
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    create_client_secret = ambient_backend_api_client.CreateClientSecret() # CreateClientSecret | 

    try:
        # Register Client
        api_response = await api_instance.register_client_oauth_clients_post(create_client_secret)
        print("The response of OauthApi->register_client_oauth_clients_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->register_client_oauth_clients_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_secret** | [**CreateClientSecret**](CreateClientSecret.md)|  | 

### Return type

[**ClientSecret**](ClientSecret.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_client_oauth_clients_post_0**
> ClientSecret register_client_oauth_clients_post_0(create_client_secret)

Register Client

Register client

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.client_secret import ClientSecret
from ambient_backend_api_client.models.create_client_secret import CreateClientSecret
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.OauthApi(api_client)
    create_client_secret = ambient_backend_api_client.CreateClientSecret() # CreateClientSecret | 

    try:
        # Register Client
        api_response = await api_instance.register_client_oauth_clients_post_0(create_client_secret)
        print("The response of OauthApi->register_client_oauth_clients_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OauthApi->register_client_oauth_clients_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_secret** | [**CreateClientSecret**](CreateClientSecret.md)|  | 

### Return type

[**ClientSecret**](ClientSecret.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

