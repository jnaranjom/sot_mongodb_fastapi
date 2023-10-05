"""
    ACLs Routes
"""
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.acls import ACLs, ACLsUpdate

acls_route = APIRouter()


@acls_route.get(
    "/acls",
    response_description="List all acls",
    response_model=List[ACLs],
)
def list_acls(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    acls_list = list(request.app.database["ACLs"].find(limit=100))
    return acls_list


@acls_route.get(
    "/acls/{object_id}",
    response_description="Get a single acl",
    response_model=ACLs,
)
def get_acl(request: Request, object_id: str):
    """ """
    if (acl := request.app.database["ACLs"].find_one({"_id": object_id})) is not None:
        return acl

    raise HTTPException(status_code=404, detail=f"ACL {object_id} not found")


@acls_route.post(
    "/acls",
    response_description="Create a acl",
    status_code=status.HTTP_201_CREATED,
    response_model=ACLs,
)
def create_acl(request: Request, acl: ACLs = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        acl (acls, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    acl = jsonable_encoder(acl)
    new_acl = request.app.database["ACLs"].insert_one(acl)
    created_acl = request.app.database["ACLs"].find_one({"_id": new_acl.inserted_id})

    return created_acl


@acls_route.put(
    "/acls/{object_id}",
    response_description="Update a acl",
    status_code=status.HTTP_200_OK,
    response_model=ACLsUpdate,
)
def update_acl(request: Request, object_id: str, acl: ACLsUpdate = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        acl (acls, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    acl = {k: v for k, v in acl.dict().items() if v is not None}
    if len(acl) >= 1:
        updated_acl = request.app.database["ACLs"].update_one(
            {"_id": object_id}, {"$set": acl}
        )

    return updated_acl


@acls_route.delete(
    "/acls/{object_id}",
    response_description="Delete a acl",
    response_model=ACLsUpdate,
)
def delete_acl(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        acl (acls, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["ACLs"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"ACL {object_id} not found")
