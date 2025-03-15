# ListResponseNetworkInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[NetworkInterface]**](NetworkInterface.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_network_interface import ListResponseNetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseNetworkInterface from a JSON string
list_response_network_interface_instance = ListResponseNetworkInterface.from_json(json)
# print the JSON string representation of the object
print(ListResponseNetworkInterface.to_json())

# convert the object into a dict
list_response_network_interface_dict = list_response_network_interface_instance.to_dict()
# create an instance of ListResponseNetworkInterface from a dict
list_response_network_interface_from_dict = ListResponseNetworkInterface.from_dict(list_response_network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


