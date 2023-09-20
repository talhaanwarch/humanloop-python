# humanloop.model.tool_config_response.ToolConfigResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name for the tool referenced by the model | 
**id** | str,  | str,  | String ID of config. Starts with &#x60;config_&#x60;. | 
**type** | str,  | str,  |  | must be one of ["tool", ] 
**description** | str,  | str,  | Description of the tool referenced by the model | [optional] 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/ | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | [optional] 
**source** | str,  | str,  | Code source of the tool. | [optional] 
**[setup_schema](#setup_schema)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/ | [optional] 
**signature** | str,  | str,  | The function signature of the tool when being called. | [optional] 
**is_preset** | bool,  | BoolClass,  | Whether the tool is one where Humanloop defines runtime or not. | [optional] 
**preset_name** | str,  | str,  | If is_preset &#x3D; true, this is the name of the preset tool on Humanloop. This is used as the key to lookup the Humanloop runtime of the tool | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/ | 

# other

Other parameters that define the config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | 

# setup_schema

Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/ | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

