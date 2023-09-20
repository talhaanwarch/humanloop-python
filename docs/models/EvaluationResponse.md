# humanloop.model.evaluation_response.EvaluationResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**testset** | [**TestsetResponse**](TestsetResponse.md) | [**TestsetResponse**](TestsetResponse.md) |  | 
**[evaluators](#evaluators)** | list, tuple,  | tuple,  |  | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique ID for the evaluation. Starts with &#x60;ev_&#x60;. | 
**config** | [**ConfigResponse**](ConfigResponse.md) | [**ConfigResponse**](ConfigResponse.md) |  | 
**status** | [**EvaluationStatus**](EvaluationStatus.md) | [**EvaluationStatus**](EvaluationStatus.md) |  | 
**testset_snapshot** | [**TestsetResponse**](TestsetResponse.md) | [**TestsetResponse**](TestsetResponse.md) |  | [optional] 
**[evaluator_aggregates](#evaluator_aggregates)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# evaluators

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EvaluatorResponse**](EvaluatorResponse.md) | [**EvaluatorResponse**](EvaluatorResponse.md) | [**EvaluatorResponse**](EvaluatorResponse.md) |  | 

# evaluator_aggregates

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) | [**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) | [**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

