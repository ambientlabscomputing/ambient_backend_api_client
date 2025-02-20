# NetworkInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InterfaceTypeEnum**](InterfaceTypeEnum.md) |  | 
**name** | **str** |  | 
**ipv4_address** | **str** |  | [optional] 
**ipv6_address** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**netmask** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**broadcast** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInterface.to_json())

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_from_dict = NetworkInterface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


