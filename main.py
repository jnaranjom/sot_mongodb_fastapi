""" FASTAPI with MongoDB APP for Network Automation
"""
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router

config = dotenv_values(".env")

app = FastAPI()


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


app.include_router(router, tags=["SoT Operations"], prefix="/api")
