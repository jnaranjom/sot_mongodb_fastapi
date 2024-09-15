"""  LOCATION MODEL """

from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field

from server.utils.pyobjectid import PyObjectId


class Locations(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    location_type: str = Field(...)
    parent: str = Field(...)
    tenant: str = Field(...)
    zip_code: str = Field(...)
    address: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "dal-br01",
                "location_type": "Branch",
                "parent": "Dallas",
                "tenant": "Branch",
                "zip_code": "75001",
                "address": "123 Main Street",
                "description": "Downtown Dallas Branch",
                "status": "Active",
            }
        }
