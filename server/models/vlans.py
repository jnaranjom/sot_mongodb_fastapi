"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Vlans(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    version: str = Field(...)
    scope: str = Field(...)
    name: str = Field(...)
    vlan_id: str = Field(...)
    vni_id: str = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "version": "0.0.1",
                "scope": "access",
                "name": "voice",
                "vlan_id": "10",
                "vni_id": "null",
            }
        }


class VlansUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    version: Optional[str]
    scope: Optional[str]
    name: Optional[str]
    vlan_id: Optional[str]
    vni_id: Optional[str]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "version": "0.0.1",
                "scope": "access",
                "name": "voice",
                "vlan_id": "10",
                "vni_id": "null",
            }
        }
