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


class FinetuneDataSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Summary of a finetuning dataset.
    """


    class MetaOapg:
        required = {
            "token_count",
            "cost",
            "dataset_id",
            "data_count",
            "dataset_name",
            "error_count",
            "errors",
            "truncated_data_count",
            "truncated_token_count",
        }
        
        class properties:
            data_count = schemas.IntSchema
            error_count = schemas.IntSchema
            truncated_data_count = schemas.IntSchema
            token_count = schemas.IntSchema
            truncated_token_count = schemas.IntSchema
            cost = schemas.NumberSchema
        
            @staticmethod
            def errors() -> typing.Type['FinetuneDataSummaryErrors']:
                return FinetuneDataSummaryErrors
            dataset_name = schemas.StrSchema
            dataset_id = schemas.StrSchema
            __annotations__ = {
                "data_count": data_count,
                "error_count": error_count,
                "truncated_data_count": truncated_data_count,
                "token_count": token_count,
                "truncated_token_count": truncated_token_count,
                "cost": cost,
                "errors": errors,
                "dataset_name": dataset_name,
                "dataset_id": dataset_id,
            }
    
    token_count: MetaOapg.properties.token_count
    cost: MetaOapg.properties.cost
    dataset_id: MetaOapg.properties.dataset_id
    data_count: MetaOapg.properties.data_count
    dataset_name: MetaOapg.properties.dataset_name
    error_count: MetaOapg.properties.error_count
    errors: 'FinetuneDataSummaryErrors'
    truncated_data_count: MetaOapg.properties.truncated_data_count
    truncated_token_count: MetaOapg.properties.truncated_token_count
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_count"]) -> MetaOapg.properties.data_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_count"]) -> MetaOapg.properties.error_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truncated_data_count"]) -> MetaOapg.properties.truncated_data_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_count"]) -> MetaOapg.properties.token_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truncated_token_count"]) -> MetaOapg.properties.truncated_token_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'FinetuneDataSummaryErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataset_name"]) -> MetaOapg.properties.dataset_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data_count", "error_count", "truncated_data_count", "token_count", "truncated_token_count", "cost", "errors", "dataset_name", "dataset_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_count"]) -> MetaOapg.properties.data_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_count"]) -> MetaOapg.properties.error_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truncated_data_count"]) -> MetaOapg.properties.truncated_data_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_count"]) -> MetaOapg.properties.token_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truncated_token_count"]) -> MetaOapg.properties.truncated_token_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'FinetuneDataSummaryErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataset_name"]) -> MetaOapg.properties.dataset_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data_count", "error_count", "truncated_data_count", "token_count", "truncated_token_count", "cost", "errors", "dataset_name", "dataset_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        token_count: typing.Union[MetaOapg.properties.token_count, decimal.Decimal, int, ],
        cost: typing.Union[MetaOapg.properties.cost, decimal.Decimal, int, float, ],
        dataset_id: typing.Union[MetaOapg.properties.dataset_id, str, ],
        data_count: typing.Union[MetaOapg.properties.data_count, decimal.Decimal, int, ],
        dataset_name: typing.Union[MetaOapg.properties.dataset_name, str, ],
        error_count: typing.Union[MetaOapg.properties.error_count, decimal.Decimal, int, ],
        errors: 'FinetuneDataSummaryErrors',
        truncated_data_count: typing.Union[MetaOapg.properties.truncated_data_count, decimal.Decimal, int, ],
        truncated_token_count: typing.Union[MetaOapg.properties.truncated_token_count, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FinetuneDataSummary':
        return super().__new__(
            cls,
            *args,
            token_count=token_count,
            cost=cost,
            dataset_id=dataset_id,
            data_count=data_count,
            dataset_name=dataset_name,
            error_count=error_count,
            errors=errors,
            truncated_data_count=truncated_data_count,
            truncated_token_count=truncated_token_count,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.finetune_data_summary_errors import FinetuneDataSummaryErrors
