"""  LOCATION MODEL """

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class Devices(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    location: str = Field(...)
    tenant: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)
    device_type: str = Field(...)
    manufacturer: str = Field(...)
    serial_number: str = Field(...)
    platform: str = Field(...)
    role: str = Field(...)

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "description": "Branch Router",
                "location": "dal-br01",
                "name": "dal-br01-rtr01",
                "status": "Planned",
                "tenant": "Branch",
                "device_type": "iol",
                "manufacturer": "Cisco",
                "serial_number": "100001",
                "platform": "ios",
                "role": "branch:edge:router",
            }
        }
