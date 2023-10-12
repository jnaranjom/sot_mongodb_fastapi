"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class BgpNeighbors(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    neighbors: list = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "lab01-pe01",
                "version": "0.0.2",
                "neighbors": [
                    {
                        "bfd": False,
                        "description": "lab01-pe02",
                        "ipv4": "5.5.5.5",
                        "remote_as": "65000",
                        "local_as": "null",
                        "maximum_routes": "null",
                        "next_hop_self": True,
                        "password": "null",
                        "route_map_in": "null",
                        "route_map_out": "null",
                        "send_community": False,
                        "shutdown": False,
                        "update_source": "loopback0",
                        "vrf": "null",
                    }
                ],
            }
        }


class BgpNeighborsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: Optional[str]
    neighbors: Optional[list]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "lab01-pe01",
                "version": "0.0.2",
                "neighbors": [
                    {
                        "bfd": False,
                        "description": "lab01-pe02",
                        "ipv4": "5.5.5.5",
                        "remote_as": "65000",
                        "local_as": "null",
                        "maximum_routes": "null",
                        "next_hop_self": True,
                        "password": "null",
                        "route_map_in": "null",
                        "route_map_out": "null",
                        "send_community": False,
                        "shutdown": False,
                        "update_source": "loopback0",
                        "vrf": "null",
                    }
                ],
            }
        }
