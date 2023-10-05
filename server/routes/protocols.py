from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.protocols import Protocols, ProtocolsUpdate

protocols_route = APIRouter()


@protocols_route.get(
    "/protocols",
    response_description="List all protocols",
    response_model=List[Protocols],
)
def list_protocols(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    protocols_list = list(request.app.database["Protocols"].find(limit=100))
    return protocols_list


@protocols_route.get(
    "/protocols/{object_id}",
    response_description="Get a single protocol",
    response_model=Protocols,
)
def get_protocol(request: Request, object_id: str):
    """ """
    if (
        protocol := request.app.database["Protocols"].find_one({"_id": object_id})
    ) is not None:
        return protocol

    raise HTTPException(status_code=404, detail=f"Protocol {object_id} not found")


@protocols_route.post(
    "/protocols",
    response_description="Create a protocol",
    status_code=status.HTTP_201_CREATED,
    response_model=Protocols,
)
def create_protocol(request: Request, protocol: Protocols = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        protocol (protocols, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    protocol = jsonable_encoder(protocol)
    new_protocol = request.app.database["Protocols"].insert_one(protocol)
    created_protocol = request.app.database["Protocols"].find_one(
        {"_id": new_protocol.inserted_id}
    )

    return created_protocol


@protocols_route.put(
    "/protocols/{object_id}",
    response_description="Update a protocol",
    status_code=status.HTTP_200_OK,
    response_model=ProtocolsUpdate,
)
def update_protocol(
    request: Request, object_id: str, protocol: ProtocolsUpdate = Body(...)
):
    """_summary_

    Args:
        request (Request): _description_
        protocol (protocols, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    protocol = {k: v for k, v in protocol.dict().items() if v is not None}
    if len(protocol) >= 1:
        updated_protocol = request.app.database["Protocols"].update_one(
            {"_id": object_id}, {"$set": protocol}
        )

    return updated_protocol


@protocols_route.delete(
    "/protocols/{object_id}",
    response_description="Delete a protocol",
    response_model=ProtocolsUpdate,
)
def delete_protocol(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        protocol (protocols, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Protocols"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Protocol {object_id} not found")
