# TokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | [**GrantType**](GrantType.md) | The type of token request | 
**duration** | **int** | The duration of the token in seconds | [optional] [default to 3600]
**token_description** | **str** |  | [optional] 
**request_type** | [**TokenRequestType**](TokenRequestType.md) | The type of token request (node or api) | 
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**node_id** | **int** |  | [optional] 
**device_code** | **str** |  | [optional] 
**user_code** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.token_request import TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequest from a JSON string
token_request_instance = TokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRequest.to_json())

# convert the object into a dict
token_request_dict = token_request_instance.to_dict()
# create an instance of TokenRequest from a dict
token_request_from_dict = TokenRequest.from_dict(token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


