# DeviceAuthorization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** |  | 
**user_code** | **str** |  | 
**created_at** | **datetime** | Time when the device authorization was created | [optional] 
**expires_in** | **int** | Time in seconds until the device authorization expires | [optional] [default to 600]
**interval** | **int** | Interval in seconds to poll for the device authorization | [optional] [default to 5]
**node_id** | **int** |  | 
**user_id** | **int** |  | 
**org_id** | **int** |  | 
**id** | **int** |  | 

## Example

```python
from ambient_backend_api_client.models.device_authorization import DeviceAuthorization

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAuthorization from a JSON string
device_authorization_instance = DeviceAuthorization.from_json(json)
# print the JSON string representation of the object
print(DeviceAuthorization.to_json())

# convert the object into a dict
device_authorization_dict = device_authorization_instance.to_dict()
# create an instance of DeviceAuthorization from a dict
device_authorization_from_dict = DeviceAuthorization.from_dict(device_authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


