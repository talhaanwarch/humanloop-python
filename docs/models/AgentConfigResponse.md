# humanloop.model.agent_config_response.AgentConfigResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[model_config](#model_config)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Model config associated with the agent. | 
**agent_class** | str,  | str,  | Class of the agent. | 
**name** | str,  | str,  | Name of config. | 
**id** | str,  | str,  | String ID of config. Starts with &#x60;config_&#x60;. | 
**type** | str,  | str,  |  | must be one of ["agent", ] 
**description** | str,  | str,  | Description of config. | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | [optional] 
**[tools](#tools)** | list, tuple,  | tuple,  | Tools associated with the agent. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# model_config

Model config associated with the agent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Model config associated with the agent. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ModelConfigRequest](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) |  | 

# other

Other parameters that define the config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | 

# tools

Tools associated with the agent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tools associated with the agent. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ToolConfigRequest**](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

