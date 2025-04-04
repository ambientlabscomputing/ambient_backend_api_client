# NodeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | 
**user_id** | **int** |  | 
**role** | [**NodeRoleEnum**](NodeRoleEnum.md) |  | 
**live** | **bool** | Node is live and will respond immediately to commands | [optional] [default to False]
**architecture** | [**NodeArchitectureEnum**](NodeArchitectureEnum.md) | Node architecture | 
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) |  | [optional] 
**advertised_interface** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**error** | **str** |  | [optional] 
**certificate** | **str** |  | [optional] 
**status** | [**StatusEnum**](StatusEnum.md) |  | 
**cluster_id** | **int** |  | [optional] 
**docker_swarm_info** | [**DockerSwarmInfo**](DockerSwarmInfo.md) |  | [optional] 
**device_authorization** | [**DeviceAuthorization**](DeviceAuthorization.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.node_input import NodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInput from a JSON string
node_input_instance = NodeInput.from_json(json)
# print the JSON string representation of the object
print(NodeInput.to_json())

# convert the object into a dict
node_input_dict = node_input_instance.to_dict()
# create an instance of NodeInput from a dict
node_input_from_dict = NodeInput.from_dict(node_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


