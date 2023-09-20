# humanloop.model.feedback_request.FeedbackRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[type](#type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The type of feedback. The default feedback types available are &#x27;rating&#x27;, &#x27;action&#x27;, &#x27;issue&#x27;, &#x27;correction&#x27;, and &#x27;comment&#x27;. | 
**value** | str,  | str,  | The feedback value to be set. This field should be left blank when unsetting &#x27;rating&#x27;, &#x27;correction&#x27; or &#x27;comment&#x27;, but is required otherwise. | [optional] 
**data_id** | str,  | str,  | ID to associate the feedback to a previously logged datapoint. | [optional] 
**user** | str,  | str,  | A unique identifier to who provided the feedback. | [optional] 
**created_at** | str, datetime,  | str,  | User defined timestamp for when the feedback was created.  | [optional] value must conform to RFC-3339 date-time
**unset** | bool,  | BoolClass,  | If true, the value for this feedback is unset. | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

