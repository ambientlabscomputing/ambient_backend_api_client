# ServiceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**image** | **str** |  | 
**replicas** | **int** |  | 
**cluster_groups** | **List[str]** |  | [optional] [default to [default]]
**tags** | **List[str]** |  | [optional] [default to []]
**clusters** | **List[str]** |  | [optional] [default to []]
**ports** | **List[str]** |  | [optional] 
**compose_location** | **str** |  | [optional] 
**state** | [**ServiceState**](ServiceState.md) |  | [optional] 
**status** | [**ServiceStatusEnum**](ServiceStatusEnum.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.service_create import ServiceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCreate from a JSON string
service_create_instance = ServiceCreate.from_json(json)
# print the JSON string representation of the object
print(ServiceCreate.to_json())

# convert the object into a dict
service_create_dict = service_create_instance.to_dict()
# create an instance of ServiceCreate from a dict
service_create_from_dict = ServiceCreate.from_dict(service_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


