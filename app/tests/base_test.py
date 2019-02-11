import json

from app.api.app import create_app
import unittest


class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        # tear down tests

        self.add_party = json.dumps({
            "party_name": "maendeleo",
            "logoUrl": "https://www.vnfojo.com/juj"

        })
        self.update_party = json.dumps({
            "party_name": "chama cha maendeleo",
            "logoUrl": "https://www.vnfojo.com/juj"
        })
        self.empty_party_name = json.dumps({
            "party_name": " ",
            "logoUrl":"https://www.vnfojo.com/juj"
        })
        self.empty_logoUrl = json.dumps({
            "party_name": "wazee united",
            "logoUrl": " "

        })
        self.add_office = json.dumps({
            "office_name": "governnemt",
            "type": "senate"
        })

    def tearDown(self):
        """Teardown tests"""
        self.app.testing = False