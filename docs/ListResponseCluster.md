# ListResponseCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Cluster]**](Cluster.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_cluster import ListResponseCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseCluster from a JSON string
list_response_cluster_instance = ListResponseCluster.from_json(json)
# print the JSON string representation of the object
print(ListResponseCluster.to_json())

# convert the object into a dict
list_response_cluster_dict = list_response_cluster_instance.to_dict()
# create an instance of ListResponseCluster from a dict
list_response_cluster_from_dict = ListResponseCluster.from_dict(list_response_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


