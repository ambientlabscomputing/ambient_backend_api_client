# RealmAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** |  | 

## Example

```python
from ambient_backend_api_client.models.realm_access import RealmAccess

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAccess from a JSON string
realm_access_instance = RealmAccess.from_json(json)
# print the JSON string representation of the object
print(RealmAccess.to_json())

# convert the object into a dict
realm_access_dict = realm_access_instance.to_dict()
# create an instance of RealmAccess from a dict
realm_access_from_dict = RealmAccess.from_dict(realm_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


