""" FASTAPI routes functions
"""
from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models import Locations, LocationsUpdate, Devices, DevicesUpdate

router = APIRouter()


@router.get(
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
    locations_list = list(request.app.database["Locations"].find(limit=100))
    return locations_list


@router.get(
    "/devices", response_description="List all devices", response_model=List[Devices]
)
def list_devices(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    devices_list = list(request.app.database["Devices"].find(limit=100))
    return devices_list


@router.post(
    "/locations",
    response_description="Create a location",
    status_code=status.HTTP_201_CREATED,
    response_model=Locations,
)
def create_location(request: Request, location: Locations = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        location (locations, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    location = jsonable_encoder(location)
    new_location = request.app.database["Locations"].insert_one(location)
    created_location = request.app.database["Locations"].find_one(
        {"_id": new_location.inserted_id}
    )

    return created_location


@router.post(
    "/devices",
    response_description="Create a device",
    status_code=status.HTTP_201_CREATED,
    response_model=Devices,
)
def create_device(request: Request, device: Devices = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        device (devices, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    device = jsonable_encoder(device)
    new_device = request.app.database["Devices"].insert_one(device)
    created_device = request.app.database["Devices"].find_one(
        {"_id": new_device.inserted_id}
    )

    return created_device
