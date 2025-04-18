# DeviceAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Device code for authorization | [optional] 
**user_code** | **str** | User code for authorization | [optional] 
**created_at** | **datetime** | Time when the device authorization was created | [optional] 
**expires_in** | **int** | Time in seconds until the device authorization expires | [optional] [default to 600]
**interval** | **int** | Interval in seconds to poll for the device authorization | [optional] [default to 5]
**verification_uri** | **str** | URI to verify the device authorization | [optional] [default to 'https://portal.ambientlabsdev.io/device-authorization']
**verification_uri_complete** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.device_authorization_request import DeviceAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAuthorizationRequest from a JSON string
device_authorization_request_instance = DeviceAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceAuthorizationRequest.to_json())

# convert the object into a dict
device_authorization_request_dict = device_authorization_request_instance.to_dict()
# create an instance of DeviceAuthorizationRequest from a dict
device_authorization_request_from_dict = DeviceAuthorizationRequest.from_dict(device_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


