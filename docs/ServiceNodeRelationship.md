# ServiceNodeRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **int** | ID of the service | 
**node_id** | **int** | ID of the node | 
**state** | [**ServiceState**](ServiceState.md) | State of the service on the node | [optional] 
**status** | [**ServiceStatusEnum**](ServiceStatusEnum.md) | Status of the service on the node | [optional] 
**error** | **str** |  | [optional] 
**docker_service_attrs** | **object** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.service_node_relationship import ServiceNodeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNodeRelationship from a JSON string
service_node_relationship_instance = ServiceNodeRelationship.from_json(json)
# print the JSON string representation of the object
print(ServiceNodeRelationship.to_json())

# convert the object into a dict
service_node_relationship_dict = service_node_relationship_instance.to_dict()
# create an instance of ServiceNodeRelationship from a dict
service_node_relationship_from_dict = ServiceNodeRelationship.from_dict(service_node_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


