# CommandCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_list** | **List[str]** |  | [optional] 
**command_str** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] 
**store_output** | **bool** |  | [optional] [default to False]
**workdir** | **str** |  | [optional] 
**os_user** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**shell** | **bool** |  | [optional] [default to False]
**node_options** | [**NodeSelectOptions**](NodeSelectOptions.md) |  | [optional] 
**cluster_options** | [**ClusterSelectOptions**](ClusterSelectOptions.md) |  | [optional] 
**command** | [**Command1**](Command1.md) |  | 

## Example

```python
from ambient_backend_api_client.models.command_create import CommandCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CommandCreate from a JSON string
command_create_instance = CommandCreate.from_json(json)
# print the JSON string representation of the object
print(CommandCreate.to_json())

# convert the object into a dict
command_create_dict = command_create_instance.to_dict()
# create an instance of CommandCreate from a dict
command_create_from_dict = CommandCreate.from_dict(command_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


