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


class SnapshotApi(object):
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

    def simengine_rest_snapshot_simulation_node_post(self, simulation, node, **kwargs):
        """
        Create snapshot of a node
        Create snapshot of a node. The snapshot will be a private image (visible only inside the same project) named as project-subtype-imagename.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_snapshot_simulation_node_post(simulation, node, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str simulation: Simulation ID (required)
        :param str node: Node name (required)
        :param str name: last part of the created image name
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.simengine_rest_snapshot_simulation_node_post_with_http_info(simulation, node, **kwargs)
        else:
            (data) = self.simengine_rest_snapshot_simulation_node_post_with_http_info(simulation, node, **kwargs)
            return data

    def simengine_rest_snapshot_simulation_node_post_with_http_info(self, simulation, node, **kwargs):
        """
        Create snapshot of a node
        Create snapshot of a node. The snapshot will be a private image (visible only inside the same project) named as project-subtype-imagename.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.simengine_rest_snapshot_simulation_node_post_with_http_info(simulation, node, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str simulation: Simulation ID (required)
        :param str node: Node name (required)
        :param str name: last part of the created image name
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['simulation', 'node', 'name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simengine_rest_snapshot_simulation_node_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'simulation' is set
        if ('simulation' not in params) or (params['simulation'] is None):
            raise ValueError("Missing the required parameter `simulation` when calling `simengine_rest_snapshot_simulation_node_post`")
        # verify the required parameter 'node' is set
        if ('node' not in params) or (params['node'] is None):
            raise ValueError("Missing the required parameter `node` when calling `simengine_rest_snapshot_simulation_node_post`")


        collection_formats = {}

        path_params = {}
        if 'simulation' in params:
            path_params['simulation'] = params['simulation']
        if 'node' in params:
            path_params['node'] = params['node']

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/simengine/rest/snapshot/{simulation}/{node}', 'POST',
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
