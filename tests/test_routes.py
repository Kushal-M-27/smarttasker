import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_health(self):
        res = self.app.get('/health')
        self.assertEqual(res.status_code, 200)
