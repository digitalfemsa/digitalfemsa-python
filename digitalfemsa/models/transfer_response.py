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
from typing_extensions import Annotated
from digitalfemsa.models.transfer_destination_response import TransferDestinationResponse
from typing import Optional, Set
from typing_extensions import Self

class TransferResponse(BaseModel):
    """
    A transfer represents the action of sending an amount to a business bank account including the status, amount and method used to make the transfer.
    """ # noqa: E501
    amount: Optional[StrictInt] = Field(default=None, description="Amount in cents of the transfer.")
    created_at: Optional[StrictInt] = Field(default=None, description="Date and time of creation of the transfer in Unix format.")
    currency: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="The currency of the transfer. It uses the 3-letter code of the [International Standard ISO 4217.](https://es.wikipedia.org/wiki/ISO_4217)")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the transfer.")
    livemode: Optional[StrictBool] = Field(default=None, description="Indicates whether the transfer was created in live mode or test mode.")
    destination: Optional[TransferDestinationResponse] = None
    object: Optional[StrictStr] = Field(default=None, description="Object name, which is transfer.")
    statement_description: Optional[StrictStr] = Field(default=None, description="Description of the transfer.")
    statement_reference: Optional[StrictStr] = Field(default=None, description="Reference number of the transfer.")
    status: Optional[StrictStr] = Field(default=None, description="Code indicating transfer status.")
    __properties: ClassVar[List[str]] = ["amount", "created_at", "currency", "id", "livemode", "destination", "object", "statement_description", "statement_reference", "status"]

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
        """Create an instance of TransferResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransferResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "destination": TransferDestinationResponse.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "object": obj.get("object"),
            "statement_description": obj.get("statement_description"),
            "statement_reference": obj.get("statement_reference"),
            "status": obj.get("status")
        })
        return _obj


