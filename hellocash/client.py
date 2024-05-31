import requests
from .articles import Articles
from .cash_book import CashBook
from .employees import Employees
from .invoices import Invoices
from .payment_methods import PaymentMethods
from .services import Services
from .users import Users


class HelloCashClient:
    BASE_URL = "https://api.hellocash.business/api/"

    def __init__(self, api_token):
        self.api_token = api_token
        self.articles = Articles(self)
        self.cash_book = CashBook(self)
        self.employees = Employees(self)
        self.invoices = Invoices(self)
        self.payment_methods = PaymentMethods(self)
        self.services = Services(self)
        self.users = Users(self)

    def _request(self, method, endpoint, data=None, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        response = requests.request(method, url, headers=headers, json=data, params=params)
        response.raise_for_status()
        return response.json()
