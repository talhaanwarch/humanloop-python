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


class CreateEvaluationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "config_id",
            "dataset_id",
            "evaluator_ids",
        }
        
        class properties:
            config_id = schemas.StrSchema
        
            @staticmethod
            def evaluator_ids() -> typing.Type['CreateEvaluationRequestEvaluatorIds']:
                return CreateEvaluationRequestEvaluatorIds
            dataset_id = schemas.StrSchema
            
            
            class provider_api_keys(
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
                            ProviderApiKeys,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'provider_api_keys':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "config_id": config_id,
                "evaluator_ids": evaluator_ids,
                "dataset_id": dataset_id,
                "provider_api_keys": provider_api_keys,
            }
    
    config_id: MetaOapg.properties.config_id
    dataset_id: MetaOapg.properties.dataset_id
    evaluator_ids: 'CreateEvaluationRequestEvaluatorIds'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_ids"]) -> 'CreateEvaluationRequestEvaluatorIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_api_keys"]) -> MetaOapg.properties.provider_api_keys: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["config_id", "evaluator_ids", "dataset_id", "provider_api_keys", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_ids"]) -> 'CreateEvaluationRequestEvaluatorIds': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_api_keys"]) -> typing.Union[MetaOapg.properties.provider_api_keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["config_id", "evaluator_ids", "dataset_id", "provider_api_keys", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        config_id: typing.Union[MetaOapg.properties.config_id, str, ],
        dataset_id: typing.Union[MetaOapg.properties.dataset_id, str, ],
        evaluator_ids: 'CreateEvaluationRequestEvaluatorIds',
        provider_api_keys: typing.Union[MetaOapg.properties.provider_api_keys, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateEvaluationRequest':
        return super().__new__(
            cls,
            *args,
            config_id=config_id,
            dataset_id=dataset_id,
            evaluator_ids=evaluator_ids,
            provider_api_keys=provider_api_keys,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.create_evaluation_request_evaluator_ids import CreateEvaluationRequestEvaluatorIds
from humanloop.model.provider_api_keys import ProviderApiKeys
