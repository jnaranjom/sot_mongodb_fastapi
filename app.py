""" FASTAPI with MongoDB APP for Network Automation

This application is built using FastAPI and integrates with MongoDB to provide
network automation functionalities. It includes routes for managing locations
and devices within a network inventory.

Modules:
    - fastapi: The FastAPI framework for building the web application.
    - pymongo: The PyMongo library for interacting with MongoDB.
    - server.routes.locations: Module containing the routes for location management.
    - server.routes.devices: Module containing the routes for device management.

Attributes:
    app (FastAPI): The FastAPI application instance.

Routes:
    - /api/v1/locations: Endpoints for managing locations.
    - /api/v1/devices: Endpoints for managing devices.

Events:
    - startup: Initializes the MongoDB client and connects to the specified database.
    - shutdown: Closes the MongoDB client connection.

Functions:
    - startup_db_client: Initializes the MongoDB client and connects to the 'inventory' database.
    - shutdown_db_client: Closes the MongoDB client connection.

Usage:
    Run the application using `uvicorn app:app --reload` to start the FastAPI server.
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
    """
    Initializes the MongoDB client and connects to the specified database.

    This function sets up the MongoDB client using the connection string provided
    and assigns the 'inventory' database to the app's database attribute. It also
    prints a confirmation message upon successful connection.

    Raises:
        pymongo.errors.ConnectionError: If the connection to MongoDB fails.
    """

    app.mongodb_client = MongoClient(
        "mongodb+srv://net_auto_admin:net_auto_admin@cluster0.gguf6wf.mongodb.net/"
    )
    app.database = app.mongodb_client["inventory"]
    print("\n Connected to the MongoDB database! \n")


@app.on_event("shutdown")
def shutdown_db_client():
    """
    Closes the MongoDB client connection.

    This function is intended to be called during the shutdown process
    to ensure that the MongoDB client connection is properly closed.
    """
    app.mongodb_client.close()
