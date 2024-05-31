class PaymentMethods:
    def __init__(self, client):
        self.client = client

    def get(self, payment_method_id):
        endpoint = f"v1/paymentMethods/{payment_method_id}"
        return self.client._request("GET", endpoint)

    def list(self):
        endpoint = "v1/paymentMethods"
        return self.client._request("GET", endpoint)
