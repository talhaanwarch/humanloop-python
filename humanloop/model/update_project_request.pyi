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


class UpdateProjectRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            active_experiment_id = schemas.StrSchema
            active_config_id = schemas.StrSchema
            
            
            class positive_labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PositiveLabel']:
                        return PositiveLabel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PositiveLabel'], typing.List['PositiveLabel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'positive_labels':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PositiveLabel':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "active_experiment_id": active_experiment_id,
                "active_config_id": active_config_id,
                "positive_labels": positive_labels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_experiment_id"]) -> MetaOapg.properties.active_experiment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_config_id"]) -> MetaOapg.properties.active_config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positive_labels"]) -> MetaOapg.properties.positive_labels: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "active_experiment_id", "active_config_id", "positive_labels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_experiment_id"]) -> typing.Union[MetaOapg.properties.active_experiment_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_config_id"]) -> typing.Union[MetaOapg.properties.active_config_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positive_labels"]) -> typing.Union[MetaOapg.properties.positive_labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "active_experiment_id", "active_config_id", "positive_labels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        active_experiment_id: typing.Union[MetaOapg.properties.active_experiment_id, str, schemas.Unset] = schemas.unset,
        active_config_id: typing.Union[MetaOapg.properties.active_config_id, str, schemas.Unset] = schemas.unset,
        positive_labels: typing.Union[MetaOapg.properties.positive_labels, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateProjectRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            active_experiment_id=active_experiment_id,
            active_config_id=active_config_id,
            positive_labels=positive_labels,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.positive_label import PositiveLabel
