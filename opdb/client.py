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

    def _public_get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
