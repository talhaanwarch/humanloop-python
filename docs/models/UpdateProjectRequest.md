# humanloop.model.update_project_request.UpdateProjectRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The new unique project name. Caution, if you are using the project name as the unique identifier in your API calls, changing the name will break the calls. | [optional] 
**active_experiment_id** | str,  | str,  | ID for an experiment to set as the project&#x27;s active deployment. Starts with &#x27;exp_&#x27;. At most one of &#x27;active_experiment_id&#x27; and &#x27;active_model_config_id&#x27; can be set. | [optional] 
**active_config_id** | str,  | str,  | ID for a config to set as the project&#x27;s active deployment. Starts with &#x27;config_&#x27;. At most one of &#x27;active_experiment_id&#x27; and &#x27;active_config_id&#x27; can be set. | [optional] 
**[positive_labels](#positive_labels)** | list, tuple,  | tuple,  | The full list of labels to treat as positive user feedback. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# positive_labels

The full list of labels to treat as positive user feedback.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The full list of labels to treat as positive user feedback. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PositiveLabel**](PositiveLabel.md) | [**PositiveLabel**](PositiveLabel.md) | [**PositiveLabel**](PositiveLabel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

