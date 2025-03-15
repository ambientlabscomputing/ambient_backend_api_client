# ambient_backend_api_client.CommandsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_command_commands_command_id_get**](CommandsApi.md#get_command_commands_command_id_get) | **GET** /commands/{command_id} | Get Command
[**get_command_outputs_commands_command_id_outputs_get**](CommandsApi.md#get_command_outputs_commands_command_id_outputs_get) | **GET** /commands/{command_id}/outputs | Get Command Outputs
[**get_commands_commands_get**](CommandsApi.md#get_commands_commands_get) | **GET** /commands/ | Get Commands
[**post_command_commands_post**](CommandsApi.md#post_command_commands_post) | **POST** /commands/ | Post Command
[**update_command_outputs_commands_outputs_put**](CommandsApi.md#update_command_outputs_commands_outputs_put) | **PUT** /commands/outputs | Update Command Outputs


# **get_command_commands_command_id_get**
> Command get_command_commands_command_id_get(command_id)

Get Command

Get command

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.command import Command
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
    api_instance = ambient_backend_api_client.CommandsApi(api_client)
    command_id = 56 # int | 

    try:
        # Get Command
        api_response = await api_instance.get_command_commands_command_id_get(command_id)
        print("The response of CommandsApi->get_command_commands_command_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->get_command_commands_command_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**|  | 

### Return type

[**Command**](Command.md)

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

# **get_command_outputs_commands_command_id_outputs_get**
> ListResponseCommandNodeRelationship get_command_outputs_commands_command_id_outputs_get(command_id, node_id=node_id)

Get Command Outputs

Get command

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_command_node_relationship import ListResponseCommandNodeRelationship
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
    api_instance = ambient_backend_api_client.CommandsApi(api_client)
    command_id = 56 # int | 
    node_id = 56 # int |  (optional)

    try:
        # Get Command Outputs
        api_response = await api_instance.get_command_outputs_commands_command_id_outputs_get(command_id, node_id=node_id)
        print("The response of CommandsApi->get_command_outputs_commands_command_id_outputs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->get_command_outputs_commands_command_id_outputs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **int**|  | 
 **node_id** | **int**|  | [optional] 

### Return type

[**ListResponseCommandNodeRelationship**](ListResponseCommandNodeRelationship.md)

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

# **get_commands_commands_get**
> ListResponseCommand get_commands_commands_get()

Get Commands

Get commands

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.list_response_command import ListResponseCommand
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
    api_instance = ambient_backend_api_client.CommandsApi(api_client)

    try:
        # Get Commands
        api_response = await api_instance.get_commands_commands_get()
        print("The response of CommandsApi->get_commands_commands_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->get_commands_commands_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListResponseCommand**](ListResponseCommand.md)

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

# **post_command_commands_post**
> Command post_command_commands_post(command_create)

Post Command

Create a command

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.command import Command
from ambient_backend_api_client.models.command_create import CommandCreate
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
    api_instance = ambient_backend_api_client.CommandsApi(api_client)
    command_create = ambient_backend_api_client.CommandCreate() # CommandCreate | 

    try:
        # Post Command
        api_response = await api_instance.post_command_commands_post(command_create)
        print("The response of CommandsApi->post_command_commands_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->post_command_commands_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_create** | [**CommandCreate**](CommandCreate.md)|  | 

### Return type

[**Command**](Command.md)

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

# **update_command_outputs_commands_outputs_put**
> CommandNodeRelationship update_command_outputs_commands_outputs_put(update_node_relationship)

Update Command Outputs

Update command outputs

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import ambient_backend_api_client
from ambient_backend_api_client.models.command_node_relationship import CommandNodeRelationship
from ambient_backend_api_client.models.update_node_relationship import UpdateNodeRelationship
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
    api_instance = ambient_backend_api_client.CommandsApi(api_client)
    update_node_relationship = ambient_backend_api_client.UpdateNodeRelationship() # UpdateNodeRelationship | 

    try:
        # Update Command Outputs
        api_response = await api_instance.update_command_outputs_commands_outputs_put(update_node_relationship)
        print("The response of CommandsApi->update_command_outputs_commands_outputs_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommandsApi->update_command_outputs_commands_outputs_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_node_relationship** | [**UpdateNodeRelationship**](UpdateNodeRelationship.md)|  | 

### Return type

[**CommandNodeRelationship**](CommandNodeRelationship.md)

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

