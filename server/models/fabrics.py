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


class Fabrics(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    fabric_id: str = Field(...)
    ibgp_prefix: str = Field(...)
    p2p_prefix: str = Field(...)
    vtep_prefix: str = Field(...)
    protocols: dict = Field(...)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fabric_id": "10",
                "ibgp_prefix": "10.0.11.0/24",
                "p2p_prefix": "172.16.2.0/24",
                "vtep_prefix": "10.0.10.0/24",
                "protocols": {
                    "bgp": {"asn": "65100"},
                    "ospf": {"area": "0", "process_id": "1", "max_lsa": "12000"},
                    "vxlan": "",
                },
            }
        }


class FabricsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    fabric_id: Optional[str]
    ibgp_prefix: Optional[str]
    p2p_prefix: Optional[str]
    vtep_prefix: Optional[str]
    protocols: Optional[dict]

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        schema_extra = {
            "example": {
                "fabric_id": "10",
                "ibgp_prefix": "10.0.11.0/24",
                "p2p_prefix": "172.16.2.0/24",
                "vtep_prefix": "10.0.10.0/24",
                "protocols": {
                    "bgp": {"asn": "65100"},
                    "ospf": {"area": "0", "process_id": "1", "max_lsa": "12000"},
                    "vxlan": "",
                },
            }
        }
