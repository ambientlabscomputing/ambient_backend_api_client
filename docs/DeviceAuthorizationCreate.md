# DeviceAuthorizationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Device code for authorization | [optional] 
**user_code** | **str** | User code for authorization | [optional] 
**created_at** | **datetime** | Time when the device authorization was created | [optional] 
**expires_in** | **int** | Time in seconds until the device authorization expires | [optional] [default to 600]
**interval** | **int** | Interval in seconds to poll for the device authorization | [optional] [default to 5]
**node_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.device_authorization_create import DeviceAuthorizationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAuthorizationCreate from a JSON string
device_authorization_create_instance = DeviceAuthorizationCreate.from_json(json)
# print the JSON string representation of the object
print(DeviceAuthorizationCreate.to_json())

# convert the object into a dict
device_authorization_create_dict = device_authorization_create_instance.to_dict()
# create an instance of DeviceAuthorizationCreate from a dict
device_authorization_create_from_dict = DeviceAuthorizationCreate.from_dict(device_authorization_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


