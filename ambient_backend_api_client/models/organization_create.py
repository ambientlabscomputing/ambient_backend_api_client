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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ambient_backend_api_client.models.resource_type_enum import ResourceTypeEnum
from ambient_backend_api_client.models.subscription_model_enum import SubscriptionModelEnum
from typing import Optional, Set
from typing_extensions import Self

class OrganizationCreate(BaseModel):
    """
    OrganizationCreate
    """ # noqa: E501
    name: StrictStr
    description: Optional[StrictStr] = None
    resource_type: Optional[ResourceTypeEnum] = None
    subscription: SubscriptionModelEnum
    root_email: StrictStr
    okta_group_id: Optional[StrictStr] = None
    auth0_org_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "description", "resource_type", "subscription", "root_email", "okta_group_id", "auth0_org_id"]

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
        """Create an instance of OrganizationCreate from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if okta_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.okta_group_id is None and "okta_group_id" in self.model_fields_set:
            _dict['okta_group_id'] = None

        # set to None if auth0_org_id (nullable) is None
        # and model_fields_set contains the field
        if self.auth0_org_id is None and "auth0_org_id" in self.model_fields_set:
            _dict['auth0_org_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "resource_type": obj.get("resource_type"),
            "subscription": obj.get("subscription"),
            "root_email": obj.get("root_email"),
            "okta_group_id": obj.get("okta_group_id"),
            "auth0_org_id": obj.get("auth0_org_id")
        })
        return _obj


