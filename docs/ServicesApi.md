# ambient_backend_api_client.ServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node_to_service_services_service_id_nodes_post**](ServicesApi.md#add_node_to_service_services_service_id_nodes_post) | **POST** /services/{service_id}/nodes | Add Node To Service
[**delete_service_services_service_id_delete**](ServicesApi.md#delete_service_services_service_id_delete) | **DELETE** /services/{service_id} | Delete Service
[**deploy_service_services_service_id_deploy_post**](ServicesApi.md#deploy_service_services_service_id_deploy_post) | **POST** /services/{service_id}/deploy | Deploy Service
[**get_service_node_relationship_services_service_id_node_relationships_node_id_get**](ServicesApi.md#get_service_node_relationship_services_service_id_node_relationships_node_id_get) | **GET** /services/{service_id}/node_relationships/{node_id} | Get Service Node Relationship
[**get_service_node_relationships_services_service_id_node_relationships_get**](ServicesApi.md#get_service_node_relationships_services_service_id_node_relationships_get) | **GET** /services/{service_id}/node_relationships | Get Service Node Relationships
[**get_service_nodes_services_service_id_nodes_get**](ServicesApi.md#get_service_nodes_services_service_id_nodes_get) | **GET** /services/{service_id}/nodes | Get Service Nodes
[**get_service_requests_services_service_id_requests_get**](ServicesApi.md#get_service_requests_services_service_id_requests_get) | **GET** /services/{service_id}/requests | Get Service Requests
[**get_service_services_service_id_get**](ServicesApi.md#get_service_services_service_id_get) | **GET** /services/{service_id} | Get Service
[**get_services_services_get**](ServicesApi.md#get_services_services_get) | **GET** /services | Get Services
[**patch_service_services_service_id_patch**](ServicesApi.md#patch_service_services_service_id_patch) | **PATCH** /services/{service_id} | Patch Service
[**update_service_node_relationship_services_node_relationships_put**](ServicesApi.md#update_service_node_relationship_services_node_relationships_put) | **PUT** /services/node_relationships | Update Service Node Relationship
[**update_service_services_service_id_put**](ServicesApi.md#update_service_services_service_id_put) | **PUT** /services/{service_id} | Update Service
[**updateservice_services_post**](ServicesApi.md#updateservice_services_post) | **POST** /services | Updateservice


# **add_node_to_service_services_service_id_nodes_post**
> DeployServiceResponse add_node_to_service_services_service_id_nodes_post(service_id, node_id)

Add Node To Service

Add a node to a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.deploy_service_response import DeployServiceResponse
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 
    node_id = 56 # int | 

    try:
        # Add Node To Service
        api_response = await api_instance.add_node_to_service_services_service_id_nodes_post(service_id, node_id)
        print("The response of ServicesApi->add_node_to_service_services_service_id_nodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->add_node_to_service_services_service_id_nodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 
 **node_id** | **int**|  | 

### Return type

[**DeployServiceResponse**](DeployServiceResponse.md)

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

# **delete_service_services_service_id_delete**
> Request delete_service_services_service_id_delete(service_id)

Delete Service

Delete a service

### Example

* Api Key Authentication (APIKeyHeader):

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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

    try:
        # Delete Service
        api_response = await api_instance.delete_service_services_service_id_delete(service_id)
        print("The response of ServicesApi->delete_service_services_service_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service_services_service_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 

### Return type

[**Request**](Request.md)

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

# **deploy_service_services_service_id_deploy_post**
> DeployServiceResponse deploy_service_services_service_id_deploy_post(service_id)

Deploy Service

Deploy a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.deploy_service_response import DeployServiceResponse
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

    try:
        # Deploy Service
        api_response = await api_instance.deploy_service_services_service_id_deploy_post(service_id)
        print("The response of ServicesApi->deploy_service_services_service_id_deploy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->deploy_service_services_service_id_deploy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 

### Return type

[**DeployServiceResponse**](DeployServiceResponse.md)

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

# **get_service_node_relationship_services_service_id_node_relationships_node_id_get**
> ServiceNodeRelationship get_service_node_relationship_services_service_id_node_relationships_node_id_get(service_id, node_id)

Get Service Node Relationship

Get a node relationship for a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service_node_relationship import ServiceNodeRelationship
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 
    node_id = 56 # int | 

    try:
        # Get Service Node Relationship
        api_response = await api_instance.get_service_node_relationship_services_service_id_node_relationships_node_id_get(service_id, node_id)
        print("The response of ServicesApi->get_service_node_relationship_services_service_id_node_relationships_node_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_node_relationship_services_service_id_node_relationships_node_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 
 **node_id** | **int**|  | 

### Return type

[**ServiceNodeRelationship**](ServiceNodeRelationship.md)

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

# **get_service_node_relationships_services_service_id_node_relationships_get**
> ListResponseServiceNodeRelationship get_service_node_relationships_services_service_id_node_relationships_get(service_id)

Get Service Node Relationships

Get all node relationships for a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_service_node_relationship import ListResponseServiceNodeRelationship
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

    try:
        # Get Service Node Relationships
        api_response = await api_instance.get_service_node_relationships_services_service_id_node_relationships_get(service_id)
        print("The response of ServicesApi->get_service_node_relationships_services_service_id_node_relationships_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_node_relationships_services_service_id_node_relationships_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 

### Return type

[**ListResponseServiceNodeRelationship**](ListResponseServiceNodeRelationship.md)

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

# **get_service_nodes_services_service_id_nodes_get**
> NodeList get_service_nodes_services_service_id_nodes_get(service_id)

Get Service Nodes

Get all nodes for a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.node_list import NodeList
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

    try:
        # Get Service Nodes
        api_response = await api_instance.get_service_nodes_services_service_id_nodes_get(service_id)
        print("The response of ServicesApi->get_service_nodes_services_service_id_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_nodes_services_service_id_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 

### Return type

[**NodeList**](NodeList.md)

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

# **get_service_requests_services_service_id_requests_get**
> RequestList get_service_requests_services_service_id_requests_get(service_id)

Get Service Requests

Get all requests for a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.request_list import RequestList
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

    try:
        # Get Service Requests
        api_response = await api_instance.get_service_requests_services_service_id_requests_get(service_id)
        print("The response of ServicesApi->get_service_requests_services_service_id_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service_requests_services_service_id_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 

### Return type

[**RequestList**](RequestList.md)

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

# **get_service_services_service_id_get**
> Service get_service_services_service_id_get(service_id)

Get Service

Get a service

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 

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
 **service_id** | **int**|  | 

### Return type

[**Service**](Service.md)

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

# **get_services_services_get**
> ServiceList get_services_services_get(limit=limit, offset=offset, order_by=order_by, order=order, name=name, user_id=user_id, org_id=org_id)

Get Services

Get all services

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    order_by = 'order_by_example' # str |  (optional)
    order = 'asc' # str |  (optional) (default to 'asc')
    name = 'name_example' # str |  (optional)
    user_id = 56 # int |  (optional)
    org_id = 56 # int |  (optional)

    try:
        # Get Services
        api_response = await api_instance.get_services_services_get(limit=limit, offset=offset, order_by=order_by, order=order, name=name, user_id=user_id, org_id=org_id)
        print("The response of ServicesApi->get_services_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_services_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **order_by** | **str**|  | [optional] 
 **order** | **str**|  | [optional] [default to &#39;asc&#39;]
 **name** | **str**|  | [optional] 
 **user_id** | **int**|  | [optional] 
 **org_id** | **int**|  | [optional] 

### Return type

[**ServiceList**](ServiceList.md)

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

# **patch_service_services_service_id_patch**
> Service patch_service_services_service_id_patch(service_id, body)

Patch Service

Patch a service

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 
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
 **service_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**Service**](Service.md)

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

# **update_service_node_relationship_services_node_relationships_put**
> ServiceNodeRelationship update_service_node_relationship_services_node_relationships_put(service_node_relationship)

Update Service Node Relationship

Update a node relationship for a service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service_node_relationship import ServiceNodeRelationship
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
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_node_relationship = ambient_backend_api_client.ServiceNodeRelationship() # ServiceNodeRelationship | 

    try:
        # Update Service Node Relationship
        api_response = await api_instance.update_service_node_relationship_services_node_relationships_put(service_node_relationship)
        print("The response of ServicesApi->update_service_node_relationship_services_node_relationships_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_node_relationship_services_node_relationships_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_node_relationship** | [**ServiceNodeRelationship**](ServiceNodeRelationship.md)|  | 

### Return type

[**ServiceNodeRelationship**](ServiceNodeRelationship.md)

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

# **update_service_services_service_id_put**
> Service update_service_services_service_id_put(service_id, service)

Update Service

Update a service

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_id = 56 # int | 
    service = ambient_backend_api_client.Service() # Service | 

    try:
        # Update Service
        api_response = await api_instance.update_service_services_service_id_put(service_id, service)
        print("The response of ServicesApi->update_service_services_service_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service_services_service_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 
 **service** | [**Service**](Service.md)|  | 

### Return type

[**Service**](Service.md)

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

# **updateservice_services_post**
> Service updateservice_services_post(service_create)

Updateservice

Deploy a new service

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.service import Service
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ServicesApi(api_client)
    service_create = ambient_backend_api_client.ServiceCreate() # ServiceCreate | 

    try:
        # Updateservice
        api_response = await api_instance.updateservice_services_post(service_create)
        print("The response of ServicesApi->updateservice_services_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->updateservice_services_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create** | [**ServiceCreate**](ServiceCreate.md)|  | 

### Return type

[**Service**](Service.md)

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

