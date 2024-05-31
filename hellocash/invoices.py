class Invoices:
    def __init__(self, client):
        self.client = client

    def cancel(self, invoice_id):
        endpoint = f"v1/invoices/{invoice_id}/cancellation"
        return self.client._request("POST", endpoint)

    def create(self, data):
        endpoint = "v1/invoices"
        return self.client._request("POST", endpoint, data)

    def list(self, limit=1000, offset=1, search=None, date_from=None, date_to=None, mode=None, show_details=None):
        endpoint = "v1/invoices"
        params = {
            "limit": limit,
            "offset": offset,
            "search": search,
            "dateFrom": date_from,
            "dateTo": date_to,
            "mode": mode,
            "showDetails": show_details
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response

    def get(self, invoice_id):
        endpoint = f"v1/invoices/{invoice_id}"
        return self.client._request("GET", endpoint)

    def get_pdf(self, invoice_id, cancellation=False, locale="en_GB"):
        endpoint = f"v1/invoices/{invoice_id}/pdf"
        params = {
            "cancellation": cancellation,
            "locale": locale
        }
        params = {k: v for k, v in params.items() if v}
        response = self.client._request("GET", endpoint, params=params)
        return response
