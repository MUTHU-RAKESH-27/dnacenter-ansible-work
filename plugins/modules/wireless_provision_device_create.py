#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_device_create
short_description: Resource module for Wireless Provision Device Create
description:
- Manage operation create of the resource Wireless Provision Device Create.
- Provision wireless devices.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Device Create's payload.
    elements: dict
    suboptions:
      deviceName:
        description: Controller Name.
        type: str
      dynamicInterfaces:
        description: Wireless Provision Device Create's dynamicInterfaces.
        elements: dict
        suboptions:
          interfaceGateway:
            description: Interface Gateway.
            type: str
          interfaceIPAddress:
            description: Interface IP Address.
            type: str
          interfaceName:
            description: Interface Name.
            type: str
          interfaceNetmaskInCIDR:
            description: Interface Netmask In CIDR.
            type: int
          lagOrPortNumber:
            description: Lag Or Port Number.
            type: int
          vlanId:
            description: VLAN ID.
            type: int
        type: list
      managedAPLocations:
        description: List of managed AP locations (Site Hierarchies).
        elements: str
        type: list
      site:
        description: Full Site Hierarchy where device has to be assigned.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.6
- python >= 3.5
notes:
  - SDK Method used are
    wireless.Wireless.provision,

  - Paths used are
    post /dna/intent/api/v1/wireless/provision,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_provision_device_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - deviceName: string
      dynamicInterfaces:
      - interfaceGateway: string
        interfaceIPAddress: string
        interfaceName: string
        interfaceNetmaskInCIDR: 1
        lagOrPortNumber: 1
        vlanId: 1
      managedAPLocations:
      - string
      site: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionUrl": "string",
      "provisioningTasks": {
        "success": [
          "string"
        ],
        "failed": [
          "string"
        ]
      }
    }
"""
