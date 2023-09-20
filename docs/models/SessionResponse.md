# humanloop.model.session_response.SessionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[projects](#projects)** | list, tuple,  | tuple,  | List of projects that have datapoints associated to this session. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**datapoints_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of datapoints associated to this session. | 
**id** | str,  | str,  | String ID of session. Starts with &#x60;sesh_&#x60;. | 
**reference_id** | str,  | str,  | Unique user-provided string identifying the session. | [optional] 
**[first_inputs](#first_inputs)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Inputs for the first datapoint in the session. | [optional] 
**last_output** | str,  | str,  | Output for the last datapoint in the session. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# projects

List of projects that have datapoints associated to this session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of projects that have datapoints associated to this session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SessionProjectResponse**](SessionProjectResponse.md) | [**SessionProjectResponse**](SessionProjectResponse.md) | [**SessionProjectResponse**](SessionProjectResponse.md) |  | 

# first_inputs

Inputs for the first datapoint in the session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Inputs for the first datapoint in the session. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

