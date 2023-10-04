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


class Locations(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    site: str = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "6505455c64514aee4b847469",
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
            }
        }


class LocationsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_
    Args:
        BaseModel (_type_): _description_
    """

    site: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    updated: Optional[str]

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "_id": "6505455c64514aee4b847469",
                "site": "lab01",
                "address": "1234 ABC Street",
                "city": "Dallas",
                "state": "Texas",
                "zip_code": "75078",
                "created": "2023-10-03T16:22:50.718911",
                "updated": "2023-10-03T16:22:50.718911",
            }
        }


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


class Services(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    servers: list = Field(...)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "version": "0.0.1",
                "name": "ntp",
                "servers": [
                    {"ipv4_host": "10.0.1.7", "prefer": True},
                    {"ipv4_host": "10.0.1.8", "prefer": False},
                ],
            }
        }


class ServicesUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str = Field(...)
    version: str = Field(...)
    servers: list = Field(...)

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        schema_extra = {
            "example": {
                "version": "0.0.1",
                "name": "ntp",
                "servers": [
                    {"ipv4_host": "10.0.1.7", "prefer": True},
                    {"ipv4_host": "10.0.1.8", "prefer": False},
                ],
            }
        }


class Protocols(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    attributes: dict = Field(...)
    environment: str = Field(...)
    scope: str = Field(...)
    aggregate_networks: list = Field(default_factory=list)
    networks: list = Field(default_factory=list)
    created: datetime.datetime = datetime.datetime.now()
    updated: datetime.datetime = datetime.datetime.now()

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "bgp",
                "version": "0.0.1",
                "attributes": {
                    "router_id": "loopback0",
                    "vrf": "default",
                    "log_neighbor_changes": True,
                    "asn": "65100",
                },
                "environment": "dev",
                "scope": "edge",
                "aggregate_networks": [
                    {"network": "10.0.0.0/8", "summary_only": "false"},
                    {"network": "192.168.2.0/24", "summary_only": "true"},
                ],
                "networks": ["192.168.10.0/24", "192.168.11.0/24", "192.168.12.0/24"],
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


# class ProtocolsUpdate(BaseModel):
#     """_summary_

#     Args:
#         BaseModel (_type_): _description_
#     """

#     name: str = Field(...)
#     version: str = Field(...)
#     servers: list = Field(...)

#     class Config:  # pylint: disable=too-few-public-methods
#         """_summary_"""

#         schema_extra = {
#             "example": {
#                 "version": "0.0.1",
#                 "name": "ntp",
#                 "servers": [
#                     {"ipv4_host": "10.0.1.7", "prefer": True},
#                     {"ipv4_host": "10.0.1.8", "prefer": False},
#                 ],
#             }
#         }
