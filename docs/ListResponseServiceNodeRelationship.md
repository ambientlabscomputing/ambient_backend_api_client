# ListResponseServiceNodeRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[ServiceNodeRelationship]**](ServiceNodeRelationship.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_service_node_relationship import ListResponseServiceNodeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseServiceNodeRelationship from a JSON string
list_response_service_node_relationship_instance = ListResponseServiceNodeRelationship.from_json(json)
# print the JSON string representation of the object
print(ListResponseServiceNodeRelationship.to_json())

# convert the object into a dict
list_response_service_node_relationship_dict = list_response_service_node_relationship_instance.to_dict()
# create an instance of ListResponseServiceNodeRelationship from a dict
list_response_service_node_relationship_from_dict = ListResponseServiceNodeRelationship.from_dict(list_response_service_node_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


