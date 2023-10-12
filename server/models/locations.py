"""_summary_
"""
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

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    site: str = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)
    country: str = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
                "country": "United States",
            }
        }


class LocationsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_
    Args:
        BaseModel (_type_): _description_
    """

    site: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    country: Optional[str]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
                "country": "United States",
            }
        }
