import json
import unittest

from app.tests.base_test import RoutesBaseTest


class PoliticalOfficeTests(RoutesBaseTest):
    """Tests functionality of the political office endpoint"""
    def test_create_an_office(self):
        response = self.client().post('/api/v1/office', data=self.add_office,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)