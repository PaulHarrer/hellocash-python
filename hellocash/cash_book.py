class CashBook:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        endpoint = "v1/cashBook"
        return self.client._request("POST", endpoint, data)

    def list(self, limit=1000, offset=1, date_from=None, date_to=None, mode=None):
        endpoint = "v1/cashBook"
        params = {
            "limit": limit,
            "offset": offset,
            "dateFrom": date_from,
            "dateTo": date_to,
            "mode": mode
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response

    def saldo(self, mode=None):
        endpoint = f"v1/cashBook/saldo"
        params = {
            "mode": mode
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response
