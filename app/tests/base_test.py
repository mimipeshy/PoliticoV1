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
        self.update_office = json.dumps({
            "party_name": "chama cha maendeleo",
            "location": "kinoo",
            "description": "ni ya madem"
        })
    def tearDown(self):
        """Teardown tests"""
        self.app.testing = False