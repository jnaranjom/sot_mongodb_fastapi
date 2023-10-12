"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Services(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    servers: list = Field(...)
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
                "name": "ntp",
                "servers": [
                    {"ipv4_host": "10.0.1.7", "prefer": True},
                    {"ipv4_host": "10.0.1.8", "prefer": False},
                ],
            }
        }


class ServicesUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: Optional[str]
    servers: Optional[list]
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
