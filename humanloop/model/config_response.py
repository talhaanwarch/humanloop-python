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


class ConfigResponse(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def discriminator():
            return {
                'type': {
                    'AgentConfigResponse': AgentConfigResponse,
                    'GenericConfigResponse': GenericConfigResponse,
                    'ModelConfigResponse': ModelConfigResponse,
                    'ToolConfigResponse': ToolConfigResponse,
                    'agent': AgentConfigResponse,
                    'generic': GenericConfigResponse,
                    'model': ModelConfigResponse,
                    'tool': ToolConfigResponse,
                }
            }
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                ModelConfigResponse,
                ToolConfigResponse,
                AgentConfigResponse,
                GenericConfigResponse,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConfigResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.agent_config_response import AgentConfigResponse
from humanloop.model.chat_message import ChatMessage
from humanloop.model.chat_role import ChatRole
from humanloop.model.generic_config_response import GenericConfigResponse
from humanloop.model.model_config_request import ModelConfigRequest
from humanloop.model.model_config_response import ModelConfigResponse
from humanloop.model.model_config_tool_request import ModelConfigToolRequest
from humanloop.model.model_endpoints import ModelEndpoints
from humanloop.model.model_providers import ModelProviders
from humanloop.model.tool_call import ToolCall
from humanloop.model.tool_config_request import ToolConfigRequest
from humanloop.model.tool_config_response import ToolConfigResponse
