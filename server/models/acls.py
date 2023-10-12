"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class ACLs(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    entries: list = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "mgmt",
                "version": "0.0.1",
                "entries": [
                    {
                        "action": "permit",
                        "destination": "any",
                        "modifier": "",
                        "name": "mgmt",
                        "port": "",
                        "protocol": "ip",
                        "range": "",
                        "remark": "",
                        "sn": "",
                        "source": "192.168.2.0/24",
                    },
                    {
                        "action": "permit",
                        "destination": "any",
                        "modifier": "0",
                        "name": "mgmt",
                        "port": "",
                        "protocol": "ip",
                        "range": "",
                        "remark": "",
                        "sn": "",
                        "source": "192.168.1.0/24",
                    },
                ],
            }
        }


class ACLsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: str = Field(...)
    entries: Optional[list]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "mgmt",
                "version": "0.0.1",
                "entries": [
                    {
                        "action": "permit",
                        "destination": "any",
                        "modifier": "",
                        "name": "mgmt",
                        "port": "",
                        "protocol": "ip",
                        "range": "",
                        "remark": "",
                        "sn": "",
                        "source": "192.168.2.0/24",
                    },
                    {
                        "action": "permit",
                        "destination": "any",
                        "modifier": "0",
                        "name": "mgmt",
                        "port": "",
                        "protocol": "ip",
                        "range": "",
                        "remark": "",
                        "sn": "",
                        "source": "192.168.1.0/24",
                    },
                ],
            }
        }
