# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from humanloop.type.agent_config_response import AgentConfigResponse
from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_role import ChatRole
from humanloop.type.generic_config_response import GenericConfigResponse
from humanloop.type.model_config_request import ModelConfigRequest
from humanloop.type.model_config_response import ModelConfigResponse
from humanloop.type.model_config_tool_request import ModelConfigToolRequest
from humanloop.type.model_endpoints import ModelEndpoints
from humanloop.type.model_providers import ModelProviders
from humanloop.type.tool_call import ToolCall
from humanloop.type.tool_config_request import ToolConfigRequest
from humanloop.type.tool_config_response import ToolConfigResponse

ConfigResponse = typing.Union[ModelConfigResponse,ToolConfigResponse,AgentConfigResponse,GenericConfigResponse]
