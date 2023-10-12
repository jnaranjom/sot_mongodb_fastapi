"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Interfaces(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    interfaces: list = Field(default_factory=list)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "lab01-edge01",
                "version": "0.0.2",
                "interfaces": [
                    {
                        "name": "Loopback",
                        "type": "routed",
                        "duplex": "full",
                        "speed": "null",
                        "policy_map": "null",
                        "port": "0",
                        "description": "ROUTER-ID",
                        "ipv4_prefix": "1.1.1.2/32",
                        "shutdown": False,
                        "vrf": "default",
                    },
                    {
                        "name": "GigabitEthernet",
                        "type": "routed",
                        "duplex": "full",
                        "speed": "null",
                        "policy_map": "null",
                        "port": "1",
                        "description": "MGMT INTERFACE",
                        "ipv4_prefix": "192.168.2.182/24",
                        "shutdown": False,
                        "vrf": "default",
                    },
                ],
            }
        }


class InterfacesUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_
    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: Optional[str]
    interfaces: Optional[list]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "lab01-edge01",
                "version": "0.0.2",
                "interfaces": [
                    {
                        "name": "Loopback",
                        "type": "routed",
                        "duplex": "full",
                        "speed": "null",
                        "policy_map": "null",
                        "port": "0",
                        "description": "ROUTER-ID",
                        "ipv4_prefix": "1.1.1.2/32",
                        "shutdown": False,
                        "vrf": "default",
                    },
                    {
                        "name": "GigabitEthernet",
                        "type": "routed",
                        "duplex": "full",
                        "speed": "null",
                        "policy_map": "null",
                        "port": "1",
                        "description": "MGMT INTERFACE",
                        "ipv4_prefix": "192.168.2.182/24",
                        "shutdown": False,
                        "vrf": "default",
                    },
                ],
            }
        }
