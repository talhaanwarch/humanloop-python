# humanloop.model.completion_response.CompletionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  | Array containing the generation responses. | 
**provider_responses** | [**CompletionResponseProviderResponses**](CompletionResponseProviderResponses.md) | [**CompletionResponseProviderResponses**](CompletionResponseProviderResponses.md) |  | 
**project_id** | str,  | str,  | Unique identifier of the parent project. Will not be provided if the request was made without providing a project name or id | [optional] 
**num_samples** | decimal.Decimal, int,  | decimal.Decimal,  | How many completions to make for each set of inputs. | [optional] if omitted the server will use the default value of 1
**logprobs** | decimal.Decimal, int,  | decimal.Decimal,  | Include the log probabilities of the top n tokens in the provider_response | [optional] 
**suffix** | str,  | str,  | The suffix that comes after a completion of inserted text. Useful for completions that act like inserts. | [optional] 
**user** | str,  | str,  | End-user ID passed through to provider call. | [optional] 
**[usage](#usage)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Counts of the number of tokens used and related stats. | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Any additional metadata to record. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

Array containing the generation responses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array containing the generation responses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataResponse**](DataResponse.md) | [**DataResponse**](DataResponse.md) | [**DataResponse**](DataResponse.md) |  | 

# usage

Counts of the number of tokens used and related stats.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Counts of the number of tokens used and related stats. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Usage](Usage.md) | [**Usage**](Usage.md) | [**Usage**](Usage.md) |  | 

# metadata

Any additional metadata to record.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Any additional metadata to record. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

