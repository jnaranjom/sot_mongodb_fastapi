""" FASTAPI with MongoDB APP for Network Automation
"""
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router
from server.routes.locations import locations_route
from server.routes.devices import devices_route

config = dotenv_values(".env")

app = FastAPI()

app.include_router(locations_route, tags=["Locations"], prefix="/api")
app.include_router(devices_route, tags=["Devices"], prefix="/api/devices")
# app.include_router(router, tags=["SoT Operations"], prefix="/api")


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
