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


class ModelConfigRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model config used for logging both chat and completion.
    """


    class MetaOapg:
        required = {
            "model",
        }
        
        class properties:
            model = schemas.StrSchema
            description = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class provider(
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
                            ModelProviders,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'provider':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            max_tokens = schemas.IntSchema
            temperature = schemas.NumberSchema
            top_p = schemas.NumberSchema
            
            
            class stop(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    
                    
                    class any_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_1':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'stop':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            presence_penalty = schemas.NumberSchema
            frequency_penalty = schemas.NumberSchema
            other = schemas.DictSchema
            
            
            class endpoint(
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
                            ModelEndpoints,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'endpoint':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            prompt_template = schemas.StrSchema
            
            
            class chat_template(
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
                ) -> 'chat_template':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChatMessage':
                    return super().__getitem__(i)
            
            
            class tools(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelConfigToolRequest']:
                        return ModelConfigToolRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ModelConfigToolRequest'], typing.List['ModelConfigToolRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tools':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelConfigToolRequest':
                    return super().__getitem__(i)
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MODEL(cls):
                    return cls("model")
            __annotations__ = {
                "model": model,
                "description": description,
                "name": name,
                "provider": provider,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "stop": stop,
                "presence_penalty": presence_penalty,
                "frequency_penalty": frequency_penalty,
                "other": other,
                "endpoint": endpoint,
                "prompt_template": prompt_template,
                "chat_template": chat_template,
                "tools": tools,
                "type": type,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    model: MetaOapg.properties.model
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_tokens"]) -> MetaOapg.properties.max_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top_p"]) -> MetaOapg.properties.top_p: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop"]) -> MetaOapg.properties.stop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presence_penalty"]) -> MetaOapg.properties.presence_penalty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency_penalty"]) -> MetaOapg.properties.frequency_penalty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other"]) -> MetaOapg.properties.other: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> MetaOapg.properties.endpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_template"]) -> MetaOapg.properties.prompt_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chat_template"]) -> MetaOapg.properties.chat_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tools"]) -> MetaOapg.properties.tools: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["model"], typing_extensions.Literal["description"], typing_extensions.Literal["name"], typing_extensions.Literal["provider"], typing_extensions.Literal["max_tokens"], typing_extensions.Literal["temperature"], typing_extensions.Literal["top_p"], typing_extensions.Literal["stop"], typing_extensions.Literal["presence_penalty"], typing_extensions.Literal["frequency_penalty"], typing_extensions.Literal["other"], typing_extensions.Literal["endpoint"], typing_extensions.Literal["prompt_template"], typing_extensions.Literal["chat_template"], typing_extensions.Literal["tools"], typing_extensions.Literal["type"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_tokens"]) -> typing.Union[MetaOapg.properties.max_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top_p"]) -> typing.Union[MetaOapg.properties.top_p, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop"]) -> typing.Union[MetaOapg.properties.stop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presence_penalty"]) -> typing.Union[MetaOapg.properties.presence_penalty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency_penalty"]) -> typing.Union[MetaOapg.properties.frequency_penalty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other"]) -> typing.Union[MetaOapg.properties.other, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> typing.Union[MetaOapg.properties.endpoint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_template"]) -> typing.Union[MetaOapg.properties.prompt_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chat_template"]) -> typing.Union[MetaOapg.properties.chat_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tools"]) -> typing.Union[MetaOapg.properties.tools, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model"], typing_extensions.Literal["description"], typing_extensions.Literal["name"], typing_extensions.Literal["provider"], typing_extensions.Literal["max_tokens"], typing_extensions.Literal["temperature"], typing_extensions.Literal["top_p"], typing_extensions.Literal["stop"], typing_extensions.Literal["presence_penalty"], typing_extensions.Literal["frequency_penalty"], typing_extensions.Literal["other"], typing_extensions.Literal["endpoint"], typing_extensions.Literal["prompt_template"], typing_extensions.Literal["chat_template"], typing_extensions.Literal["tools"], typing_extensions.Literal["type"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        provider: typing.Union[MetaOapg.properties.provider, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        max_tokens: typing.Union[MetaOapg.properties.max_tokens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        top_p: typing.Union[MetaOapg.properties.top_p, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        stop: typing.Union[MetaOapg.properties.stop, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        presence_penalty: typing.Union[MetaOapg.properties.presence_penalty, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        frequency_penalty: typing.Union[MetaOapg.properties.frequency_penalty, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        other: typing.Union[MetaOapg.properties.other, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        endpoint: typing.Union[MetaOapg.properties.endpoint, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        prompt_template: typing.Union[MetaOapg.properties.prompt_template, str, schemas.Unset] = schemas.unset,
        chat_template: typing.Union[MetaOapg.properties.chat_template, list, tuple, schemas.Unset] = schemas.unset,
        tools: typing.Union[MetaOapg.properties.tools, list, tuple, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'ModelConfigRequest':
        return super().__new__(
            cls,
            *args,
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            endpoint=endpoint,
            prompt_template=prompt_template,
            chat_template=chat_template,
            tools=tools,
            type=type,
            _configuration=_configuration,
        )

from humanloop.model.chat_message import ChatMessage
from humanloop.model.chat_role import ChatRole
from humanloop.model.model_config_tool_request import ModelConfigToolRequest
from humanloop.model.model_endpoints import ModelEndpoints
from humanloop.model.model_providers import ModelProviders
from humanloop.model.tool_call import ToolCall
