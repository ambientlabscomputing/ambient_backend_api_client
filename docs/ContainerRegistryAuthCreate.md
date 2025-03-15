# ContainerRegistryAuthCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from ambient_backend_api_client.models.container_registry_auth_create import ContainerRegistryAuthCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryAuthCreate from a JSON string
container_registry_auth_create_instance = ContainerRegistryAuthCreate.from_json(json)
# print the JSON string representation of the object
print(ContainerRegistryAuthCreate.to_json())

# convert the object into a dict
container_registry_auth_create_dict = container_registry_auth_create_instance.to_dict()
# create an instance of ContainerRegistryAuthCreate from a dict
container_registry_auth_create_from_dict = ContainerRegistryAuthCreate.from_dict(container_registry_auth_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


