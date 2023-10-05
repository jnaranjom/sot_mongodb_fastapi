"""
    Locations Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.locations import Locations, LocationsUpdate

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
    locations_list = list(request.app.database["Locations"].find(limit=100))
    return locations_list


@locations_route.get(
    "/locations/{object_id}",
    response_description="Get a single location",
    response_model=Locations,
)
def get_location(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    if (
        location := request.app.database["Locations"].find_one({"_id": object_id})
    ) is not None:
        return location

    raise HTTPException(status_code=404, detail=f"Location {object_id} not found")


@locations_route.post(
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


@locations_route.put(
    "/locations/{object_id}",
    response_description="Update a location",
    status_code=status.HTTP_200_OK,
    response_model=LocationsUpdate,
)
def update_location(
    request: Request, object_id: str, location: LocationsUpdate = Body(...)
):
    """_summary_

    Args:
        request (Request): _description_
        location (locations, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    location = {k: v for k, v in location.dict().items() if v is not None}
    if len(location) >= 1:
        updated_location = request.app.database["Locations"].update_one(
            {"_id": object_id}, {"$set": location}
        )

    return updated_location


@locations_route.delete(
    "/locations/{object_id}",
    response_description="Delete a location",
    response_model=LocationsUpdate,
)
def delete_location(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        location (locations, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Locations"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Location {object_id} not found")
