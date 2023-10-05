"""
    Interfaces Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.interfaces import Interfaces, InterfacesUpdate

interfaces_route = APIRouter()


@interfaces_route.get(
    "/interfaces",
    response_description="List all interfaces",
    response_model=List[Interfaces],
)
def list_interfaces(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    interfaces_list = list(request.app.database["Interfaces"].find(limit=100))
    return interfaces_list


@interfaces_route.get(
    "/interfaces/{object_id}",
    response_description="Get a single interface",
    response_model=Interfaces,
)
def get_interface(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    if (
        interface := request.app.database["Interfaces"].find_one({"_id": object_id})
    ) is not None:
        return interface

    raise HTTPException(status_code=404, detail=f"Interface {object_id} not found")


@interfaces_route.post(
    "/interfaces",
    response_description="Create a interface",
    status_code=status.HTTP_201_CREATED,
    response_model=Interfaces,
)
def create_interface(request: Request, interface: Interfaces = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        interface (interfaces, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    interface = jsonable_encoder(interface)
    new_interface = request.app.database["Interfaces"].insert_one(interface)
    created_interface = request.app.database["Interfaces"].find_one(
        {"_id": new_interface.inserted_id}
    )

    return created_interface


@interfaces_route.put(
    "/interfaces/{object_id}",
    response_description="Update a interface",
    status_code=status.HTTP_200_OK,
    response_model=InterfacesUpdate,
)
def update_interface(
    request: Request, object_id: str, interface: InterfacesUpdate = Body(...)
):
    """_summary_

    Args:
        request (Request): _description_
        interface (interfaces, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    interface = {k: v for k, v in interface.dict().items() if v is not None}
    if len(interface) >= 1:
        updated_interface = request.app.database["Interfaces"].update_one(
            {"_id": object_id}, {"$set": interface}
        )

    return updated_interface


@interfaces_route.delete(
    "/interfaces/{object_id}",
    response_description="Delete a interface",
    response_model=InterfacesUpdate,
)
def delete_interface(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        interface (interfaces, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Interfaces"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Interface {object_id} not found")
