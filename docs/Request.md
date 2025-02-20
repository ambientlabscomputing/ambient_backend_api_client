# Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | 
**owner_id** | **str** |  | 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**status** | [**RequestStatusEnum**](RequestStatusEnum.md) |  | [optional] 
**error** | **str** |  | [optional] 
**requested_ts** | **float** |  | [optional] [default to 1.715390426038406E9]
**started_ts** | **float** |  | [optional] 
**failed_ts** | **float** |  | [optional] 
**completed_ts** | **float** |  | [optional] 
**notes** | **List[str]** |  | [optional] [default to []]
**data** | **object** |  | [optional] 

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


