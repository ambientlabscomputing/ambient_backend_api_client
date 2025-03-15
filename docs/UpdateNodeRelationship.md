# UpdateNodeRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_id** | **int** |  | 
**node_id** | **int** |  | 
**status** | [**CommandStatusEnum**](CommandStatusEnum.md) |  | [optional] 
**error** | **str** |  | [optional] 
**output** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.update_node_relationship import UpdateNodeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodeRelationship from a JSON string
update_node_relationship_instance = UpdateNodeRelationship.from_json(json)
# print the JSON string representation of the object
print(UpdateNodeRelationship.to_json())

# convert the object into a dict
update_node_relationship_dict = update_node_relationship_instance.to_dict()
# create an instance of UpdateNodeRelationship from a dict
update_node_relationship_from_dict = UpdateNodeRelationship.from_dict(update_node_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


