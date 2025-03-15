# SetNodeAdvertisedInterfaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** |  | 
**advertised_interface_id** | **int** |  | [optional] 
**advertised_interface_ipv4** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.set_node_advertised_interface_request import SetNodeAdvertisedInterfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetNodeAdvertisedInterfaceRequest from a JSON string
set_node_advertised_interface_request_instance = SetNodeAdvertisedInterfaceRequest.from_json(json)
# print the JSON string representation of the object
print(SetNodeAdvertisedInterfaceRequest.to_json())

# convert the object into a dict
set_node_advertised_interface_request_dict = set_node_advertised_interface_request_instance.to_dict()
# create an instance of SetNodeAdvertisedInterfaceRequest from a dict
set_node_advertised_interface_request_from_dict = SetNodeAdvertisedInterfaceRequest.from_dict(set_node_advertised_interface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


