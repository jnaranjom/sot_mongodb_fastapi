from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models import locations, devices

router = APIRouter()


@router.get(
    "/locations",
    response_description="List all locations",
    response_model=List[locations],
)
def list_locations(request: Request):
    locations_list = list(request.app.database["locations"].find(limit=100))
    return locations_list


@router.get(
    "/devices", response_description="List all devices", response_model=List[devices]
)
def list_devices(request: Request):
    devices_list = list(request.app.database["devices"].find(limit=100))
    return devices_list
