# Network Source of Truth using MongoDB and Fast API

## Overview

The following package is intended the demostrate the use of MongoDB along with FastAPI to deploy a Network Source of Truth for Network Automation. There are tools available to perform this function, but the goal of the package is to help engineers understand concepts in regards to Network Source of Truth (i.e. Data Models/Version Control) while learning how to use FastAPI for this use case.

Once the package is deployed on the testing network, it is possible to interact with the DataBase via with any API request method (Python/Ansible/Postman) to perform CRUD operations and integrate with configuration management tools to deploy intended configurations on Network devices.

## Components

### Database - MongoDB

MongoDB is document oriented NonSQL database that can store structured, semi-structured and ustructured data in documents instead of tables. It integrates easily with development tools. For this particular use case provides and easy method to create network intended data models that can be retrieved for network automation.

Additional details for [MongoDB.](https://www.mongodb.com/docs/)

This package uses the free version of the MongoDB cloud service Atlas.

### FrontEnd - FastAPI

FastAPI is a Web Framework for building RESTful APIs developed in Python that integrates easily with MongoDB. Using the API allows access to the Database (Network Source of Truth) using configuration management tools like Ansible which then can deploy configuration to devices.

See the documentation for [FastAPI](https://fastapi.tiangolo.com/)

### Data Models

The most relevant component on this solution are the data models. The models are the representation of the network elements and configuration objects. Since MongoDB provides the functionality to store the Data Models, these can be retrieved in JSON format and injected directly into the automation tools for deployment on network devices. See some additional details abotu data models:

- https://www.educative.io/answers/what-are-data-models-in-network-automation
- https://blog.networktocode.com/post/data-modeling-for-network-engineers/
- https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9500/software/release/16-5/configuration_guide/prog/b_165_prog_9500_cg/data_models.pdf

The current basic data models used for this package are stored [here.](data_models/)

#### Data model considerations

1. Defining a proper set of data models that cover most of the use cases is key to develop a solution that can be extensible, reusable and easy to maintain.
2. The data models desgined should match the corresponding model defined in the FastAPI application (within the server/models files) so the CRUD operations against the Network SoT can be executed.
3. The FastAPI BaseModel Class provide the method for the CRUD operations, the data model created for the objects (in MongoDB) or from the Network Infrastructure must be defined within the Classes so FastAPI can the perform the required operations.

## Deploying the application

### Create MongoDB Cloud Atlas Account

 - Create MongoDB Atlas account
 - Create Test DB (network_inventory) in MongoDB Atlas:
    - Create user and resource permissions
    - Retrieve MongoDB connection link and credentials

### Server deployment

 - Create Python venv
    - Update the virtual environment via pip
 - Install requirements
    - pip install -r requirements.txt
 - Create .env file with the DB connection link secrects as documented here:

    ```shell
        ATLAS_URI=mongodb+srv://username:password@cluster0.gguf6wf.mongodb.net/?retryWrites=true&w=majority
        DB_NAME=network_inventory
    ```
    *Update the URL as provided by the Cloud Atlas tool*
    - Install MongoDB Compass on a separate machine to have visualization of the Database

## Running the APP
 - Clone this repo
    - git clone git@github.com:jnaranjom/sot_mongodb_fastapi.git
    - cd sot_mongodb_fastapi

 - Enable venv:
    - source venv/bin/activate

 - Start the application: `python -m uvicorn main:app --host <your-server-ip> --reload``

## Validate Access to the API

 - Open a browser and go to http://<your-server-ip>:8000/docs to see the API documentation
 - Go to http://<your-server-ip>:8000/api/devices to see the list of devices
