#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

from sys import path
from os import getcwd
path.append(getcwd() + "/../meraki")
from meraki import Meraki

# Constantes for test and
token = 'c912f1ae714f1b013c1e20c8ab7c6a13ee84423c'
url = 'https://dashboard.meraki.com/api/v0'

debug = True

""" organization validation constantes definition ---------------------------------------------------------------"""
organization_id = ''
organization_name = ''
organizations_result = ''
organization_result = ''
organization_by_result = ''

""" network validation constantes definition --------------------------------------------------------------------"""
network_id = ''
network_name = ''
networks_result = ''
network_result = ''

""" ap validation constantes definition -------------------------------------------------------------------------"""
ap_post = ''
ap_serial = ''
ap_name = ''
ap_name_put = ''
ap_mac = ''
ap_ip = ''

ap_building = ''
ap_floor = ''
ap_lat = ''
ap_lng = ''
ap_tags = ''
ap_address = ''
apss_result = ''

aps_result = ''
ap_result = ''
ap_search_result = ''


"""
Meraki Test Class
"""
class Test(Meraki):
    def __init__(self):
        self.token = token
        self.url = url
        self.debug = debug

        self.organizations_result = organizations_result
        self.organization_result = organization_result
        self.organization_id = organization_id
        self.organization_name = organization_name

        self.networks_result = networks_result
        self.network_result = network_result
        self.network_id = network_id
        self.network_name = network_name

        self.apss_result = apss_result
        self.aps_result = aps_result
        self.ap_result = ap_result
        self.ap_search_result = ap_search_result
        self.ap_post = ap_post

        self.ap_serial = ap_serial
        self.ap_name = ap_name
        self.ap_name_put = ap_name_put
        self.ap_mac = ap_mac

        self.ap_building = ap_building
        self.ap_floor = ap_floor
        self.ap_lat = ap_lat
        self.ap_lng = ap_lng
        self.ap_tags = ap_tags
        self.ap_address = ap_address

        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None

    def test_exe(self):

        res_exe = self.exe

        if self.by_field not in('', None) or self.by_list:
            res_exe = self.filter(self.exe)

        if res_exe != self.res:
            print('{} - {} :  Ko'.format(self.run_name, self.title))
            if self.debug:
                print('  >>>> Exe: {} /--/ Expected: {}'.format(res_exe, self.res))

        else:
            print('{} - {} :  Ok'.format(self.run_name, self.title))

