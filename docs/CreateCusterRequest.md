# CreateCusterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_data** | [**ClusterCreate**](ClusterCreate.md) |  | 
**node_ids** | **List[int]** |  | [optional] [default to []]

## Example

```python
from ambient_backend_api_client.models.create_custer_request import CreateCusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCusterRequest from a JSON string
create_custer_request_instance = CreateCusterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCusterRequest.to_json())

# convert the object into a dict
create_custer_request_dict = create_custer_request_instance.to_dict()
# create an instance of CreateCusterRequest from a dict
create_custer_request_from_dict = CreateCusterRequest.from_dict(create_custer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


