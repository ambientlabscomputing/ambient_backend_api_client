# Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | 
**owner_id** | **str** |  | [optional] 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**role** | [**NodeRoleEnum**](NodeRoleEnum.md) |  | 
**architecture** | [**NodeArchitectureEnum**](NodeArchitectureEnum.md) |  | 
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) |  | [optional] 
**last_seen** | **str** |  | [optional] 
**status** | [**ModelsNodeStatusEnum**](ModelsNodeStatusEnum.md) |  | 
**cluster** | **str** |  | [optional] 
**authorization** | [**Auth0DeviceCodeResponse**](Auth0DeviceCodeResponse.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


