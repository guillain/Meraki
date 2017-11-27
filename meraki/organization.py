#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Meraki class"""
__status__ = "Prototype"
__author__ = "guillain@gmail.com"
__license__ = "GPL-3.0"

from meraki import Meraki

"""
Meraki Organization Class
description::
    - Provide easy organization management via class
    - FullREST API
    - Get (ToDo: Post, Put, Delete)
    - All returned values are in JSON format when it's not id or name request
"""
class Organization(Meraki):

    """ ------------------------------------------ ""
    GET request
    :description: provide list of organization or one organization
    optionnal params::
         - organization_id
    :return: json(organization(s)) 

    example::
            $ organizations = organization.get()
            $ for organization in organizations:
            $     print(organization['name']

            $ organization = organization.get(organization_id = <organization_id>)

    """
    def get(self, organization_id = None):

        if organization_id not in('', None):
            return self.filter(self.request("GET", "/organizations/{}".format(organization_id)))

        return self.filter(self.request("GET", "/organizations"))

