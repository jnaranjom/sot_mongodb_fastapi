"""
    Devices Routes
"""

from typing import List
from fastapi import APIRouter, Request
from server.models.devices import Devices

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
