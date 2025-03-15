# RegistryNodeAssociation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** |  | 
**registry_id** | **int** |  | 
**status** | [**RegistryNodeAssociationStatusEnum**](RegistryNodeAssociationStatusEnum.md) |  | 
**error** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.registry_node_association import RegistryNodeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryNodeAssociation from a JSON string
registry_node_association_instance = RegistryNodeAssociation.from_json(json)
# print the JSON string representation of the object
print(RegistryNodeAssociation.to_json())

# convert the object into a dict
registry_node_association_dict = registry_node_association_instance.to_dict()
# create an instance of RegistryNodeAssociation from a dict
registry_node_association_from_dict = RegistryNodeAssociation.from_dict(registry_node_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


