import json
import unittest

from app.tests.base_test import RoutesBaseTest


class PoliticalTests(RoutesBaseTest):
    """Tests functionality of the political endpoint"""

    def test_create_party(self):
        """Test API can create a product"""
        response = self.client().post('/api/v1/party', data=self.add_party,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_parties(self):
        """Tests API can get all parties"""
        parties = {"parties": "parties"}
        response = self.client().get('/api/v1/party', data=parties,
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_by_id(self):
        """Tests API can get a specific party by using its id"""
        self.client().post('/api/v1/party', data=self.add_party,
                           content_type='application/json')
        response = self.client().get('/api/v1/party/1',
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 200)

    def test_get_wrong_political_party(self):
        self.client().post('/api/v1/party', data=self.add_party,
                           content_type='application/json')
        response = self.client().get('/api/v1/party/10',
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 404)

    def test_political_update_successfully(self):
        self.client().post('/api/v1/party', data=self.add_party,
                           content_type='application/json')
        response = self.client().put('/api/v1/party/1', data=self.update_office,
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 200)

        response = self.client().put('/api/v1/party/6', data=self.update_office,
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
