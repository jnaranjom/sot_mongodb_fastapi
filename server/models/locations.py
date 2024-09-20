"""  LOCATION MODEL """

from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class Locations(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Locations model representing a network location.
    """

    name: str = Field(..., description="The name of the location")
    location_type: str = Field(..., description="The type of the location, e.g., Branch, HQ")
    parent: str = Field(..., description="The parent location")
    tenant: str = Field(..., description="The tenant associated with the location")
    zip_code: str = Field(..., description="The zip code of the location")
    address: str = Field(..., description="The address of the location")
    description: str = Field(..., description="A brief description of the location")
    status: str = Field(..., description="The status of the location, e.g., Active, Staging")

    class ConfigDict:  # pylint: disable=too-few-public-methods
        """_summary_"""

        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "dal-br01",
                "location_type": "Branch",
                "parent": "Dallas",
                "tenant": "Branch",
                "zip_code": "75001",
                "address": "123 Main Street",
                "description": "Downtown Dallas Branch",
                "status": "Active",
            }
        }
