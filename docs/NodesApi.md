# ambient_backend_api_client.NodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_nodes_post**](NodesApi.md#create_node_nodes_post) | **POST** /nodes | Create Node
[**delete_node_nodes_node_id_delete**](NodesApi.md#delete_node_nodes_node_id_delete) | **DELETE** /nodes/{node_id} | Delete Node
[**get_node_advertised_interface_nodes_node_id_interfaces_advertised_get**](NodesApi.md#get_node_advertised_interface_nodes_node_id_interfaces_advertised_get) | **GET** /nodes/{node_id}/interfaces/advertised | Get Node Advertised Interface
[**get_node_certificate_nodes_node_id_certificate_get**](NodesApi.md#get_node_certificate_nodes_node_id_certificate_get) | **GET** /nodes/{node_id}/certificate | Get Node Certificate
[**get_node_interfaces_nodes_node_id_interfaces_get**](NodesApi.md#get_node_interfaces_nodes_node_id_interfaces_get) | **GET** /nodes/{node_id}/interfaces | Get Node Interfaces
[**get_node_nodes_node_id_get**](NodesApi.md#get_node_nodes_node_id_get) | **GET** /nodes/{node_id} | Get Node
[**get_node_panel_data_nodes_panel_data_get**](NodesApi.md#get_node_panel_data_nodes_panel_data_get) | **GET** /nodes/panel_data | Get Node Panel Data
[**get_node_services_nodes_node_id_services_get**](NodesApi.md#get_node_services_nodes_node_id_services_get) | **GET** /nodes/{node_id}/services | Get Node Services
[**get_nodes_nodes_get**](NodesApi.md#get_nodes_nodes_get) | **GET** /nodes | Get Nodes
[**put_node_nodes_node_id_put**](NodesApi.md#put_node_nodes_node_id_put) | **PUT** /nodes/{node_id} | Put Node
[**set_node_advertised_interface_nodes_set_advertised_interface_post**](NodesApi.md#set_node_advertised_interface_nodes_set_advertised_interface_post) | **POST** /nodes/set_advertised_interface | Set Node Advertised Interface
[**update_node_nodes_node_id_patch**](NodesApi.md#update_node_nodes_node_id_patch) | **PATCH** /nodes/{node_id} | Update Node


# **create_node_nodes_post**
> NodeOutput create_node_nodes_post(node_create)

Create Node

Create a new node

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_create import NodeCreate
from ambient_backend_api_client.models.node_output import NodeOutput
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

[**NodeOutput**](NodeOutput.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

    try:
        # Delete Node
        await api_instance.delete_node_nodes_node_id_delete(node_id)
    except Exception as e:
        print("Exception when calling NodesApi->delete_node_nodes_node_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_advertised_interface_nodes_node_id_interfaces_advertised_get**
> NetworkInterface get_node_advertised_interface_nodes_node_id_interfaces_advertised_get(node_id)

Get Node Advertised Interface

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.network_interface import NetworkInterface
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node Advertised Interface
        api_response = await api_instance.get_node_advertised_interface_nodes_node_id_interfaces_advertised_get(node_id)
        print("The response of NodesApi->get_node_advertised_interface_nodes_node_id_interfaces_advertised_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_advertised_interface_nodes_node_id_interfaces_advertised_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

[**NetworkInterface**](NetworkInterface.md)

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

# **get_node_certificate_nodes_node_id_certificate_get**
> object get_node_certificate_nodes_node_id_certificate_get(node_id)

Get Node Certificate

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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node Certificate
        api_response = await api_instance.get_node_certificate_nodes_node_id_certificate_get(node_id)
        print("The response of NodesApi->get_node_certificate_nodes_node_id_certificate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_certificate_nodes_node_id_certificate_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_interfaces_nodes_node_id_interfaces_get**
> ListResponseNetworkInterface get_node_interfaces_nodes_node_id_interfaces_get(node_id)

Get Node Interfaces

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_network_interface import ListResponseNetworkInterface
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node Interfaces
        api_response = await api_instance.get_node_interfaces_nodes_node_id_interfaces_get(node_id)
        print("The response of NodesApi->get_node_interfaces_nodes_node_id_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_interfaces_nodes_node_id_interfaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

[**ListResponseNetworkInterface**](ListResponseNetworkInterface.md)

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

# **get_node_nodes_node_id_get**
> NodeOutput get_node_nodes_node_id_get(node_id)

Get Node

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_output import NodeOutput
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

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
 **node_id** | **int**|  | 

### Return type

[**NodeOutput**](NodeOutput.md)

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

# **get_node_panel_data_nodes_panel_data_get**
> NodePagePanelData get_node_panel_data_nodes_panel_data_get()

Get Node Panel Data

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_page_panel_data import NodePagePanelData
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)

    try:
        # Get Node Panel Data
        api_response = await api_instance.get_node_panel_data_nodes_panel_data_get()
        print("The response of NodesApi->get_node_panel_data_nodes_panel_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_panel_data_nodes_panel_data_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NodePagePanelData**](NodePagePanelData.md)

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

# **get_node_services_nodes_node_id_services_get**
> ListResponseService get_node_services_nodes_node_id_services_get(node_id)

Get Node Services

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_service import ListResponseService
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 

    try:
        # Get Node Services
        api_response = await api_instance.get_node_services_nodes_node_id_services_get(node_id)
        print("The response of NodesApi->get_node_services_nodes_node_id_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_node_services_nodes_node_id_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 

### Return type

[**ListResponseService**](ListResponseService.md)

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

# **get_nodes_nodes_get**
> ListResponseNode get_nodes_nodes_get(limit=limit, offset=offset, sort=sort, order=order, name=name, name_starts_with=name_starts_with, role=role, status=status, architecture=architecture, org_id=org_id, user_id=user_id, live=live, cluster_id=cluster_id, request_body=request_body)

Get Nodes

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_node import ListResponseNode
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    sort = 'last_seen' # str |  (optional) (default to 'last_seen')
    order = 'desc' # str |  (optional) (default to 'desc')
    name = '' # str |  (optional) (default to '')
    name_starts_with = '' # str |  (optional) (default to '')
    role = '' # str |  (optional) (default to '')
    status = '' # str |  (optional) (default to '')
    architecture = '' # str |  (optional) (default to '')
    org_id = 0 # int |  (optional) (default to 0)
    user_id = 0 # int |  (optional) (default to 0)
    live = False # bool |  (optional) (default to False)
    cluster_id = 0 # int |  (optional) (default to 0)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Get Nodes
        api_response = await api_instance.get_nodes_nodes_get(limit=limit, offset=offset, sort=sort, order=order, name=name, name_starts_with=name_starts_with, role=role, status=status, architecture=architecture, org_id=org_id, user_id=user_id, live=live, cluster_id=cluster_id, request_body=request_body)
        print("The response of NodesApi->get_nodes_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->get_nodes_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**|  | [optional] [default to &#39;last_seen&#39;]
 **order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **name** | **str**|  | [optional] [default to &#39;&#39;]
 **name_starts_with** | **str**|  | [optional] [default to &#39;&#39;]
 **role** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **str**|  | [optional] [default to &#39;&#39;]
 **architecture** | **str**|  | [optional] [default to &#39;&#39;]
 **org_id** | **int**|  | [optional] [default to 0]
 **user_id** | **int**|  | [optional] [default to 0]
 **live** | **bool**|  | [optional] [default to False]
 **cluster_id** | **int**|  | [optional] [default to 0]
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ListResponseNode**](ListResponseNode.md)

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

# **put_node_nodes_node_id_put**
> NodeOutput put_node_nodes_node_id_put(node_id, node_input)

Put Node

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_input import NodeInput
from ambient_backend_api_client.models.node_output import NodeOutput
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 
    node_input = ambient_backend_api_client.NodeInput() # NodeInput | 

    try:
        # Put Node
        api_response = await api_instance.put_node_nodes_node_id_put(node_id, node_input)
        print("The response of NodesApi->put_node_nodes_node_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->put_node_nodes_node_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**|  | 
 **node_input** | [**NodeInput**](NodeInput.md)|  | 

### Return type

[**NodeOutput**](NodeOutput.md)

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

# **set_node_advertised_interface_nodes_set_advertised_interface_post**
> NodeOutput set_node_advertised_interface_nodes_set_advertised_interface_post(set_node_advertised_interface_request)

Set Node Advertised Interface

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_output import NodeOutput
from ambient_backend_api_client.models.set_node_advertised_interface_request import SetNodeAdvertisedInterfaceRequest
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    set_node_advertised_interface_request = ambient_backend_api_client.SetNodeAdvertisedInterfaceRequest() # SetNodeAdvertisedInterfaceRequest | 

    try:
        # Set Node Advertised Interface
        api_response = await api_instance.set_node_advertised_interface_nodes_set_advertised_interface_post(set_node_advertised_interface_request)
        print("The response of NodesApi->set_node_advertised_interface_nodes_set_advertised_interface_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesApi->set_node_advertised_interface_nodes_set_advertised_interface_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_node_advertised_interface_request** | [**SetNodeAdvertisedInterfaceRequest**](SetNodeAdvertisedInterfaceRequest.md)|  | 

### Return type

[**NodeOutput**](NodeOutput.md)

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

# **update_node_nodes_node_id_patch**
> NodeOutput update_node_nodes_node_id_patch(node_id, body)

Update Node

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_output import NodeOutput
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
    api_instance = ambient_backend_api_client.NodesApi(api_client)
    node_id = 56 # int | 
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
 **node_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**NodeOutput**](NodeOutput.md)

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

