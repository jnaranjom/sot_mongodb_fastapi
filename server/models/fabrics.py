"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Fabrics(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    attributes: dict = Field(default_factory=dict)
    fabric_id: str = Field(...)
    version: str = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "fabric_10",
                "attributes": [
                    {"prefix": "10.10.0.0/24", "name": "ibgp"},
                    {"prefix": "10.10.1.0/24", "name": "mgmt"},
                ],
                "fabric_id": "10",
                "version": "0.0.1",
            }
        }


class FabricsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    attributes: dict = Field(default_factory=dict)
    fabric_id: str = Field(...)
    version: str = Field(...)
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "fabric_10",
                "attributes": [
                    {"prefix": "10.10.0.0/24", "name": "ibgp"},
                    {"prefix": "10.10.1.0/24", "name": "mgmt"},
                ],
                "fabric_id": "10",
                "version": "0.0.1",
            }
        }
