import json

from app.api.app import create_app
import unittest


class RoutesBaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        # tear down tests

        self.add_party = json.dumps({
            "name": "maendeleo",
            "hqAddress":"kilimani",
            "logoUrl": "http://facebook.com/pic.jpg"

        })
        self.update_party = json.dumps({
            "name": "chama cha maendeleo"
        })
        self.empty_party_name = json.dumps({
            "name": "",
            "hqAddress":"koko",
            "logoUrl": "http://facebook.com/pic.jpg"
        })
        self.empty_logoUrl = json.dumps({
            "name": "wazee united",
            "hqAddress":"kokoo",
            "logoUrl": " "

        })
        self.empty_hqAddress = json.dumps({
            "name": "wazee united",
            "hqAddress": "",
            "logoUrl": "http://facebook.com/pic.jpg "

        })
        self.add_office = json.dumps({
            "name": "governnemt",
            "type": "senate"
        })

    def tearDown(self):
        """Teardown tests"""
        self.app.testing = False
