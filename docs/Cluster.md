# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]
**status** | [**ClusterStatusEnum**](ClusterStatusEnum.md) |  | 
**docker_data** | [**DockerClusterData**](DockerClusterData.md) |  | [optional] 

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


