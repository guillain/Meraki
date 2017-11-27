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
from organization import Organization

class Test_organization(Test):

    def run(self):
        self.run_name = "Organization"

        self.organization = Organization(
            token = self.token,
            base_url = self.url
        )
      
        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None


        self.title = "Get"
        self.res = self.organizations_result
        self.exe = self.organization.get()
        self.test_exe()

        self.title = "Get: organization_id" 
        self.exe = self.organization.get(organization_id = self.organization_id),
        self.res = self.organization_result
        self.test_exe()


        self.exe = self.organization.get()


        self.title = "Get: by_field(id)"
        self.by_field = 'id'
        self.by_value = self.organization_id
        self.res = self.organization_result
        self.test_exe()

        self.title = "Get: by_field(id), by_list"
        self.by_list = True
        self.res = [self.organization_result]
        self.test_exe()

        self.title = "Get: by_field(id), ret_field"
        self.ret_field = 'name'
        self.by_list = False
        self.res = self.organization_name
        self.test_exe()

        self.title = "Get: by_field(id), ret_field, by_list"
        self.by_list = True
        self.res = [self.organization_name]
        self.test_exe()


        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None


        self.title = "Get: by_field(name)"
        self.by_field = 'name'
        self.by_value = self.organization_name
        self.res = self.organization_result
        self.test_exe()

        self.title = "Get: by_field(name), by_list"
        self.by_list = True
        self.res = [self.organization_result]
        self.test_exe()

        self.title = "Get: by_field(name), ret_field"
        self.ret_field = 'id'
        self.by_list = False
        self.res = self.organization_id
        self.test_exe()

        self.title = "Get: by_field(name), ret_field, by_list"
        self.by_list = True
        self.res = [self.organization_id]
        self.test_exe()
 
