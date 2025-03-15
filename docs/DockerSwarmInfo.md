# DockerSwarmInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the node in the swarm | [optional] [default to '']
**node_addr** | **str** | Address of the node in the swarm | [optional] [default to '']
**local_node_state** | **str** | Local node state | [optional] [default to '']
**error** | **str** | Error message | [optional] [default to '']

## Example

```python
from ambient_backend_api_client.models.docker_swarm_info import DockerSwarmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DockerSwarmInfo from a JSON string
docker_swarm_info_instance = DockerSwarmInfo.from_json(json)
# print the JSON string representation of the object
print(DockerSwarmInfo.to_json())

# convert the object into a dict
docker_swarm_info_dict = docker_swarm_info_instance.to_dict()
# create an instance of DockerSwarmInfo from a dict
docker_swarm_info_from_dict = DockerSwarmInfo.from_dict(docker_swarm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


