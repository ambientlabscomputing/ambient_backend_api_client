# NodeWithRegistries


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
**registry_associations** | [**List[RegistryNodeAssociation]**](RegistryNodeAssociation.md) |  | [optional] [default to []]
**registries** | [**List[ContainerRegistry]**](ContainerRegistry.md) |  | [optional] [default to []]

## Example

```python
from ambient_backend_api_client.models.node_with_registries import NodeWithRegistries

# TODO update the JSON string below
json = "{}"
# create an instance of NodeWithRegistries from a JSON string
node_with_registries_instance = NodeWithRegistries.from_json(json)
# print the JSON string representation of the object
print(NodeWithRegistries.to_json())

# convert the object into a dict
node_with_registries_dict = node_with_registries_instance.to_dict()
# create an instance of NodeWithRegistries from a dict
node_with_registries_from_dict = NodeWithRegistries.from_dict(node_with_registries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


