# ambient_backend_api_client.NodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_node_nodes_node_id_authorize_post**](NodesApi.md#authorize_node_nodes_node_id_authorize_post) | **POST** /nodes/{node_id}/authorize | Authorize Node
[**create_node_nodes_post**](NodesApi.md#create_node_nodes_post) | **POST** /nodes | Create Node
[**delete_node_nodes_node_id_delete**](NodesApi.md#delete_node_nodes_node_id_delete) | **DELETE** /nodes/{node_id} | Delete Node
[**get_node_nodes_node_id_get**](NodesApi.md#get_node_nodes_node_id_get) | **GET** /nodes/{node_id} | Get Node
[**get_nodes_nodes_get**](NodesApi.md#get_nodes_nodes_get) | **GET** /nodes | Get Nodes
[**refresh_node_token_nodes_node_id_refresh_token_post**](NodesApi.md#refresh_node_token_nodes_node_id_refresh_token_post) | **POST** /nodes/{node_id}/refresh_token | Refresh Node Token
[**request_new_auth_nodes_node_id_auth_post**](NodesApi.md#request_new_auth_nodes_node_id_auth_post) | **POST** /nodes/{node_id}/auth | Request New Auth
[**update_node_nodes_node_id_patch**](NodesApi.md#update_node_nodes_node_id_patch) | **PATCH** /nodes/{node_id} | Update Node


# **authorize_node_nodes_node_id_authorize_post**
> TokenResponse authorize_node_nodes_node_id_authorize_post(node_id, device_code)

Authorize Node

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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 
    device_code = 'device_code_example' # str | 

    try:
        # Authorize Node
        api_response = await api_instance.authorize_node_nodes_node_id_authorize_post(node_id, device_code)
        print("The response of NodesApi->authorize_node_nodes_node_id_authorize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->authorize_node_nodes_node_id_authorize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **device_code** | **str**|  | 

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

# **create_node_nodes_post**
> Node create_node_nodes_post(node_create)

Create Node

Create a new node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node import Node
from ambient_backend_api_client.models.node_create import NodeCreate
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_create = ambient_backend_api_client.NodeCreate() # NodeCreate | 

    try:
        # Create Node
        api_response = await api_instance.create_node_nodes_post(node_create)
        print("The response of NodesApi->create_node_nodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->create_node_nodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_create** | [**NodeCreate**](NodeCreate.md)|  | 

### Return type

[**Node**](Node.md)

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

# **delete_node_nodes_node_id_delete**
> delete_node_nodes_node_id_delete(node_id)

Delete Node

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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 

    try:
        # Delete Node
        await api_instance.delete_node_nodes_node_id_delete(node_id)
    except Exception as e:
        print("Exception when calling NodesApi->delete_node_nodes_node_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_nodes_node_id_get**
> Node get_node_nodes_node_id_get(node_id)

Get Node

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node import Node
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 

    try:
        # Get Node
        api_response = await api_instance.get_node_nodes_node_id_get(node_id)
        print("The response of NodesApi->get_node_nodes_node_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_nodes_node_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**Node**](Node.md)

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

# **get_nodes_nodes_get**
> ListResultsResponse get_nodes_nodes_get(q=q)

Get Nodes

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_results_response import ListResultsResponse
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    q = '' # str |  (optional) (default to '')

    try:
        # Get Nodes
        api_response = await api_instance.get_nodes_nodes_get(q=q)
        print("The response of NodesApi->get_nodes_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_nodes_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ListResultsResponse**](ListResultsResponse.md)

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

# **refresh_node_token_nodes_node_id_refresh_token_post**
> TokenResponse refresh_node_token_nodes_node_id_refresh_token_post(node_id, refresh_token)

Refresh Node Token

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Refresh Node Token
        api_response = await api_instance.refresh_node_token_nodes_node_id_refresh_token_post(node_id, refresh_token)
        print("The response of NodesApi->refresh_node_token_nodes_node_id_refresh_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->refresh_node_token_nodes_node_id_refresh_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **refresh_token** | **str**|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

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

# **request_new_auth_nodes_node_id_auth_post**
> Node request_new_auth_nodes_node_id_auth_post(node_id)

Request New Auth

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node import Node
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 

    try:
        # Request New Auth
        api_response = await api_instance.request_new_auth_nodes_node_id_auth_post(node_id)
        print("The response of NodesApi->request_new_auth_nodes_node_id_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->request_new_auth_nodes_node_id_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**Node**](Node.md)

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

# **update_node_nodes_node_id_patch**
> Node update_node_nodes_node_id_patch(node_id, body)

Update Node

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node import Node
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 'node_id_example' # str | 
    body = None # object | 

    try:
        # Update Node
        api_response = await api_instance.update_node_nodes_node_id_patch(node_id, body)
        print("The response of NodesApi->update_node_nodes_node_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->update_node_nodes_node_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Node**](Node.md)

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

