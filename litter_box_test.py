"""Test for litter_box"""
import unittest

from flask import Flask
from litter_box import app

class TestAppRoutes(unittest.TestCase):
    """Testing all controllers"""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_healthz(self):
        """Testing healthz endpoint"""
        response = self.app.get('/healthz')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("message"), "OK")

if __name__ == '__main__':
    unittest.main()
