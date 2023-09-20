# humanloop.model.log_request.LogRequest

Request model for logging a datapoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model for logging a datapoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**project** | str,  | str,  | Unique project name. If no project exists with this name, a new project will be created. | [optional] 
**project_id** | str,  | str,  | Unique ID of a project to associate to the log. Either this or &#x60;project&#x60; must be provided. | [optional] 
**session_id** | str,  | str,  | ID of the session to associate the datapoint. | [optional] 
**session_reference_id** | str,  | str,  | A unique string identifying the session to associate the datapoint to. Allows you to log multiple datapoints to a session (using an ID kept by your internal systems) by passing the same &#x60;session_reference_id&#x60; in subsequent log requests. Specify at most one of this or &#x60;session_id&#x60;. | [optional] 
**parent_id** | str,  | str,  | ID associated to the parent datapoint in a session. | [optional] 
**parent_reference_id** | str,  | str,  | A unique string identifying the previously-logged parent datapoint in a session. Allows you to log nested datapoints with your internal system IDs by passing the same reference ID as &#x60;parent_id&#x60; in a prior log request. Specify at most one of this or &#x60;parent_id&#x60;. Note that this cannot refer to a datapoint being logged in the same request. | [optional] 
**[inputs](#inputs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The inputs passed to the prompt template. | [optional] if omitted the server will use the default value of {}
**source** | str,  | str,  | Identifies where the model was called from. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Any additional metadata to record. | [optional] 
**reference_id** | str,  | str,  | A unique string to reference the datapoint. Allows you to log nested datapoints with your internal system IDs by passing the same reference ID as &#x60;parent_id&#x60; in a subsequent log request. | [optional] 
**trial_id** | str,  | str,  | Unique ID of an experiment trial to associate to the log. | [optional] 
**[messages](#messages)** | list, tuple,  | tuple,  | The messages passed to the to provider chat endpoint. | [optional] 
**output** | str,  | str,  | Generated output from your model for the provided inputs. Can be &#x60;None&#x60; if logging an error, or if logging a parent datapoint with the intention to populate it later | [optional] 
**[config](#config)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The model config used for this generation. Required unless &#x60;trial_id&#x60; is provided. | [optional] 
**[feedback](#feedback)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Optional parameter to provide feedback with your logged datapoint. | [optional] 
**created_at** | str, datetime,  | str,  | User defined timestamp for when the log was created.  | [optional] value must conform to RFC-3339 date-time
**error** | str,  | str,  | Error message if the log is an error. | [optional] 
**duration** | decimal.Decimal, int, float,  | decimal.Decimal,  | Duration of the logged event in seconds. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# inputs

The inputs passed to the prompt template.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The inputs passed to the prompt template. | if omitted the server will use the default value of {}

# metadata

Any additional metadata to record.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Any additional metadata to record. | 

# messages

The messages passed to the to provider chat endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The messages passed to the to provider chat endpoint. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) | [**ChatMessage**](ChatMessage.md) |  | 

# config

The model config used for this generation. Required unless `trial_id` is provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The model config used for this generation. Required unless &#x60;trial_id&#x60; is provided. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ModelConfigRequest](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) | [**ModelConfigRequest**](ModelConfigRequest.md) |  | 
[ToolConfigRequest](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) | [**ToolConfigRequest**](ToolConfigRequest.md) |  | 
[GenericConfigRequest](GenericConfigRequest.md) | [**GenericConfigRequest**](GenericConfigRequest.md) | [**GenericConfigRequest**](GenericConfigRequest.md) |  | 
[AgentConfigRequest](AgentConfigRequest.md) | [**AgentConfigRequest**](AgentConfigRequest.md) | [**AgentConfigRequest**](AgentConfigRequest.md) |  | 

# feedback

Optional parameter to provide feedback with your logged datapoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Optional parameter to provide feedback with your logged datapoint. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Feedback](Feedback.md) | [**Feedback**](Feedback.md) | [**Feedback**](Feedback.md) |  | 
[any_of_1](#any_of_1) | list, tuple,  | tuple,  |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Feedback**](Feedback.md) | [**Feedback**](Feedback.md) | [**Feedback**](Feedback.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

