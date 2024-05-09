# Auth0DeviceCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** |  | 
**user_code** | **str** |  | 
**verification_uri** | **str** |  | 
**verification_uri_complete** | **str** |  | 
**expires_in** | **int** |  | 
**interval** | **int** |  | 

## Example

```python
from ambient_backend_api_client.models.auth0_device_code_response import Auth0DeviceCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Auth0DeviceCodeResponse from a JSON string
auth0_device_code_response_instance = Auth0DeviceCodeResponse.from_json(json)
# print the JSON string representation of the object
print(Auth0DeviceCodeResponse.to_json())

# convert the object into a dict
auth0_device_code_response_dict = auth0_device_code_response_instance.to_dict()
# create an instance of Auth0DeviceCodeResponse from a dict
auth0_device_code_response_from_dict = Auth0DeviceCodeResponse.from_dict(auth0_device_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


