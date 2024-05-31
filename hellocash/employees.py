class Employees:
    def __init__(self, client):
        self.client = client

    def list(self):
        endpoint = "v1/employees"
        return self.client._request("GET", endpoint)
