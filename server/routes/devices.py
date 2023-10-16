"""
    Devices Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.devices import Devices, DevicesUpdate

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
    devices_list = list(request.app.database["Devices"].find(limit=100))
    return devices_list


@devices_route.get(
    "/devices/{object_id}",
    response_description="Get a single device",
    response_model=Devices,
)
def get_device_by_id(request: Request, object_id: str):
    """Function to retrieve a single device from MongoDB"""
    if (
        device := request.app.database["Devices"].find_one({"_id": object_id})
    ) is not None:
        return device

    raise HTTPException(status_code=404, detail=f"Device {object_id} not found")


@devices_route.post(
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


@devices_route.put(
    "/devices/{object_id}",
    response_description="Update a device",
    status_code=status.HTTP_200_OK,
    response_model=DevicesUpdate,
)
def update_device(request: Request, object_id: str, device: DevicesUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        device (devices, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    device = {k: v for k, v in device.dict().items() if v is not None}
    if len(device) >= 1:
        updated_device = request.app.database["Devices"].update_one(
            {"_id": object_id}, {"$set": device}
        )

    return updated_device


@devices_route.delete(
    "/devices/{object_id}",
    response_description="Delete a device",
    response_model=DevicesUpdate,
)
def delete_device(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        device (devices, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Devices"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Device {object_id} not found")
