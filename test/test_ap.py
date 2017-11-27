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
from ap import AP

class Test_ap(Test):

    def run(self):
        self.run_name = "AP"

        self.ap = AP(
            token = self.token,
            base_url = self.url
        )

        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None

        """
        GET
        """

        """Get: network_id"""
        self.exe = self.ap.get(network_id = self.network_id)

        self.title = "Get: network_id"
        self.res = self.aps_result
        self.test_exe()

        self.title = "Get: network_id - by_field(name)"
        self.res = self.ap_result
        self.by_field = "name"
        self.by_value = self.ap_result
        self.test_exe()

        self.title = "Get: network_id - by_field(name), by_list"
        self.res = [self.ap_result]
        self.by_list = True
        self.test_exe()

        self.title = "Get: network_id - by_field(name), ret_field(serial)"
        self.res = self.ap_name
        self.by_field = "name"
        self.by_value = self.ap_serial
        self.ret_field = "serial"
        self.by_list = False
        self.test_exe()

        self.title = "Get: network_id - by_field(name), by_list, ret_field(serial)"
        self.res = [self.ap_serial]
        self.by_list = True
        self.test_exe()


        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None


        """Get: organzation_id"""
        self.exe = self.ap.get(organization_id = self.organization_id)

        self.title = "Get: organization_id"
        self.res = self.aps_result
        self.test_exe()

        self.title = "Get: organization_id - by_field(name)"
        self.res = self.ap_result
        self.by_field = "name"
        self.by_value = self.ap_name
        self.test_exe()

        self.title = "Get: organization_id - by_field(name), by_list"
        self.res = [self.ap_result]
        self.by_list = True
        self.test_exe()

        self.title = "Get: organization_id - by_field(name), ret_field(serial)"
        self.res = self.ap_serial
        self.by_field = "name"
        self.by_value = self.ap_name
        self.ret_field = "serial"
        self.by_list = False
        self.test_exe()

        self.title = "Get: organization_id - by_field(name), by_list, ret_field(serial)"
        self.res = [self.ap_serial]
        self.by_list = True
        self.test_exe()


        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None


        """ Search tests """
        self.exe = self.ap.search(by_field = 'name', by_value = self.ap_name)

        self.title = "Get: Search(name)"
        self.res = self.ap_search_result
        self.test_exe()

        self.title = "Get: Search(name), ret_field(serial)"
        self.ret_field = "serial"
        self.res = self.ap_serial
        self.test_exe()

        self.title = "Get: Search(name), by_list"
        self.by_list = True
        self.ret_field = None
        self.res = [self.ap_search_result]
        self.test_exe()

        self.title = "Get: Search(name), by_list, ret_field(serial)"
        self.ret_field = "serial"
        self.res = [self.ap_serial]
        self.test_exe()


        self.by_field = None
        self.by_list = False
        self.ret_field = None


        """
        POST
        """
        self.res = self.ap_post

        self.title = "Post"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial)
        self.test_exe()

        self.title = "Post: with name"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial, name = self.ap_name_put)
        self.test_exe()

        self.title = "Post: with geolocalisation"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial, lat = self.ap_lat, lng = self.ap_lng)
        self.test_exe()

        self.title = "Post: with tags"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial, tags = self.ap_tags)
        self.test_exe()

        self.title = "Post: with address"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial, address = self.ap_address)
        self.test_exe()

        self.title = "Post: with ALL params"
        self.exe = self.ap.post(organization_id = self.organization_id, serial = self.ap_serial, name = self.ap_name_put, lat = self.ap_lat, lng = self.ap_lng, tags = self.ap_tags, address = self.ap_address)
        self.test_exe()

        """
        Put test
        """
        self.res = self.ap_result

        self.title = "Put"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial)
        self.test_exe()

        self.title = "Put: with name"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial, name = self.ap_name_put)
        self.test_exe()

        self.title = "Put: with geolocalisation"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial, lat = self.ap_lat, lng = self.ap_lng)
        self.test_exe()

        self.title = "Put: with tags"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial, tags = self.ap_tags)
        self.test_exe()

        self.title = "Put: with address"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial, address = self.ap_address)
        self.test_exe()

        self.title = "Put: with ALL params"
        self.exe = self.ap.put(network_id = self.network_id, serial = self.ap_serial, name = self.ap_name_put, lat = self.ap_lat, lng = self.ap_lng, tags = self.ap_tags, address = self.ap_address)
        self.test_exe()

        """
        Delete test
        """
        self.title = "Put: with address"
        self.exe = self.ap.delete(organization_id = self.organization_id, serial = self.ap_serial)
        self.res = self.ap_result
        #self.test_exe()


