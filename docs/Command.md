# Command


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
**id** | **int** |  | 
**user_id** | **int** |  | 
**org_id** | **int** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from ambient_backend_api_client.models.command import Command

# TODO update the JSON string below
json = "{}"
# create an instance of Command from a JSON string
command_instance = Command.from_json(json)
# print the JSON string representation of the object
print(Command.to_json())

# convert the object into a dict
command_dict = command_instance.to_dict()
# create an instance of Command from a dict
command_from_dict = Command.from_dict(command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


