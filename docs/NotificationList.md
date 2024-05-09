# NotificationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**timestamp** | **str** |  | [optional] [default to 'Wed May  8 19:55:26 2024']
**results** | [**List[Notification]**](Notification.md) |  | 

## Example

```python
from ambient_backend_api_client.models.notification_list import NotificationList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationList from a JSON string
notification_list_instance = NotificationList.from_json(json)
# print the JSON string representation of the object
print(NotificationList.to_json())

# convert the object into a dict
notification_list_dict = notification_list_instance.to_dict()
# create an instance of NotificationList from a dict
notification_list_from_dict = NotificationList.from_dict(notification_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


