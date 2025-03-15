# RequestedServiceSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**service_id** | **int** |  | [optional] 
**image** | **str** | Docker image to deploy | 
**tags** | **List[str]** | List of tags to apply to the service | [optional] [default to []]
**ports** | **List[str]** | List of ports to expose | [optional] [default to []]
**replicas** | **int** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**env_vars** | **List[str]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**mounts** | **List[str]** |  | [optional] 
**networks** | **List[str]** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.requested_service_spec import RequestedServiceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedServiceSpec from a JSON string
requested_service_spec_instance = RequestedServiceSpec.from_json(json)
# print the JSON string representation of the object
print(RequestedServiceSpec.to_json())

# convert the object into a dict
requested_service_spec_dict = requested_service_spec_instance.to_dict()
# create an instance of RequestedServiceSpec from a dict
requested_service_spec_from_dict = RequestedServiceSpec.from_dict(requested_service_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


