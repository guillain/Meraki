#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

from meraki import Meraki

"""
Meraki Network Class
:description: 
  - Provide easy Network management via class
  - FullREST API
  - Get (ToDo: Post, Put, Delete)
  - All returned values are in JSON format when it's not id or name request
"""
class Network(Meraki):

    """ ------------------------------------------ ""
    GET request
    :description: provide list of network or one network
    mandatory params::
            - organization_id
    optionnal params::
            - network_id: retour oly one network record
    :return: json(network(s))

    example::
            $ networks = network.get(<organization_id>) 
            $ for network in networks:
            $     print(network['name'])

            $ network = network.get(<organization_id>, <network_id> = <network_id>)
    """
    def get(self, organization_id, network_id = None):

        if network_id not in('', None):
            return self.filter(self.request("GET", "/organizations/{}/networks/{}".format(organization_id, network_id)))
        
        return self.filter(self.request("GET", "/organizations/{}/networks".format(organization_id)))

