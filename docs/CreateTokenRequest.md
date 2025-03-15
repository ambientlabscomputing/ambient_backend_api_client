# CreateTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | [**TokenType**](TokenType.md) |  | 
**duration** | **int** |  | [optional] [default to 3600]
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**node_id** | **int** |  | [optional] 
**request_type** | [**TokenRequestType**](TokenRequestType.md) |  | 

## Example

```python
from ambient_backend_api_client.models.create_token_request import CreateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenRequest from a JSON string
create_token_request_instance = CreateTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTokenRequest.to_json())

# convert the object into a dict
create_token_request_dict = create_token_request_instance.to_dict()
# create an instance of CreateTokenRequest from a dict
create_token_request_from_dict = CreateTokenRequest.from_dict(create_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


