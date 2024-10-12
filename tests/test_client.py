import unittest
import opdb

class TestClient(unittest.TestCase):
    def test_initialization(self):
        self.client = opdb.Client(api_key="secret_key")
        self.assertEqual(self.client.api_key, "secret_key")
        self.assertEqual(self.client.base_url, "https://opdb.org/api")
