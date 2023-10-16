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
    name: str = Field(...)
    version: str = Field(...)
    scope: str = Field(...)
    vlans: list = Field(default_factory=list)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "access vlans",
                "version": "0.0.1",
                "scope": "access",
                "vlans": [
                    {"name": "voice", "vlan_id": "10", "vni_id": "null"},
                    {"name": "multicast", "vlan_id": "20", "vni_id": "null"},
                ],
            }
        }


class VlansUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    version: str = Field(...)
    scope: str = Field(...)
    vlans: list = Field(default_factory=list)
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "access vlans",
                "version": "0.0.1",
                "scope": "access",
                "vlans": [
                    {"name": "voice", "vlan_id": "10", "vni_id": "null"},
                    {"name": "multicast", "vlan_id": "20", "vni_id": "null"},
                ],
            }
        }
