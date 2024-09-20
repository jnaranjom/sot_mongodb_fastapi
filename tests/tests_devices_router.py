import unittest
from unittest.mock import MagicMock
from fastapi import Request
import sys

sys.path.insert(0, "/home/netadmin/sot_mongodb_fastapi")
from server.routes.devices import list_devices


class TestListDevices(unittest.TestCase):
    def setUp(self):
        self.request = MagicMock(spec=Request)
        self.request.app.database = {"Devices": MagicMock()}

    def test_list_devices(self):
        # Mock the database find method
        mock_devices = [{"name": "Device1"}, {"name": "Device2"}]
        self.request.app.database["Devices"].find.return_value = mock_devices

        # Call the function
        response = list_devices(self.request)

        # Assertions
        self.request.app.database["Devices"].find.assert_called_once_with(limit=200)
        self.assertEqual(response, mock_devices)


if __name__ == "__main__":
    unittest.main()
