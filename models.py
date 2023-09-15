"""_summary_
"""
from typing import Optional
from pydantic import BaseModel, Field


class Locations(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    site: str = Field(...)
    bgp_asn: str = Field(...)
    snmp_community: str = Field(...)
    ospf_id: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)

    class Config:
        """_summary_"""

        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "site": "lab01",
                "bgp_asn": "65000",
                "snmp_community": "lab01",
                "ospf_id": "1",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
            }
        }


class LocationsUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    site: Optional[str]
    bgp_asn: Optional[str]
    snmp_community: Optional[str]
    ospf_id: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

    class Config:
        """_summary_"""

        schema_extra = {
            "example": {
                "site": "lab01",
                "bgp_asn": "65000",
                "snmp_community": "lab01",
                "ospf_id": "1",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
            }
        }


class Devices(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    vendor: str = Field(...)
    model: str = Field(...)
    ipv4_host: str = Field(...)
    hostname: str = Field(...)
    role: str = Field(...)
    asset_class: str = Field(...)
    os: str = Field(...)

    class Config:
        """_summary_"""

        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "vendor": "cisco",
                "model": "asr1000",
                "os": "cisco.ios.ios",
                "ipv4_host": "192.168.2.100/24",
                "hostname": "lab01-edge01",
                "role": "edge",
                "asset_class": "ip_router",
            }
        }


class DevicesUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    vendor: Optional[str]
    model: Optional[str]
    os: Optional[str]
    ipv4_host: Optional[str]
    hostname: Optional[str]
    role: Optional[str]
    asset_class: Optional[str]

    class Config:
        """_summary_"""

        schema_extra = {
            "example": {
                "vendor": "cisco",
                "model": "asr1000",
                "os": "cisco.ios.ios",
                "ipv4_host": "192.168.2.100/24",
                "hostname": "lab01-edge01",
                "role": "edge",
                "asset_class": "Texas",
            }
        }
