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
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)

    class Config:
        """_summary_"""

        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "site": "lab01",
                "address": "1234 ABC Street",
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
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]

    class Config:
        """_summary_"""

        schema_extra = {
            "example": {
                "site": "lab01",
                "address": "1234 ABC Street",
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
    role: dict = Field(...)
    asset_class: str = Field(...)
    os: str = Field(...)
    site: str = Field(...)
    fabric_id: str = Field(...)

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
                "role": {"name": "edge", "id": "01"},
                "asset_class": "ip_router",
                "site": "lab01",
                "fabric_id": "10",
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
    role: Optional[dict]
    asset_class: Optional[str]
    site: Optional[str]
    fabric_id: Optional[str]

    class Config:
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


class Fabrics(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    fabric_id: str = Field(...)
    ibgp_prefix: str = Field(...)
    p2p_prefix: str = Field(...)
    vtep_prefix: str = Field(...)
    protocols: dict = Field(...)

    class Config:
        """_summary_"""

        allow_population_by_field_name = True
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


class FabricsUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    fabric_id: Optional[str]
    ibgp_prefix: Optional[str]
    p2p_prefix: Optional[str]
    vtep_prefix: Optional[str]
    protocols: Optional[dict]

    class Config:
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


class ACLs(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    version: str = Field(...)
    entries: list = Field(...)

    class Config:
        """_summary_"""

        allow_population_by_field_name = True
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


class ACLsUpdate(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: str = Field(...)
    entries: Optional[list]

    class Config:
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
