# coding: utf-8

"""
    Femsa API

    Femsa sdk

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@femsa.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from digitalfemsa.models.get_transactions_response import GetTransactionsResponse
from digitalfemsa.models.transaction_response import TransactionResponse

from digitalfemsa.api_client import ApiClient, RequestSerialized
from digitalfemsa.api_response import ApiResponse
from digitalfemsa.rest import RESTResponseType


class TransactionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_transaction(
        self,
        id: Annotated[StrictStr, Field(description="Identifier of the resource")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> TransactionResponse:
        """Get transaction

        Get the details of a transaction

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transaction_serialize(
            id=id,
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TransactionResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_transaction_with_http_info(
        self,
        id: Annotated[StrictStr, Field(description="Identifier of the resource")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[TransactionResponse]:
        """Get transaction

        Get the details of a transaction

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transaction_serialize(
            id=id,
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TransactionResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_transaction_without_preload_content(
        self,
        id: Annotated[StrictStr, Field(description="Identifier of the resource")],
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get transaction

        Get the details of a transaction

        :param id: Identifier of the resource (required)
        :type id: str
        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transaction_serialize(
            id=id,
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TransactionResponse",
            '401': "Error",
            '404': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_transaction_serialize(
        self,
        id,
        accept_language,
        x_child_company_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if accept_language is not None:
            _header_params['Accept-Language'] = accept_language
        if x_child_company_id is not None:
            _header_params['X-Child-Company-Id'] = x_child_company_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.app-v2.1.0+json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'bearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/transactions/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_transactions(
        self,
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=250, strict=True, ge=1)]], Field(description="The numbers of items to return, the maximum value is 250")] = None,
        next: Annotated[Optional[StrictStr], Field(description="next page")] = None,
        previous: Annotated[Optional[StrictStr], Field(description="previous page")] = None,
        id: Annotated[Optional[StrictStr], Field(description="id of the object to be retrieved")] = None,
        charge_id: Annotated[Optional[StrictStr], Field(description="id of the charge used for filtering")] = None,
        type: Annotated[Optional[StrictStr], Field(description="type of the object to be retrieved")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="currency of the object to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetTransactionsResponse:
        """Get List transactions

        Get transaction details in the form of a list

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
        :param id: id of the object to be retrieved
        :type id: str
        :param charge_id: id of the charge used for filtering
        :type charge_id: str
        :param type: type of the object to be retrieved
        :type type: str
        :param currency: currency of the object to be retrieved
        :type currency: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transactions_serialize(
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            limit=limit,
            next=next,
            previous=previous,
            id=id,
            charge_id=charge_id,
            type=type,
            currency=currency,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetTransactionsResponse",
            '401': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_transactions_with_http_info(
        self,
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=250, strict=True, ge=1)]], Field(description="The numbers of items to return, the maximum value is 250")] = None,
        next: Annotated[Optional[StrictStr], Field(description="next page")] = None,
        previous: Annotated[Optional[StrictStr], Field(description="previous page")] = None,
        id: Annotated[Optional[StrictStr], Field(description="id of the object to be retrieved")] = None,
        charge_id: Annotated[Optional[StrictStr], Field(description="id of the charge used for filtering")] = None,
        type: Annotated[Optional[StrictStr], Field(description="type of the object to be retrieved")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="currency of the object to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetTransactionsResponse]:
        """Get List transactions

        Get transaction details in the form of a list

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
        :param id: id of the object to be retrieved
        :type id: str
        :param charge_id: id of the charge used for filtering
        :type charge_id: str
        :param type: type of the object to be retrieved
        :type type: str
        :param currency: currency of the object to be retrieved
        :type currency: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transactions_serialize(
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            limit=limit,
            next=next,
            previous=previous,
            id=id,
            charge_id=charge_id,
            type=type,
            currency=currency,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetTransactionsResponse",
            '401': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_transactions_without_preload_content(
        self,
        accept_language: Annotated[Optional[StrictStr], Field(description="Use for knowing which language to use")] = None,
        x_child_company_id: Annotated[Optional[StrictStr], Field(description="In the case of a holding company, the company id of the child company to which will process the request.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=250, strict=True, ge=1)]], Field(description="The numbers of items to return, the maximum value is 250")] = None,
        next: Annotated[Optional[StrictStr], Field(description="next page")] = None,
        previous: Annotated[Optional[StrictStr], Field(description="previous page")] = None,
        id: Annotated[Optional[StrictStr], Field(description="id of the object to be retrieved")] = None,
        charge_id: Annotated[Optional[StrictStr], Field(description="id of the charge used for filtering")] = None,
        type: Annotated[Optional[StrictStr], Field(description="type of the object to be retrieved")] = None,
        currency: Annotated[Optional[StrictStr], Field(description="currency of the object to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get List transactions

        Get transaction details in the form of a list

        :param accept_language: Use for knowing which language to use
        :type accept_language: str
        :param x_child_company_id: In the case of a holding company, the company id of the child company to which will process the request.
        :type x_child_company_id: str
        :param limit: The numbers of items to return, the maximum value is 250
        :type limit: int
        :param next: next page
        :type next: str
        :param previous: previous page
        :type previous: str
        :param id: id of the object to be retrieved
        :type id: str
        :param charge_id: id of the charge used for filtering
        :type charge_id: str
        :param type: type of the object to be retrieved
        :type type: str
        :param currency: currency of the object to be retrieved
        :type currency: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_transactions_serialize(
            accept_language=accept_language,
            x_child_company_id=x_child_company_id,
            limit=limit,
            next=next,
            previous=previous,
            id=id,
            charge_id=charge_id,
            type=type,
            currency=currency,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetTransactionsResponse",
            '401': "Error",
            '500': "Error",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_transactions_serialize(
        self,
        accept_language,
        x_child_company_id,
        limit,
        next,
        previous,
        id,
        charge_id,
        type,
        currency,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if next is not None:
            
            _query_params.append(('next', next))
            
        if previous is not None:
            
            _query_params.append(('previous', previous))
            
        if id is not None:
            
            _query_params.append(('id', id))
            
        if charge_id is not None:
            
            _query_params.append(('charge_id', charge_id))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if currency is not None:
            
            _query_params.append(('currency', currency))
            
        # process the header parameters
        if accept_language is not None:
            _header_params['Accept-Language'] = accept_language
        if x_child_company_id is not None:
            _header_params['X-Child-Company-Id'] = x_child_company_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.app-v2.1.0+json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'bearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/transactions',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


