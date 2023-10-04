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


class ACLs(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    entries: list = Field(...)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

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

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

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
