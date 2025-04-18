# DeployServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** |  | 
**requested_ts** | **str** |  | [optional] [default to '2025-04-17T03:38:54.771014']
**location_root** | **str** |  | [optional] [default to 'http://localhost:8001/requests/']
**refresh_interval** | **int** |  | [optional] [default to 10]
**location** | **str** |  | [optional] 
**service** | [**Service**](Service.md) |  | 
**request** | [**Request**](Request.md) |  | 

## Example

```python
from ambient_backend_api_client.models.deploy_service_response import DeployServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployServiceResponse from a JSON string
deploy_service_response_instance = DeployServiceResponse.from_json(json)
# print the JSON string representation of the object
print(DeployServiceResponse.to_json())

# convert the object into a dict
deploy_service_response_dict = deploy_service_response_instance.to_dict()
# create an instance of DeployServiceResponse from a dict
deploy_service_response_from_dict = DeployServiceResponse.from_dict(deploy_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


