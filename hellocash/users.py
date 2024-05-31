class Users:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        endpoint = "v1/users"
        return self.client._request("POST", endpoint, data)

    def get(self, user_id):
        endpoint = f"v1/users/{user_id}"
        return self.client._request("GET", endpoint)

    # https://api.hellocash.business/api/v1/users?limit=250&offset=1
    def list(self, limit=250, offset=1):
        endpoint = "v1/users"
        params = {
            "limit": limit,
            "offset": offset
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response

    def update(self, user_id, data):
        endpoint = f"v1/users/{user_id}"
        return self.client._request("POST", endpoint, data)
