#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

import sys, requests, json

"""
Meraki Class
description::
  - Provide easy Meraki management via class
  - FullREST API
  - Get, Post, Put, Delete
  - All returned values are in JSON format
"""
class Meraki:
    def __init__(self, token, base_url):
        self.token = token
        self.base_url = base_url

        self.by_field = None
        self.by_value = None
        self.by_list = False
        self.ret_field = None

    def __repr__(self):
        return "{} - {}".format(
            self.token, self.base_url
        )

    """ ------------------------------------------ ""
    request
    :description: provide request template
    mandatory params::
            - action: GET, POST, PUT, DELETE (they other should work but not integrated)
            - path: the meraki API path (so without the hostname:port and API version)
    optionnal params::
            - data: to transmit (ie on POST and PUT request)
    :return: request callback data
    """
    def request(self, action, path, data = None):
        headers = {
            'x-cisco-meraki-api-key': self.token,
            'cache-control': "no-cache",
        }
        r = requests.request(action, self.base_url + path, headers=headers, data=data)
        if r.status_code != requests.codes.ok:
            return 'null'
        return r.json()

    """ ------------------------------------------ ""
    filter
    :description: provide a filter for data
    mandatory params::
            - data: data to filter
    :return: 
    """
    def filter(self, data):
        res_data = []

        """Check if filter params is set"""
        if self.by_field in('', None):
            return data

        if self.by_value in('', None):
            return data
        
        for d in data:

            """Check if by_field[by_value] match"""
            if self.by_field in d:
                if d[self.by_field] == self.by_value:

                    """Return the field value?"""
                    if self.ret_field not in('', None):
                        res = d[self.ret_field]
                    else:
                        res = d

                    """Return a consolidate list of result?"""
                    if self.by_list:
                        res_data.append(res)
                    else:
                        return res

        if self.by_list and res_data not in('', None):
            return json.dumps(res_data)

