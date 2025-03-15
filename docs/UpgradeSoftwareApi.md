# ambient_backend_api_client.UpgradeSoftwareApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_version_upgrade_software_versions_get**](UpgradeSoftwareApi.md#list_version_upgrade_software_versions_get) | **GET** /upgrade_software/versions | List Version


# **list_version_upgrade_software_versions_get**
> List[AppVersion] list_version_upgrade_software_versions_get()

List Version

### Example


```python
import ambient_backend_api_client
from ambient_backend_api_client.models.app_version import AppVersion
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
    api_instance = ambient_backend_api_client.UpgradeSoftwareApi(api_client)

    try:
        # List Version
        api_response = await api_instance.list_version_upgrade_software_versions_get()
        print("The response of UpgradeSoftwareApi->list_version_upgrade_software_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpgradeSoftwareApi->list_version_upgrade_software_versions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppVersion]**](AppVersion.md)

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

