# humanloop.model.model_config_tool_request.ModelConfigToolRequest

Definition of tool within a model config.  The subset of ToolConfig parameters received by the chat endpoint. Does not have things like the signature or setup schema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of tool within a model config.  The subset of ToolConfig parameters received by the chat endpoint. Does not have things like the signature or setup schema. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the tool shown to the model. | 
**description** | str,  | str,  | The description of the tool shown to the model. | [optional] 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/ | [optional] 
**source** | str,  | str,  | Code source of the tool. | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | [optional] 
**preset_name** | str,  | str,  | If is_preset &#x3D; true, this is the name of the preset tool on Humanloop. This is used as the key to look up the Humanloop runtime of the tool | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

