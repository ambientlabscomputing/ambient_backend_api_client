# ListResponseToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**count** | **int** |  | [optional] 
**results** | [**List[Token]**](Token.md) |  | 

## Example

```python
from ambient_backend_api_client.models.list_response_token import ListResponseToken

# TODO update the JSON string below
json = "{}"
# create an instance of ListResponseToken from a JSON string
list_response_token_instance = ListResponseToken.from_json(json)
# print the JSON string representation of the object
print(ListResponseToken.to_json())

# convert the object into a dict
list_response_token_dict = list_response_token_instance.to_dict()
# create an instance of ListResponseToken from a dict
list_response_token_from_dict = ListResponseToken.from_dict(list_response_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


