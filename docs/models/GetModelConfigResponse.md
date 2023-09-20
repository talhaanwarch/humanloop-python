# humanloop.model.get_model_config_response.GetModelConfigResponse

A selected model configuration.  If the model configuration was selected in the context of an experiment, the response will include a trial_id to associate a subsequent log() call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A selected model configuration.  If the model configuration was selected in the context of an experiment, the response will include a trial_id to associate a subsequent log() call. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**project_id** | str,  | str,  | String ID of project the model config belongs to. Starts with &#x60;pr_&#x60;. | 
**last_used** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**project_name** | str,  | str,  | Name of the project the model config belongs to. | 
**config** | [**ConfigResponse**](ConfigResponse.md) | [**ConfigResponse**](ConfigResponse.md) |  | 
**[feedback_stats](#feedback_stats)** | list, tuple,  | tuple,  | Feedback statistics for the project model config. | [optional] 
**num_datapoints** | decimal.Decimal, int,  | decimal.Decimal,  | Number of datapoints associated with this project model config. | [optional] 
**experiment_id** | str,  | str,  | The ID of the experiment the model config has been registered to. Only populated when registering a model config to an experiment. | [optional] 
**[evaluation_aggregates](#evaluation_aggregates)** | list, tuple,  | tuple,  | Aggregates of evaluators for the model config. | [optional] 
**trial_id** | str,  | str,  | ID of trial to reference in subsequent log calls. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# feedback_stats

Feedback statistics for the project model config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Feedback statistics for the project model config. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProjectModelConfigFeedbackStatsResponse**](ProjectModelConfigFeedbackStatsResponse.md) | [**ProjectModelConfigFeedbackStatsResponse**](ProjectModelConfigFeedbackStatsResponse.md) | [**ProjectModelConfigFeedbackStatsResponse**](ProjectModelConfigFeedbackStatsResponse.md) |  | 

# evaluation_aggregates

Aggregates of evaluators for the model config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Aggregates of evaluators for the model config. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) | [**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) | [**ModelConfigEvaluatorAggregateResponse**](ModelConfigEvaluatorAggregateResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

