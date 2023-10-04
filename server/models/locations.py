"""_summary_
"""
from typing import Optional
import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):  # pylint: disable=too-few-public-methods
    """ """

    @classmethod
    def __get_validators__(cls):
        """ """
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """ """
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        """ """
        field_schema.update(type="string")


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
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "6505455c64514aee4b847469",
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
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
    updated: Optional[str]

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "_id": "6505455c64514aee4b847469",
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
                "created": "2023-10-03T16:22:50.718911",
                "updated": "2023-10-03T16:22:50.718911",
            }
        }
