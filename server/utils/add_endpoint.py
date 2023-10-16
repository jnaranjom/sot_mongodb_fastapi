"""
    Function to add new endpoints to FastAPI
"""
from jinja2 import Environment, FileSystemLoader
import sys
import json


def create_endpoint_routes(endpoint, endpoint_model):
    """ """
    with open("../routes/" + endpoint + ".py", "w") as endpoint_file:
        template = env.get_template("routes.j2")
        output = template.render(endpoint=endpoint, endpoint_model=endpoint_model)
        endpoint_file.write(output)


def create_endpoint_models(endpoint, endpoint_model):
    """ """
    with open("../models/" + endpoint + ".py", "w") as endpoint_file:
        template = env.get_template("models.j2")
        output = template.render(endpoint=endpoint, endpoint_model=endpoint_model)
        endpoint_file.write(output)


if __name__ == "__main__":

    endpoint = sys.argv[1]
    model_filename = sys.argv[2]
    with open("build_models/" + model_filename, "r") as model_file:
        model = model_file.read()
        endpoint_model = json.loads(model)

    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)
    create_endpoint_routes(endpoint, endpoint_model)
    create_endpoint_models(endpoint, endpoint_model)
