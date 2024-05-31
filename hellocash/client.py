import requests
from .employees import Employees
from .invoices import Invoices


class HelloCashClient:
    BASE_URL = "https://api.hellocash.business/api/"

    def __init__(self, api_token):
        self.api_token = api_token
        self.employees = Employees(self)
        self.invoices = Invoices(self)

    def _request(self, method, endpoint, data=None, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        response = requests.request(method, url, headers=headers, json=data, params=params)
        response.raise_for_status()
        return response.json()
