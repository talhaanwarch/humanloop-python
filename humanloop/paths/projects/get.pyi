# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from humanloop.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from humanloop.api_response import AsyncGeneratorResponse
from humanloop import api_client, exceptions
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

from humanloop.model.sort_order import SortOrder as SortOrderSchema
from humanloop.model.experiment_config_response import ExperimentConfigResponse as ExperimentConfigResponseSchema
from humanloop.model.experiment_status import ExperimentStatus as ExperimentStatusSchema
from humanloop.model.validation_error_loc import ValidationErrorLoc as ValidationErrorLocSchema
from humanloop.model.project_sort_by import ProjectSortBy as ProjectSortBySchema
from humanloop.model.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse as ModelConfigEvaluatorAggregateResponseSchema
from humanloop.model.evaluator_arguments_type import EvaluatorArgumentsType as EvaluatorArgumentsTypeSchema
from humanloop.model.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse as ProjectModelConfigFeedbackStatsResponseSchema
from humanloop.model.config_response import ConfigResponse as ConfigResponseSchema
from humanloop.model.project_user_response import ProjectUserResponse as ProjectUserResponseSchema
from humanloop.model.project_response import ProjectResponse as ProjectResponseSchema
from humanloop.model.evaluator_response import EvaluatorResponse as EvaluatorResponseSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.positive_label import PositiveLabel as PositiveLabelSchema
from humanloop.model.paginated_data_project_response import PaginatedDataProjectResponse as PaginatedDataProjectResponseSchema
from humanloop.model.config_type import ConfigType as ConfigTypeSchema
from humanloop.model.experiment_response import ExperimentResponse as ExperimentResponseSchema
from humanloop.model.project_config_response import ProjectConfigResponse as ProjectConfigResponseSchema
from humanloop.model.evaluator_return_type_enum import EvaluatorReturnTypeEnum as EvaluatorReturnTypeEnumSchema
from humanloop.model.feedback_types import FeedbackTypes as FeedbackTypesSchema
from humanloop.model.base_metric_response import BaseMetricResponse as BaseMetricResponseSchema
from humanloop.model.validation_error import ValidationError as ValidationErrorSchema

from humanloop.type.config_response import ConfigResponse
from humanloop.type.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse
from humanloop.type.project_sort_by import ProjectSortBy
from humanloop.type.experiment_response import ExperimentResponse
from humanloop.type.evaluator_arguments_type import EvaluatorArgumentsType
from humanloop.type.positive_label import PositiveLabel
from humanloop.type.feedback_types import FeedbackTypes
from humanloop.type.experiment_status import ExperimentStatus
from humanloop.type.config_type import ConfigType
from humanloop.type.validation_error_loc import ValidationErrorLoc
from humanloop.type.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.type.paginated_data_project_response import PaginatedDataProjectResponse
from humanloop.type.validation_error import ValidationError
from humanloop.type.base_metric_response import BaseMetricResponse
from humanloop.type.experiment_config_response import ExperimentConfigResponse
from humanloop.type.project_user_response import ProjectUserResponse
from humanloop.type.project_response import ProjectResponse
from humanloop.type.evaluator_response import EvaluatorResponse
from humanloop.type.sort_order import SortOrder
from humanloop.type.evaluator_return_type_enum import EvaluatorReturnTypeEnum
from humanloop.type.project_config_response import ProjectConfigResponse
from humanloop.type.http_validation_error import HTTPValidationError

# Query params
PageSchema = schemas.IntSchema
SizeSchema = schemas.IntSchema
OrganizationIdSchema = schemas.StrSchema
FilterSchema = schemas.StrSchema
UserFilterSchema = schemas.StrSchema


class SortBySchema(
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
                ProjectSortBySchema,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SortBySchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


class OrderSchema(
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
                SortOrderSchema,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'size': typing.Union[SizeSchema, decimal.Decimal, int, ],
        'organization_id': typing.Union[OrganizationIdSchema, str, ],
        'filter': typing.Union[FilterSchema, str, ],
        'user_filter': typing.Union[UserFilterSchema, str, ],
        'sort_by': typing.Union[SortBySchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'order': typing.Union[OrderSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_size = api_client.QueryParameter(
    name="size",
    style=api_client.ParameterStyle.FORM,
    schema=SizeSchema,
    explode=True,
)
request_query_organization_id = api_client.QueryParameter(
    name="organization_id",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationIdSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_user_filter = api_client.QueryParameter(
    name="user_filter",
    style=api_client.ParameterStyle.FORM,
    schema=UserFilterSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PaginatedDataProjectResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaginatedDataProjectResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaginatedDataProjectResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        user_filter: typing.Optional[str] = None,
        sort_by: typing.Optional[ProjectSortBy] = None,
        order: typing.Optional[SortOrder] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if page is not None:
            _query_params["page"] = page
        if size is not None:
            _query_params["size"] = size
        if organization_id is not None:
            _query_params["organization_id"] = organization_id
        if filter is not None:
            _query_params["filter"] = filter
        if user_filter is not None:
            _query_params["user_filter"] = user_filter
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        if order is not None:
            _query_params["order"] = order
        args.query = _query_params
        return args

    async def _alist_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_size,
            request_query_organization_id,
            request_query_filter,
            request_query_user_filter,
            request_query_sort_by,
            request_query_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_size,
            request_query_organization_id,
            request_query_filter,
            request_query_user_filter,
            request_query_sort_by,
            request_query_order,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class List(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        user_filter: typing.Optional[str] = None,
        sort_by: typing.Optional[ProjectSortBy] = None,
        order: typing.Optional[SortOrder] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            page=page,
            size=size,
            organization_id=organization_id,
            filter=filter,
            user_filter=user_filter,
            sort_by=sort_by,
            order=order,
        )
        return await self._alist_oapg(
            query_params=args.query,
        )
    
    def list(
        self,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        user_filter: typing.Optional[str] = None,
        sort_by: typing.Optional[ProjectSortBy] = None,
        order: typing.Optional[SortOrder] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            page=page,
            size=size,
            organization_id=organization_id,
            filter=filter,
            user_filter=user_filter,
            sort_by=sort_by,
            order=order,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        user_filter: typing.Optional[str] = None,
        sort_by: typing.Optional[ProjectSortBy] = None,
        order: typing.Optional[SortOrder] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            page=page,
            size=size,
            organization_id=organization_id,
            filter=filter,
            user_filter=user_filter,
            sort_by=sort_by,
            order=order,
        )
        return await self._alist_oapg(
            query_params=args.query,
        )
    
    def get(
        self,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        organization_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        user_filter: typing.Optional[str] = None,
        sort_by: typing.Optional[ProjectSortBy] = None,
        order: typing.Optional[SortOrder] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            page=page,
            size=size,
            organization_id=organization_id,
            filter=filter,
            user_filter=user_filter,
            sort_by=sort_by,
            order=order,
        )
        return self._list_oapg(
            query_params=args.query,
        )

