class Employees:
    def __init__(self, client):
        self.client = client

    def get(self, employee_id):
        endpoint = f"v1/employees/{employee_id}"
        return self.client._request("GET", endpoint)

    def list(self):
        endpoint = "v1/employees"
        return self.client._request("GET", endpoint)
