# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from humanloop import schemas  # noqa: F401


class LogResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Request model for logging a datapoint.
    """


    class MetaOapg:
        required = {
            "observability_status",
            "updated_at",
            "evaluation_results",
            "id",
            "config",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def config() -> typing.Type['ConfigResponse']:
                return ConfigResponse
            
            
            class evaluation_results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EvaluationResultResponse']:
                        return EvaluationResultResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EvaluationResultResponse'], typing.List['EvaluationResultResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'evaluation_results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EvaluationResultResponse':
                    return super().__getitem__(i)
        
            @staticmethod
            def observability_status() -> typing.Type['ObservabilityStatus']:
                return ObservabilityStatus
            updated_at = schemas.DateTimeSchema
            project = schemas.StrSchema
            project_id = schemas.StrSchema
            session_id = schemas.StrSchema
            session_reference_id = schemas.StrSchema
            parent_id = schemas.StrSchema
            parent_reference_id = schemas.StrSchema
            inputs = schemas.DictSchema
            source = schemas.StrSchema
            metadata = schemas.DictSchema
            source_datapoint_id = schemas.StrSchema
            reference_id = schemas.StrSchema
            trial_id = schemas.StrSchema
            
            
            class messages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChatMessage']:
                        return ChatMessage
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChatMessage'], typing.List['ChatMessage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChatMessage':
                    return super().__getitem__(i)
            output = schemas.StrSchema
            config_id = schemas.StrSchema
            environment = schemas.StrSchema
            
            
            class feedback(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FeedbackResponse']:
                        return FeedbackResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FeedbackResponse'], typing.List['FeedbackResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'feedback':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FeedbackResponse':
                    return super().__getitem__(i)
            created_at = schemas.DateTimeSchema
            error = schemas.StrSchema
            duration = schemas.NumberSchema
            
            
            class output_message(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ChatMessage,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'output_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class model_config(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ProjectConfigResponse,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'model_config':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            user = schemas.StrSchema
            
            
            class provider_response(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.DictSchema
                    items = schemas.StrSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.items,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'provider_response':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            provider_latency = schemas.NumberSchema
            raw_output = schemas.StrSchema
            finish_reason = schemas.StrSchema
            
            
            class metric_values(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MetricValueResponse']:
                        return MetricValueResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MetricValueResponse'], typing.List['MetricValueResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'metric_values':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MetricValueResponse':
                    return super().__getitem__(i)
            
            
            class tools(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ToolResultResponse']:
                        return ToolResultResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ToolResultResponse'], typing.List['ToolResultResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tools':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ToolResultResponse':
                    return super().__getitem__(i)
            
            
            class tool_choice(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "none": "NONE",
                            }
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls("none")
                    
                    
                    class any_of_1(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "auto": "AUTO",
                            }
                        
                        @schemas.classproperty
                        def AUTO(cls):
                            return cls("auto")
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            ToolChoice,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tool_choice':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "config": config,
                "evaluation_results": evaluation_results,
                "observability_status": observability_status,
                "updated_at": updated_at,
                "project": project,
                "project_id": project_id,
                "session_id": session_id,
                "session_reference_id": session_reference_id,
                "parent_id": parent_id,
                "parent_reference_id": parent_reference_id,
                "inputs": inputs,
                "source": source,
                "metadata": metadata,
                "source_datapoint_id": source_datapoint_id,
                "reference_id": reference_id,
                "trial_id": trial_id,
                "messages": messages,
                "output": output,
                "config_id": config_id,
                "environment": environment,
                "feedback": feedback,
                "created_at": created_at,
                "error": error,
                "duration": duration,
                "output_message": output_message,
                "model_config": model_config,
                "user": user,
                "provider_response": provider_response,
                "provider_latency": provider_latency,
                "raw_output": raw_output,
                "finish_reason": finish_reason,
                "metric_values": metric_values,
                "tools": tools,
                "tool_choice": tool_choice,
            }
    
    observability_status: 'ObservabilityStatus'
    updated_at: MetaOapg.properties.updated_at
    evaluation_results: MetaOapg.properties.evaluation_results
    id: MetaOapg.properties.id
    config: 'ConfigResponse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'ConfigResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observability_status"]) -> 'ObservabilityStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> MetaOapg.properties.project: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_id"]) -> MetaOapg.properties.session_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_reference_id"]) -> MetaOapg.properties.session_reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_reference_id"]) -> MetaOapg.properties.parent_reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_datapoint_id"]) -> MetaOapg.properties.source_datapoint_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference_id"]) -> MetaOapg.properties.reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trial_id"]) -> MetaOapg.properties.trial_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feedback"]) -> MetaOapg.properties.feedback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_message"]) -> MetaOapg.properties.output_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_config"]) -> MetaOapg.properties.model_config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_response"]) -> MetaOapg.properties.provider_response: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_latency"]) -> MetaOapg.properties.provider_latency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_output"]) -> MetaOapg.properties.raw_output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finish_reason"]) -> MetaOapg.properties.finish_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric_values"]) -> MetaOapg.properties.metric_values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tools"]) -> MetaOapg.properties.tools: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool_choice"]) -> MetaOapg.properties.tool_choice: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "config", "evaluation_results", "observability_status", "updated_at", "project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "source_datapoint_id", "reference_id", "trial_id", "messages", "output", "config_id", "environment", "feedback", "created_at", "error", "duration", "output_message", "model_config", "user", "provider_response", "provider_latency", "raw_output", "finish_reason", "metric_values", "tools", "tool_choice", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> 'ConfigResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observability_status"]) -> 'ObservabilityStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union[MetaOapg.properties.project, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_id"]) -> typing.Union[MetaOapg.properties.session_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_reference_id"]) -> typing.Union[MetaOapg.properties.session_reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_reference_id"]) -> typing.Union[MetaOapg.properties.parent_reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_datapoint_id"]) -> typing.Union[MetaOapg.properties.source_datapoint_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference_id"]) -> typing.Union[MetaOapg.properties.reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_id"]) -> typing.Union[MetaOapg.properties.trial_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> typing.Union[MetaOapg.properties.messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output"]) -> typing.Union[MetaOapg.properties.output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_id"]) -> typing.Union[MetaOapg.properties.config_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> typing.Union[MetaOapg.properties.environment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feedback"]) -> typing.Union[MetaOapg.properties.feedback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_message"]) -> typing.Union[MetaOapg.properties.output_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_config"]) -> typing.Union[MetaOapg.properties.model_config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_response"]) -> typing.Union[MetaOapg.properties.provider_response, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_latency"]) -> typing.Union[MetaOapg.properties.provider_latency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_output"]) -> typing.Union[MetaOapg.properties.raw_output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finish_reason"]) -> typing.Union[MetaOapg.properties.finish_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric_values"]) -> typing.Union[MetaOapg.properties.metric_values, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tools"]) -> typing.Union[MetaOapg.properties.tools, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool_choice"]) -> typing.Union[MetaOapg.properties.tool_choice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "config", "evaluation_results", "observability_status", "updated_at", "project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "source_datapoint_id", "reference_id", "trial_id", "messages", "output", "config_id", "environment", "feedback", "created_at", "error", "duration", "output_message", "model_config", "user", "provider_response", "provider_latency", "raw_output", "finish_reason", "metric_values", "tools", "tool_choice", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        observability_status: 'ObservabilityStatus',
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        evaluation_results: typing.Union[MetaOapg.properties.evaluation_results, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        config: 'ConfigResponse',
        project: typing.Union[MetaOapg.properties.project, str, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, schemas.Unset] = schemas.unset,
        session_id: typing.Union[MetaOapg.properties.session_id, str, schemas.Unset] = schemas.unset,
        session_reference_id: typing.Union[MetaOapg.properties.session_reference_id, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, str, schemas.Unset] = schemas.unset,
        parent_reference_id: typing.Union[MetaOapg.properties.parent_reference_id, str, schemas.Unset] = schemas.unset,
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        source_datapoint_id: typing.Union[MetaOapg.properties.source_datapoint_id, str, schemas.Unset] = schemas.unset,
        reference_id: typing.Union[MetaOapg.properties.reference_id, str, schemas.Unset] = schemas.unset,
        trial_id: typing.Union[MetaOapg.properties.trial_id, str, schemas.Unset] = schemas.unset,
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, schemas.Unset] = schemas.unset,
        output: typing.Union[MetaOapg.properties.output, str, schemas.Unset] = schemas.unset,
        config_id: typing.Union[MetaOapg.properties.config_id, str, schemas.Unset] = schemas.unset,
        environment: typing.Union[MetaOapg.properties.environment, str, schemas.Unset] = schemas.unset,
        feedback: typing.Union[MetaOapg.properties.feedback, list, tuple, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        output_message: typing.Union[MetaOapg.properties.output_message, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        model_config: typing.Union[MetaOapg.properties.model_config, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        provider_response: typing.Union[MetaOapg.properties.provider_response, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        provider_latency: typing.Union[MetaOapg.properties.provider_latency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        raw_output: typing.Union[MetaOapg.properties.raw_output, str, schemas.Unset] = schemas.unset,
        finish_reason: typing.Union[MetaOapg.properties.finish_reason, str, schemas.Unset] = schemas.unset,
        metric_values: typing.Union[MetaOapg.properties.metric_values, list, tuple, schemas.Unset] = schemas.unset,
        tools: typing.Union[MetaOapg.properties.tools, list, tuple, schemas.Unset] = schemas.unset,
        tool_choice: typing.Union[MetaOapg.properties.tool_choice, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogResponse':
        return super().__new__(
            cls,
            *args,
            observability_status=observability_status,
            updated_at=updated_at,
            evaluation_results=evaluation_results,
            id=id,
            config=config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            reference_id=reference_id,
            trial_id=trial_id,
            messages=messages,
            output=output,
            config_id=config_id,
            environment=environment,
            feedback=feedback,
            created_at=created_at,
            error=error,
            duration=duration,
            output_message=output_message,
            model_config=model_config,
            user=user,
            provider_response=provider_response,
            provider_latency=provider_latency,
            raw_output=raw_output,
            finish_reason=finish_reason,
            metric_values=metric_values,
            tools=tools,
            tool_choice=tool_choice,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.chat_message import ChatMessage
from humanloop.model.config_response import ConfigResponse
from humanloop.model.evaluation_result_response import EvaluationResultResponse
from humanloop.model.feedback_response import FeedbackResponse
from humanloop.model.metric_value_response import MetricValueResponse
from humanloop.model.observability_status import ObservabilityStatus
from humanloop.model.project_config_response import ProjectConfigResponse
from humanloop.model.tool_choice import ToolChoice
from humanloop.model.tool_result_response import ToolResultResponse
