"""
    Prefixlists Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.prefixlists import Prefixlists, PrefixlistsUpdate

prefixlists_route = APIRouter()


@prefixlists_route.get(
    "/prefixlists",
    response_description="List all prefixlists",
    response_model=List[Prefixlists],
)
def list_prefixlists(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    prefixlists_list = list(request.app.database["Prefixlists"].find(limit=100))
    return prefixlists_list


@prefixlists_route.get(
    "/prefixlists/{object_id}",
    response_description="Get a single prefixlist",
    response_model=Prefixlists,
)
def get_prefixlist_by_id(request: Request, object_id: str):
    """Function to retrieve a single prefixlist from MongoDB"""
    if (
        prefixlist := request.app.database["Prefixlists"].find_one({"_id": object_id})
    ) is not None:
        return prefixlist

    raise HTTPException(status_code=404, detail=f"Device {object_id} not found")


@prefixlists_route.post(
    "/prefixlists",
    response_description="Create a prefixlist",
    status_code=status.HTTP_201_CREATED,
    response_model=Prefixlists,
)
def create_prefixlist(request: Request, prefixlist: Prefixlists = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        prefixlist (prefixlists, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    prefixlist = jsonable_encoder(prefixlist)
    new_prefixlist = request.app.database["Prefixlists"].insert_one(prefixlist)
    created_prefixlist = request.app.database["Prefixlists"].find_one(
        {"_id": new_prefixlist.inserted_id}
    )

    return created_prefixlist


@prefixlists_route.put(
    "/prefixlists/{object_id}",
    response_description="Update a prefixlist",
    status_code=status.HTTP_200_OK,
    response_model=PrefixlistsUpdate,
)
def update_prefixlist(request: Request, object_id: str, prefixlist: PrefixlistsUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        prefixlist (prefixlists, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    prefixlist = {k: v for k, v in prefixlist.dict().items() if v is not None}
    if len(prefixlist) >= 1:
        updated_prefixlist = request.app.database["Prefixlists"].update_one(
            {"_id": object_id}, {"$set": prefixlist}
        )

    return updated_prefixlist


@prefixlists_route.delete(
    "/prefixlists/{object_id}",
    response_description="Delete a prefixlist",
    response_model=PrefixlistsUpdate,
)
def delete_prefixlist(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        prefixlist (prefixlists, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Prefixlists"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Prefixlist {object_id} not found")