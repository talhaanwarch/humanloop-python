# humanloop.model.experiment_config_response.ExperimentConfigResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**active** | bool,  | BoolClass,  | Whether the model config is active in the experiment. Only active model configs can be sampled from the experiment. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str,  | str,  | String ID of model config. Starts with &#x60;config_&#x60;. | 
**display_name** | str,  | str,  | Display name of model config. If this is not set by the user, a friendly name is generated. | 
**[config](#config)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Definition of the config used in the experiment. | 
**trials_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of datapoints with feedback associated to the experiment. | 
**mean** | decimal.Decimal, int, float,  | decimal.Decimal,  | The mean performance of the model config. | [optional] 
**spread** | decimal.Decimal, int, float,  | decimal.Decimal,  | The spread of performance of the model config. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

Definition of the config used in the experiment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Definition of the config used in the experiment. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ConfigResponse](ConfigResponse.md) | [**ConfigResponse**](ConfigResponse.md) | [**ConfigResponse**](ConfigResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

