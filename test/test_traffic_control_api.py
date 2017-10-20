# coding: utf-8

"""
    VIRL STD API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import virl
from virl.rest import ApiException
from virl.apis.traffic_control_api import TrafficControlApi


class TestTrafficControlApi(unittest.TestCase):
    """ TrafficControlApi unit test stubs """

    def setUp(self):
        self.api = virl.apis.traffic_control_api.TrafficControlApi()

    def tearDown(self):
        pass

    def test_simengine_rest_shaping_interfaces_simulation_id_delete(self):
        """
        Test case for simengine_rest_shaping_interfaces_simulation_id_delete

        Delete interface-level traffic control settings for all links in simulation
        """
        pass

    def test_simengine_rest_shaping_interfaces_simulation_id_get(self):
        """
        Test case for simengine_rest_shaping_interfaces_simulation_id_get

        List interface-level traffic control settings
        """
        pass

    def test_simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get(self):
        """
        Test case for simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_get

        List interface-level traffic control settings for a given node in simulation
        """
        pass

    def test_simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get(self):
        """
        Test case for simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_get

        List interface-level traffic control setting for a given interface of node in simulation
        """
        pass

    def test_simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put(self):
        """
        Test case for simengine_rest_shaping_interfaces_stringsimulation_id_stringnode_id_stringiface_id_put

        Set interface-level traffic control settings for particular interface
        """
        pass

    def test_simengine_rest_shaping_simulation_id_delete(self):
        """
        Test case for simengine_rest_shaping_simulation_id_delete

        Delete link-level traffic control settings for all links in simulation
        """
        pass

    def test_simengine_rest_shaping_simulation_id_get(self):
        """
        Test case for simengine_rest_shaping_simulation_id_get

        List link-level traffic control settings
        """
        pass

    def test_simengine_rest_shaping_simulation_id_link_id_delete(self):
        """
        Test case for simengine_rest_shaping_simulation_id_link_id_delete

        Delete link-level traffic control settings for particular link
        """
        pass

    def test_simengine_rest_shaping_simulation_id_link_id_get(self):
        """
        Test case for simengine_rest_shaping_simulation_id_link_id_get

        List link-level traffic control settings for a given link
        """
        pass

    def test_simengine_rest_shaping_simulation_id_link_id_put(self):
        """
        Test case for simengine_rest_shaping_simulation_id_link_id_put

        Set link-level traffic control settings for particular link
        """
        pass


if __name__ == '__main__':
    unittest.main()
