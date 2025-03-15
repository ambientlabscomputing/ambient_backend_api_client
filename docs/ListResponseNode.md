# ListResponseNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[NodeOutput]**](NodeOutput.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_node import ListResponseNode

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseNode from a JSON string
list_response_node_instance = ListResponseNode.from_json(json)
# print the JSON string representation of the object
print(ListResponseNode.to_json())

# convert the object into a dict
list_response_node_dict = list_response_node_instance.to_dict()
# create an instance of ListResponseNode from a dict
list_response_node_from_dict = ListResponseNode.from_dict(list_response_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


