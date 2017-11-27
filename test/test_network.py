#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

from sys import path
from os import getcwd
from test_test import Test

path.append(getcwd() + "/../meraki")
from network import Network

class Test_network(Test):

    def run(self):

        self.run_name = "Network"

        self.network = Network(
            token = self.token,
            base_url = self.url
        )

        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None

       
        self.title = "Get: network_id"
        self.res = self.network_result
        self.exe = self.network.get(organization_id = self.organization_id, network_id = self.network_id)
        self.test_exe()

        self.exe = self.network.get(organization_id = self.organization_id)
 
        self.title = "Get: organization_id"
        self.res = self.networks_result
        self.test_exe()


        self.title = "Get: by_field(id)"
        self.res = self.network_result
        self.by_field = 'id'
        self.by_value = self.network_id
        self.test_exe()

        self.title = "Get: by_field(id), by_list"
        self.res = [self.network_result]
        self.by_list = True
        self.test_exe()

        self.title = "Get: by_field(id), ret_field"
        self.res = self.network_name
        self.ret_field = 'name'
        self.by_list = False
        self.test_exe()

        self.title = "Get: by_field(id), by_list, ret_field"
        self.res = [self.network_name]
        self.by_list = True
        self.test_exe()


        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None


        self.title = "Get: by_field(name)",
        self.res = self.network_result
        self.by_field = 'name'
        self.by_value = self.network_name
        self.test_exe()

        self.title = "Get: by_field(name), by_list"
        self.res = [self.network_result]
        self.by_list = True
        self.test_exe()

        self.title = "Get: by_field(name), ret_field"
        self.res = self.network_id
        self.ret_field = 'id'
        self.by_list = False
        self.test_exe()

        self.title = "Get: by_field(name), by_list, ret_field"
        self.res = [self.network_id]
        self.by_list = True
        self.test_exe()


