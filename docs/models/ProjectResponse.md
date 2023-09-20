# humanloop.model.project_response.ProjectResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**feedback_types** | [**FeedbackTypes**](FeedbackTypes.md) | [**FeedbackTypes**](FeedbackTypes.md) |  | 
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | str,  | str,  | Unique project name. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  | Project ID | 
**team_id** | str,  | str,  | Unique ID of the team the project belongs to. Starts with &#x60;tm_&#x60;. | 
**data_count** | decimal.Decimal, int,  | decimal.Decimal,  | The count of datapoints that have been logged to the project. | 
**[users](#users)** | list, tuple,  | tuple,  | Users associated to the project. | 
**[active_experiment](#active_experiment)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Experiment that has been set as the project&#x27;s active deployment. At most one of active_experiment and active_model_config can be set. | [optional] 
**[active_config](#active_config)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Config that has been set as the project&#x27;s active deployment. At most one of active_experiment and active_model_config can be set. | [optional] 
**config_type** | [**ConfigType**](ConfigType.md) | [**ConfigType**](ConfigType.md) |  | [optional] 
**[active_evaluators](#active_evaluators)** | list, tuple,  | tuple,  | Evaluators that have been set as active for the project. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

Users associated to the project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Users associated to the project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProjectUserResponse**](ProjectUserResponse.md) | [**ProjectUserResponse**](ProjectUserResponse.md) | [**ProjectUserResponse**](ProjectUserResponse.md) |  | 

# active_experiment

Experiment that has been set as the project's active deployment. At most one of active_experiment and active_model_config can be set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Experiment that has been set as the project&#x27;s active deployment. At most one of active_experiment and active_model_config can be set. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ExperimentResponse](ExperimentResponse.md) | [**ExperimentResponse**](ExperimentResponse.md) | [**ExperimentResponse**](ExperimentResponse.md) |  | 

# active_config

Config that has been set as the project's active deployment. At most one of active_experiment and active_model_config can be set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Config that has been set as the project&#x27;s active deployment. At most one of active_experiment and active_model_config can be set. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ProjectConfigResponse](ProjectConfigResponse.md) | [**ProjectConfigResponse**](ProjectConfigResponse.md) | [**ProjectConfigResponse**](ProjectConfigResponse.md) |  | 

# active_evaluators

Evaluators that have been set as active for the project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Evaluators that have been set as active for the project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EvaluatorResponse**](EvaluatorResponse.md) | [**EvaluatorResponse**](EvaluatorResponse.md) | [**EvaluatorResponse**](EvaluatorResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

