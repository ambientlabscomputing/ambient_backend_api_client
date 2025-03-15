# NodeSelectOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ids** | **List[int]** |  | [optional] [default to []]
**node_names** | **List[str]** |  | [optional] [default to []]
**tags** | **List[str]** |  | [optional] [default to []]

## Example

```python
from ambient_backend_api_client.models.node_select_options import NodeSelectOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSelectOptions from a JSON string
node_select_options_instance = NodeSelectOptions.from_json(json)
# print the JSON string representation of the object
print(NodeSelectOptions.to_json())

# convert the object into a dict
node_select_options_dict = node_select_options_instance.to_dict()
# create an instance of NodeSelectOptions from a dict
node_select_options_from_dict = NodeSelectOptions.from_dict(node_select_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


