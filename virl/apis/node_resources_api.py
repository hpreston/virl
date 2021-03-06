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


class NodeResourcesApi(object):
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

    def openstack_rest_create_port_post(self, network_name, port_name, **kwargs):
        """
        Create a port on an OpenStack network
        Create a port on an OpenStack network
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_create_port_post(network_name, port_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str network_name: name of the network on which the port should be created (required)
        :param str port_name: name of the new port (required)
        :param str tenant_name: port owner; if not specified, the current user's project will be used
        :param str fixed_ip: custom fixed IP of the new port
        :param str floating_ip: custom floating IP of the new port
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_create_port_post_with_http_info(network_name, port_name, **kwargs)
        else:
            (data) = self.openstack_rest_create_port_post_with_http_info(network_name, port_name, **kwargs)
            return data

    def openstack_rest_create_port_post_with_http_info(self, network_name, port_name, **kwargs):
        """
        Create a port on an OpenStack network
        Create a port on an OpenStack network
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_create_port_post_with_http_info(network_name, port_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str network_name: name of the network on which the port should be created (required)
        :param str port_name: name of the new port (required)
        :param str tenant_name: port owner; if not specified, the current user's project will be used
        :param str fixed_ip: custom fixed IP of the new port
        :param str floating_ip: custom floating IP of the new port
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_name', 'port_name', 'tenant_name', 'fixed_ip', 'floating_ip']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method openstack_rest_create_port_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_name' is set
        if ('network_name' not in params) or (params['network_name'] is None):
            raise ValueError("Missing the required parameter `network_name` when calling `openstack_rest_create_port_post`")
        # verify the required parameter 'port_name' is set
        if ('port_name' not in params) or (params['port_name'] is None):
            raise ValueError("Missing the required parameter `port_name` when calling `openstack_rest_create_port_post`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'network_name' in params:
            query_params.append(('network_name', params['network_name']))
        if 'port_name' in params:
            query_params.append(('port_name', params['port_name']))
        if 'tenant_name' in params:
            query_params.append(('tenant_name', params['tenant_name']))
        if 'fixed_ip' in params:
            query_params.append(('fixed_ip', params['fixed_ip']))
        if 'floating_ip' in params:
            query_params.append(('floating_ip', params['floating_ip']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/openstack/rest/create-port', 'POST',
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

    def openstack_rest_flavors_get(self, **kwargs):
        """
        Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
        Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_flavors_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_flavors_get_with_http_info(**kwargs)
        else:
            (data) = self.openstack_rest_flavors_get_with_http_info(**kwargs)
            return data

    def openstack_rest_flavors_get_with_http_info(self, **kwargs):
        """
        Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
        Return information about currently installed OpenStack VM flavors. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_flavors_get_with_http_info(callback=callback_function)

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
                    " to method openstack_rest_flavors_get" % key
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

        return self.api_client.call_api('/openstack/rest/flavors', 'GET',
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

    def openstack_rest_images_get(self, **kwargs):
        """
        Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
        Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_images_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_images_get_with_http_info(**kwargs)
        else:
            (data) = self.openstack_rest_images_get_with_http_info(**kwargs)
            return data

    def openstack_rest_images_get_with_http_info(self, **kwargs):
        """
        Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
        Return information about currently installed OpenStack VM images. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_images_get_with_http_info(callback=callback_function)

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
                    " to method openstack_rest_images_get" % key
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

        return self.api_client.call_api('/openstack/rest/images', 'GET',
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

    def openstack_rest_networks_get(self, **kwargs):
        """
        Return information about OpenStack networks.
        Return information about OpenStack networks.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_networks_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_networks_get_with_http_info(**kwargs)
        else:
            (data) = self.openstack_rest_networks_get_with_http_info(**kwargs)
            return data

    def openstack_rest_networks_get_with_http_info(self, **kwargs):
        """
        Return information about OpenStack networks.
        Return information about OpenStack networks.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_networks_get_with_http_info(callback=callback_function)

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
                    " to method openstack_rest_networks_get" % key
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

        return self.api_client.call_api('/openstack/rest/networks', 'GET',
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

    def openstack_rest_ports_network_name_get(self, network_name, **kwargs):
        """
        Return information about the ports of an OpenStack network.
        Return information about the ports of an OpenStack network.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_ports_network_name_get(network_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str network_name: Name of an OpenStack network. (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_ports_network_name_get_with_http_info(network_name, **kwargs)
        else:
            (data) = self.openstack_rest_ports_network_name_get_with_http_info(network_name, **kwargs)
            return data

    def openstack_rest_ports_network_name_get_with_http_info(self, network_name, **kwargs):
        """
        Return information about the ports of an OpenStack network.
        Return information about the ports of an OpenStack network.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_ports_network_name_get_with_http_info(network_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str network_name: Name of an OpenStack network. (required)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['network_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method openstack_rest_ports_network_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'network_name' is set
        if ('network_name' not in params) or (params['network_name'] is None):
            raise ValueError("Missing the required parameter `network_name` when calling `openstack_rest_ports_network_name_get`")


        collection_formats = {}

        path_params = {}
        if 'network_name' in params:
            path_params['network_name'] = params['network_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/openstack/rest/ports/{network_name}', 'GET',
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

    def openstack_rest_test_get(self, **kwargs):
        """
        Verify the user is authenticated and return openstack API version.
        Verify the user is authenticated and return openstack API version.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_test_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_test_get_with_http_info(**kwargs)
        else:
            (data) = self.openstack_rest_test_get_with_http_info(**kwargs)
            return data

    def openstack_rest_test_get_with_http_info(self, **kwargs):
        """
        Verify the user is authenticated and return openstack API version.
        Verify the user is authenticated and return openstack API version.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_test_get_with_http_info(callback=callback_function)

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
                    " to method openstack_rest_test_get" % key
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

        return self.api_client.call_api('/openstack/rest/test', 'GET',
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

    def openstack_rest_volumes_get(self, **kwargs):
        """
        Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
        Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_volumes_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: StdDefsJsondefinitionsnoschema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.openstack_rest_volumes_get_with_http_info(**kwargs)
        else:
            (data) = self.openstack_rest_volumes_get_with_http_info(**kwargs)
            return data

    def openstack_rest_volumes_get_with_http_info(self, **kwargs):
        """
        Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
        Return information about VM volumes present in OpenStack. Volume snapshots are not listed here. This information is mainly for use in the topology design phase in GUI.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.openstack_rest_volumes_get_with_http_info(callback=callback_function)

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
                    " to method openstack_rest_volumes_get" % key
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

        return self.api_client.call_api('/openstack/rest/volumes', 'GET',
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
