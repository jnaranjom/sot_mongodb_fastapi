""" FASTAPI routes functions
"""
from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from server.models.fabrics import Fabrics
from server.models.acls import ACLs
from server.models.services import Services
from server.models.protocols import Protocols

router = APIRouter()


@router.get(
    "/fabrics", response_description="List all fabrics", response_model=List[Fabrics]
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


@router.post(
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


@router.get("/acls", response_description="List all acls", response_model=List[ACLs])
def list_acls(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    acls_list = list(request.app.database["ACLs"].find(limit=100))
    return acls_list


@router.post(
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


@router.get(
    "/services", response_description="List all services", response_model=List[Services]
)
def list_services(request: Request):
    """_summary_

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    services_list = list(request.app.database["Services"].find(limit=100))
    return services_list


@router.post(
    "/services",
    response_description="Create a service",
    status_code=status.HTTP_201_CREATED,
    response_model=Services,
)
def create_service(request: Request, service: Services = Body(...)):
    """_summary_

    Args:
        request (Request): _description_
        service (services, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    service = jsonable_encoder(service)
    new_service = request.app.database["Services"].insert_one(service)
    created_service = request.app.database["Services"].find_one(
        {"_id": new_service.inserted_id}
    )

    return created_service


@router.get(
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
