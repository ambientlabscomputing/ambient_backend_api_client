# JWTClaims


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss** | **str** |  | 
**sub** | **str** |  | 
**aud** | [**Aud**](Aud.md) |  | [optional] 
**iat** | **int** |  | 
**exp** | **int** |  | 
**azp** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**preferred_username** | **str** |  | [optional] 
**realm_access** | [**RealmAccess**](RealmAccess.md) |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.jwt_claims import JWTClaims

# TODO update the JSON string below
json = "{}"
# create an instance of JWTClaims from a JSON string
jwt_claims_instance = JWTClaims.from_json(json)
# print the JSON string representation of the object
print(JWTClaims.to_json())

# convert the object into a dict
jwt_claims_dict = jwt_claims_instance.to_dict()
# create an instance of JWTClaims from a dict
jwt_claims_from_dict = JWTClaims.from_dict(jwt_claims_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


