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

from humanloop.type.model_providers import ModelProviders

class RequiredFinetuneConfig(TypedDict):
    # Unique reference to the model the fine-tuning was based on.
    base_model: str

class OptionalFinetuneConfig(TypedDict, total=False):
    # Provider specific hyper-parameter settings that along with your base model will configure the fine-tuning process with the provider.
    parameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The company who is hosting the target model.This is used only if an existing experiment_id or model_config_id are not provided.
    provider: ModelProviders

class FinetuneConfig(RequiredFinetuneConfig, OptionalFinetuneConfig):
    pass
