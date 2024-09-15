"""
    Locations Routes
"""

from typing import List
from fastapi import APIRouter, Request
from server.models.locations import Locations

locations_route = APIRouter()


@locations_route.get(
    "/locations",
    response_description="List all locations",
    response_model=List[Locations],
)
def list_locations(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    locations_list = list(request.app.database["Locations"].find(limit=200))
    return locations_list


# @locations_route.get(
#     "/locations/{object_id}",
#     response_description="Get a single location",
#     response_model=Locations,
# )
# def get_location(request: Request, object_id: str):
#     """_summary_

#     Args:
#         request (Request): _description_

#     Returns:
#         _type_: _description_
#     """
#     if (
#         location := request.app.database["Locations"].find_one({"_id": object_id})
#     ) is not None:
#         return location

#     raise HTTPException(status_code=404, detail=f"Location {object_id} not found")
