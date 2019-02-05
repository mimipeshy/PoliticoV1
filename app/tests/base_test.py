import json

from app.api.app import create_app
import unittest


class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    # tear down tests

        self.add_party = json.dumps({
            "party_name": "sugar",
            "location": "kinoo",
            "description": "thiijo"
        })
    def tearDown(self):
        """Teardown tests"""
        self.app.testing = False