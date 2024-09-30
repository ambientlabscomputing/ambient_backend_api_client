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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Command(BaseModel):
    """
    Command
    """ # noqa: E501
    command: List[StrictStr]
    timeout: StrictInt
    node_ids: Optional[List[StrictInt]] = None
    tags: Optional[List[StrictStr]] = None
    store_output: Optional[StrictBool] = False
    id: StrictInt
    user_id: StrictInt
    org_id: StrictInt
    timestamp: datetime
    __properties: ClassVar[List[str]] = ["command", "timeout", "node_ids", "tags", "store_output", "id", "user_id", "org_id", "timestamp"]

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
        """Create an instance of Command from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Command from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "command": obj.get("command"),
            "timeout": obj.get("timeout"),
            "node_ids": obj.get("node_ids"),
            "tags": obj.get("tags"),
            "store_output": obj.get("store_output") if obj.get("store_output") is not None else False,
            "id": obj.get("id"),
            "user_id": obj.get("user_id"),
            "org_id": obj.get("org_id"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


