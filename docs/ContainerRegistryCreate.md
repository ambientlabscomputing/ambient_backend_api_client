# ContainerRegistryCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**url** | **str** |  | 
**registry_type** | [**ContainerRegistryType**](ContainerRegistryType.md) |  | 

## Example

```python
from ambient_backend_api_client.models.container_registry_create import ContainerRegistryCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryCreate from a JSON string
container_registry_create_instance = ContainerRegistryCreate.from_json(json)
# print the JSON string representation of the object
print(ContainerRegistryCreate.to_json())

# convert the object into a dict
container_registry_create_dict = container_registry_create_instance.to_dict()
# create an instance of ContainerRegistryCreate from a dict
container_registry_create_from_dict = ContainerRegistryCreate.from_dict(container_registry_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


