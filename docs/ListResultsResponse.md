# ListResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**timestamp** | **str** |  | [optional] [default to 'Wed May  8 20:38:23 2024']
**results** | **List[object]** |  | 

## Example

```python
from ambient_backend_api_client.models.list_results_response import ListResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListResultsResponse from a JSON string
list_results_response_instance = ListResultsResponse.from_json(json)
# print the JSON string representation of the object
print(ListResultsResponse.to_json())

# convert the object into a dict
list_results_response_dict = list_results_response_instance.to_dict()
# create an instance of ListResultsResponse from a dict
list_results_response_from_dict = ListResultsResponse.from_dict(list_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


