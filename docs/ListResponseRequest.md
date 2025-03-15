# ListResponseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Request]**](Request.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_request import ListResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseRequest from a JSON string
list_response_request_instance = ListResponseRequest.from_json(json)
# print the JSON string representation of the object
print(ListResponseRequest.to_json())

# convert the object into a dict
list_response_request_dict = list_response_request_instance.to_dict()
# create an instance of ListResponseRequest from a dict
list_response_request_from_dict = ListResponseRequest.from_dict(list_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


