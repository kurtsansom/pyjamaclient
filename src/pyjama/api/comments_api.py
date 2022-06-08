"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..api_client import ApiClient
from ..api_client import Endpoint as _Endpoint
from ..model.comment_data_list_wrapper import CommentDataListWrapper
from ..model.comment_data_wrapper import CommentDataWrapper
from ..model.created_response import CreatedResponse
from ..model.request_comment import RequestComment
from ..model_utils import check_allowed_values  # noqa: F401
from ..model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class CommentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_comment_endpoint = _Endpoint(
            settings={
                "response_type": (CreatedResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/comments",
                "operation_id": "add_comment",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": ["body",],
                "required": ["body",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"body": (RequestComment,),},
                "attribute_map": {},
                "location_map": {"body": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.get_comment_endpoint = _Endpoint(
            settings={
                "response_type": (CommentDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/comments/{id}",
                "operation_id": "get_comment",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["id", "include",],
                "required": ["id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"id": (int,), "include": ([str],),},
                "attribute_map": {"id": "id", "include": "include",},
                "location_map": {"id": "path", "include": "query",},
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_comment_replies_endpoint = _Endpoint(
            settings={
                "response_type": (CommentDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/comments/{id}/replies",
                "operation_id": "get_comment_replies",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["id", "start_at", "max_results", "include",],
                "required": ["id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "id": (int,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "id": "id",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "id": "path",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_comments_endpoint = _Endpoint(
            settings={
                "response_type": (CommentDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/comments",
                "operation_id": "get_comments",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["start_at", "max_results", "root_comments_only", "include",],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "start_at": (int,),
                    "max_results": (int,),
                    "root_comments_only": (bool,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "root_comments_only": "rootCommentsOnly",
                    "include": "include",
                },
                "location_map": {
                    "start_at": "query",
                    "max_results": "query",
                    "root_comments_only": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )

    def add_comment(self, body, **kwargs):
        """Create a new comment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_comment(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (RequestComment):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CreatedResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["body"] = body
        return self.add_comment_endpoint.call_with_http_info(**kwargs)

    def get_comment(self, id, **kwargs):
        """Get the comment with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_comment(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):

        Keyword Args:
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CommentDataWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["id"] = id
        return self.get_comment_endpoint.call_with_http_info(**kwargs)

    def get_comment_replies(self, id, **kwargs):
        """Get all reply comments for the comment with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_comment_replies(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):

        Keyword Args:
            start_at (int): [optional]
            max_results (int): If not set, this defaults to 20. This cannot be larger than 50. [optional]
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CommentDataListWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["id"] = id
        return self.get_comment_replies_endpoint.call_with_http_info(**kwargs)

    def get_comments(self, **kwargs):
        """Get all comments viewable by the current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_comments(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            start_at (int): [optional]
            max_results (int): If not set, this defaults to 20. This cannot be larger than 50. [optional]
            root_comments_only (bool): whether to show only root comments; true to get only root comments, without their comment replies. [optional] if omitted the server will use the default value of False
            include ([str]): Links to include as full objects in the linked map. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CommentDataListWrapper
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.get_comments_endpoint.call_with_http_info(**kwargs)