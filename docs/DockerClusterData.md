# DockerClusterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiated** | **bool** |  | [optional] [default to False]
**cluster_id** | **str** |  | [optional] [default to '']
**remote_managers** | **List[object]** |  | [optional] [default to []]

## Example

```python
from ambient_backend_api_client.models.docker_cluster_data import DockerClusterData

# TODO update the JSON string below
json = "{}"
# create an instance of DockerClusterData from a JSON string
docker_cluster_data_instance = DockerClusterData.from_json(json)
# print the JSON string representation of the object
print(DockerClusterData.to_json())

# convert the object into a dict
docker_cluster_data_dict = docker_cluster_data_instance.to_dict()
# create an instance of DockerClusterData from a dict
docker_cluster_data_from_dict = DockerClusterData.from_dict(docker_cluster_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


