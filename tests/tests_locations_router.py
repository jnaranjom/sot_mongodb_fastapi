import unittest
from unittest.mock import MagicMock
from fastapi import Request
import sys

sys.path.insert(0, "/home/netadmin/sot_mongodb_fastapi")
from server.routes.locations import list_locations


class TestListlocations(unittest.TestCase):
    def setUp(self):
        self.request = MagicMock(spec=Request)
        self.request.app.database = {"Locations": MagicMock()}

    def test_list_locations(self):
        # Mock the database find method
        mock_locations = [{"name": "Location1"}, {"name": "Location2"}]
        self.request.app.database["Locations"].find.return_value = mock_locations

        # Call the function
        response = list_locations(self.request)

        # Assertions
        self.request.app.database["Locations"].find.assert_called_once_with(limit=200)
        self.assertEqual(response, mock_locations)


if __name__ == "__main__":
    unittest.main()
