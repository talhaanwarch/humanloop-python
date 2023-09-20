# humanloop.model.model_config_response.ModelConfigResponse

Model config request.  Contains fields that are common to all (i.e. both chat and complete) endpoints.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Model config request.  Contains fields that are common to all (i.e. both chat and complete) endpoints. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model** | str,  | str,  | The model instance used. E.g. text-davinci-002. | 
**id** | str,  | str,  | String ID of config. Starts with &#x60;config_&#x60;. | 
**type** | str,  | str,  |  | must be one of ["model", ] 
**description** | str,  | str,  | A description of the model config. | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameter values to be passed to the provider call. | [optional] if omitted the server will use the default value of {}
**name** | str,  | str,  | A friendly display name for the model config. If not provided, a name will be generated. | [optional] 
**[provider](#provider)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The company providing the underlying model service. | [optional] if omitted the server will use the default value of openai
**max_tokens** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of tokens to generate. Provide max_tokens&#x3D;-1 to dynamically calculate the maximum number of tokens to generate given the length of the prompt | [optional] if omitted the server will use the default value of -1
**temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  | What sampling temperature to use when making a generation. Higher values means the model will be more creative. | [optional] if omitted the server will use the default value of 1
**top_p** | decimal.Decimal, int, float,  | decimal.Decimal,  | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. | [optional] if omitted the server will use the default value of 1
**[stop](#stop)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The string (or list of strings) after which the model will stop generating. The returned text will not contain the stop sequence. | [optional] 
**presence_penalty** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the generation so far. | [optional] if omitted the server will use the default value of 0
**frequency_penalty** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number between -2.0 and 2.0. Positive values penalize new tokens based on how frequently they appear in the generation so far. | [optional] if omitted the server will use the default value of 0
**prompt_template** | str,  | str,  | Prompt template that will take your specified inputs to form your final request to the model. NB: Input variables within the prompt template should be specified with syntax: {{INPUT_NAME}}. | [optional] 
**[chat_template](#chat_template)** | list, tuple,  | tuple,  | Messages prepended to the list of messages sent to the provider. These messages that will take your specified inputs to form your final request to the provider model. NB: Input variables within the template should be specified with syntax: {{INPUT_NAME}}. | [optional] 
**[tool_configs](#tool_configs)** | list, tuple,  | tuple,  | Definition of tools shown to the model. | [optional] 
**[endpoint](#endpoint)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The provider model endpoint used. | [optional] 

# other

Other parameter values to be passed to the provider call.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameter values to be passed to the provider call. | if omitted the server will use the default value of {}

# provider

The company providing the underlying model service.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The company providing the underlying model service. | if omitted the server will use the default value of openai

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ModelProviders](ModelProviders.md) | [**ModelProviders**](ModelProviders.md) | [**ModelProviders**](ModelProviders.md) |  | 

# stop

The string (or list of strings) after which the model will stop generating. The returned text will not contain the stop sequence.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The string (or list of strings) after which the model will stop generating. The returned text will not contain the stop sequence. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | 
[any_of_1](#any_of_1) | list, tuple,  | tuple,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# chat_template

Messages prepended to the list of messages sent to the provider. These messages that will take your specified inputs to form your final request to the provider model. NB: Input variables within the template should be specified with syntax: {{INPUT_NAME}}.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Messages prepended to the list of messages sent to the provider. These messages that will take your specified inputs to form your final request to the provider model. NB: Input variables within the template should be specified with syntax: {{INPUT_NAME}}. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) |  | 

# tool_configs

Definition of tools shown to the model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Definition of tools shown to the model. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ToolConfigResponse**](ToolConfigResponse.md) | [**ToolConfigResponse**](ToolConfigResponse.md) | [**ToolConfigResponse**](ToolConfigResponse.md) |  | 

# endpoint

The provider model endpoint used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The provider model endpoint used. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ModelEndpoints](ModelEndpoints.md) | [**ModelEndpoints**](ModelEndpoints.md) | [**ModelEndpoints**](ModelEndpoints.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

