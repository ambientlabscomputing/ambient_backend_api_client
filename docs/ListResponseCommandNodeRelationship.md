# ListResponseCommandNodeRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[CommandNodeRelationship]**](CommandNodeRelationship.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_command_node_relationship import ListResponseCommandNodeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseCommandNodeRelationship from a JSON string
list_response_command_node_relationship_instance = ListResponseCommandNodeRelationship.from_json(json)
# print the JSON string representation of the object
print(ListResponseCommandNodeRelationship.to_json())

# convert the object into a dict
list_response_command_node_relationship_dict = list_response_command_node_relationship_instance.to_dict()
# create an instance of ListResponseCommandNodeRelationship from a dict
list_response_command_node_relationship_from_dict = ListResponseCommandNodeRelationship.from_dict(list_response_command_node_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


