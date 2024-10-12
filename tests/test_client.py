import unittest
import requests
import responses
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

    @responses.activate
    def test_get_changelog(self):
        """ Get the changelog from the public API """
        responses.add(
            responses.GET,
            'https://opdb.org/api/changelog',
            json=[
                {
                    "changelog_id": 1,
                    "opdb_id_deleted": "GrdNZ-MQo1e",
                    "action": "move",
                    "opdb_id_replacement": "GRveZ-MNE38",
                    "created_at": "2018-10-19T15:06:20.000000Z",
                    "updated_at": "2018-10-19T15:06:20.000000Z"
                },
            ],
            status=200
        )

        self.client = opdb.Client()
        self.assertEqual(
            self.client.get_changelog(),
            [
                {
                    "changelog_id": 1,
                    "opdb_id_deleted": "GrdNZ-MQo1e",
                    "action": "move",
                    "opdb_id_replacement": "GRveZ-MNE38",
                    "created_at": "2018-10-19T15:06:20.000000Z",
                    "updated_at": "2018-10-19T15:06:20.000000Z"
                },
            ]
        )

    @responses.activate
    def test_get_changelog_timeout(self):
        """ Simulate a timeout when getting the changelog from the public API """
        responses.add(
            responses.GET,
            'https://opdb.org/api/changelog',
            body=requests.exceptions.Timeout()
        )

        self.client = opdb.Client()
        with self.assertRaises(requests.exceptions.Timeout):
            self.client.get_changelog()

    @responses.activate
    def test_typeahead_search(self):
        responses.add(
            responses.GET,
            'https://opdb.org/api/search/typeahead?q=Metallica',
            json=[
                {
                    "id": "GRBE4-MOE4l",
                    "text": "Metallica (LE) (Stern, 2012)",
                    "name": "Metallica (LE)",
                    "supplementary": "Stern, 2012",
                    "display": "dmd"
                },
            ],
            status=200
        )

        self.client = opdb.Client()
        self.assertEqual(
            self.client.typeahead_search("Metallica"),
            [
                {
                    "id": "GRBE4-MOE4l",
                    "text": "Metallica (LE) (Stern, 2012)",
                    "name": "Metallica (LE)",
                    "supplementary": "Stern, 2012",
                    "display": "dmd"
                },
            ],
        )

