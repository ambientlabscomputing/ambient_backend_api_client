# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.5.2
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ambient_backend_api_client.models.interface_type_enum import InterfaceTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class NetworkInterface(BaseModel):
    """
    NetworkInterface
    """ # noqa: E501
    type: InterfaceTypeEnum
    name: StrictStr
    ipv4_address: Optional[StrictStr] = None
    ipv6_address: Optional[StrictStr] = None
    mac_address: Optional[StrictStr] = None
    netmask: Optional[StrictStr] = None
    gateway: Optional[StrictStr] = None
    broadcast: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["type", "name", "ipv4_address", "ipv6_address", "mac_address", "netmask", "gateway", "broadcast"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NetworkInterface from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if ipv4_address (nullable) is None
        # and model_fields_set contains the field
        if self.ipv4_address is None and "ipv4_address" in self.model_fields_set:
            _dict['ipv4_address'] = None

        # set to None if ipv6_address (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6_address is None and "ipv6_address" in self.model_fields_set:
            _dict['ipv6_address'] = None

        # set to None if mac_address (nullable) is None
        # and model_fields_set contains the field
        if self.mac_address is None and "mac_address" in self.model_fields_set:
            _dict['mac_address'] = None

        # set to None if netmask (nullable) is None
        # and model_fields_set contains the field
        if self.netmask is None and "netmask" in self.model_fields_set:
            _dict['netmask'] = None

        # set to None if gateway (nullable) is None
        # and model_fields_set contains the field
        if self.gateway is None and "gateway" in self.model_fields_set:
            _dict['gateway'] = None

        # set to None if broadcast (nullable) is None
        # and model_fields_set contains the field
        if self.broadcast is None and "broadcast" in self.model_fields_set:
            _dict['broadcast'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkInterface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "name": obj.get("name"),
            "ipv4_address": obj.get("ipv4_address"),
            "ipv6_address": obj.get("ipv6_address"),
            "mac_address": obj.get("mac_address"),
            "netmask": obj.get("netmask"),
            "gateway": obj.get("gateway"),
            "broadcast": obj.get("broadcast")
        })
        return _obj


