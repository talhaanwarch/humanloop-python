# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
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


class CreateTestcaseRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def inputs() -> typing.Type['CreateTestcaseRequestInputs']:
                return CreateTestcaseRequestInputs
            
            
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
        
            @staticmethod
            def target() -> typing.Type['CreateTestcaseRequestTarget']:
                return CreateTestcaseRequestTarget
            __annotations__ = {
                "inputs": inputs,
                "messages": messages,
                "target": target,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> 'CreateTestcaseRequestInputs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> 'CreateTestcaseRequestTarget': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inputs", "messages", "target", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union['CreateTestcaseRequestInputs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> typing.Union[MetaOapg.properties.messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union['CreateTestcaseRequestTarget', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inputs", "messages", "target", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        inputs: typing.Union['CreateTestcaseRequestInputs', schemas.Unset] = schemas.unset,
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, schemas.Unset] = schemas.unset,
        target: typing.Union['CreateTestcaseRequestTarget', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateTestcaseRequest':
        return super().__new__(
            cls,
            *args,
            inputs=inputs,
            messages=messages,
            target=target,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.chat_message import ChatMessage
from humanloop.model.chat_role import ChatRole
from humanloop.model.create_testcase_request_inputs import CreateTestcaseRequestInputs
from humanloop.model.create_testcase_request_target import CreateTestcaseRequestTarget
from humanloop.model.tool_call import ToolCall
