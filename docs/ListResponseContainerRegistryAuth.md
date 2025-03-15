# ListResponseContainerRegistryAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[ContainerRegistryAuth]**](ContainerRegistryAuth.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_container_registry_auth import ListResponseContainerRegistryAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseContainerRegistryAuth from a JSON string
list_response_container_registry_auth_instance = ListResponseContainerRegistryAuth.from_json(json)
# print the JSON string representation of the object
print(ListResponseContainerRegistryAuth.to_json())

# convert the object into a dict
list_response_container_registry_auth_dict = list_response_container_registry_auth_instance.to_dict()
# create an instance of ListResponseContainerRegistryAuth from a dict
list_response_container_registry_auth_from_dict = ListResponseContainerRegistryAuth.from_dict(list_response_container_registry_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


