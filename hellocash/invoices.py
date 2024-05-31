class Invoices:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        endpoint = "v1/invoices"
        return self.client._request("POST", endpoint, data)
