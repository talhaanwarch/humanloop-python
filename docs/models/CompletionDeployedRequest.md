# humanloop.model.completion_deployed_request.CompletionDeployedRequest

Completion request using the project's active deployment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Completion request using the project&#x27;s active deployment. | 

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
**[provider_api_keys](#provider_api_keys)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization. | [optional] 
**num_samples** | decimal.Decimal, int,  | decimal.Decimal,  | The number of generations. | [optional] if omitted the server will use the default value of 1
**logprobs** | decimal.Decimal, int,  | decimal.Decimal,  | Include the log probabilities of the top n tokens in the provider_response | [optional] 
**stream** | bool,  | BoolClass,  | If true, tokens will be sent as data-only server-sent events. If num_samples &gt; 1, samples are streamed back independently. | [optional] if omitted the server will use the default value of False
**suffix** | str,  | str,  | The suffix that comes after a completion of inserted text. Useful for completions that act like inserts. | [optional] 
**user** | str,  | str,  | End-user ID passed through to provider call. | [optional] 
**environment** | str,  | str,  | The environment name used to create a chat response. If not specified, the default environment will be used. | [optional] 

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

# provider_api_keys

API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ProviderApiKeys](ProviderApiKeys.md) | [**ProviderApiKeys**](ProviderApiKeys.md) | [**ProviderApiKeys**](ProviderApiKeys.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

