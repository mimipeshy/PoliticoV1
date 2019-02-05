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


if __name__ == '__main__':
    unittest.main()
