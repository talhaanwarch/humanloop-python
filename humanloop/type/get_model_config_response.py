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

from humanloop.type.config_response import ConfigResponse
from humanloop.type.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.type.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse

class RequiredGetModelConfigResponse(TypedDict):
    # String ID of project the model config belongs to. Starts with `pr_`.
    project_id: str

    # Name of the project the model config belongs to.
    project_name: str

    created_at: datetime

    updated_at: datetime

    last_used: datetime

    config: ConfigResponse

class OptionalGetModelConfigResponse(TypedDict, total=False):
    # Feedback statistics for the project model config.
    feedback_stats: typing.List[ProjectModelConfigFeedbackStatsResponse]

    # Number of datapoints associated with this project model config.
    num_datapoints: int

    # The ID of the experiment the model config has been registered to. Only populated when registering a model config to an experiment.
    experiment_id: str

    # Aggregates of evaluators for the model config.
    evaluation_aggregates: typing.List[ModelConfigEvaluatorAggregateResponse]

    # ID of trial to reference in subsequent log calls.
    trial_id: str

    # ID of environment to reference in subsequent log calls.
    environment_id: str

class GetModelConfigResponse(RequiredGetModelConfigResponse, OptionalGetModelConfigResponse):
    pass
