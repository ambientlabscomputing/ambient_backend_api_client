# ContainerRegistryAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**id** | **int** |  | 
**registry_id** | **int** |  | 

## Example

```python
from ambient_backend_api_client.models.container_registry_auth import ContainerRegistryAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryAuth from a JSON string
container_registry_auth_instance = ContainerRegistryAuth.from_json(json)
# print the JSON string representation of the object
print(ContainerRegistryAuth.to_json())

# convert the object into a dict
container_registry_auth_dict = container_registry_auth_instance.to_dict()
# create an instance of ContainerRegistryAuth from a dict
container_registry_auth_from_dict = ContainerRegistryAuth.from_dict(container_registry_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


