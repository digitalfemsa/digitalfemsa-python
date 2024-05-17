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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodCash(BaseModel):
    """
    PaymentMethodCash
    """ # noqa: E501
    type: Optional[StrictStr] = None
    object: StrictStr
    auth_code: Optional[StrictInt] = None
    cashier_id: Optional[StrictStr] = None
    reference: Optional[StrictStr] = None
    barcode_url: Optional[StrictStr] = None
    expires_at: Optional[StrictInt] = None
    service_name: Optional[StrictStr] = None
    store: Optional[StrictStr] = None
    store_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["type", "object", "auth_code", "cashier_id", "reference", "barcode_url", "expires_at", "service_name", "store", "store_name"]

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
        """Create an instance of PaymentMethodCash from a JSON string"""
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
        # set to None if auth_code (nullable) is None
        # and model_fields_set contains the field
        if self.auth_code is None and "auth_code" in self.model_fields_set:
            _dict['auth_code'] = None

        # set to None if cashier_id (nullable) is None
        # and model_fields_set contains the field
        if self.cashier_id is None and "cashier_id" in self.model_fields_set:
            _dict['cashier_id'] = None

        # set to None if store (nullable) is None
        # and model_fields_set contains the field
        if self.store is None and "store" in self.model_fields_set:
            _dict['store'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodCash from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "object": obj.get("object"),
            "auth_code": obj.get("auth_code"),
            "cashier_id": obj.get("cashier_id"),
            "reference": obj.get("reference"),
            "barcode_url": obj.get("barcode_url"),
            "expires_at": obj.get("expires_at"),
            "service_name": obj.get("service_name"),
            "store": obj.get("store"),
            "store_name": obj.get("store_name")
        })
        return _obj

