""" Open Pinball DB Client """

import requests
from .exceptions import OpdbMissingApiKey, OpdbHTTPError, OpdbTimeoutError

class Client:
    """ The Opdb Client """

    def __init__(self, api_key: str = None):
        self.base_url = "https://opdb.org/api"
        self.__api_key = api_key
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "python open-pinball-db client"
        }
        if self.__api_key:
            self.headers["Authorization"] = f"Bearer {self.__api_key}"

    def get_changelog(self):
        """ Get changelog """
        return self._get(endpoint="changelog")

    def typeahead_search(
            self,
            q: str,
            include_aliases: bool = True,
            include_groups: bool = False):
        """ Typeahead search """
        params = {"q": q}
        if include_aliases is False:
            params["include_aliases"] = "0"
        if include_groups is True:
            params["include_groups"] = "1"

        return self._get(
            endpoint="search/typeahead",
            params=params,
        )

    # pylint: disable=R0913,R0917
    def search(
            self,
            q: str,
            require_opdb: bool = True,
            include_aliases: bool = True,
            include_groups: bool = False,
            include_grouping_entries: bool = False):
        """ Search """
        self._ensure_api_key()
        params = {"q": q}
        if require_opdb is False:
            params["require_opdb"] = "0"
        if include_aliases is False:
            params["include_aliases"] = "0"
        if include_groups is True:
            params["include_groups"] = "1"
        if include_grouping_entries is True:
            params["include_grouping_entries"] = "1"

        return self._get(
            endpoint="search",
            params=params,
        )

    def get_machine(self, opdb_id: str):
        """ Get Machine by Opdb id (requires api key) """
        self._ensure_api_key()
        return self._get(endpoint=f"machines/{opdb_id}")

    def get_machine_by_ipdb_id(self, ipdb_id: int):
        """ Get Machine by Ipdb id (requires api key) """
        self._ensure_api_key()
        return self._get(endpoint=f"machines/ipdb/{ipdb_id}")

    def export_machines_and_aliases(self):
        """
            Export all machines and aliases into one json document (requires api key)
            According to the OPDB API docs this endpoint is rate limited to once every hour
        """
        self._ensure_api_key()
        return self._get(endpoint="export",timeout=30)

    def export_machine_groups(self):
        """ Export all machines groups into one json document (requires api key) """
        self._ensure_api_key()
        return self._get(endpoint="export/groups",timeout=30)

    def _get(self, endpoint: str, params: dict = None, timeout: int = 10):
        """ get request helper """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise OpdbHTTPError(response.status_code, response.text) from http_err
        except requests.exceptions.Timeout as timeout_err:
            raise OpdbTimeoutError() from timeout_err
        return response.json()

    def _ensure_api_key(self):
        """Ensure that the API key is present."""
        if not self.__api_key:
            raise OpdbMissingApiKey("API key is missing")
