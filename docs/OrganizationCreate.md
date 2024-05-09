# OrganizationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**identifier** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_type** | [**OwnerTypeEnum**](OwnerTypeEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**requests** | **List[str]** |  | [optional] [default to []]
**notifications** | **List[str]** |  | [optional] [default to []]
**subscription** | [**SubscriptionModelEnum**](SubscriptionModelEnum.md) |  | 
**root_email** | **str** |  | 
**okta_group_id** | **str** |  | [optional] 
**auth0_org_id** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.organization_create import OrganizationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreate from a JSON string
organization_create_instance = OrganizationCreate.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreate.to_json())

# convert the object into a dict
organization_create_dict = organization_create_instance.to_dict()
# create an instance of OrganizationCreate from a dict
organization_create_from_dict = OrganizationCreate.from_dict(organization_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


