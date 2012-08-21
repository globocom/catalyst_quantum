# Copyright 2011 Nicira Networks, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# @author: Marco Sinhorel, globo.com

import logging

from quantum.db import api as db

from quantum.openstack.common import importutils

from quantum.db.db_base_plugin_v2 import QuantumDbPluginV2

from abc import abstractmethod

class CatalystQuantumPlugin(QuantumDbPluginV2):
    def create_subnet(self, context, subnet):

        '''

        LOG.debug("CatalystQuantumPlugin:create_subnet() called\n")
        new_subnet = super(CatalystQuantumPlugin, self).create_subnet(context, subnet)
        try:
            self._invoke_device_plugins(self._func_name(), [context,
                                                            new_subnet])
            return new_subnet
        except:
            super(PluginV2, self).delete_subnet(context, new_subnet['id'])
            raise
            '''
        pass

    def update_subnet(self, context, id, subnet):
        pass

    def get_subnet(self, context, id, fields=None, verbose=None):
        pass

    def delete_subnet(self, context, id):
        pass

    def get_subnets(self, context, filters=None, fields=None, verbose=None):
        pass

    def create_network(self, context, network):
        """
        Creates a new Virtual Network, assigns a name and associates

        :param net_data:
          {
           'name': a human-readable name associated
                   with network referenced by net-id
                   example: "net-1"
           'admin-state-up': indicates whether this network should
                             be operational.
           'subnets': list of subnet uuids associated with this
                      network.
          }
        :raises:
        """
        pass

    def update_network(self, context, id, network):
        pass

    def delete_network(self, context, id):
        pass

    def get_network(self, context, id, fields=None, verbose=None):
        pass

    def get_networks(self, context, filters=None, fields=None, verbose=None):
        pass

    def create_port(self, context, port):
        """
        Creates a port on the specified Virtual Network. Optionally
        specify customization of port IP-related attributes, otherwise
        the port gets the default values of these attributes associated with
        the subnet.

        :param port_data:
          {"network_id" : UUID of network that this port is attached to.
           "admin-state-up" : boolean indicating whether this port should be
                              operational.
           "mac_address" : (optional) mac address used on this port.  If no
                           value is specified, the plugin will generate a
                           MAC address based on internal configuration.
           "fixed_ips" : (optional) list of dictionaries describing the
                         fixed IPs to be allocated for use by the device on
                         this port. If not specified, the plugin will
                         attempt to find a v4 and v6 subnet associated
                         with the network and allocate an IP for that
                         subnet.
                         Note: "address" is optional, in which case an
                               address from the specified subnet is
                               selected.
                         example: [{"subnet": "<uuid>",
                                    "address": "10.0.0.9"}]
           "routes" : (optional) list of routes to be injected into this
                      device. If not specified, the port will get a
                      route for its local subnet, a route for the default
                      gateway, and each of the routes in the
                      'additional_routes' field of the subnet.
                      example: [ { "destination" : "192.168.0.0/16",
                                   "nexthop" : "10.0.0.5" } ]
          }
        :raises: exception.NetworkNotFound
        :raises: exception.RequestedFixedIPNotAvailable
        :raises: exception.FixedIPNotAvailable
        :raises: exception.RouteInvalid
        """
        pass

    def update_port(self, context, id, port):
        """
        Updates the attributes of a specific port on the
        specified Virtual Network.

        :returns: a mapping sequence with the following signature:
                    {'port-id': uuid representing the
                                 updated port on specified quantum network
                     'port-state': update port state( UP or DOWN)
                    }
        :raises: exception.StateInvalid
        :raises: exception.PortNotFound
        """
        pass

    def delete_port(self, context, id):
        """
        Deletes a port on a specified Virtual Network,
        if the port contains a remote interface attachment,
        the remote interface is first un-plugged and then the port
        is deleted.

        :returns: a mapping sequence with the following signature:
                    {'port-id': uuid representing the deleted port
                                 on specified quantum network
                    }
        :raises: exception.PortInUse
        :raises: exception.PortNotFound
        :raises: exception.NetworkNotFound
        """
        pass

    def get_port(self, context, id, fields=None, verbose=None):
        pass

    def get_ports(self, context, filters=None, fields=None, verbose=None):
        pass
