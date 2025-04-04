# ambient_backend_api_client.RegistriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_registry_auth_registries_registry_id_creds_post**](RegistriesApi.md#add_registry_auth_registries_registry_id_creds_post) | **POST** /registries/{registry_id}/creds | Add Registry Auth
[**add_registry_auth_registries_registry_id_creds_post_0**](RegistriesApi.md#add_registry_auth_registries_registry_id_creds_post_0) | **POST** /registries/{registry_id}/creds | Add Registry Auth
[**create_registry_registries_post**](RegistriesApi.md#create_registry_registries_post) | **POST** /registries/ | Create Registry
[**create_registry_registries_post_0**](RegistriesApi.md#create_registry_registries_post_0) | **POST** /registries/ | Create Registry
[**delete_registry_auth_cred_registries_creds_creds_id_delete**](RegistriesApi.md#delete_registry_auth_cred_registries_creds_creds_id_delete) | **DELETE** /registries/creds/{creds_id} | Delete Registry Auth Cred
[**delete_registry_auth_cred_registries_creds_creds_id_delete_0**](RegistriesApi.md#delete_registry_auth_cred_registries_creds_creds_id_delete_0) | **DELETE** /registries/creds/{creds_id} | Delete Registry Auth Cred
[**delete_registry_registries_registry_id_delete**](RegistriesApi.md#delete_registry_registries_registry_id_delete) | **DELETE** /registries/{registry_id} | Delete Registry
[**delete_registry_registries_registry_id_delete_0**](RegistriesApi.md#delete_registry_registries_registry_id_delete_0) | **DELETE** /registries/{registry_id} | Delete Registry
[**get_nodes_for_registry_registries_registry_id_nodes_get**](RegistriesApi.md#get_nodes_for_registry_registries_registry_id_nodes_get) | **GET** /registries/{registry_id}/nodes | Get Nodes For Registry
[**get_nodes_for_registry_registries_registry_id_nodes_get_0**](RegistriesApi.md#get_nodes_for_registry_registries_registry_id_nodes_get_0) | **GET** /registries/{registry_id}/nodes | Get Nodes For Registry
[**get_registries_registries_get**](RegistriesApi.md#get_registries_registries_get) | **GET** /registries/ | Get Registries
[**get_registries_registries_get_0**](RegistriesApi.md#get_registries_registries_get_0) | **GET** /registries/ | Get Registries
[**get_registry_auth_cred_registries_creds_creds_id_get**](RegistriesApi.md#get_registry_auth_cred_registries_creds_creds_id_get) | **GET** /registries/creds/{creds_id} | Get Registry Auth Cred
[**get_registry_auth_cred_registries_creds_creds_id_get_0**](RegistriesApi.md#get_registry_auth_cred_registries_creds_creds_id_get_0) | **GET** /registries/creds/{creds_id} | Get Registry Auth Cred
[**get_registry_auth_creds_registries_registry_id_creds_get**](RegistriesApi.md#get_registry_auth_creds_registries_registry_id_creds_get) | **GET** /registries/{registry_id}/creds | Get Registry Auth Creds
[**get_registry_auth_creds_registries_registry_id_creds_get_0**](RegistriesApi.md#get_registry_auth_creds_registries_registry_id_creds_get_0) | **GET** /registries/{registry_id}/creds | Get Registry Auth Creds
[**get_registry_registries_registry_id_get**](RegistriesApi.md#get_registry_registries_registry_id_get) | **GET** /registries/{registry_id} | Get Registry
[**get_registry_registries_registry_id_get_0**](RegistriesApi.md#get_registry_registries_registry_id_get_0) | **GET** /registries/{registry_id} | Get Registry
[**get_requests_for_registry_registries_registry_id_requests_get**](RegistriesApi.md#get_requests_for_registry_registries_registry_id_requests_get) | **GET** /registries/{registry_id}/requests | Get Requests For Registry
[**get_requests_for_registry_registries_registry_id_requests_get_0**](RegistriesApi.md#get_requests_for_registry_registries_registry_id_requests_get_0) | **GET** /registries/{registry_id}/requests | Get Requests For Registry
[**trigger_registry_auth_registries_creds_creds_id_trigger_auth_post**](RegistriesApi.md#trigger_registry_auth_registries_creds_creds_id_trigger_auth_post) | **POST** /registries/creds/{creds_id}/trigger_auth | Trigger Registry Auth
[**trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0**](RegistriesApi.md#trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0) | **POST** /registries/creds/{creds_id}/trigger_auth | Trigger Registry Auth
[**update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch**](RegistriesApi.md#update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch) | **PATCH** /registries/{registry_id}/nodes/{node_id}/relationship | Update Registry Node Relationship
[**update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0**](RegistriesApi.md#update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0) | **PATCH** /registries/{registry_id}/nodes/{node_id}/relationship | Update Registry Node Relationship
[**update_registry_registries_registry_id_patch**](RegistriesApi.md#update_registry_registries_registry_id_patch) | **PATCH** /registries/{registry_id} | Update Registry
[**update_registry_registries_registry_id_patch_0**](RegistriesApi.md#update_registry_registries_registry_id_patch_0) | **PATCH** /registries/{registry_id} | Update Registry


# **add_registry_auth_registries_registry_id_creds_post**
> ContainerRegistryAuth add_registry_auth_registries_registry_id_creds_post(registry_id, container_registry_auth_create)

Add Registry Auth

Add auth credentials to a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry_auth import ContainerRegistryAuth
from ambient_backend_api_client.models.container_registry_auth_create import ContainerRegistryAuthCreate
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    container_registry_auth_create = ambient_backend_api_client.ContainerRegistryAuthCreate() # ContainerRegistryAuthCreate | 

    try:
        # Add Registry Auth
        api_response = await api_instance.add_registry_auth_registries_registry_id_creds_post(registry_id, container_registry_auth_create)
        print("The response of RegistriesApi->add_registry_auth_registries_registry_id_creds_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->add_registry_auth_registries_registry_id_creds_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **container_registry_auth_create** | [**ContainerRegistryAuthCreate**](ContainerRegistryAuthCreate.md)|  | 

### Return type

[**ContainerRegistryAuth**](ContainerRegistryAuth.md)

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

# **add_registry_auth_registries_registry_id_creds_post_0**
> ContainerRegistryAuth add_registry_auth_registries_registry_id_creds_post_0(registry_id, container_registry_auth_create)

Add Registry Auth

Add auth credentials to a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry_auth import ContainerRegistryAuth
from ambient_backend_api_client.models.container_registry_auth_create import ContainerRegistryAuthCreate
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    container_registry_auth_create = ambient_backend_api_client.ContainerRegistryAuthCreate() # ContainerRegistryAuthCreate | 

    try:
        # Add Registry Auth
        api_response = await api_instance.add_registry_auth_registries_registry_id_creds_post_0(registry_id, container_registry_auth_create)
        print("The response of RegistriesApi->add_registry_auth_registries_registry_id_creds_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->add_registry_auth_registries_registry_id_creds_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **container_registry_auth_create** | [**ContainerRegistryAuthCreate**](ContainerRegistryAuthCreate.md)|  | 

### Return type

[**ContainerRegistryAuth**](ContainerRegistryAuth.md)

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

# **create_registry_registries_post**
> ContainerRegistry create_registry_registries_post(container_registry_create)

Create Registry

Create a new registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
from ambient_backend_api_client.models.container_registry_create import ContainerRegistryCreate
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    container_registry_create = ambient_backend_api_client.ContainerRegistryCreate() # ContainerRegistryCreate | 

    try:
        # Create Registry
        api_response = await api_instance.create_registry_registries_post(container_registry_create)
        print("The response of RegistriesApi->create_registry_registries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->create_registry_registries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_registry_create** | [**ContainerRegistryCreate**](ContainerRegistryCreate.md)|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

# **create_registry_registries_post_0**
> ContainerRegistry create_registry_registries_post_0(container_registry_create)

Create Registry

Create a new registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
from ambient_backend_api_client.models.container_registry_create import ContainerRegistryCreate
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    container_registry_create = ambient_backend_api_client.ContainerRegistryCreate() # ContainerRegistryCreate | 

    try:
        # Create Registry
        api_response = await api_instance.create_registry_registries_post_0(container_registry_create)
        print("The response of RegistriesApi->create_registry_registries_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->create_registry_registries_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_registry_create** | [**ContainerRegistryCreate**](ContainerRegistryCreate.md)|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

# **delete_registry_auth_cred_registries_creds_creds_id_delete**
> delete_registry_auth_cred_registries_creds_creds_id_delete(creds_id)

Delete Registry Auth Cred

Delete an auth credential

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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Delete Registry Auth Cred
        await api_instance.delete_registry_auth_cred_registries_creds_creds_id_delete(creds_id)
    except Exception as e:
        print("Exception when calling RegistriesApi->delete_registry_auth_cred_registries_creds_creds_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

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

# **delete_registry_auth_cred_registries_creds_creds_id_delete_0**
> delete_registry_auth_cred_registries_creds_creds_id_delete_0(creds_id)

Delete Registry Auth Cred

Delete an auth credential

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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Delete Registry Auth Cred
        await api_instance.delete_registry_auth_cred_registries_creds_creds_id_delete_0(creds_id)
    except Exception as e:
        print("Exception when calling RegistriesApi->delete_registry_auth_cred_registries_creds_creds_id_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

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

# **delete_registry_registries_registry_id_delete**
> object delete_registry_registries_registry_id_delete(registry_id)

Delete Registry

Delete a registry

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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Delete Registry
        api_response = await api_instance.delete_registry_registries_registry_id_delete(registry_id)
        print("The response of RegistriesApi->delete_registry_registries_registry_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->delete_registry_registries_registry_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

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

# **delete_registry_registries_registry_id_delete_0**
> object delete_registry_registries_registry_id_delete_0(registry_id)

Delete Registry

Delete a registry

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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Delete Registry
        api_response = await api_instance.delete_registry_registries_registry_id_delete_0(registry_id)
        print("The response of RegistriesApi->delete_registry_registries_registry_id_delete_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->delete_registry_registries_registry_id_delete_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

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

# **get_nodes_for_registry_registries_registry_id_nodes_get**
> ListResponseNodeWithRegistries get_nodes_for_registry_registries_registry_id_nodes_get(registry_id)

Get Nodes For Registry

Get nodes that have access to a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_node_with_registries import ListResponseNodeWithRegistries
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Nodes For Registry
        api_response = await api_instance.get_nodes_for_registry_registries_registry_id_nodes_get(registry_id)
        print("The response of RegistriesApi->get_nodes_for_registry_registries_registry_id_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_nodes_for_registry_registries_registry_id_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseNodeWithRegistries**](ListResponseNodeWithRegistries.md)

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

# **get_nodes_for_registry_registries_registry_id_nodes_get_0**
> ListResponseNodeWithRegistries get_nodes_for_registry_registries_registry_id_nodes_get_0(registry_id)

Get Nodes For Registry

Get nodes that have access to a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_node_with_registries import ListResponseNodeWithRegistries
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Nodes For Registry
        api_response = await api_instance.get_nodes_for_registry_registries_registry_id_nodes_get_0(registry_id)
        print("The response of RegistriesApi->get_nodes_for_registry_registries_registry_id_nodes_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_nodes_for_registry_registries_registry_id_nodes_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseNodeWithRegistries**](ListResponseNodeWithRegistries.md)

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

# **get_registries_registries_get**
> ListResponseContainerRegistry get_registries_registries_get()

Get Registries

Get all registries

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_container_registry import ListResponseContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)

    try:
        # Get Registries
        api_response = await api_instance.get_registries_registries_get()
        print("The response of RegistriesApi->get_registries_registries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registries_registries_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListResponseContainerRegistry**](ListResponseContainerRegistry.md)

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

# **get_registries_registries_get_0**
> ListResponseContainerRegistry get_registries_registries_get_0()

Get Registries

Get all registries

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_container_registry import ListResponseContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)

    try:
        # Get Registries
        api_response = await api_instance.get_registries_registries_get_0()
        print("The response of RegistriesApi->get_registries_registries_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registries_registries_get_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListResponseContainerRegistry**](ListResponseContainerRegistry.md)

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

# **get_registry_auth_cred_registries_creds_creds_id_get**
> ContainerRegistryAuth get_registry_auth_cred_registries_creds_creds_id_get(creds_id)

Get Registry Auth Cred

Get a specific auth credential

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry_auth import ContainerRegistryAuth
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Get Registry Auth Cred
        api_response = await api_instance.get_registry_auth_cred_registries_creds_creds_id_get(creds_id)
        print("The response of RegistriesApi->get_registry_auth_cred_registries_creds_creds_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_auth_cred_registries_creds_creds_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

### Return type

[**ContainerRegistryAuth**](ContainerRegistryAuth.md)

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

# **get_registry_auth_cred_registries_creds_creds_id_get_0**
> ContainerRegistryAuth get_registry_auth_cred_registries_creds_creds_id_get_0(creds_id)

Get Registry Auth Cred

Get a specific auth credential

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry_auth import ContainerRegistryAuth
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Get Registry Auth Cred
        api_response = await api_instance.get_registry_auth_cred_registries_creds_creds_id_get_0(creds_id)
        print("The response of RegistriesApi->get_registry_auth_cred_registries_creds_creds_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_auth_cred_registries_creds_creds_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

### Return type

[**ContainerRegistryAuth**](ContainerRegistryAuth.md)

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

# **get_registry_auth_creds_registries_registry_id_creds_get**
> ListResponseContainerRegistryAuth get_registry_auth_creds_registries_registry_id_creds_get(registry_id)

Get Registry Auth Creds

Get auth credentials for a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_container_registry_auth import ListResponseContainerRegistryAuth
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Registry Auth Creds
        api_response = await api_instance.get_registry_auth_creds_registries_registry_id_creds_get(registry_id)
        print("The response of RegistriesApi->get_registry_auth_creds_registries_registry_id_creds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_auth_creds_registries_registry_id_creds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseContainerRegistryAuth**](ListResponseContainerRegistryAuth.md)

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

# **get_registry_auth_creds_registries_registry_id_creds_get_0**
> ListResponseContainerRegistryAuth get_registry_auth_creds_registries_registry_id_creds_get_0(registry_id)

Get Registry Auth Creds

Get auth credentials for a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_container_registry_auth import ListResponseContainerRegistryAuth
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Registry Auth Creds
        api_response = await api_instance.get_registry_auth_creds_registries_registry_id_creds_get_0(registry_id)
        print("The response of RegistriesApi->get_registry_auth_creds_registries_registry_id_creds_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_auth_creds_registries_registry_id_creds_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseContainerRegistryAuth**](ListResponseContainerRegistryAuth.md)

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

# **get_registry_registries_registry_id_get**
> ContainerRegistry get_registry_registries_registry_id_get(registry_id)

Get Registry

Get a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Registry
        api_response = await api_instance.get_registry_registries_registry_id_get(registry_id)
        print("The response of RegistriesApi->get_registry_registries_registry_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_registries_registry_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

# **get_registry_registries_registry_id_get_0**
> ContainerRegistry get_registry_registries_registry_id_get_0(registry_id)

Get Registry

Get a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Registry
        api_response = await api_instance.get_registry_registries_registry_id_get_0(registry_id)
        print("The response of RegistriesApi->get_registry_registries_registry_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_registry_registries_registry_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

# **get_requests_for_registry_registries_registry_id_requests_get**
> ListResponseRequest get_requests_for_registry_registries_registry_id_requests_get(registry_id)

Get Requests For Registry

Get requests for a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_request import ListResponseRequest
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Requests For Registry
        api_response = await api_instance.get_requests_for_registry_registries_registry_id_requests_get(registry_id)
        print("The response of RegistriesApi->get_requests_for_registry_registries_registry_id_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_requests_for_registry_registries_registry_id_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseRequest**](ListResponseRequest.md)

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

# **get_requests_for_registry_registries_registry_id_requests_get_0**
> ListResponseRequest get_requests_for_registry_registries_registry_id_requests_get_0(registry_id)

Get Requests For Registry

Get requests for a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_request import ListResponseRequest
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 

    try:
        # Get Requests For Registry
        api_response = await api_instance.get_requests_for_registry_registries_registry_id_requests_get_0(registry_id)
        print("The response of RegistriesApi->get_requests_for_registry_registries_registry_id_requests_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->get_requests_for_registry_registries_registry_id_requests_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 

### Return type

[**ListResponseRequest**](ListResponseRequest.md)

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

# **trigger_registry_auth_registries_creds_creds_id_trigger_auth_post**
> PostRegistriesCredsTriggerResponse trigger_registry_auth_registries_creds_creds_id_trigger_auth_post(creds_id)

Trigger Registry Auth

Trigger a registry auth

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.post_registries_creds_trigger_response import PostRegistriesCredsTriggerResponse
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Trigger Registry Auth
        api_response = await api_instance.trigger_registry_auth_registries_creds_creds_id_trigger_auth_post(creds_id)
        print("The response of RegistriesApi->trigger_registry_auth_registries_creds_creds_id_trigger_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->trigger_registry_auth_registries_creds_creds_id_trigger_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

### Return type

[**PostRegistriesCredsTriggerResponse**](PostRegistriesCredsTriggerResponse.md)

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

# **trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0**
> PostRegistriesCredsTriggerResponse trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0(creds_id)

Trigger Registry Auth

Trigger a registry auth

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.post_registries_creds_trigger_response import PostRegistriesCredsTriggerResponse
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    creds_id = 56 # int | 

    try:
        # Trigger Registry Auth
        api_response = await api_instance.trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0(creds_id)
        print("The response of RegistriesApi->trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->trigger_registry_auth_registries_creds_creds_id_trigger_auth_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_id** | **int**|  | 

### Return type

[**PostRegistriesCredsTriggerResponse**](PostRegistriesCredsTriggerResponse.md)

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

# **update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch**
> update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch(registry_id, node_id, status, error=error)

Update Registry Node Relationship

Update the relationship between a node and a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.registry_node_association_status_enum import RegistryNodeAssociationStatusEnum
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    node_id = 56 # int | 
    status = ambient_backend_api_client.RegistryNodeAssociationStatusEnum() # RegistryNodeAssociationStatusEnum | 
    error = 'error_example' # str |  (optional)

    try:
        # Update Registry Node Relationship
        await api_instance.update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch(registry_id, node_id, status, error=error)
    except Exception as e:
        print("Exception when calling RegistriesApi->update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **node_id** | **int**|  | 
 **status** | [**RegistryNodeAssociationStatusEnum**](.md)|  | 
 **error** | **str**|  | [optional] 

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

# **update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0**
> update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0(registry_id, node_id, status, error=error)

Update Registry Node Relationship

Update the relationship between a node and a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.registry_node_association_status_enum import RegistryNodeAssociationStatusEnum
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    node_id = 56 # int | 
    status = ambient_backend_api_client.RegistryNodeAssociationStatusEnum() # RegistryNodeAssociationStatusEnum | 
    error = 'error_example' # str |  (optional)

    try:
        # Update Registry Node Relationship
        await api_instance.update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0(registry_id, node_id, status, error=error)
    except Exception as e:
        print("Exception when calling RegistriesApi->update_registry_node_relationship_registries_registry_id_nodes_node_id_relationship_patch_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **node_id** | **int**|  | 
 **status** | [**RegistryNodeAssociationStatusEnum**](.md)|  | 
 **error** | **str**|  | [optional] 

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

# **update_registry_registries_registry_id_patch**
> ContainerRegistry update_registry_registries_registry_id_patch(registry_id, body)

Update Registry

Update a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    body = None # object | 

    try:
        # Update Registry
        api_response = await api_instance.update_registry_registries_registry_id_patch(registry_id, body)
        print("The response of RegistriesApi->update_registry_registries_registry_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->update_registry_registries_registry_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

# **update_registry_registries_registry_id_patch_0**
> ContainerRegistry update_registry_registries_registry_id_patch_0(registry_id, body)

Update Registry

Update a registry

### Example

* Api Key Authentication (APIKeyHeader):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.container_registry import ContainerRegistry
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
    api_instance = ambient_backend_api_client.RegistriesApi(api_client)
    registry_id = 56 # int | 
    body = None # object | 

    try:
        # Update Registry
        api_response = await api_instance.update_registry_registries_registry_id_patch_0(registry_id, body)
        print("The response of RegistriesApi->update_registry_registries_registry_id_patch_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->update_registry_registries_registry_id_patch_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**ContainerRegistry**](ContainerRegistry.md)

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

