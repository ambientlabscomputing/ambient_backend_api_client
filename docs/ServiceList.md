# ServiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**timestamp** | **str** |  | [optional] [default to 'Wed May  8 19:55:26 2024']
**results** | [**List[Service]**](Service.md) |  | 

## Example

```python
from ambient_backend_api_client.models.service_list import ServiceList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceList from a JSON string
service_list_instance = ServiceList.from_json(json)
# print the JSON string representation of the object
print(ServiceList.to_json())

# convert the object into a dict
service_list_dict = service_list_instance.to_dict()
# create an instance of ServiceList from a dict
service_list_from_dict = ServiceList.from_dict(service_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


