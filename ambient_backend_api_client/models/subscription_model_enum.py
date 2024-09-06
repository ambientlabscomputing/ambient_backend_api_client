# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.4.1
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SubscriptionModelEnum(str, Enum):
    """
    SubscriptionModelEnum
    """

    """
    allowed enum values
    """
    FREE = 'free'
    BASIC = 'basic'
    PRO = 'pro'
    ENTERPRISE = 'enterprise'
    TEST = 'test'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SubscriptionModelEnum from a JSON string"""
        return cls(json.loads(json_str))


