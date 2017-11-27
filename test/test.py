#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

import sys, json

def main():
    from test_network import Test_network
    test_network = Test_network()
    test_network.run()

    from test_organization import Test_organization
    test_organization = Test_organization()
    test_organization.run()

    from test_ap import Test_ap
    test_ap = Test_ap()
    test_ap.run()

if __name__ == '__main__':
    main()

