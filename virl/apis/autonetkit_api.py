# coding: utf-8

"""
    VIRL STD API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AutonetkitApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def ank_rest_process_post(self, **kwargs):
        """
        Process a VIRL XML Topology
        This call processes a VIRL XML Topology file with AutoNetkit and assign initial configuration into each node’s config extension entry, based on parameters included in other extension entries throughout the file. In case the AutoNetkit subprocess returns with an error, the response will contain the log of the AutoNetkit process. Since AutoNetkit’s logs may be vital even in case of a successful configuration, the logs may be requested to be returned in a MIME multipart response. This behaviour can be turned on via the Accept HTTP header
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ank_rest_process_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str debug: Enable debug logging
        :param str uuid: Identifier for AutoNetkit Visualization Web UI
        :param str session: DEPRECATED, the same as uuid
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.ank_rest_process_post_with_http_info(**kwargs)
        else:
            (data) = self.ank_rest_process_post_with_http_info(**kwargs)
            return data

    def ank_rest_process_post_with_http_info(self, **kwargs):
        """
        Process a VIRL XML Topology
        This call processes a VIRL XML Topology file with AutoNetkit and assign initial configuration into each node’s config extension entry, based on parameters included in other extension entries throughout the file. In case the AutoNetkit subprocess returns with an error, the response will contain the log of the AutoNetkit process. Since AutoNetkit’s logs may be vital even in case of a successful configuration, the logs may be requested to be returned in a MIME multipart response. This behaviour can be turned on via the Accept HTTP header
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ank_rest_process_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str debug: Enable debug logging
        :param str uuid: Identifier for AutoNetkit Visualization Web UI
        :param str session: DEPRECATED, the same as uuid
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debug', 'uuid', 'session']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ank_rest_process_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'debug' in params:
            query_params.append(('debug', params['debug']))
        if 'uuid' in params:
            query_params.append(('uuid', params['uuid']))
        if 'session' in params:
            query_params.append(('session', params['session']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/xml', 'multipart/mixed'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/xml', 'multipart/mixed'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ank/rest/process', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='object',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def ank_rest_test_get(self, **kwargs):
        """
        Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
        Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ank_rest_test_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.ank_rest_test_get_with_http_info(**kwargs)
        else:
            (data) = self.ank_rest_test_get_with_http_info(**kwargs)
            return data

    def ank_rest_test_get_with_http_info(self, **kwargs):
        """
        Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
        Verify the user is authenticated and return autonetkit API version. Also displays installed AutoNetkit version
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.ank_rest_test_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ank_rest_test_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ank/rest/test', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StdDefsJsondefinitionsnoschema',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
