# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | 
**owner_id** | **str** |  | 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**account_type** | [**AccountType**](AccountType.md) |  | [optional] 
**creation_method** | [**CreationMethod**](CreationMethod.md) |  | [optional] 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**role** | [**UserRoleEnum**](UserRoleEnum.md) |  | [optional] 
**preferences** | [**UserPreferences**](UserPreferences.md) |  | [optional] 
**auth_provider_uid** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**is_super_admin** | **bool** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


