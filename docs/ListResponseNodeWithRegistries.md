# ListResponseNodeWithRegistries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[NodeWithRegistries]**](NodeWithRegistries.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_node_with_registries import ListResponseNodeWithRegistries

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseNodeWithRegistries from a JSON string
list_response_node_with_registries_instance = ListResponseNodeWithRegistries.from_json(json)
# print the JSON string representation of the object
print(ListResponseNodeWithRegistries.to_json())

# convert the object into a dict
list_response_node_with_registries_dict = list_response_node_with_registries_instance.to_dict()
# create an instance of ListResponseNodeWithRegistries from a dict
list_response_node_with_registries_from_dict = ListResponseNodeWithRegistries.from_dict(list_response_node_with_registries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


