# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.7.0
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DockerSwarmInfo(BaseModel):
    """
    DockerSwarmInfo
    """ # noqa: E501
    node_id: Optional[StrictStr] = Field(default='', description="Unique identifier of the node in the swarm", alias="NodeID")
    node_addr: Optional[StrictStr] = Field(default='', description="Address of the node in the swarm", alias="NodeAddr")
    local_node_state: Optional[StrictStr] = Field(default='', description="Local node state", alias="LocalNodeState")
    error: Optional[StrictStr] = Field(default='', description="Error message", alias="Error")
    __properties: ClassVar[List[str]] = ["NodeID", "NodeAddr", "LocalNodeState", "Error"]

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
        """Create an instance of DockerSwarmInfo from a JSON string"""
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
        """Create an instance of DockerSwarmInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NodeID": obj.get("NodeID") if obj.get("NodeID") is not None else '',
            "NodeAddr": obj.get("NodeAddr") if obj.get("NodeAddr") is not None else '',
            "LocalNodeState": obj.get("LocalNodeState") if obj.get("LocalNodeState") is not None else '',
            "Error": obj.get("Error") if obj.get("Error") is not None else ''
        })
        return _obj


