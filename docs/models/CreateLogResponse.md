# humanloop.model.create_log_response.CreateLogResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**project_id** | str,  | str,  | String ID of project the datapoint belongs to. Starts with &#x60;pr_&#x60;. | 
**id** | str,  | str,  | String ID of logged datapoint. Starts with &#x60;data_&#x60;. | 
**session_id** | str,  | str,  | String ID of session the datapoint belongs to. Populated only if the datapoint was logged with &#x60;session_id&#x60; or &#x60;session_reference_id&#x60;, and is &#x60;None&#x60; otherwise. Starts with &#x60;sesh_&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

