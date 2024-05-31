class Services:
    def __init__(self, client):
        self.client = client

    def list(self, limit=250, offset=1, caid=None):
        endpoint = "v1/services"
        params = {
            "limit": limit,
            "offset": offset,
            "caid": caid
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response

    def get(self, service_id):
        endpoint = f"v1/services/{service_id}"
        return self.client._request("GET", endpoint)
