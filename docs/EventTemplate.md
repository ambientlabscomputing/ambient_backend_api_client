# EventTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root** | **str** |  | 
**event_label** | [**EventLabel**](EventLabel.md) |  | 
**event_type** | [**AmbientEventTypeEnum**](AmbientEventTypeEnum.md) |  | 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | 
**resource_id** | **str** |  | [optional] 
**action** | [**AmbientActionEnum**](AmbientActionEnum.md) |  | [optional] 

## Example

```python
from ambient_backend_api_client.models.event_template import EventTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EventTemplate from a JSON string
event_template_instance = EventTemplate.from_json(json)
# print the JSON string representation of the object
print(EventTemplate.to_json())

# convert the object into a dict
event_template_dict = event_template_instance.to_dict()
# create an instance of EventTemplate from a dict
event_template_from_dict = EventTemplate.from_dict(event_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


