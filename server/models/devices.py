"""_summary_
"""
from typing import Optional
import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class Devices(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    vendor: str = Field(...)
    model: str = Field(...)
    serial_number: str = Field(...)
    ipv4_host: str = Field(...)
    hostname: str = Field(...)
    role: dict = Field(...)
    asset_class: str = Field(...)
    asset_id: str = Field(...)
    environment: str = Field(...)
    type: str = Field(...)
    os: str = Field(...)
    locations: list = Field(default_factory=list)
    fabric_id: str = Field(...)
    services: list = Field(default_factory=list)
    protocols: list = Field(default_factory=list)
    interfaces: list = Field(default_factory=list)
    acls: list = Field(default_factory=list)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "vendor": "cisco",
                "model": "csr1000v",
                "serial_number": "ABCDEFGHI",
                "ipv4_host": "192.168.2.240/24",
                "hostname": "edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "asset_id": "123456",
                "environment": "dev",
                "type": "virtual",
                "os": "cisco.ios.ios",
                "locations": [{"name": "site01", "id": "6510edf5c427b184028d642c"}],
                "fabric_id": "",
                "services": [{"name": "ntp", "id": "651c457435114b4d8239473c"}],
                "protocols": [{"name": "bgp", "id": "6510edf5c427b184028d642b"}],
                "interfaces": [
                    {"name": "lab01-edge01", "id": "6510edf5c427b184028d642b"}
                ],
                "acls": [{"name": "mgmt", "id": "6510edf5c427b184028d642c"}],
            }
        }


class DevicesUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    vendor: Optional[str]
    model: Optional[str]
    serial_number: Optional[str]
    ipv4_host: Optional[str]
    hostname: Optional[str]
    role: Optional[dict]
    asset_class: Optional[str]
    asset_id: Optional[str]
    environment: Optional[str]
    type: Optional[str]
    locations: Optional[list]
    os: Optional[str]
    fabric_id: Optional[str]
    services: Optional[list]
    protocols: Optional[list]
    interfaces: Optional[list]
    acls: Optional[list]

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        schema_extra = {
            "example": {
                "vendor": "cisco",
                "model": "csr1000v",
                "serial_number": "ABCDEFGHI",
                "ipv4_host": "192.168.2.240/24",
                "hostname": "edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "asset_id": "123456",
                "environment": "dev",
                "type": "virtual",
                "os": "cisco.ios.ios",
                "location": {"name": "site01", "id": "6510edf5c427b184028d642c"},
                "fabric_id": "",
                "services": [{"name": "ntp", "id": "651c457435114b4d8239473c"}],
                "protocols": [{"name": "bgp", "id": "6510edf5c427b184028d642b"}],
                "interfaces": [
                    {"name": "lab01-edge01", "id": "6510edf5c427b184028d642b"}
                ],
                "acls": [{"name": "mgmt", "id": "6510edf5c427b184028d642c"}],
            }
        }
