# ambient_backend_api_client.ClustersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_clusters_post**](ClustersApi.md#create_cluster_clusters_post) | **POST** /clusters | Create Cluster
[**delete_cluster_clusters_cluster_id_delete**](ClustersApi.md#delete_cluster_clusters_cluster_id_delete) | **DELETE** /clusters/{cluster_id} | Delete Cluster
[**deploy_cluster_clusters_cluster_id_deployments_post**](ClustersApi.md#deploy_cluster_clusters_cluster_id_deployments_post) | **POST** /clusters/{cluster_id}/deployments | Deploy Cluster
[**get_cluster_clusters_cluster_id_get**](ClustersApi.md#get_cluster_clusters_cluster_id_get) | **GET** /clusters/{cluster_id} | Get Cluster
[**get_cluster_deployments_clusters_cluster_id_deployments_get**](ClustersApi.md#get_cluster_deployments_clusters_cluster_id_deployments_get) | **GET** /clusters/{cluster_id}/deployments | Get Cluster Deployments
[**get_clusters_clusters_get**](ClustersApi.md#get_clusters_clusters_get) | **GET** /clusters | Get Clusters
[**patch_cluster_clusters_cluster_id_patch**](ClustersApi.md#patch_cluster_clusters_cluster_id_patch) | **PATCH** /clusters/{cluster_id} | Patch Cluster


# **create_cluster_clusters_post**
> PostClustersResponse create_cluster_clusters_post(cluster_create)

Create Cluster

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.cluster_create import ClusterCreate
from ambient_backend_api_client.models.post_clusters_response import PostClustersResponse
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
    cluster_create = ambient_backend_api_client.ClusterCreate() # ClusterCreate | 

    try:
        # Create Cluster
        api_response = await api_instance.create_cluster_clusters_post(cluster_create)
        print("The response of ClustersApi->create_cluster_clusters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster_clusters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_create** | [**ClusterCreate**](ClusterCreate.md)|  | 

### Return type

[**PostClustersResponse**](PostClustersResponse.md)

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
    cluster_id = 'cluster_id_example' # str | 

    try:
        # Delete Cluster
        await api_instance.delete_cluster_clusters_cluster_id_delete(cluster_id)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster_clusters_cluster_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

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

# **deploy_cluster_clusters_cluster_id_deployments_post**
> Cluster deploy_cluster_clusters_cluster_id_deployments_post(cluster_id)

Deploy Cluster

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
    cluster_id = 'cluster_id_example' # str | 

    try:
        # Deploy Cluster
        api_response = await api_instance.deploy_cluster_clusters_cluster_id_deployments_post(cluster_id)
        print("The response of ClustersApi->deploy_cluster_clusters_cluster_id_deployments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->deploy_cluster_clusters_cluster_id_deployments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

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

# **get_cluster_clusters_cluster_id_get**
> Cluster get_cluster_clusters_cluster_id_get(cluster_id)

Get Cluster

### Example


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


# Enter a context with an instance of the API client
async with ambient_backend_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 

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
 **cluster_id** | **str**|  | 

### Return type

[**Cluster**](Cluster.md)

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

# **get_cluster_deployments_clusters_cluster_id_deployments_get**
> ListResultsResponse get_cluster_deployments_clusters_cluster_id_deployments_get(cluster_id)

Get Cluster Deployments

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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    cluster_id = 'cluster_id_example' # str | 

    try:
        # Get Cluster Deployments
        api_response = await api_instance.get_cluster_deployments_clusters_cluster_id_deployments_get(cluster_id)
        print("The response of ClustersApi->get_cluster_deployments_clusters_cluster_id_deployments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_deployments_clusters_cluster_id_deployments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

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

# **get_clusters_clusters_get**
> ListResultsResponse get_clusters_clusters_get(q=q)

Get Clusters

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
    api_instance = ambient_backend_api_client.ClustersApi(api_client)
    q = '' # str |  (optional) (default to '')

    try:
        # Get Clusters
        api_response = await api_instance.get_clusters_clusters_get(q=q)
        print("The response of ClustersApi->get_clusters_clusters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_clusters_clusters_get: %s\n" % e)
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

# **patch_cluster_clusters_cluster_id_patch**
> Cluster patch_cluster_clusters_cluster_id_patch(cluster_id, body)

Patch Cluster

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
    cluster_id = 'cluster_id_example' # str | 
    body = None # object | 

    try:
        # Patch Cluster
        api_response = await api_instance.patch_cluster_clusters_cluster_id_patch(cluster_id, body)
        print("The response of ClustersApi->patch_cluster_clusters_cluster_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->patch_cluster_clusters_cluster_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **body** | **object**|  | 

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

