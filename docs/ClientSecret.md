# ClientSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**path** | **str** |  | 
**value_hash** | **str** |  | 
**description** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**org_id** | **int** |  | [optional] 
**updated_ts** | **datetime** |  | 
**updated_by** | **str** |  | 
**internal** | **bool** |  | [optional] [default to False]

## Example

```python
from ambient_backend_api_client.models.client_secret import ClientSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSecret from a JSON string
client_secret_instance = ClientSecret.from_json(json)
# print the JSON string representation of the object
print(ClientSecret.to_json())

# convert the object into a dict
client_secret_dict = client_secret_instance.to_dict()
# create an instance of ClientSecret from a dict
client_secret_from_dict = ClientSecret.from_dict(client_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


