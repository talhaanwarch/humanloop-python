# humanloop.model.usage.Usage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**generation_tokens** | decimal.Decimal, int,  | decimal.Decimal,  | Number of tokens produced by the generation. | 
**prompt_tokens** | decimal.Decimal, int,  | decimal.Decimal,  | Number of tokens used in the prompt. | 
**total_tokens** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of tokens used by the prompt and generation combined. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

