# humanloop.model.generic_config_request.GenericConfigRequest

Base config request for all config types.  Contains fields that are common to all config types. Specifically, `name` and `description` that are saved at the organization-level.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Base config request for all config types.  Contains fields that are common to all config types. Specifically, &#x60;name&#x60; and &#x60;description&#x60; that are saved at the organization-level. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | must be one of ["generic", ] 
**description** | str,  | str,  | A description of the model config. | [optional] 
**name** | str,  | str,  | A friendly display name for the model config. If not provided, a name will be generated. | [optional] 
**[other](#other)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | [optional] 

# other

Other parameters that define the config.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other parameters that define the config. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

