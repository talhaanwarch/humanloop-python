# humanloop.model.base_metric_response.BaseMetricResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**default** | bool,  | BoolClass,  | Whether the metric is a global default metric. Metrics with this flag enabled cannot be deleted or modified. | 
**code** | str,  | str,  | Python code used to calculate a metric value on each logged datapoint. | 
**updated_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The name of the metric. | 
**active** | bool,  | BoolClass,  | If enabled, the metric is calculated for every logged datapoint. | 
**created_at** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**description** | str,  | str,  | A description of what the metric measures. | 
**id** | str,  | str,  | ID of the metric. Starts with &#x27;metric_&#x27;. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

