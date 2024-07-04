# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.3.1
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class InterfaceTypeEnum(str, Enum):
    """
    InterfaceTypeEnum
    """

    """
    allowed enum values
    """
    ETHERNET = 'ethernet'
    WIFI = 'wifi'
    ENUM_4G = '4g'
    ENUM_4G_CBRS = '4g_cbrs'
    ENUM_5G = '5g'
    I2C = 'i2c'
    SPI = 'spi'
    USB = 'usb'
    CAN = 'can'
    BLUETOOTH = 'bluetooth'
    ZIGBEE = 'zigbee'
    ZWAVE = 'zwave'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InterfaceTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


