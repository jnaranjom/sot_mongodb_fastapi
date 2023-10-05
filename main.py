""" FASTAPI with MongoDB APP for Network Automation
"""
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from server.routes.locations import locations_route
from server.routes.devices import devices_route
from server.routes.fabrics import fabrics_route
from server.routes.acls import acls_route
from server.routes.services import services_route
from server.routes.protocols import protocols_route
from server.routes.interfaces import interfaces_route


config = dotenv_values(".env")

app = FastAPI()

app.include_router(locations_route, tags=["Locations"], prefix="/api")
app.include_router(devices_route, tags=["Devices"], prefix="/api")
app.include_router(fabrics_route, tags=["Fabrics"], prefix="/api")
app.include_router(acls_route, tags=["ACLs"], prefix="/api")
app.include_router(services_route, tags=["Services"], prefix="/api")
app.include_router(protocols_route, tags=["Protocols"], prefix="/api")
app.include_router(interfaces_route, tags=["Interfaces"], prefix="/api")


@app.on_event("startup")
def startup_db_client():
    """_summary_"""
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("\n Connected to the MongoDB database! \n")


@app.on_event("shutdown")
def shutdown_db_client():
    """_summary_"""
    app.mongodb_client.close()
