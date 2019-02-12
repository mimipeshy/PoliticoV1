import json
import unittest
from app.api.routes.models.political import parties
from app.tests.base_test import RoutesBaseTest


class PoliticalTests(RoutesBaseTest):
    """Tests functionality of the political endpoint"""

    def test_create_party(self):
        """Test API can create a party"""
        response = self.client().post('/api/v1/party', data=self.add_party,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode())
        self.assertTrue(data['Status'] == 201)
        self.assertTrue(data['Data'] == parties)

    def test_get_all_parties(self):
        """Tests API can get all parties"""
        self.client().post('/api/v1/party', data=self.add_party,
                           content_type='application/json')
        response = self.client().get('/api/v1/party',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertTrue(data['Status'] == 200)
        self.assertTrue(data['Data']== parties)

    def test_get_specific_by_id(self):
        """Tests API can get a specific party by using its id"""
        self.client().post('/api/v1/party', data=self.add_party,
                           content_type='application/json')
        response = self.client().get('/api/v1/party/1',
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertTrue(data['Status'] == 200)

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
        response = self.client().patch('/api/v1/party/1/name', data=self.update_party,
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 200)

    def test_political_update_forbidden(self):
        response = self.client().patch('/api/v1/party/56/name', data=self.update_party,
                                       content_type='application/json',
                                       )
        self.assertEqual(response.status_code, 404)

    def test_delete_party_by_id(self):
        """Tests API can delete one by using its id"""

        response = self.client().delete('/api/v1/party/1',
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 200)

    def test_delete_non_existing_party(self):
        response = self.client().delete('/api/v1/party/4',
                                        content_type='application/json',
                                        )
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()
