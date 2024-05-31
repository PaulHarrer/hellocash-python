class Articles:
    def __init__(self, client):
        self.client = client

    def categories(self):
        endpoint = "v1/articles/categories"
        return self.client._request("GET", endpoint)

    def change_stock(self, article_id, data):
        endpoint = f"v1/articles/{article_id}/change-stock"
        return self.client._request("POST", endpoint, data)

    def create_or_update(self, data):
        endpoint = "v1/articles"
        return self.client._request("POST", endpoint, data)

    def get(self, article_id):
        endpoint = f"v1/articles/{article_id}"
        return self.client._request("GET", endpoint)

    def list(self, limit=250, offset=1, caid=None):
        endpoint = "v1/articles"
        params = {
            "limit": limit,
            "offset": offset,
            "caid": caid
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response

    def stock_changes(self, article_id):
        endpoint = f"v1/articles/{article_id}/stock-changes"
        return self.client._request("GET", endpoint)
