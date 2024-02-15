# coding: utf-8

"""
    CMS Source Code

    Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.source_code.api_client import ApiClient
from hubspot.cms.source_code.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class ContentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, environment, path, **kwargs):  # noqa: E501
        """Delete a file  # noqa: E501

        Deletes the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(environment, path, **kwargs)  # noqa: E501

    def archive_with_http_info(self, environment, path, **kwargs):  # noqa: E501
        """Delete a file  # noqa: E501

        Deletes the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = ["environment", "path"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'environment' is set
        if self.api_client.client_side_validation and local_var_params.get("environment") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `environment` when calling `archive`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and local_var_params.get("path") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `archive`")  # noqa: E501

        if self.api_client.client_side_validation and "path" in local_var_params and not re.search(r".+", local_var_params["path"]):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `path` when calling `archive`, must conform to the pattern `/.+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "environment" in local_var_params:
            path_params["environment"] = local_var_params["environment"]  # noqa: E501
        if "path" in local_var_params:
            path_params["path"] = local_var_params["path"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/cms/v3/source-code/{environment}/content/{path}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def create(self, environment, path, **kwargs):  # noqa: E501
        """Create a file  # noqa: E501

        Creates a file at the specified path in the specified environment. Accepts multipart/form-data content type. Throws an error if a file already exists at the specified path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param file: The file to upload.
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AssetFileMetadata
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(environment, path, **kwargs)  # noqa: E501

    def create_with_http_info(self, environment, path, **kwargs):  # noqa: E501
        """Create a file  # noqa: E501

        Creates a file at the specified path in the specified environment. Accepts multipart/form-data content type. Throws an error if a file already exists at the specified path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_with_http_info(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param file: The file to upload.
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AssetFileMetadata, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["environment", "path", "file"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'environment' is set
        if self.api_client.client_side_validation and local_var_params.get("environment") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `environment` when calling `create`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and local_var_params.get("path") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `create`")  # noqa: E501

        if self.api_client.client_side_validation and "path" in local_var_params and not re.search(r".+", local_var_params["path"]):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `path` when calling `create`, must conform to the pattern `/.+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "environment" in local_var_params:
            path_params["environment"] = local_var_params["environment"]  # noqa: E501
        if "path" in local_var_params:
            path_params["path"] = local_var_params["path"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}
        if "file" in local_var_params:
            local_var_files["file"] = local_var_params["file"]  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["multipart/form-data"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "AssetFileMetadata",
        }

        return self.api_client.call_api(
            "/cms/v3/source-code/{environment}/content/{path}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def create_or_update(self, environment, path, **kwargs):  # noqa: E501
        """Create or update a file  # noqa: E501

        Upserts a file at the specified path in the specified environment. Accepts multipart/form-data content type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_or_update(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param file: The file to upload.
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AssetFileMetadata
        """
        kwargs["_return_http_data_only"] = True
        return self.create_or_update_with_http_info(environment, path, **kwargs)  # noqa: E501

    def create_or_update_with_http_info(self, environment, path, **kwargs):  # noqa: E501
        """Create or update a file  # noqa: E501

        Upserts a file at the specified path in the specified environment. Accepts multipart/form-data content type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_or_update_with_http_info(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param file: The file to upload.
        :type file: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AssetFileMetadata, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["environment", "path", "file"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create_or_update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'environment' is set
        if self.api_client.client_side_validation and local_var_params.get("environment") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `environment` when calling `create_or_update`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and local_var_params.get("path") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `create_or_update`")  # noqa: E501

        if self.api_client.client_side_validation and "path" in local_var_params and not re.search(r".+", local_var_params["path"]):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `path` when calling `create_or_update`, must conform to the pattern `/.+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "environment" in local_var_params:
            path_params["environment"] = local_var_params["environment"]  # noqa: E501
        if "path" in local_var_params:
            path_params["path"] = local_var_params["path"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}
        if "file" in local_var_params:
            local_var_files["file"] = local_var_params["file"]  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["multipart/form-data"], "PUT", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "AssetFileMetadata",
        }

        return self.api_client.call_api(
            "/cms/v3/source-code/{environment}/content/{path}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def download(self, environment, path, **kwargs):  # noqa: E501
        """Download a file  # noqa: E501

        Downloads the byte contents of the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Error
        """
        kwargs["_return_http_data_only"] = True
        return self.download_with_http_info(environment, path, **kwargs)  # noqa: E501

    def download_with_http_info(self, environment, path, **kwargs):  # noqa: E501
        """Download a file  # noqa: E501

        Downloads the byte contents of the file at the specified path in the specified environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_with_http_info(environment, path, async_req=True)
        >>> result = thread.get()

        :param environment: The environment of the file (\"draft\" or \"published\"). (required)
        :type environment: str
        :param path: The file system location of the file. (required)
        :type path: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Error, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["environment", "path"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method download" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'environment' is set
        if self.api_client.client_side_validation and local_var_params.get("environment") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `environment` when calling `download`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and local_var_params.get("path") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `path` when calling `download`")  # noqa: E501

        if self.api_client.client_side_validation and "path" in local_var_params and not re.search(r".+", local_var_params["path"]):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `path` when calling `download`, must conform to the pattern `/.+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "environment" in local_var_params:
            path_params["environment"] = local_var_params["environment"]  # noqa: E501
        if "path" in local_var_params:
            path_params["path"] = local_var_params["path"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/cms/v3/source-code/{environment}/content/{path}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
