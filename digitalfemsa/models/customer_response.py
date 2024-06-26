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
from digitalfemsa.models.customer_antifraud_info_response import CustomerAntifraudInfoResponse
from digitalfemsa.models.customer_fiscal_entities_response import CustomerFiscalEntitiesResponse
from digitalfemsa.models.customer_payment_methods_response import CustomerPaymentMethodsResponse
from digitalfemsa.models.customer_response_shipping_contacts import CustomerResponseShippingContacts
from typing import Optional, Set
from typing_extensions import Self

class CustomerResponse(BaseModel):
    """
    customer response
    """ # noqa: E501
    antifraud_info: Optional[CustomerAntifraudInfoResponse] = None
    corporate: Optional[StrictBool] = Field(default=None, description="true if the customer is a company")
    created_at: StrictInt = Field(description="Creation date of the object")
    custom_reference: Optional[StrictStr] = Field(default=None, description="Custom reference")
    default_fiscal_entity_id: Optional[StrictStr] = None
    default_shipping_contact_id: Optional[StrictStr] = None
    default_payment_source_id: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    fiscal_entities: Optional[CustomerFiscalEntitiesResponse] = None
    id: StrictStr = Field(description="Customer's ID")
    livemode: StrictBool = Field(description="true if the object exists in live mode or the value false if the object exists in test mode")
    name: StrictStr = Field(description="Customer's name")
    metadata: Optional[Dict[str, Any]] = None
    object: StrictStr
    payment_sources: Optional[CustomerPaymentMethodsResponse] = None
    phone: Optional[StrictStr] = Field(default=None, description="Customer's phone number")
    shipping_contacts: Optional[CustomerResponseShippingContacts] = None
    __properties: ClassVar[List[str]] = ["antifraud_info", "corporate", "created_at", "custom_reference", "default_fiscal_entity_id", "default_shipping_contact_id", "default_payment_source_id", "email", "fiscal_entities", "id", "livemode", "name", "metadata", "object", "payment_sources", "phone", "shipping_contacts"]

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
        """Create an instance of CustomerResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of antifraud_info
        if self.antifraud_info:
            _dict['antifraud_info'] = self.antifraud_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fiscal_entities
        if self.fiscal_entities:
            _dict['fiscal_entities'] = self.fiscal_entities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_sources
        if self.payment_sources:
            _dict['payment_sources'] = self.payment_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_contacts
        if self.shipping_contacts:
            _dict['shipping_contacts'] = self.shipping_contacts.to_dict()
        # set to None if antifraud_info (nullable) is None
        # and model_fields_set contains the field
        if self.antifraud_info is None and "antifraud_info" in self.model_fields_set:
            _dict['antifraud_info'] = None

        # set to None if default_fiscal_entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.default_fiscal_entity_id is None and "default_fiscal_entity_id" in self.model_fields_set:
            _dict['default_fiscal_entity_id'] = None

        # set to None if default_payment_source_id (nullable) is None
        # and model_fields_set contains the field
        if self.default_payment_source_id is None and "default_payment_source_id" in self.model_fields_set:
            _dict['default_payment_source_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "antifraud_info": CustomerAntifraudInfoResponse.from_dict(obj["antifraud_info"]) if obj.get("antifraud_info") is not None else None,
            "corporate": obj.get("corporate"),
            "created_at": obj.get("created_at"),
            "custom_reference": obj.get("custom_reference"),
            "default_fiscal_entity_id": obj.get("default_fiscal_entity_id"),
            "default_shipping_contact_id": obj.get("default_shipping_contact_id"),
            "default_payment_source_id": obj.get("default_payment_source_id"),
            "email": obj.get("email"),
            "fiscal_entities": CustomerFiscalEntitiesResponse.from_dict(obj["fiscal_entities"]) if obj.get("fiscal_entities") is not None else None,
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "object": obj.get("object"),
            "payment_sources": CustomerPaymentMethodsResponse.from_dict(obj["payment_sources"]) if obj.get("payment_sources") is not None else None,
            "phone": obj.get("phone"),
            "shipping_contacts": CustomerResponseShippingContacts.from_dict(obj["shipping_contacts"]) if obj.get("shipping_contacts") is not None else None
        })
        return _obj


