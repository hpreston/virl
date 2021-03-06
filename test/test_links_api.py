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
from virl.apis.links_api import LinksApi


class TestLinksApi(unittest.TestCase):
    """ LinksApi unit test stubs """

    def setUp(self):
        self.api = virl.apis.links_api.LinksApi()

    def tearDown(self):
        pass

    def test_simengine_rest_link_simulation_id_get(self):
        """
        Test case for simengine_rest_link_simulation_id_get

        Get link identifiers for selected simulation
        """
        pass

    def test_simengine_rest_link_simulation_id_stringnode_id_iface_id_get(self):
        """
        Test case for simengine_rest_link_simulation_id_stringnode_id_iface_id_get

        Get info about a given link
        """
        pass


if __name__ == '__main__':
    unittest.main()
