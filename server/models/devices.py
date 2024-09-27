""" LOCATION MODEL """

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class Devices(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Devices model representing a network device.
    """

    name: str = Field(..., description="The name of the device")
    location: str = Field(..., description="The location of the device")
    tenant: str = Field(..., description="The tenant of the device")
    description: str = Field(..., description="A description of the device")
    status: str = Field(..., description="The status of the device")
    device_type: str = Field(..., description="The type of the device")
    manufacturer: str = Field(..., description="The manufacturer of the device")
    serial_number: str = Field(..., description="The serial number of the device")
    platform: str = Field(..., description="The platform of the device")
    role: str = Field(..., description="The role of the device")

    class ConfigDict:  # pylint: disable=too-few-public-methods
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


class DeviceCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=100)
    tenant: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=255)
    status: str = Field(..., min_length=1, max_length=50)
    device_type: str = Field(..., min_length=1, max_length=50)
    manufacturer: str = Field(..., min_length=1, max_length=100)
    serial_number: str = Field(..., min_length=1, max_length=100)
    platform: str = Field(..., min_length=1, max_length=50)
    role: str = Field(..., min_length=1, max_length=50)

    class ConfigDict:  # pylint: disable=too-few-public-methods
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
