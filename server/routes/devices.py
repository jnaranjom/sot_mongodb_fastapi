"""
    Devices Routes
"""

from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.devices import Devices

devices_route = APIRouter()


@devices_route.get(
    "/devices",
    response_description="List all devices",
    response_model=List[Devices],
)
def list_devices(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    devices_list = list(request.app.database["Devices"].find(limit=200))
    return devices_list


# @devices_route.get(
#     "/devices/{object_id}",
#     response_description="Get a single location",
#     response_model=Devices,
# )
# def get_location(request: Request, object_id: str):
#     """_summary_

#     Args:
#         request (Request): _description_

#     Returns:
#         _type_: _description_
#     """
#     if (
#         location := request.app.database["Devices"].find_one({"_id": object_id})
#     ) is not None:
#         return location

#     raise HTTPException(status_code=404, detail=f"Location {object_id} not found")
