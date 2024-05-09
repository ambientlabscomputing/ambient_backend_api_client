# ClusterCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | [optional] [default to '02439f7a-5a39-457d-b117-9a8d9effe62f']
**owner_id** | **str** |  | [optional] 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**role** | [**RoleEnum**](RoleEnum.md) |  | 
**architecture** | [**ArchitectureEnum**](ArchitectureEnum.md) |  | 
**nodes** | **List[str]** |  | 
**docker_swarm_attrs** | **object** |  | [optional] 
**site** | **str** |  | [optional] [default to '']
**manager_node** | **str** |  | [optional] 
**cluster_group** | **str** |  | [optional] [default to 'default']
**tags** | **List[str]** |  | [optional] [default to []]

## Example

```python
from ambient_backend_api_client.models.cluster_create import ClusterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreate from a JSON string
cluster_create_instance = ClusterCreate.from_json(json)
# print the JSON string representation of the object
print(ClusterCreate.to_json())

# convert the object into a dict
cluster_create_dict = cluster_create_instance.to_dict()
# create an instance of ClusterCreate from a dict
cluster_create_from_dict = ClusterCreate.from_dict(cluster_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


