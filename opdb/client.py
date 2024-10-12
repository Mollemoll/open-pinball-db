import requests

class Client:
    def __init__(self):
        self.base_url = "https://opdb.org/api"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "python opdb client"
        }

    def get_changelog(self):
        return self._public_get(endpoint="changelog")

    def typeahead_search(self, q: str, include_aliases: bool = True, include_groups: bool = False):
        params = { "q": q }
        if include_aliases is False:
            params["include_aliases"] = "0"
        if include_groups is True:
            params["include_groups"] = "1"

        return self._public_get(
            endpoint="search/typeahead",
            params=params,
        )

    def _public_get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
