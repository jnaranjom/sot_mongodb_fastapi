import uuid
from typing import Optional
from pydantic import BaseModel, Field


class locations(BaseModel):
    site: str = Field(...)
    bgp_asn: str = Field(...)
    snmp_community: str = Field(...)
    ospf_id: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)

    class Config:
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


class devices(BaseModel):
    vendor: str = Field(...)
    model: str = Field(...)
    ipv4_host: str = Field(...)
    hostname: str = Field(...)
    role: str = Field(...)
    asset_class: str = Field(...)
    os: str = Field(...)

    class Config:
        allow_population_by_field_name = True
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
