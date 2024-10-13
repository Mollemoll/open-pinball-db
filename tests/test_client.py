""" Tests for the opdb.Client class. """

import unittest
import json
import requests
import responses
import opdb

class TestClient(unittest.TestCase):
    """ Test the opdb.Client class """

    def test_initialization(self):
        """ Test the initialization of the client """
        client = opdb.Client()
        self.assertEqual(client.base_url, "https://opdb.org/api")
        self.assertEqual(
            client.headers,
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "python opdb client"
            })

    def test_initialization_with_api_key(self):
        """ Test the initialization of the client with an api key"""
        client = opdb.Client(api_key="my-secret-api-key")
        self.assertEqual(client.base_url, "https://opdb.org/api")
        self.assertEqual(
            client.headers,
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "python opdb client",
                "Authorization": "Bearer my-secret-api-key"
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

        client = opdb.Client()
        self.assertEqual(
            client.get_changelog(),
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

        client = opdb.Client()
        with self.assertRaises(requests.exceptions.Timeout):
            client.get_changelog()

    @responses.activate
    def test_typeahead_search(self):
        """ Test the typeahead search method """
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

        client = opdb.Client()
        self.assertEqual(
            client.typeahead_search("Metallica"),
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

    @responses.activate
    def test_typeahead_search_with_groups(self):
        """ Test the typeahead search method with groups """
        responses.add(responses.GET,
                      'https://opdb.org/api/search/typeahead?q=Metallica&include_groups=1',
                      json=[{"id": "GRBE4",
                             "text": "Metallica",
                             "name": "Metallica"},
                            {"id": "GRBE4-MOE4l",
                             "text": "Metallica (LE) (Stern, 2012)",
                             "name": "Metallica (LE)",
                             "supplementary": "Stern, 2012",
                             "display": "dmd"},
                            ],
                      status=200)

        client = opdb.Client()
        self.assertEqual(
            client.typeahead_search("Metallica", include_groups=True),
            [
                {
                    "id": "GRBE4",
                    "text": "Metallica",
                    "name": "Metallica"
                },
                {
                    "id": "GRBE4-MOE4l",
                    "text": "Metallica (LE) (Stern, 2012)",
                    "name": "Metallica (LE)",
                    "supplementary": "Stern, 2012",
                    "display": "dmd"
                },
            ],
        )

    @responses.activate
    def test_typeahead_search_without_aliases(self):
        """ Test the typeahead search method without aliases """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search/typeahead?q=Metallica&include_aliases=0',
            json=[
                {
                    "id": "GRBE4-MOE4l",
                    "text": "Metallica (LE) (Stern, 2012)",
                    "name": "Metallica (LE)",
                    "supplementary": "Stern, 2012",
                    "display": "dmd"},
            ],
            status=200)

        client = opdb.Client()
        self.assertEqual(
            client.typeahead_search("Metallica", include_aliases=False),
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

    @responses.activate
    def test_search(self):
        """ Test the search method """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search?q=Metallica',
            json=[],
            status=200)

        client = opdb.Client()
        client.search("Metallica")
        self.assertEqual(responses.calls[-1].response.status_code, 200)

    @responses.activate
    def test_search_with_require_opdb(self):
        """ Test the search method """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search?q=Metallica&require_opdb=0',
            json=[],
            status=200)

        client = opdb.Client()
        client.search("Metallica", require_opdb = False)
        self.assertEqual(responses.calls[-1].response.status_code, 200)

    @responses.activate
    def test_search_without_aliases(self):
        """ Test the search method """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search?q=Metallica&include_aliases=0',
            json=[],
            status=200)

        client = opdb.Client()
        client.search("Metallica", include_aliases = False)
        self.assertEqual(responses.calls[-1].response.status_code, 200)

    @responses.activate
    def test_search_with_groups(self):
        """ Test the search method """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search?q=Metallica&include_groups=1',
            json=[],
            status=200)

        client = opdb.Client()
        client.search("Metallica", include_groups = True)
        self.assertEqual(responses.calls[-1].response.status_code, 200)

    @responses.activate
    def test_search_with_grouping_entries(self):
        """ Test the search method """
        responses.add(
            responses.GET,
            'https://opdb.org/api/search?q=Metallica&include_grouping_entries=1',
            json=[],
            status=200)

        client = opdb.Client()
        client.search("Metallica", include_grouping_entries = True)
        self.assertEqual(responses.calls[-1].response.status_code, 200)

    @responses.activate
    def test_get_machine_by_ipdb_id(self):
        """ Test the get_machine_by_ipdb_id method """
        with open('tests/fixtures/machine.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        responses.add(
            responses.GET,
            'https://opdb.org/api/machines/ipdb/6028',
            json=data,
            status=200,
        )

        client = opdb.Client()
        response = client.get_machine_by_ipdb_id(6028)
        self.assertEqual(responses.calls[-1].response.status_code, 200)
        self.assertEqual(response["ipdb_id"], 6028)

    @responses.activate
    def test_get_machine(self):
        """ Test the get_machine method """
        with open('tests/fixtures/machine.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        responses.add(
            responses.GET,
            'https://opdb.org/api/machines/GRBE4-MQK1Z',
            json=data,
            status=200,
        )

        client = opdb.Client()
        response = client.get_machine("GRBE4-MQK1Z")
        self.assertEqual(responses.calls[-1].response.status_code, 200)
        self.assertEqual(response["opdb_id"], "GRBE4-MQK1Z")
