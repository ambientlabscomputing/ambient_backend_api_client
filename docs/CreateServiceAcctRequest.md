# CreateServiceAcctRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**system** | **bool** | Whether the service account is a system account | [optional] [default to False]
**description** | **str** |  | [optional] 
**auth_provider_uid** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.create_service_acct_request import CreateServiceAcctRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceAcctRequest from a JSON string
create_service_acct_request_instance = CreateServiceAcctRequest.from_json(json)
# print the JSON string representation of the object
print(CreateServiceAcctRequest.to_json())

# convert the object into a dict
create_service_acct_request_dict = create_service_acct_request_instance.to_dict()
# create an instance of CreateServiceAcctRequest from a dict
create_service_acct_request_from_dict = CreateServiceAcctRequest.from_dict(create_service_acct_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


