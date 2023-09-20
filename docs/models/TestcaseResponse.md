# humanloop.model.testcase_response.TestcaseResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**testset_id** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**inputs** | [**TestcaseResponseInputs**](TestcaseResponseInputs.md) | [**TestcaseResponseInputs**](TestcaseResponseInputs.md) |  | [optional] 
**[messages](#messages)** | list, tuple,  | tuple,  |  | [optional] 
**target** | [**TestcaseResponseTarget**](TestcaseResponseTarget.md) | [**TestcaseResponseTarget**](TestcaseResponseTarget.md) |  | [optional] 
**source_project_data_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# messages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

