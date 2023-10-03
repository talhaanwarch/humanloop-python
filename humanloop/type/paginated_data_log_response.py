# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_role import ChatRole
from humanloop.type.config_response import ConfigResponse
from humanloop.type.feedback import Feedback
from humanloop.type.feedback_type import FeedbackType
from humanloop.type.log_response import LogResponse
from humanloop.type.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.type.project_config_response import ProjectConfigResponse
from humanloop.type.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse
from humanloop.type.tool_call import ToolCall

class RequiredPaginatedDataLogResponse(TypedDict):
    records: typing.List[LogResponse]

    page: int

    size: int

    total: int

class OptionalPaginatedDataLogResponse(TypedDict, total=False):
    pass

class PaginatedDataLogResponse(RequiredPaginatedDataLogResponse, OptionalPaginatedDataLogResponse):
    pass
