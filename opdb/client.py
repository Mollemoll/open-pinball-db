class Client:
    def __init__(self):
        self.base_url = "https://opdb.org/api"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "python opdb client"
        }
