# humanloop.model.feedback_type_request.FeedbackTypeRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of feedback to update. | 
**[values](#values)** | list, tuple,  | tuple,  | The feedback values to be available. This field should only be populated when updating a &#x27;select&#x27; or &#x27;multi_select&#x27; feedback class. | [optional] 
**[class](#class)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The data type associated to this feedback type; whether it is a &#x27;text&#x27;/&#x27;select&#x27;/&#x27;multi_select&#x27;. This is optional when updating the default feedback types (i.e. when &#x60;type&#x60; is &#x27;rating&#x27;, &#x27;action&#x27; or &#x27;issue&#x27;). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

The feedback values to be available. This field should only be populated when updating a 'select' or 'multi_select' feedback class.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The feedback values to be available. This field should only be populated when updating a &#x27;select&#x27; or &#x27;multi_select&#x27; feedback class. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FeedbackLabelRequest**](FeedbackLabelRequest.md) | [**FeedbackLabelRequest**](FeedbackLabelRequest.md) | [**FeedbackLabelRequest**](FeedbackLabelRequest.md) |  | 

# class

The data type associated to this feedback type; whether it is a 'text'/'select'/'multi_select'. This is optional when updating the default feedback types (i.e. when `type` is 'rating', 'action' or 'issue').

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The data type associated to this feedback type; whether it is a &#x27;text&#x27;/&#x27;select&#x27;/&#x27;multi_select&#x27;. This is optional when updating the default feedback types (i.e. when &#x60;type&#x60; is &#x27;rating&#x27;, &#x27;action&#x27; or &#x27;issue&#x27;). | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[FeedbackClass](FeedbackClass.md) | [**FeedbackClass**](FeedbackClass.md) | [**FeedbackClass**](FeedbackClass.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

