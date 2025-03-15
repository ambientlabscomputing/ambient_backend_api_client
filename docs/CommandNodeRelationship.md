# CommandNodeRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_id** | **int** |  | 
**node_id** | **int** |  | 
**status** | [**CommandStatusEnum**](CommandStatusEnum.md) |  | 
**error** | **str** |  | [optional] 
**output** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.command_node_relationship import CommandNodeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of CommandNodeRelationship from a JSON string
command_node_relationship_instance = CommandNodeRelationship.from_json(json)
# print the JSON string representation of the object
print(CommandNodeRelationship.to_json())

# convert the object into a dict
command_node_relationship_dict = command_node_relationship_instance.to_dict()
# create an instance of CommandNodeRelationship from a dict
command_node_relationship_from_dict = CommandNodeRelationship.from_dict(command_node_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


