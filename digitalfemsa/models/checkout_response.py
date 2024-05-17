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

class CheckoutResponse(BaseModel):
    """
    checkout response
    """ # noqa: E501
    allowed_payment_methods: Optional[List[StrictStr]] = None
    can_not_expire: Optional[StrictBool] = None
    emails_sent: Optional[StrictInt] = None
    expires_at: Optional[StrictInt] = None
    failure_url: Optional[StrictStr] = None
    id: StrictStr
    livemode: StrictBool
    metadata: Optional[Dict[str, Any]] = None
    name: StrictStr = Field(description="Reason for charge")
    needs_shipping_contact: Optional[StrictBool] = None
    object: StrictStr
    paid_payments_count: Optional[StrictInt] = None
    payments_limit_count: Optional[StrictInt] = None
    recurrent: Optional[StrictBool] = None
    slug: Optional[StrictStr] = None
    sms_sent: Optional[StrictInt] = None
    starts_at: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    success_url: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["allowed_payment_methods", "can_not_expire", "emails_sent", "expires_at", "failure_url", "id", "livemode", "metadata", "name", "needs_shipping_contact", "object", "paid_payments_count", "payments_limit_count", "recurrent", "slug", "sms_sent", "starts_at", "status", "success_url", "type", "url"]

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
        """Create an instance of CheckoutResponse from a JSON string"""
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
        # set to None if payments_limit_count (nullable) is None
        # and model_fields_set contains the field
        if self.payments_limit_count is None and "payments_limit_count" in self.model_fields_set:
            _dict['payments_limit_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CheckoutResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_payment_methods": obj.get("allowed_payment_methods"),
            "can_not_expire": obj.get("can_not_expire"),
            "emails_sent": obj.get("emails_sent"),
            "expires_at": obj.get("expires_at"),
            "failure_url": obj.get("failure_url"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "needs_shipping_contact": obj.get("needs_shipping_contact"),
            "object": obj.get("object"),
            "paid_payments_count": obj.get("paid_payments_count"),
            "payments_limit_count": obj.get("payments_limit_count"),
            "recurrent": obj.get("recurrent"),
            "slug": obj.get("slug"),
            "sms_sent": obj.get("sms_sent"),
            "starts_at": obj.get("starts_at"),
            "status": obj.get("status"),
            "success_url": obj.get("success_url"),
            "type": obj.get("type"),
            "url": obj.get("url")
        })
        return _obj


