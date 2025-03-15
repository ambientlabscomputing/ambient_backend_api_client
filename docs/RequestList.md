# RequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**timestamp** | **datetime** |  | [optional] 
**results** | [**List[Request]**](Request.md) |  | 

## Example

```python
from ambient_backend_api_client.models.request_list import RequestList

# TODO update the JSON string below
json = "{}"
# create an instance of RequestList from a JSON string
request_list_instance = RequestList.from_json(json)
# print the JSON string representation of the object
print(RequestList.to_json())

# convert the object into a dict
request_list_dict = request_list_instance.to_dict()
# create an instance of RequestList from a dict
request_list_from_dict = RequestList.from_dict(request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


