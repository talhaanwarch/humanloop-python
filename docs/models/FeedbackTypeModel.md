# humanloop.model.feedback_type_model.FeedbackTypeModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[type](#type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The type of feedback. The default feedback types available are &#x27;rating&#x27;, &#x27;action&#x27;, &#x27;issue&#x27;, &#x27;correction&#x27;, and &#x27;comment&#x27;. | 
**[values](#values)** | list, tuple,  | tuple,  | The allowed values for categorical feedback types. Not populated for &#x60;correction&#x60; and &#x60;comment&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# type

The type of feedback. The default feedback types available are 'rating', 'action', 'issue', 'correction', and 'comment'.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The type of feedback. The default feedback types available are &#x27;rating&#x27;, &#x27;action&#x27;, &#x27;issue&#x27;, &#x27;correction&#x27;, and &#x27;comment&#x27;. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[FeedbackType](FeedbackType.md) | [**FeedbackType**](FeedbackType.md) | [**FeedbackType**](FeedbackType.md) |  | 
[items](#items) | str,  | str,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# values

The allowed values for categorical feedback types. Not populated for `correction` and `comment`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The allowed values for categorical feedback types. Not populated for &#x60;correction&#x60; and &#x60;comment&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CategoricalFeedbackLabel**](CategoricalFeedbackLabel.md) | [**CategoricalFeedbackLabel**](CategoricalFeedbackLabel.md) | [**CategoricalFeedbackLabel**](CategoricalFeedbackLabel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

