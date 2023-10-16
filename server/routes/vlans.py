"""
    Vlans Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.vlans import Vlans, VlansUpdate

vlans_route = APIRouter()


@vlans_route.get(
    "/vlans",
    response_description="List all vlans",
    response_model=List[Vlans],
)
def list_vlans(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    vlans_list = list(request.app.database["Vlans"].find(limit=100))
    return vlans_list


@vlans_route.get(
    "/vlans/{object_id}",
    response_description="Get a single vlan",
    response_model=Vlans,
)
def get_vlan_by_id(request: Request, object_id: str):
    """Function to retrieve a single vlan from MongoDB"""
    if (vlan := request.app.database["Vlans"].find_one({"_id": object_id})) is not None:
        return vlan

    raise HTTPException(status_code=404, detail=f"Device {object_id} not found")


@vlans_route.post(
    "/vlans",
    response_description="Create a vlan",
    status_code=status.HTTP_201_CREATED,
    response_model=Vlans,
)
def create_vlan(request: Request, vlan: Vlans = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        vlan (vlans, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    vlan = jsonable_encoder(vlan)
    new_vlan = request.app.database["Vlans"].insert_one(vlan)
    created_vlan = request.app.database["Vlans"].find_one({"_id": new_vlan.inserted_id})

    return created_vlan


@vlans_route.put(
    "/vlans/{object_id}",
    response_description="Update a vlan",
    status_code=status.HTTP_200_OK,
    response_model=VlansUpdate,
)
def update_vlan(request: Request, object_id: str, vlan: VlansUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        vlan (vlans, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    vlan = {k: v for k, v in vlan.dict().items() if v is not None}
    if len(vlan) >= 1:
        updated_vlan = request.app.database["Vlans"].update_one(
            {"_id": object_id}, {"$set": vlan}
        )

    return updated_vlan


@vlans_route.delete(
    "/vlans/{object_id}",
    response_description="Delete a vlan",
    response_model=VlansUpdate,
)
def delete_vlan(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        vlan (vlans, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Vlans"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Vlan {object_id} not found")
