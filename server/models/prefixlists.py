"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Prefixlists(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    entries: list = Field(default_factory=list)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "OSPF_Redist",
                "version": "0.0.2",
                "entries": [
                    {
                        "name": "OSPF_Redist",
                        "seq": "5",
                        "action": "deny",
                        "network": "10.0.0.0",
                        "netmask": "24",
                        "le": "",
                        "ge": "",
                    },
                    {
                        "name": "OSPF_Redist",
                        "seq": "10",
                        "action": "permit",
                        "network": "0.0.0.0",
                        "netmask": "0",
                        "le": "32",
                        "ge": "",
                    },
                    {
                        "name": "OSPF_Redist",
                        "seq": "15",
                        "action": "deny",
                        "network": "10.0.0.0",
                        "netmask": "8",
                        "le": "20",
                        "ge": "10",
                    },
                ],
            }
        }


class PrefixlistsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    version: str = Field(...)
    entries: list = Field(default_factory=list)
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "OSPF_Redist",
                "version": "0.0.2",
                "entries": [
                    {
                        "name": "OSPF_Redist",
                        "seq": "5",
                        "action": "deny",
                        "network": "10.0.0.0",
                        "netmask": "24",
                        "le": "",
                        "ge": "",
                    },
                    {
                        "name": "OSPF_Redist",
                        "seq": "10",
                        "action": "permit",
                        "network": "0.0.0.0",
                        "netmask": "0",
                        "le": "32",
                        "ge": "",
                    },
                    {
                        "name": "OSPF_Redist",
                        "seq": "15",
                        "action": "deny",
                        "network": "10.0.0.0",
                        "netmask": "8",
                        "le": "20",
                        "ge": "10",
                    },
                ],
            }
        }
