""" FASTAPI with MongoDB APP for Network Automation
"""

from fastapi import FastAPI
from pymongo import MongoClient
from server.routes.locations import locations_route
from server.routes.devices import devices_route

app = FastAPI()

app.include_router(locations_route, tags=["Locations"], prefix="/api/v1")
app.include_router(devices_route, tags=["Devices"], prefix="/api/v1")


@app.on_event("startup")
def startup_db_client():
    """_summary_"""
    app.mongodb_client = MongoClient(
        "mongodb+srv://net_auto_admin:net_auto_admin@cluster0.gguf6wf.mongodb.net/"
    )
    app.database = app.mongodb_client["inventory"]
    print("\n Connected to the MongoDB database! \n")


@app.on_event("shutdown")
def shutdown_db_client():
    """_summary_"""
    app.mongodb_client.close()
