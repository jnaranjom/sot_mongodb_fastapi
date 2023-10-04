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


class Devices(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    vendor: str = Field(...)
    model: str = Field(...)
    ipv4_host: str = Field(...)
    hostname: str = Field(...)
    role: dict = Field(...)
    asset_class: str = Field(...)
    os: str = Field(...)
    site: str = Field(...)
    fabric_id: str = Field(...)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "6505f1fcfb548a14a25ab11e",
                "vendor": "cisco",
                "model": "asr1000",
                "os": "cisco.ios.ios",
                "ipv4_host": "192.168.2.100/24",
                "hostname": "lab01-edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "site": "lab01",
                "fabric_id": "10",
            }
        }


class DevicesUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    vendor: Optional[str]
    model: Optional[str]
    os: Optional[str]
    ipv4_host: Optional[str]
    hostname: Optional[str]
    role: Optional[dict]
    asset_class: Optional[str]
    site: Optional[str]
    fabric_id: Optional[str]

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        schema_extra = {
            "example": {
                "vendor": "cisco",
                "model": "asr1000",
                "os": "cisco.ios.ios",
                "ipv4_host": "192.168.2.100/24",
                "hostname": "lab01-edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "Texas",
                "site": "lab01",
                "fabric_id": "10",
            }
        }
