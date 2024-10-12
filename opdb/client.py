import requests

class Client:
    def __init__(self, api_key: str = None):
        self.base_url = "https://opdb.org/api"
        self.__api_key = api_key
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "python opdb client"
        }
        if self.__api_key:
            self.headers["Authorization"] = f"Bearer {self.__api_key}"

    def get_changelog(self):
        return self._get(endpoint="changelog")

    def typeahead_search(self, q: str, include_aliases: bool = True, include_groups: bool = False):
        params = { "q": q }
        if include_aliases is False:
            params["include_aliases"] = "0"
        if include_groups is True:
            params["include_groups"] = "1"

        return self._get(
            endpoint="search/typeahead",
            params=params,
        )

    def get_machine_by_ipdb_id(self, ipdb_id: int):
        return self._get(endpoint=f"machines/ipdb/{ipdb_id}")

    def _get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()