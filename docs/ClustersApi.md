# ambient_backend_api_client.ClustersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_nodes_to_cluster_clusters_cluster_id_nodes_post**](ClustersApi.md#add_nodes_to_cluster_clusters_cluster_id_nodes_post) | **POST** /clusters/{cluster_id}/nodes | Add Nodes To Cluster
[**create_cluster_clusters_post**](ClustersApi.md#create_cluster_clusters_post) | **POST** /clusters | Create Cluster
[**delete_cluster_clusters_cluster_id_delete**](ClustersApi.md#delete_cluster_clusters_cluster_id_delete) | **DELETE** /clusters/{cluster_id} | Delete Cluster
[**get_cluster_clusters_cluster_id_get**](ClustersApi.md#get_cluster_clusters_cluster_id_get) | **GET** /clusters/{cluster_id} | Get Cluster
[**get_cluster_nodes_clusters_cluster_id_nodes_get**](ClustersApi.md#get_cluster_nodes_clusters_cluster_id_nodes_get) | **GET** /clusters/{cluster_id}/nodes | Get Cluster Nodes
[**get_clusters_clusters_get**](ClustersApi.md#get_clusters_clusters_get) | **GET** /clusters | Get Clusters
[**remove_nodes_from_cluster_clusters_cluster_id_nodes_delete**](ClustersApi.md#remove_nodes_from_cluster_clusters_cluster_id_nodes_delete) | **DELETE** /clusters/{cluster_id}/nodes | Remove Nodes From Cluster
[**update_cluster_clusters_cluster_id_put**](ClustersApi.md#update_cluster_clusters_cluster_id_put) | **PUT** /clusters/{cluster_id} | Update Cluster


# **add_nodes_to_cluster_clusters_cluster_id_nodes_post**
> add_nodes_to_cluster_clusters_cluster_id_nodes_post(cluster_id, request_body)

Add Nodes To Cluster

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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    request_body = [56] # List[int] | 

    try:
        # Add Nodes To Cluster
        await api_instance.add_nodes_to_cluster_clusters_cluster_id_nodes_post(cluster_id, request_body)
    except Exception as e:
        print("Exception when calling ClustersApi->add_nodes_to_cluster_clusters_cluster_id_nodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_clusters_post**
> Cluster create_cluster_clusters_post(create_custer_request)

Create Cluster

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.cluster import Cluster
from ambient_backend_api_client.models.create_custer_request import CreateCusterRequest
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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    create_custer_request = ambient_backend_api_client.CreateCusterRequest() # CreateCusterRequest | 

    try:
        # Create Cluster
        api_response = await api_instance.create_cluster_clusters_post(create_custer_request)
        print("The response of ClustersApi->create_cluster_clusters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster_clusters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custer_request** | [**CreateCusterRequest**](CreateCusterRequest.md)|  | 

### Return type

[**Cluster**](Cluster.md)

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

# **delete_cluster_clusters_cluster_id_delete**
> delete_cluster_clusters_cluster_id_delete(cluster_id)

Delete Cluster

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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # Delete Cluster
        await api_instance.delete_cluster_clusters_cluster_id_delete(cluster_id)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster_clusters_cluster_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

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

# **get_cluster_clusters_cluster_id_get**
> Cluster get_cluster_clusters_cluster_id_get(cluster_id)

Get Cluster

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.cluster import Cluster
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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # Get Cluster
        api_response = await api_instance.get_cluster_clusters_cluster_id_get(cluster_id)
        print("The response of ClustersApi->get_cluster_clusters_cluster_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_clusters_cluster_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

[**Cluster**](Cluster.md)

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

# **get_cluster_nodes_clusters_cluster_id_nodes_get**
> ListResponseNode get_cluster_nodes_clusters_cluster_id_nodes_get(cluster_id)

Get Cluster Nodes

### Example

* OAuth Authentication (OAuth2PasswordBearer):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 

    try:
        # Get Cluster Nodes
        api_response = await api_instance.get_cluster_nodes_clusters_cluster_id_nodes_get(cluster_id)
        print("The response of ClustersApi->get_cluster_nodes_clusters_cluster_id_nodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_nodes_clusters_cluster_id_nodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

[**ListResponseNode**](ListResponseNode.md)

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

# **get_clusters_clusters_get**
> ListResponseCluster get_clusters_clusters_get(limit=limit, offset=offset, sort=sort, order=order, name=name, name_starts_with=name_starts_with, status=status, org_id=org_id, user_id=user_id, request_body=request_body)

Get Clusters

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_cluster import ListResponseCluster
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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    sort = 'id' # str |  (optional) (default to 'id')
    order = 'desc' # str |  (optional) (default to 'desc')
    name = '' # str |  (optional) (default to '')
    name_starts_with = '' # str |  (optional) (default to '')
    status = '' # str |  (optional) (default to '')
    org_id = 0 # int |  (optional) (default to 0)
    user_id = 0 # int |  (optional) (default to 0)
    request_body = ['request_body_example'] # List[Optional[str]] |  (optional)

    try:
        # Get Clusters
        api_response = await api_instance.get_clusters_clusters_get(limit=limit, offset=offset, sort=sort, order=order, name=name, name_starts_with=name_starts_with, status=status, org_id=org_id, user_id=user_id, request_body=request_body)
        print("The response of ClustersApi->get_clusters_clusters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_clusters_clusters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**|  | [optional] [default to &#39;id&#39;]
 **order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **name** | **str**|  | [optional] [default to &#39;&#39;]
 **name_starts_with** | **str**|  | [optional] [default to &#39;&#39;]
 **status** | **str**|  | [optional] [default to &#39;&#39;]
 **org_id** | **int**|  | [optional] [default to 0]
 **user_id** | **int**|  | [optional] [default to 0]
 **request_body** | [**List[Optional[str]]**](str.md)|  | [optional] 

### Return type

[**ListResponseCluster**](ListResponseCluster.md)

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

# **remove_nodes_from_cluster_clusters_cluster_id_nodes_delete**
> remove_nodes_from_cluster_clusters_cluster_id_nodes_delete(cluster_id, request_body)

Remove Nodes From Cluster

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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    request_body = [56] # List[Optional[int]] | 

    try:
        # Remove Nodes From Cluster
        await api_instance.remove_nodes_from_cluster_clusters_cluster_id_nodes_delete(cluster_id, request_body)
    except Exception as e:
        print("Exception when calling ClustersApi->remove_nodes_from_cluster_clusters_cluster_id_nodes_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **request_body** | [**List[Optional[int]]**](int.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_clusters_cluster_id_put**
> Cluster update_cluster_clusters_cluster_id_put(cluster_id, update_cluster)

Update Cluster

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.cluster import Cluster
from ambient_backend_api_client.models.update_cluster import UpdateCluster
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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 56 # int | 
    update_cluster = ambient_backend_api_client.UpdateCluster() # UpdateCluster | 

    try:
        # Update Cluster
        api_response = await api_instance.update_cluster_clusters_cluster_id_put(cluster_id, update_cluster)
        print("The response of ClustersApi->update_cluster_clusters_cluster_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_clusters_cluster_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **update_cluster** | [**UpdateCluster**](UpdateCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

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

