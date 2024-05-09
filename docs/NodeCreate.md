# NodeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**role** | [**NodeRoleEnum**](NodeRoleEnum.md) |  | 
**architecture** | [**NodeArchitectureEnum**](NodeArchitectureEnum.md) |  | 
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) |  | [optional] 
**last_seen** | **str** |  | [optional] 
**status** | [**StatusEnumInput**](StatusEnumInput.md) |  | [optional] 
**cluster** | **str** |  | [optional] 
**authorization** | [**Auth0DeviceCodeResponse**](Auth0DeviceCodeResponse.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.node_create import NodeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of NodeCreate from a JSON string
node_create_instance = NodeCreate.from_json(json)
# print the JSON string representation of the object
print(NodeCreate.to_json())

# convert the object into a dict
node_create_dict = node_create_instance.to_dict()
# create an instance of NodeCreate from a dict
node_create_from_dict = NodeCreate.from_dict(node_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


