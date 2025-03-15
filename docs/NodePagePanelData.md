# NodePagePanelData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** |  | 
**active** | **int** |  | 
**inactive** | **int** |  | 
**error** | **int** |  | 
**live** | **int** |  | 

## Example

```python
from ambient_backend_api_client.models.node_page_panel_data import NodePagePanelData

# TODO update the JSON string below
json = "{}"
# create an instance of NodePagePanelData from a JSON string
node_page_panel_data_instance = NodePagePanelData.from_json(json)
# print the JSON string representation of the object
print(NodePagePanelData.to_json())

# convert the object into a dict
node_page_panel_data_dict = node_page_panel_data_instance.to_dict()
# create an instance of NodePagePanelData from a dict
node_page_panel_data_from_dict = NodePagePanelData.from_dict(node_page_panel_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


