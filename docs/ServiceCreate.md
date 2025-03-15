# ServiceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**desired_state** | [**ServiceState**](ServiceState.md) | Desired state of the service | [optional] 
**requested_service_spec** | [**RequestedServiceSpec**](RequestedServiceSpec.md) |  | 
**node_ids** | **List[int]** |  | [optional] [default to []]

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


