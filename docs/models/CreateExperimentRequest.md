# humanloop.model.create_experiment_request.CreateExperimentRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[positive_labels](#positive_labels)** | list, tuple,  | tuple,  | Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment. | 
**name** | str,  | str,  | Name of experiment. | 
**config_ids** | [**CreateExperimentRequestConfigIds**](CreateExperimentRequestConfigIds.md) | [**CreateExperimentRequestConfigIds**](CreateExperimentRequestConfigIds.md) |  | [optional] 
**set_active** | bool,  | BoolClass,  | Whether to set the created project as the project&#x27;s active experiment. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

