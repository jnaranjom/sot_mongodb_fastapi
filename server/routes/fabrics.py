"""
    Fabrics Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.fabrics import Fabrics, FabricsUpdate

fabrics_route = APIRouter()


@fabrics_route.get(
    "/fabrics",
    response_description="List all fabrics",
    response_model=List[Fabrics],
)
def list_fabrics(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    fabrics_list = list(request.app.database["Fabrics"].find(limit=100))
    return fabrics_list


@fabrics_route.get(
    "/fabrics/{object_id}",
    response_description="Get a single fabric",
    response_model=Fabrics,
)
def get_fabric_by_id(request: Request, object_id: str):
    """Function to retrieve a single fabric from MongoDB"""
    if (
        fabric := request.app.database["Fabrics"].find_one({"_id": object_id})
    ) is not None:
        return fabric

    raise HTTPException(status_code=404, detail=f"Device {object_id} not found")


@fabrics_route.post(
    "/fabrics",
    response_description="Create a fabric",
    status_code=status.HTTP_201_CREATED,
    response_model=Fabrics,
)
def create_fabric(request: Request, fabric: Fabrics = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        fabric (fabrics, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    fabric = jsonable_encoder(fabric)
    new_fabric = request.app.database["Fabrics"].insert_one(fabric)
    created_fabric = request.app.database["Fabrics"].find_one(
        {"_id": new_fabric.inserted_id}
    )

    return created_fabric


@fabrics_route.put(
    "/fabrics/{object_id}",
    response_description="Update a fabric",
    status_code=status.HTTP_200_OK,
    response_model=FabricsUpdate,
)
def update_fabric(request: Request, object_id: str, fabric: FabricsUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        fabric (fabrics, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    fabric = {k: v for k, v in fabric.dict().items() if v is not None}
    if len(fabric) >= 1:
        updated_fabric = request.app.database["Fabrics"].update_one(
            {"_id": object_id}, {"$set": fabric}
        )

    return updated_fabric


@fabrics_route.delete(
    "/fabrics/{object_id}",
    response_description="Delete a fabric",
    response_model=FabricsUpdate,
)
def delete_fabric(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        fabric (fabrics, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Fabrics"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Fabric {object_id} not found")
