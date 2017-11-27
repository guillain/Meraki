#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

import json
from meraki import Meraki

"""
Meraki AP Class
:description: Provide easy AP management via class
feature::
  - Full REST API
  - Get, Post, Put, Delete
  - All returned values are in JSON format
"""
class AP(Meraki):

    """ ------------------------------------------ ""
    GET request
    :description: provide list of AP or one AP
    optionnal params::
            - organization_id
            - network_id
    :return: json(AP) | json(APs)

    example::
            $ APs = AP.get(<organization_id>, <network_id>)
            $ for AP in APs:
            $     print(AP['name']

            $ AP = AP.get(<network_id>, by_field = <by_field>, by_value = <by_value>)

            $ APname = AP.get(<network_id>, by_field = <by_field>, by_value = <by_value>, ret_field = 'name')

    """
    def get(self, organization_id = None, network_id = None):

        if network_id not in('', None):
            return self.filter(self.request("GET", "/networks/{}/devices".format(network_id)))

        if organization_id not in('', None):
            res_data = []

            for network in self.request("GET", "/organizations/{}/networks".format(organization_id)):
                res = self.filter(self.request("GET", "/networks/{}/devices".format(network['id'])))

                if self.by_list:
                    res_data.append(res)

                elif res not in('', None):
                    return res

        return self.search(by_field, by_value, by_list, ret_field)

    """ ------------------------------------------ ""
    Search
    :description: search AP with params
    mandatory params::
            - by_field: search on which field
            - by_value: search the value on the condered field
    optionnal params::
            - by_list: contnue the search and build a list of result
            - ret_field: filter to return only one field
    :return: json(AP) | json(APs) | json(field)

    example::
            $ AP = ap.get(by_field = <id,name>, by_value=<by_value>)

            $ myAPSerial = ap.get(by_field = <name>, by_value=<by_value>, ret_field = 'serial')
    """
    def search(self, by_field, by_value, by_list = None, ret_field = None):
        ap_data = []
        for organization in self.request("GET", "/organizations"):
            for ap_inv in self.request("GET", "/organizations/{}/inventory".format(organization['id'])):
                ap = self.request("GET", "/networks/{}/devices/{}".format(ap_inv['networkId'], ap_inv['serial']))
                if ap not in('', None):
                    if ap[by_field] == by_value:
                        if ret_field not in('', None):
                            if ret_field in ap:
                                if by_list:
                                    ap_data.append(ap[ret_field])
                                else:
                                    return ap[ret_field]
                        else:
                            if by_list:
                                ap_data.append(ap)
                            else:
                                return ap


    """ ------------------------------------------ ""
    POST
    :description: add new AP
    mandatory params::
            - organization_id
            - serial
    optionnal params::
            - name
            - lat (latitude)
            - lng (longitude)
            - tags
            - address
    :return: new AP
    """
    def post(self, organization_id, serial, name = None, lat = None, lng = None, tags = None, address = None):
        data = {}
        data['serial'] = serial

        r = self.request(
            "POST",
            "/networks/{}/devices/claim".format(organization_id),
            json.dumps(data)
        )

        if r in ('', None):
            return

        if name not in('', None) or lat not in('', None) or lng not in('', None) or tags not in('', None) or address not in('', None):
            r = self.put(serial, name, lat, lng, tags)

        return r

    """ ------------------------------------------ ""
    PUT
    :description: update an AP
    mandatory params::
            - network_id
            - serial
    optionnal params::
            - name
            - lat (latitude)
            - lng (longitude)
            - tags
            - address
    :return: AP updated
    """
    def put(self, network_id, serial, name = None, lat = None, lng = None, tags = None, address = None):

        data = {}
        if name not in ('', None):
            data['name'] = name
        if lat not in ('', None):
            data['lat'] = lat
        if lng not in ('', None):
            data['lng'] = lng
        if tags not in ('', None):
            data['tags'] = tags
        if address not in ('', None):
            data['address'] = address

        r = self.request(
            "PUT",
            "/networks/{}/devices/{}".format(network_id, serial), 
            json.dumps(data)
        )

        return r

    """ ------------------------------------------ ""
    DELETE
    :description: delete (unlink to be correct) an AP
    mandatory params::
            - organization_id
            - serial
    :return: AP unlinked
    """
    def delete(self, organization_id, serial):
        return self.request(
            "POST", 
            "/networks/{}/devices/{}/remove".format(organization_id, serial),
            ""
        )


