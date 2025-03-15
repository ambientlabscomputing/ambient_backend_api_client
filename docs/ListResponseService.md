# ListResponseService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Service]**](Service.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_service import ListResponseService

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseService from a JSON string
list_response_service_instance = ListResponseService.from_json(json)
# print the JSON string representation of the object
print(ListResponseService.to_json())

# convert the object into a dict
list_response_service_dict = list_response_service_instance.to_dict()
# create an instance of ListResponseService from a dict
list_response_service_from_dict = ListResponseService.from_dict(list_response_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


