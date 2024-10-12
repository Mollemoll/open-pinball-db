import unittest
import opdb

class TestClient(unittest.TestCase):
    def test_initialization(self):
        self.client = opdb.Client()
        self.assertEqual(self.client.base_url, "https://opdb.org/api")
        self.assertEqual(
            self.client.headers,
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "python opdb client"
            })
