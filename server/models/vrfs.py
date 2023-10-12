"""_summary_
"""
from typing import Optional
from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from server.utils.pyobjectid import PyObjectId


class VRFs(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    version: str = Field(...)
    export_route_policy: str = Field(...)
    export_rt: str = Field(...)
    import_route_policy: str = Field(...)
    import_rt: str = Field(...)
    rd: str = Field(...)
    created: datetime = Field(datetime.now())
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "export_route_policy": "null",
                "export_rt": "100:100",
                "import_route_policy": "null",
                "import_rt": "100:100",
                "name": "CUST1_VRF",
                "version": "0.0.1",
                "rd": "100:100",
            }
        }


class VRFsUpdate(BaseModel):  # pylint: disable=too-few-public-methods
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: Optional[str]
    version: Optional[str]
    export_route_policy: str = Field(...)
    export_rt: str = Field(...)
    import_route_policy: str = Field(...)
    import_rt: str = Field(...)
    rd: str = Field(...)
    updated: datetime = Field(datetime.now())

    class Config:  # pylint: disable=too-few-public-methods
        """_summary_"""

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "export_route_policy": "null",
                "export_rt": "100:100",
                "import_route_policy": "null",
                "import_rt": "100:100",
                "name": "CUST1_VRF",
                "version": "0.0.1",
                "rd": "100:100",
            }
        }
