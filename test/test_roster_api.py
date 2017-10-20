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
from virl.apis.roster_api import RosterApi


class TestRosterApi(unittest.TestCase):
    """ RosterApi unit test stubs """

    def setUp(self):
        self.api = virl.apis.roster_api.RosterApi()

    def tearDown(self):
        pass

    def test_roster_rest_get(self):
        """
        Test case for roster_rest_get

        Get GUI-related information on all user’s simulations
        """
        pass

    def test_roster_rest_test_get(self):
        """
        Test case for roster_rest_test_get

        Verify the user is authenticated and return roster API version
        """
        pass


if __name__ == '__main__':
    unittest.main()
