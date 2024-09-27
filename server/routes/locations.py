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
    """Retrieves a list of network locations from the database.

    Args:
        request (Request): The request object containing the application context and database connection.

    Returns:
        List[dict]: A list of locations retrieved from the "Locations" collection in the database.
    """
    locations_list = list(request.app.database["Locations"].find(limit=200))
    return locations_list


@locations_route.get(
    "/locations/name/{location_name}",
    response_description="Get a single location by name",
    response_model=Locations,
)
def get_location_by_name(location_name: str, request: Request):
    """Retrieves a single network location by its name from the database.

    Args:
        name (str): The name of the location to retrieve.
        request (Request): The request object containing the application context and database connection.

    Returns:
        dict: The location document retrieved from the "Locations" collection in the database.
    """
    location = request.app.database["Locations"].find_one({"name": location_name})
    if device is None:
        return {"error": "Device not found"}
    return device
