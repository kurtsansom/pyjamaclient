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
from ..model.abstract_rest_response import AbstractRestResponse
from ..model.created_response import CreatedResponse
from ..model.request_group_user import RequestGroupUser
from ..model.request_user_group import RequestUserGroup
from ..model.user_data_list_wrapper import UserDataListWrapper
from ..model.user_group_data_list_wrapper import UserGroupDataListWrapper
from ..model.user_group_data_wrapper import UserGroupDataWrapper
from ..model_utils import check_allowed_values  # noqa: F401
from ..model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class UsergroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_user_group_endpoint = _Endpoint(
            settings={
                "response_type": (CreatedResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups",
                "operation_id": "add_user_group",
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
                "openapi_types": {"body": (RequestUserGroup,),},
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
        self.add_user_to_group_endpoint = _Endpoint(
            settings={
                "response_type": (CreatedResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}/users",
                "operation_id": "add_user_to_group",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": ["id", "body",],
                "required": ["id", "body",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"id": (int,), "body": (RequestGroupUser,),},
                "attribute_map": {"id": "id",},
                "location_map": {"id": "path", "body": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )
        self.delete_user_group_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}",
                "operation_id": "delete_user_group",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["id",],
                "required": ["id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"id": (int,),},
                "attribute_map": {"id": "id",},
                "location_map": {"id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.get_group_endpoint = _Endpoint(
            settings={
                "response_type": (UserGroupDataWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}",
                "operation_id": "get_group",
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
        self.get_group_users_endpoint = _Endpoint(
            settings={
                "response_type": (UserDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}/users",
                "operation_id": "get_group_users",
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
        self.get_user_groups_endpoint = _Endpoint(
            settings={
                "response_type": (UserGroupDataListWrapper,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups",
                "operation_id": "get_user_groups",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["project", "start_at", "max_results", "include",],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project": (int,),
                    "start_at": (int,),
                    "max_results": (int,),
                    "include": ([str],),
                },
                "attribute_map": {
                    "project": "project",
                    "start_at": "startAt",
                    "max_results": "maxResults",
                    "include": "include",
                },
                "location_map": {
                    "project": "query",
                    "start_at": "query",
                    "max_results": "query",
                    "include": "query",
                },
                "collection_format_map": {"include": "multi",},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.remove_user_from_group_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}/users/{userId}",
                "operation_id": "remove_user_from_group",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["user_id", "id",],
                "required": ["user_id", "id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"user_id": (int,), "id": (int,),},
                "attribute_map": {"user_id": "userId", "id": "id",},
                "location_map": {"user_id": "path", "id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
        )
        self.update_user_group_endpoint = _Endpoint(
            settings={
                "response_type": (AbstractRestResponse,),
                "auth": ["basic", "oauth2"],
                "endpoint_path": "/usergroups/{id}",
                "operation_id": "update_user_group",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": ["id", "body",],
                "required": ["id", "body",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"id": (int,), "body": (RequestUserGroup,),},
                "attribute_map": {"id": "id",},
                "location_map": {"id": "path", "body": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

    def add_user_group(self, body, **kwargs):
        """Create a new user group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_group(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (RequestUserGroup):

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
        return self.add_user_group_endpoint.call_with_http_info(**kwargs)

    def add_user_to_group(self, id, body, **kwargs):
        """Add an existing user to the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_user_to_group(id, body, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):
            body (RequestGroupUser):

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
        kwargs["id"] = id
        kwargs["body"] = body
        return self.add_user_to_group_endpoint.call_with_http_info(**kwargs)

    def delete_user_group(self, id, **kwargs):
        """Delete the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_group(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):

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
            AbstractRestResponse
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
        return self.delete_user_group_endpoint.call_with_http_info(**kwargs)

    def get_group(self, id, **kwargs):
        """Get the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group(id, async_req=True)
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
            UserGroupDataWrapper
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
        return self.get_group_endpoint.call_with_http_info(**kwargs)

    def get_group_users(self, id, **kwargs):
        """Get all users for the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_users(id, async_req=True)
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
            UserDataListWrapper
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
        return self.get_group_users_endpoint.call_with_http_info(**kwargs)

    def get_user_groups(self, **kwargs):
        """Get all user groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_groups(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            project (int): [optional]
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
            UserGroupDataListWrapper
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
        return self.get_user_groups_endpoint.call_with_http_info(**kwargs)

    def remove_user_from_group(self, user_id, id, **kwargs):
        """Remove an existing user from the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_user_from_group(user_id, id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (int):
            id (int):

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
            AbstractRestResponse
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
        kwargs["user_id"] = user_id
        kwargs["id"] = id
        return self.remove_user_from_group_endpoint.call_with_http_info(**kwargs)

    def update_user_group(self, id, body, **kwargs):
        """Update the user group with the specified ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_group(id, body, async_req=True)
        >>> result = thread.get()

        Args:
            id (int):
            body (RequestUserGroup):

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
            AbstractRestResponse
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
        kwargs["body"] = body
        return self.update_user_group_endpoint.call_with_http_info(**kwargs)