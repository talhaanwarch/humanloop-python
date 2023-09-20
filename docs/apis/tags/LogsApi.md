<a name="__pageTop"></a>
# humanloop.apis.tags.logs_api.LogsApi

All URIs are relative to *https://api.humanloop.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log**](#log) | **post** /logs | Log
[**update**](#update) | **patch** /logs/{id} | Update
[**update_by_ref**](#update_by_ref) | **patch** /logs | Update By Reference Id

# **log**

Log

Log a datapoint or array of datapoints to your Humanloop project.

### Example

```python
from pprint import pprint
from humanloop import Humanloop, ApiException

humanloop = Humanloop(
    # Defining the host is optional and defaults to https://api.humanloop.com/v4
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.humanloop.com/v4",
    openai_api_key="OPENAI_API_KEY",
    openai_azure_api_key="OPENAI_AZURE_API_KEY",
    openai_azure_endpoint_api_key="OPENAI_AZURE_ENDPOINT_API_KEY",
    ai21_api_key="AI21_API_KEY",
    mock_api_key="MOCK_API_KEY",
    anthropic_api_key="ANTHROPIC_API_KEY",
    cohere_api_key="COHERE_API_KEY",
    # Configure API key authorization: APIKeyHeader
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'APIKeyHeader': 'Bearer'},
)

try:
    # Log
    log_response = humanloop.log(
        body=[{}],  # required
        project="string_example",  # optional
        project_id="string_example",  # optional
        session_id="string_example",  # optional
        session_reference_id="string_example",  # optional
        parent_id="string_example",  # optional
        parent_reference_id="string_example",  # optional
        inputs={},  # optional
        source="string_example",  # optional
        metadata={},  # optional
        reference_id="string_example",  # optional
        trial_id="string_example",  # optional
        messages=[
            {
                "role": "user",
            }
        ],  # optional
        output="string_example",  # optional
        config={
            "type": "AgentConfigRequest",
            "agent_class": "agent_class_example",
            "model_config": {
                "model": "model_example",
                "max_tokens": -1,
                "temperature": 1,
                "top_p": 1,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "type": "model",
            },
        },  # optional
        feedback={
            "type": "string_example",
            "value": 3.14,
        },  # optional
        created_at="1970-01-01T00:00:00.00Z",  # optional
        error="string_example",  # optional
        duration=3.14,  # optional
    )
    pprint(log_response.body)
    pprint(log_response.headers)
    pprint(log_response.status)
    pprint(log_response.round_trip_time)
except ApiException as e:
    print("Exception when calling LogsApi.log: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LogDatapointRequest**](../../models/LogDatapointRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#log.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#log.ApiResponseFor422) | Validation Error

#### log.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LogsLogResponse**](../../models/LogsLogResponse.md) |  | 


#### log.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update**

Update

Update a logged datapoint in your Humanloop project.

### Example

```python
from pprint import pprint
from humanloop import Humanloop, ApiException

humanloop = Humanloop(
    # Defining the host is optional and defaults to https://api.humanloop.com/v4
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.humanloop.com/v4",
    openai_api_key="OPENAI_API_KEY",
    openai_azure_api_key="OPENAI_AZURE_API_KEY",
    openai_azure_endpoint_api_key="OPENAI_AZURE_ENDPOINT_API_KEY",
    ai21_api_key="AI21_API_KEY",
    mock_api_key="MOCK_API_KEY",
    anthropic_api_key="ANTHROPIC_API_KEY",
    cohere_api_key="COHERE_API_KEY",
    # Configure API key authorization: APIKeyHeader
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'APIKeyHeader': 'Bearer'},
)

try:
    # Update
    update_response = humanloop.logs.update(
        id="id_example",  # required
        output="string_example",  # optional
        error="string_example",  # optional
        duration=3.14,  # optional
    )
    pprint(update_response.body)
    pprint(update_response.body["config"])
    pprint(update_response.body["id"])
    pprint(update_response.body["project"])
    pprint(update_response.body["project_id"])
    pprint(update_response.body["session_id"])
    pprint(update_response.body["session_reference_id"])
    pprint(update_response.body["parent_id"])
    pprint(update_response.body["parent_reference_id"])
    pprint(update_response.body["inputs"])
    pprint(update_response.body["source"])
    pprint(update_response.body["metadata"])
    pprint(update_response.body["reference_id"])
    pprint(update_response.body["trial_id"])
    pprint(update_response.body["messages"])
    pprint(update_response.body["output"])
    pprint(update_response.body["feedback"])
    pprint(update_response.body["created_at"])
    pprint(update_response.body["error"])
    pprint(update_response.body["duration"])
    pprint(update_response.body["model_config"])
    pprint(update_response.body["user"])
    pprint(update_response.body["provider_response"])
    pprint(update_response.body["provider_latency"])
    pprint(update_response.body["raw_output"])
    pprint(update_response.body["finish_reason"])
    pprint(update_response.headers)
    pprint(update_response.status)
    pprint(update_response.round_trip_time)
except ApiException as e:
    print("Exception when calling LogsApi.update: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateLogRequest**](../../models/UpdateLogRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

String ID of logged datapoint to return. Starts with `data_`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | String ID of logged datapoint to return. Starts with &#x60;data_&#x60;. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update.ApiResponseFor422) | Validation Error

#### update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LogResponse**](../../models/LogResponse.md) |  | 


#### update.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_by_ref**

Update By Reference Id

Update a logged datapoint by its reference ID.  The `reference_id` query parameter must be provided, and refers to the `reference_id` of a previously-logged datapoint.

### Example

```python
from pprint import pprint
from humanloop import Humanloop, ApiException

humanloop = Humanloop(
    # Defining the host is optional and defaults to https://api.humanloop.com/v4
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.humanloop.com/v4",
    openai_api_key="OPENAI_API_KEY",
    openai_azure_api_key="OPENAI_AZURE_API_KEY",
    openai_azure_endpoint_api_key="OPENAI_AZURE_ENDPOINT_API_KEY",
    ai21_api_key="AI21_API_KEY",
    mock_api_key="MOCK_API_KEY",
    anthropic_api_key="ANTHROPIC_API_KEY",
    cohere_api_key="COHERE_API_KEY",
    # Configure API key authorization: APIKeyHeader
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'APIKeyHeader': 'Bearer'},
)

try:
    # Update By Reference Id
    update_by_ref_response = humanloop.logs.update_by_ref(
        reference_id="reference_id_example",  # required
        output="string_example",  # optional
        error="string_example",  # optional
        duration=3.14,  # optional
    )
    pprint(update_by_ref_response.body)
    pprint(update_by_ref_response.body["config"])
    pprint(update_by_ref_response.body["id"])
    pprint(update_by_ref_response.body["project"])
    pprint(update_by_ref_response.body["project_id"])
    pprint(update_by_ref_response.body["session_id"])
    pprint(update_by_ref_response.body["session_reference_id"])
    pprint(update_by_ref_response.body["parent_id"])
    pprint(update_by_ref_response.body["parent_reference_id"])
    pprint(update_by_ref_response.body["inputs"])
    pprint(update_by_ref_response.body["source"])
    pprint(update_by_ref_response.body["metadata"])
    pprint(update_by_ref_response.body["reference_id"])
    pprint(update_by_ref_response.body["trial_id"])
    pprint(update_by_ref_response.body["messages"])
    pprint(update_by_ref_response.body["output"])
    pprint(update_by_ref_response.body["feedback"])
    pprint(update_by_ref_response.body["created_at"])
    pprint(update_by_ref_response.body["error"])
    pprint(update_by_ref_response.body["duration"])
    pprint(update_by_ref_response.body["model_config"])
    pprint(update_by_ref_response.body["user"])
    pprint(update_by_ref_response.body["provider_response"])
    pprint(update_by_ref_response.body["provider_latency"])
    pprint(update_by_ref_response.body["raw_output"])
    pprint(update_by_ref_response.body["finish_reason"])
    pprint(update_by_ref_response.headers)
    pprint(update_by_ref_response.status)
    pprint(update_by_ref_response.round_trip_time)
except ApiException as e:
    print("Exception when calling LogsApi.update_by_ref: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateLogRequest**](../../models/UpdateLogRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
reference_id | ReferenceIdSchema | | 


# ReferenceIdSchema

A unique string to reference the datapoint. Identifies the logged datapoint created with the same `reference_id`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A unique string to reference the datapoint. Identifies the logged datapoint created with the same &#x60;reference_id&#x60;. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_by_ref.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_by_ref.ApiResponseFor422) | Validation Error

#### update_by_ref.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LogResponse**](../../models/LogResponse.md) |  | 


#### update_by_ref.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKeyHeader](../../../README.md#APIKeyHeader)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

