# coding: utf-8

"""
    Femsa API

    Femsa sdk

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@femsa.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeleteApiKeysResponse(BaseModel):
    """
    DeleteApiKeysResponse
    """ # noqa: E501
    active: Optional[StrictBool] = Field(default=None, description="Indicates if the api key is active")
    created_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp in seconds of when the api key was created")
    description: Optional[StrictStr] = Field(default=None, description="A name or brief explanation of what this api key is used for")
    livemode: Optional[StrictBool] = Field(default=None, description="Indicates if the api key is in production")
    prefix: Optional[StrictStr] = Field(default=None, description="The first few characters of the authentication_token")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the api key")
    object: Optional[StrictStr] = Field(default=None, description="Object name, value is 'api_key'")
    deleted: Optional[StrictBool] = None
    role: Optional[StrictStr] = Field(default=None, description="Indicates if the api key is private or public")
    __properties: ClassVar[List[str]] = ["active", "created_at", "description", "livemode", "prefix", "id", "object", "deleted", "role"]

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
        """Create an instance of DeleteApiKeysResponse from a JSON string"""
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
        """Create an instance of DeleteApiKeysResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "livemode": obj.get("livemode"),
            "prefix": obj.get("prefix"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "deleted": obj.get("deleted"),
            "role": obj.get("role")
        })
        return _obj


