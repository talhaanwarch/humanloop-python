# humanloop.model.experiment_response.ExperimentResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[positive_labels](#positive_labels)** | list, tuple,  | tuple,  | Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment. | 
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**[metric](#metric)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Metric used as the experiment&#x27;s objective. | 
**project_id** | str,  | str,  | String ID of project the experiment belongs to. Starts with &#x60;pr_&#x60;. | 
**name** | str,  | str,  | Name of experiment. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  | String ID of experiment. Starts with &#x60;exp_&#x60;. | 
**[status](#status)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Status of experiment. | 
**[configs](#configs)** | list, tuple,  | tuple,  | List of configs associated to the experiment. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# status

Status of experiment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Status of experiment. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ExperimentStatus](ExperimentStatus.md) | [**ExperimentStatus**](ExperimentStatus.md) | [**ExperimentStatus**](ExperimentStatus.md) |  | 

# metric

Metric used as the experiment's objective.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Metric used as the experiment&#x27;s objective. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseMetricResponse](BaseMetricResponse.md) | [**BaseMetricResponse**](BaseMetricResponse.md) | [**BaseMetricResponse**](BaseMetricResponse.md) |  | 

# positive_labels

Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PositiveLabel**](PositiveLabel.md) | [**PositiveLabel**](PositiveLabel.md) | [**PositiveLabel**](PositiveLabel.md) |  | 

# configs

List of configs associated to the experiment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of configs associated to the experiment. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExperimentConfigResponse**](ExperimentConfigResponse.md) | [**ExperimentConfigResponse**](ExperimentConfigResponse.md) | [**ExperimentConfigResponse**](ExperimentConfigResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

