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


class VolumeApi(object):
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

    def simengine_rest_simulation_node_attach_volume_get(self, node, simulation, volume, **kwargs):
        """
        Attach volume to a running node.
        Attach volume to a running node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_simulation_node_attach_volume_get(node, simulation, volume, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node: Node to attach the volume to (required)
        :param str simulation: Simulation ID (required)
        :param str volume: name of the volume to attach (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.simengine_rest_simulation_node_attach_volume_get_with_http_info(node, simulation, volume, **kwargs)
        else:
            (data) = self.simengine_rest_simulation_node_attach_volume_get_with_http_info(node, simulation, volume, **kwargs)
            return data

    def simengine_rest_simulation_node_attach_volume_get_with_http_info(self, node, simulation, volume, **kwargs):
        """
        Attach volume to a running node.
        Attach volume to a running node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_simulation_node_attach_volume_get_with_http_info(node, simulation, volume, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node: Node to attach the volume to (required)
        :param str simulation: Simulation ID (required)
        :param str volume: name of the volume to attach (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node', 'simulation', 'volume']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simengine_rest_simulation_node_attach_volume_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node' is set
        if ('node' not in params) or (params['node'] is None):
            raise ValueError("Missing the required parameter `node` when calling `simengine_rest_simulation_node_attach_volume_get`")
        # verify the required parameter 'simulation' is set
        if ('simulation' not in params) or (params['simulation'] is None):
            raise ValueError("Missing the required parameter `simulation` when calling `simengine_rest_simulation_node_attach_volume_get`")
        # verify the required parameter 'volume' is set
        if ('volume' not in params) or (params['volume'] is None):
            raise ValueError("Missing the required parameter `volume` when calling `simengine_rest_simulation_node_attach_volume_get`")


        collection_formats = {}

        path_params = {}
        if 'node' in params:
            path_params['node'] = params['node']
        if 'simulation' in params:
            path_params['simulation'] = params['simulation']
        if 'volume' in params:
            path_params['volume'] = params['volume']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/simengine/rest/{simulation}/{node}/attach/{volume}', 'GET',
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

    def simengine_rest_simulation_node_detach_volume_get(self, node, simulation, volume, **kwargs):
        """
        Detach volume from a running node.
        Detach volume from a running node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_simulation_node_detach_volume_get(node, simulation, volume, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node: Node to detach the volume from (required)
        :param str simulation: Simulation ID (required)
        :param str volume: name of the volume to detach (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.simengine_rest_simulation_node_detach_volume_get_with_http_info(node, simulation, volume, **kwargs)
        else:
            (data) = self.simengine_rest_simulation_node_detach_volume_get_with_http_info(node, simulation, volume, **kwargs)
            return data

    def simengine_rest_simulation_node_detach_volume_get_with_http_info(self, node, simulation, volume, **kwargs):
        """
        Detach volume from a running node.
        Detach volume from a running node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_simulation_node_detach_volume_get_with_http_info(node, simulation, volume, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node: Node to detach the volume from (required)
        :param str simulation: Simulation ID (required)
        :param str volume: name of the volume to detach (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node', 'simulation', 'volume']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simengine_rest_simulation_node_detach_volume_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node' is set
        if ('node' not in params) or (params['node'] is None):
            raise ValueError("Missing the required parameter `node` when calling `simengine_rest_simulation_node_detach_volume_get`")
        # verify the required parameter 'simulation' is set
        if ('simulation' not in params) or (params['simulation'] is None):
            raise ValueError("Missing the required parameter `simulation` when calling `simengine_rest_simulation_node_detach_volume_get`")
        # verify the required parameter 'volume' is set
        if ('volume' not in params) or (params['volume'] is None):
            raise ValueError("Missing the required parameter `volume` when calling `simengine_rest_simulation_node_detach_volume_get`")


        collection_formats = {}

        path_params = {}
        if 'node' in params:
            path_params['node'] = params['node']
        if 'simulation' in params:
            path_params['simulation'] = params['simulation']
        if 'volume' in params:
            path_params['volume'] = params['volume']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/simengine/rest/{simulation}/{node}/detach/{volume}', 'GET',
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
