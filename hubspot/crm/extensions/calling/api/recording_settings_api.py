# coding: utf-8

"""
    CRM Calling Extensions

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.extensions.calling.api_client import ApiClient
from hubspot.crm.extensions.calling.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class RecordingSettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_url_format(self, app_id, **kwargs):  # noqa: E501
        """Read calling app recording settings  # noqa: E501

        Retrieve the recording endpoint configured for a calling extension app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_url_format(app_id, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
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
        :rtype: RecordingSettingsResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.get_url_format_with_http_info(app_id, **kwargs)  # noqa: E501

    def get_url_format_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """Read calling app recording settings  # noqa: E501

        Retrieve the recording endpoint configured for a calling extension app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_url_format_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
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
        :rtype: tuple(RecordingSettingsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["app_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_url_format" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_url_format`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        response_types_map = {
            200: "RecordingSettingsResponse",
        }

        return self.api_client.call_api(
            "/crm/v3/extensions/calling/{appId}/settings/recording",
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

    def mark_as_ready(self, mark_recording_as_ready_request, **kwargs):  # noqa: E501
        """Mark recording as ready for transcription  # noqa: E501

        Mark a call recording as ready for transcription, specifying the call by its ID (`engagementid`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mark_as_ready(mark_recording_as_ready_request, async_req=True)
        >>> result = thread.get()

        :param mark_recording_as_ready_request: (required)
        :type mark_recording_as_ready_request: MarkRecordingAsReadyRequest
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
        return self.mark_as_ready_with_http_info(mark_recording_as_ready_request, **kwargs)  # noqa: E501

    def mark_as_ready_with_http_info(self, mark_recording_as_ready_request, **kwargs):  # noqa: E501
        """Mark recording as ready for transcription  # noqa: E501

        Mark a call recording as ready for transcription, specifying the call by its ID (`engagementid`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mark_as_ready_with_http_info(mark_recording_as_ready_request, async_req=True)
        >>> result = thread.get()

        :param mark_recording_as_ready_request: (required)
        :type mark_recording_as_ready_request: MarkRecordingAsReadyRequest
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

        all_params = ["mark_recording_as_ready_request"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method mark_as_ready" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'mark_recording_as_ready_request' is set
        if self.api_client.client_side_validation and local_var_params.get("mark_recording_as_ready_request") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `mark_recording_as_ready_request` when calling `mark_as_ready`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "mark_recording_as_ready_request" in local_var_params:
            body_params = local_var_params["mark_recording_as_ready_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/crm/v3/extensions/calling/recordings/ready",
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

    def register_url_format(self, app_id, recording_settings_request, **kwargs):  # noqa: E501
        """Register calling app for recording  # noqa: E501

        Configure a calling extension app with an external URL that HubSpot will use to retrieve call recordings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.register_url_format(app_id, recording_settings_request, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
        :param recording_settings_request: (required)
        :type recording_settings_request: RecordingSettingsRequest
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
        :rtype: RecordingSettingsResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.register_url_format_with_http_info(app_id, recording_settings_request, **kwargs)  # noqa: E501

    def register_url_format_with_http_info(self, app_id, recording_settings_request, **kwargs):  # noqa: E501
        """Register calling app for recording  # noqa: E501

        Configure a calling extension app with an external URL that HubSpot will use to retrieve call recordings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.register_url_format_with_http_info(app_id, recording_settings_request, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
        :param recording_settings_request: (required)
        :type recording_settings_request: RecordingSettingsRequest
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
        :rtype: tuple(RecordingSettingsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["app_id", "recording_settings_request"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method register_url_format" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `register_url_format`")  # noqa: E501
        # verify the required parameter 'recording_settings_request' is set
        if self.api_client.client_side_validation and local_var_params.get("recording_settings_request") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `recording_settings_request` when calling `register_url_format`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "recording_settings_request" in local_var_params:
            body_params = local_var_params["recording_settings_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        response_types_map = {
            200: "RecordingSettingsResponse",
        }

        return self.api_client.call_api(
            "/crm/v3/extensions/calling/{appId}/settings/recording",
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

    def update_url_format(self, app_id, recording_settings_patch_request, **kwargs):  # noqa: E501
        """Update calling app's recording settings  # noqa: E501

        Update the URL that HubSpot will use to retrieve call recordings for a calling extension app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_url_format(app_id, recording_settings_patch_request, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
        :param recording_settings_patch_request: (required)
        :type recording_settings_patch_request: RecordingSettingsPatchRequest
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
        :rtype: RecordingSettingsResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.update_url_format_with_http_info(app_id, recording_settings_patch_request, **kwargs)  # noqa: E501

    def update_url_format_with_http_info(self, app_id, recording_settings_patch_request, **kwargs):  # noqa: E501
        """Update calling app's recording settings  # noqa: E501

        Update the URL that HubSpot will use to retrieve call recordings for a calling extension app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_url_format_with_http_info(app_id, recording_settings_patch_request, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the app. (required)
        :type app_id: int
        :param recording_settings_patch_request: (required)
        :type recording_settings_patch_request: RecordingSettingsPatchRequest
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
        :rtype: tuple(RecordingSettingsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["app_id", "recording_settings_patch_request"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method update_url_format" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `update_url_format`")  # noqa: E501
        # verify the required parameter 'recording_settings_patch_request' is set
        if self.api_client.client_side_validation and local_var_params.get("recording_settings_patch_request") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `recording_settings_patch_request` when calling `update_url_format`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "recording_settings_patch_request" in local_var_params:
            body_params = local_var_params["recording_settings_patch_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "PATCH", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["developer_hapikey"]  # noqa: E501

        response_types_map = {
            200: "RecordingSettingsResponse",
        }

        return self.api_client.call_api(
            "/crm/v3/extensions/calling/{appId}/settings/recording",
            "PATCH",
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