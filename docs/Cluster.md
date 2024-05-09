# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | [optional] [default to '3e880c1c-5fa7-414c-92b4-d58119c93ee7']
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
**status** | [**ModelsClusterStatusEnum**](ModelsClusterStatusEnum.md) |  | 

## Example

```python
from ambient_backend_api_client.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


