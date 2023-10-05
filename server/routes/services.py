from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, HTTPException, status
from server.models.services import Services, ServicesUpdate

services_route = APIRouter()


@services_route.get(
    "/services",
    response_description="List all services",
    response_model=List[Services],
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


@services_route.get(
    "/services/{object_id}",
    response_description="Get a single service",
    response_model=Services,
)
def get_service(request: Request, object_id: str):
    """ """
    if (
        service := request.app.database["Services"].find_one({"_id": object_id})
    ) is not None:
        return service

    raise HTTPException(status_code=404, detail=f"Service {object_id} not found")


@services_route.post(
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


@services_route.put(
    "/services/{object_id}",
    response_description="Update a service",
    status_code=status.HTTP_200_OK,
    response_model=ServicesUpdate,
)
def update_service(
    request: Request, object_id: str, service: ServicesUpdate = Body(...)
):
    """_summary_

    Args:
        request (Request): _description_
        service (services, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    service = {k: v for k, v in service.dict().items() if v is not None}
    if len(service) >= 1:
        updated_service = request.app.database["Services"].update_one(
            {"_id": object_id}, {"$set": service}
        )

    return updated_service


@services_route.delete(
    "/services/{object_id}",
    response_description="Delete a service",
    response_model=ServicesUpdate,
)
def delete_service(request: Request, object_id: str):
    """_summary_

    Args:
        request (Request): _description_
        service (services, optional): _description_. Defaults to Body(...).

    Returns:
        _type_: _description_
    """
    delete_result = request.app.database["Services"].delete_one({"_id": object_id})

    if delete_result.deleted_count == 1:
        print(delete_result)
        return delete_result

    raise HTTPException(status_code=404, detail=f"Service {object_id} not found")
