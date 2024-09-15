"""
    Class to convert MongoDB object DI from BSON to a JSON string
"""

from bson.objectid import ObjectId
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic_core import CoreSchema, core_schema


class PyObjectId(ObjectId):  # pylint: disable=too-few-public-methods
    """ """

    @classmethod
    def __get_validators__(cls):
        """ """
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """ """
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    # @classmethod
    # def __get_pydantic_json_schema__(cls, schema: CoreSchema, handler: GetJsonSchemaHandler):
    #     """ """
    #     CoreSchema.update(type="string")
