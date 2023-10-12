from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.vrfs import VRFs, VRFsUpdate

vrfs_route = APIRouter()


@vrfs_route.get(
    "/vrfs",
    response_description="List all vrfs",
    response_model=List[VRFs],
)
def list_vrfs(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    vrfs_list = list(request.app.database["VRFs"].find(limit=100))
    return vrfs_list


@vrfs_route.get(
    "/vrfs/{object_id}",
    response_description="Get a single vrf",
    response_model=VRFs,
)
def get_vrf(request: Request, object_id: str):
    """ """
    if (vrf := request.app.database["VRFs"].find_one({"_id": object_id})) is not None:
        return vrf

    raise HTTPException(status_code=404, detail=f"VRF {object_id} not found")


@vrfs_route.post(
    "/vrfs",
    response_description="Create a vrf",
    status_code=status.HTTP_201_CREATED,
    response_model=VRFs,
)
def create_vrf(request: Request, vrf: VRFs = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        vrf (vrfs, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    vrf = jsonable_encoder(vrf)
    new_vrf = request.app.database["VRFs"].insert_one(vrf)
    created_vrf = request.app.database["VRFs"].find_one({"_id": new_vrf.inserted_id})

    return created_vrf


@vrfs_route.put(
    "/vrfs/{object_id}",
    response_description="Update a vrf",
    status_code=status.HTTP_200_OK,
    response_model=VRFsUpdate,
)
def update_vrf(request: Request, object_id: str, vrf: VRFsUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        vrf (vrfs, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    vrf = {k: v for k, v in vrf.dict().items() if v is not None}
    if len(vrf) >= 1:
        updated_vrf = request.app.database["VRFs"].update_one(
            {"_id": object_id}, {"$set": vrf}
        )

    return updated_vrf


@vrfs_route.delete(
    "/vrfs/{object_id}",
    response_description="Delete a vrf",
    response_model=VRFsUpdate,
)
def delete_vrf(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        vrf (vrfs, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["VRFs"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"VRF {object_id} not found")
