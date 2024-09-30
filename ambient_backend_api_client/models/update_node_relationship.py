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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ambient_backend_api_client.models.command_status_enum import CommandStatusEnum
from typing import Optional, Set
from typing_extensions import Self

class UpdateNodeRelationship(BaseModel):
    """
    UpdateNodeRelationship
    """ # noqa: E501
    command_id: StrictInt
    node_id: StrictInt
    status: Optional[CommandStatusEnum] = None
    error: Optional[StrictStr] = None
    output: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["command_id", "node_id", "status", "error", "output"]

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
        """Create an instance of UpdateNodeRelationship from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if output (nullable) is None
        # and model_fields_set contains the field
        if self.output is None and "output" in self.model_fields_set:
            _dict['output'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateNodeRelationship from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "command_id": obj.get("command_id"),
            "node_id": obj.get("node_id"),
            "status": obj.get("status"),
            "error": obj.get("error"),
            "output": obj.get("output")
        })
        return _obj


