# ListResponseCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Command]**](Command.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_command import ListResponseCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseCommand from a JSON string
list_response_command_instance = ListResponseCommand.from_json(json)
# print the JSON string representation of the object
print(ListResponseCommand.to_json())

# convert the object into a dict
list_response_command_dict = list_response_command_instance.to_dict()
# create an instance of ListResponseCommand from a dict
list_response_command_from_dict = ListResponseCommand.from_dict(list_response_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


