from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from server.models.devices import Devices, DevicesUpdate

devices_route = APIRouter()


@devices_route.get(
    "/", response_description="List all devices", response_model=List[Devices]
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


@devices_route.post(
    "/",
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
