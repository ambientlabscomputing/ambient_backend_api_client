# Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**status** | [**RequestStatusEnum**](RequestStatusEnum.md) |  | [optional] 
**error** | **str** |  | [optional] 
**requested_ts** | **str** |  | [optional] 
**started_ts** | **str** |  | [optional] 
**failed_ts** | **str** |  | [optional] 
**completed_ts** | **str** |  | [optional] 
**notes** | **List[str]** |  | [optional] [default to []]
**data** | [**Data**](Data.md) |  | [optional] 
**registry_id** | **int** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.request import Request

# TODO update the JSON string below
json = "{}"
# create an instance of Request from a JSON string
request_instance = Request.from_json(json)
# print the JSON string representation of the object
print(Request.to_json())

# convert the object into a dict
request_dict = request_instance.to_dict()
# create an instance of Request from a dict
request_from_dict = Request.from_dict(request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


