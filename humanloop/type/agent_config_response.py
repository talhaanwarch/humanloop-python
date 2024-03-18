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
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from humanloop.type.model_config_request import ModelConfigRequest
from humanloop.type.tool_config_request import ToolConfigRequest
from humanloop.type.user_response import UserResponse

class RequiredAgentConfigResponse(TypedDict):
    # String ID of config. Starts with `config_`.
    id: str

    type: str

    # Whether the config is committed or not.
    status: str

    # Name of config.
    name: str

    # Class of the agent.
    agent_class: str

    # Model config associated with the agent.
    model_config: ModelConfigRequest

class OptionalAgentConfigResponse(TypedDict, total=False):
    # Description of config.
    description: str

    # Other parameters that define the config.
    other: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The user who created the config.
    created_by: UserResponse

    # Tools associated with the agent.
    tools: typing.List[ToolConfigRequest]

class AgentConfigResponse(RequiredAgentConfigResponse, OptionalAgentConfigResponse):
    pass
