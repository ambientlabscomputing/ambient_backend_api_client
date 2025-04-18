# CreateClientSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.create_client_secret import CreateClientSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientSecret from a JSON string
create_client_secret_instance = CreateClientSecret.from_json(json)
# print the JSON string representation of the object
print(CreateClientSecret.to_json())

# convert the object into a dict
create_client_secret_dict = create_client_secret_instance.to_dict()
# create an instance of CreateClientSecret from a dict
create_client_secret_from_dict = CreateClientSecret.from_dict(create_client_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


