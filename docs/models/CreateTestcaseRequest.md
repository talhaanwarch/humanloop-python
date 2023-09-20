# humanloop.model.create_testcase_request.CreateTestcaseRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**inputs** | [**CreateTestcaseRequestInputs**](CreateTestcaseRequestInputs.md) | [**CreateTestcaseRequestInputs**](CreateTestcaseRequestInputs.md) |  | [optional] 
**[messages](#messages)** | list, tuple,  | tuple,  | The chat messages for this testcase. | [optional] 
**target** | [**CreateTestcaseRequestTarget**](CreateTestcaseRequestTarget.md) | [**CreateTestcaseRequestTarget**](CreateTestcaseRequestTarget.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# messages

The chat messages for this testcase.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The chat messages for this testcase. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

