# humanloop.model.agent_config_request.AgentConfigRequest

Base config request for all config types.  Contains fields that are common to all config types. Specifically, `name` and `description` that are saved at the organization-level.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base config request for all config types.  Contains fields that are common to all config types. Specifically, &#x60;name&#x60; and &#x60;description&#x60; that are saved at the organization-level. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[model_config](#model_config)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Model config to associate with the agent. | 
**agent_class** | str,  | str,  | Class of the agent. | 
**type** | str,  | str,  |  | must be one of ["agent", ] 
**description** | str,  | str,  | A description of the model config. | [optional] 
**name** | str,  | str,  | A friendly display name for the model config. If not provided, a name will be generated. | [optional] 
**[tools](#tools)** | list, tuple,  | tuple,  | Tools to associate with the agent. | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | [optional] 

# model_config

Model config to associate with the agent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Model config to associate with the agent. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ModelConfigRequest](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) |  | 

# tools

Tools to associate with the agent.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tools to associate with the agent. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ToolConfigRequest**](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) |  | 

# other

Other parameters that define the config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

