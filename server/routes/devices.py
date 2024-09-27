"""
    Devices Routes
"""

from typing import List
from fastapi import APIRouter, Request
from server.models.devices import Devices
from fastapi import HTTPException, status
from server.models.devices import DeviceCreate
from pydantic import BaseModel, Field

devices_route = APIRouter()


@devices_route.get(
    "/devices",
    response_description="List all devices",
    response_model=List[Devices],
)
def list_devices(request: Request):
    """Retrieves a list of devices from the database.

    Args:
        request (Request): The request object containing the application context and database connection.

    Returns:
        List[dict]: A list of devices retrieved from the "Devices" collection in the database.
    """
    devices_list = list(request.app.database["Devices"].find(limit=200))
    return devices_list


@devices_route.get(
    "/devices/name/{device_name}",
    response_description="Get a single device by name",
    response_model=Devices,
)
def get_device_by_name(device_name: str, request: Request):
    """Retrieves a single device from the database by its name.

    Args:
        device_name (str): The name of the device to retrieve.
        request (Request): The request object containing the application context and database connection.

    Returns:
        dict: The device retrieved from the "Devices" collection in the database.
    """
    device = request.app.database["Devices"].find_one({"name": device_name})
    if device is None:
        return {"error": "Device not found"}
    return device


@devices_route.post(
    "/devices",
    response_description="Add a new device",
    response_model=Devices,
)
def create_device(request: Request, device: DeviceCreate):
    """Creates a new device in the database.

    Args:
        request (Request): The request object containing the application context and database connection.
        device (DeviceCreate): The device data to be created.

    Returns:
        dict: The newly created device.
    """
    # Ensure the device has all required attributes
    device = DeviceCreate(**device.dict())

    # Check if a device with the same name already exists
    device_exists = request.app.database["Devices"].find_one({"name": device.name})
    if device_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Device with this name already exists",
        )

    new_device = request.app.database["Devices"].insert_one(device.dict())
    created_device = request.app.database["Devices"].find_one({"_id": new_device.inserted_id})
    return created_device
