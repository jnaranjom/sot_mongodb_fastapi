"""_summary_
"""
from typing import Optional
from datetime import datetime
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
    attributes: dict = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": {"$oid": "652467f7c61673db1752d433"},
                "vendor": "cisco",
                "model": "csr1000v",
                "serial_number": "ABCDEFGHI",
                "ipv4_host": "192.168.2.50/24",
                "hostname": "edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "asset_id": "123456",
                "environment": "dev",
                "type": "virtual",
                "os": "cisco.ios.ios",
                "attributes": {
                    "services": [
                        {"name": "ntp", "id": "651c457435114b4d8239473c"},
                        {"name": "dns", "id": "6524698848f3fe822fcd6616"},
                    ],
                    "acls": [{"name": "mgmt", "id": "651c443104e4fff54121780f"}],
                    "protocols": [
                        {"name": "ospf", "id": "651f8855a5e098e62533d597"},
                        {"name": "bgp", "id": "651f32f55f35cb3f3da188cd"},
                    ],
                    "locations": [{"name": "lab01", "id": "651ed9c9036ed8004b7c0c34"}],
                    "interfaces": [
                        {"name": "interfaces", "id": "65246eeec61673db1752d435"}
                    ],
                    "bgp_neighbors": [
                        {"name": "ISP01", "id": "652470e8c61673db1752d438"}
                    ],
                },
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
    os: Optional[str]
    attributes: Optional[dict]
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "_id": {"$oid": "652467f7c61673db1752d433"},
                "vendor": "cisco",
                "model": "csr1000v",
                "serial_number": "ABCDEFGHI",
                "ipv4_host": "192.168.2.50/24",
                "hostname": "edge01",
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "asset_id": "123456",
                "environment": "dev",
                "type": "virtual",
                "os": "cisco.ios.ios",
                "attributes": {
                    "services": [
                        {"name": "ntp", "id": "651c457435114b4d8239473c"},
                        {"name": "dns", "id": "6524698848f3fe822fcd6616"},
                    ],
                    "acls": [{"name": "mgmt", "id": "651c443104e4fff54121780f"}],
                    "protocols": [
                        {"name": "ospf", "id": "651f8855a5e098e62533d597"},
                        {"name": "bgp", "id": "651f32f55f35cb3f3da188cd"},
                    ],
                    "locations": [{"name": "lab01", "id": "651ed9c9036ed8004b7c0c34"}],
                    "interfaces": [
                        {"name": "interfaces", "id": "65246eeec61673db1752d435"}
                    ],
                    "bgp_neighbors": [
                        {"name": "ISP01", "id": "652470e8c61673db1752d438"}
                    ],
                },
            }
        }
