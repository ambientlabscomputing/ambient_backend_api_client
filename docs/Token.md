# Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**description** | **str** |  | [optional] 
**expires_at** | **datetime** |  | 
**uid** | **str** |  | 
**tombstoned** | **bool** |  | [optional] [default to False]
**user_id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**node_id** | **int** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print(Token.to_json())

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_from_dict = Token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


