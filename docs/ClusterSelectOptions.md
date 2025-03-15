# ClusterSelectOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ids** | **List[int]** |  | [optional] [default to []]
**cluster_names** | **List[str]** |  | [optional] [default to []]
**tags** | **List[str]** |  | [optional] [default to []]
**run_type** | [**ClusterRunType**](ClusterRunType.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.cluster_select_options import ClusterSelectOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSelectOptions from a JSON string
cluster_select_options_instance = ClusterSelectOptions.from_json(json)
# print the JSON string representation of the object
print(ClusterSelectOptions.to_json())

# convert the object into a dict
cluster_select_options_dict = cluster_select_options_instance.to_dict()
# create an instance of ClusterSelectOptions from a dict
cluster_select_options_from_dict = ClusterSelectOptions.from_dict(cluster_select_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


