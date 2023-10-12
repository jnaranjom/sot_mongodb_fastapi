from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.bgpneighbors import BgpNeighbors, BgpNeighborsUpdate

bgpneighbors_route = APIRouter()


@bgpneighbors_route.get(
    "/bgpneighbors",
    response_description="List all bgpneighbors",
    response_model=List[BgpNeighbors],
)
def list_bgpneighbors(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    bgpneighbors_list = list(request.app.database["BgpNeighbors"].find(limit=100))
    return bgpneighbors_list


@bgpneighbors_route.get(
    "/bgpneighbors/{object_id}",
    response_description="Get a single bgpneighbor",
    response_model=BgpNeighbors,
)
def get_bgpneighbor(request: Request, object_id: str):
    """ """
    if (
        bgpneighbor := request.app.database["BgpNeighbors"].find_one({"_id": object_id})
    ) is not None:
        return bgpneighbor

    raise HTTPException(status_code=404, detail=f"BgpNeighbor {object_id} not found")


@bgpneighbors_route.post(
    "/bgpneighbors",
    response_description="Create a bgpneighbor",
    status_code=status.HTTP_201_CREATED,
    response_model=BgpNeighbors,
)
def create_bgpneighbor(request: Request, bgpneighbor: BgpNeighbors = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        bgpneighbor (bgpneighbors, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    bgpneighbor = jsonable_encoder(bgpneighbor)
    new_bgpneighbor = request.app.database["BgpNeighbors"].insert_one(bgpneighbor)
    created_bgpneighbor = request.app.database["BgpNeighbors"].find_one(
        {"_id": new_bgpneighbor.inserted_id}
    )

    return created_bgpneighbor


@bgpneighbors_route.put(
    "/bgpneighbors/{object_id}",
    response_description="Update a bgpneighbor",
    status_code=status.HTTP_200_OK,
    response_model=BgpNeighborsUpdate,
)
def update_bgpneighbor(
    request: Request, object_id: str, bgpneighbor: BgpNeighborsUpdate = Body(...)
):
    """_summary_

    Args:
        request (Request): _description_
        bgpneighbor (bgpneighbors, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    bgpneighbor = {k: v for k, v in bgpneighbor.dict().items() if v is not None}
    if len(bgpneighbor) >= 1:
        updated_bgpneighbor = request.app.database["BgpNeighbors"].update_one(
            {"_id": object_id}, {"$set": bgpneighbor}
        )

    return updated_bgpneighbor


@bgpneighbors_route.delete(
    "/bgpneighbors/{object_id}",
    response_description="Delete a bgpneighbor",
    response_model=BgpNeighborsUpdate,
)
def delete_bgpneighbor(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        bgpneighbor (bgpneighbors, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["BgpNeighbors"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"BgpNeighbor {object_id} not found")
