import json
import unittest

from app.tests.base_test import RoutesBaseTest


class ValidationTests(RoutesBaseTest):
    def test_empty_strings(self):
        """Tests API can get all offices"""

        response = self.client().post('/api/v1/party', data=self.empty_party_name,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client().post('/api/v1/party', data=self.empty_location,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client().post('/api/v1/party', data=self.empty_description,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()