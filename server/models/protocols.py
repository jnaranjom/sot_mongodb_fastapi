"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Protocols(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    attributes: dict = Field(...)
    environment: str = Field(...)
    scope: str = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "bgp",
                "version": "0.0.1",
                "attributes": {
                    "router_id": "loopback0",
                    "vrf": "default",
                    "log_neighbor_changes": True,
                    "asn": "65100",
                    "aggregate_networks": [
                        {"network": "10.0.0.0/8", "summary_only": "false"},
                        {"network": "192.168.2.0/24", "summary_only": "true"},
                    ],
                    "networks": [
                        "192.168.10.0/24",
                        "192.168.11.0/24",
                        "192.168.12.0/24",
                    ],
                },
                "environment": "dev",
                "scope": "edge",
            }
        }


class ProtocolsUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: Optional[str]
    attributes: Optional[str]
    environment: Optional[str]
    scope: Optional[str]
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
                "name": "ntp",
                "servers": [
                    {"ipv4_host": "10.0.1.7", "prefer": True},
                    {"ipv4_host": "10.0.1.8", "prefer": False},
                ],
            }
        }
