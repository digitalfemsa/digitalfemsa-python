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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from digitalfemsa.models.customer_address import CustomerAddress
from typing import Optional, Set
from typing_extensions import Self

class CustomerFiscalEntitiesDataResponse(BaseModel):
    """
    CustomerFiscalEntitiesDataResponse
    """ # noqa: E501
    address: CustomerAddress
    tax_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    company_name: Optional[StrictStr] = None
    id: StrictStr
    object: StrictStr
    created_at: StrictInt
    parent_id: Optional[StrictStr] = None
    default: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["address", "tax_id", "email", "phone", "metadata", "company_name", "id", "object", "created_at", "parent_id", "default"]

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
        """Create an instance of CustomerFiscalEntitiesDataResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerFiscalEntitiesDataResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": CustomerAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "tax_id": obj.get("tax_id"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "metadata": obj.get("metadata"),
            "company_name": obj.get("company_name"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "parent_id": obj.get("parent_id"),
            "default": obj.get("default")
        })
        return _obj

