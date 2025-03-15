# ListResponseContainerRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[ContainerRegistry]**](ContainerRegistry.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_container_registry import ListResponseContainerRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseContainerRegistry from a JSON string
list_response_container_registry_instance = ListResponseContainerRegistry.from_json(json)
# print the JSON string representation of the object
print(ListResponseContainerRegistry.to_json())

# convert the object into a dict
list_response_container_registry_dict = list_response_container_registry_instance.to_dict()
# create an instance of ListResponseContainerRegistry from a dict
list_response_container_registry_from_dict = ListResponseContainerRegistry.from_dict(list_response_container_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


