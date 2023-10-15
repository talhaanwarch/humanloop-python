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


class RequiredEnvironmentProjectConfigResponse(TypedDict):
    # String ID of project the model config belongs to. Starts with `pr_`.
    project_id: str

    # Name of the project the model config belongs to.
    project_name: str

    # The ID of the environment.
    environment_id: str

    # The name of the environment.
    environment_name: str

    # Tag for the environment e.g. 'default' or 'other'.
    environment_tag: str

class OptionalEnvironmentProjectConfigResponse(TypedDict, total=False):
    # Model config unique identifier generated by Humanloop.
    model_config_id: str

    # A friendly display name for the model config.
    model_config_name: str

    # String ID of experiment. Starts with `exp_`.
    experiment_id: str

    # Display name of experiment.
    experiment_name: str

class EnvironmentProjectConfigResponse(RequiredEnvironmentProjectConfigResponse, OptionalEnvironmentProjectConfigResponse):
    pass
