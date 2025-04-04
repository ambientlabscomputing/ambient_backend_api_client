# PostRegistriesCredsTriggerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** |  | 
**requested_ts** | **str** |  | [optional] [default to '2025-04-03T21:01:12.078425']
**location_root** | **str** |  | [optional] [default to 'http://localhost:8001/requests/']
**refresh_interval** | **int** |  | [optional] [default to 10]
**location** | **str** |  | [optional] 
**creds** | [**ContainerRegistryAuth**](ContainerRegistryAuth.md) |  | 
**request** | [**Request**](Request.md) |  | 
**event** | [**Event**](Event.md) |  | 

## Example

```python
from ambient_backend_api_client.models.post_registries_creds_trigger_response import PostRegistriesCredsTriggerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRegistriesCredsTriggerResponse from a JSON string
post_registries_creds_trigger_response_instance = PostRegistriesCredsTriggerResponse.from_json(json)
# print the JSON string representation of the object
print(PostRegistriesCredsTriggerResponse.to_json())

# convert the object into a dict
post_registries_creds_trigger_response_dict = post_registries_creds_trigger_response_instance.to_dict()
# create an instance of PostRegistriesCredsTriggerResponse from a dict
post_registries_creds_trigger_response_from_dict = PostRegistriesCredsTriggerResponse.from_dict(post_registries_creds_trigger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


