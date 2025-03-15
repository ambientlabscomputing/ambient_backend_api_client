# UpdateCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]
**docker_data** | [**DockerClusterData**](DockerClusterData.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.update_cluster import UpdateCluster

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCluster from a JSON string
update_cluster_instance = UpdateCluster.from_json(json)
# print the JSON string representation of the object
print(UpdateCluster.to_json())

# convert the object into a dict
update_cluster_dict = update_cluster_instance.to_dict()
# create an instance of UpdateCluster from a dict
update_cluster_from_dict = UpdateCluster.from_dict(update_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


