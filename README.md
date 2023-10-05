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

The current basic data models used for this package are stored [here](data_models/)

## Deployment

 - Create venv
 - Install requirements
 - Create .env file with secrects
 - Create MongoDB Atlas account
 - Create Test DB in MongoDB Atlas:
    - Create user and resource permissions
    - Retrieve MongoDB connection link

## Running the APP
 - Enable venv
 - Start the application: `python -m uvicorn main:app --reload`
