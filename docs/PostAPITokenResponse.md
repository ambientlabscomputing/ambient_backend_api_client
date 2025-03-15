# PostAPITokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from ambient_backend_api_client.models.post_api_token_response import PostAPITokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAPITokenResponse from a JSON string
post_api_token_response_instance = PostAPITokenResponse.from_json(json)
# print the JSON string representation of the object
print(PostAPITokenResponse.to_json())

# convert the object into a dict
post_api_token_response_dict = post_api_token_response_instance.to_dict()
# create an instance of PostAPITokenResponse from a dict
post_api_token_response_from_dict = PostAPITokenResponse.from_dict(post_api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


