# NodeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**role** | [**NodeRoleEnum**](NodeRoleEnum.md) |  | 
**live** | **bool** | Node is live and will respond immediately to commands | [optional] [default to False]
**architecture** | [**NodeArchitectureEnum**](NodeArchitectureEnum.md) | Node architecture | 
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) |  | [optional] 
**advertised_interface** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**error** | **str** |  | [optional] 
**certificate** | **str** |  | [optional] 
**status** | [**StatusEnum**](StatusEnum.md) | Node status | [optional] 

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


