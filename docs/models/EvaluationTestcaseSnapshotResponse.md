# humanloop.model.evaluation_testcase_snapshot_response.EvaluationTestcaseSnapshotResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[evaluation_results](#evaluation_results)** | list, tuple,  | tuple,  |  | 
**testcase** | [**TestcaseResponse**](TestcaseResponse.md) | [**TestcaseResponse**](TestcaseResponse.md) |  | 
**datapoint** | [**LogResponse**](LogResponse.md) | [**LogResponse**](LogResponse.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# evaluation_results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EvaluationResultResponse**](EvaluationResultResponse.md) | [**EvaluationResultResponse**](EvaluationResultResponse.md) | [**EvaluationResultResponse**](EvaluationResultResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

