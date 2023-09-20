# humanloop.model.evaluator_response.EvaluatorResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[return_type](#return_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The type of the return value of the evaluator. | 
**code** | str,  | str,  | The code for the evaluator. This code will be executed in a sandboxed environment. | 
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The name of the evaluator. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**description** | str,  | str,  | The description of the evaluator. | 
**[arguments_type](#arguments_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Whether this evaluator is target-free or target-required. | 
**id** | str,  | str,  | Unique ID for the evaluator. Starts with &#x60;evfn_&#x60;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# arguments_type

Whether this evaluator is target-free or target-required.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Whether this evaluator is target-free or target-required. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EvaluatorArgumentsType](EvaluatorArgumentsType.md) | [**EvaluatorArgumentsType**](EvaluatorArgumentsType.md) | [**EvaluatorArgumentsType**](EvaluatorArgumentsType.md) |  | 

# return_type

The type of the return value of the evaluator.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The type of the return value of the evaluator. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EvaluatorReturnTypeEnum](EvaluatorReturnTypeEnum.md) | [**EvaluatorReturnTypeEnum**](EvaluatorReturnTypeEnum.md) | [**EvaluatorReturnTypeEnum**](EvaluatorReturnTypeEnum.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

