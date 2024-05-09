# PostClustersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**requested_ts** | **str** |  | [optional] [default to 'Wed May  8 20:30:12 2024']
**location_root** | **str** |  | [optional] [default to 'http://localhost:8001/requests/']
**refresh_interval** | **int** |  | [optional] [default to 10]
**cluster** | [**Cluster**](Cluster.md) |  | 

## Example

```python
from ambient_backend_api_client.models.post_clusters_response import PostClustersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClustersResponse from a JSON string
post_clusters_response_instance = PostClustersResponse.from_json(json)
# print the JSON string representation of the object
print(PostClustersResponse.to_json())

# convert the object into a dict
post_clusters_response_dict = post_clusters_response_instance.to_dict()
# create an instance of PostClustersResponse from a dict
post_clusters_response_from_dict = PostClustersResponse.from_dict(post_clusters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


