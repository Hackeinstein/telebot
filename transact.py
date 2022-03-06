import requests
import json

class Transact:
    def __init__(self,chat_id,price,type) :
        self.user=chat_id
        self.price=price
        self.type=type
        url = f"https://api.sandbox.nowpayments.io/v1/estimate?amount={self.price}.5000&currency_from=usd&currency_to=btc"
        payload={}
        headers = {
        'x-api-key': 'FCJYVV9-QTG4KY6-P3AR9T9-F50HKFE'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        jsonreq=response.json()
        self.btc=jsonreq["estimated_amount"]
    def pay (self):
        url = "https://api.sandbox.nowpayments.io/v1/payment"
        payload = json.dumps({
            "price_amount": f"{self.price}",
            "price_currency": "usd",
            "pay_amount": f"{self.btc}",
            "pay_currency": "btc",
        })
        headers = {
             'x-api-key': 'FCJYVV9-QTG4KY6-P3AR9T9-F50HKFE',
             'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        self.invoice_id=response.json()['payment_id']
        self.pay_stats=response.json()['payment_status']
    def get_id(self):
            return self.invoice_id
    def status (self):
        url = f"https://api.sandbox.nowpayments.io/v1/payment/{self.invoice_id}"

        payload={}
        headers = {
             'x-api-key': 'FCJYVV9-QTG4KY6-P3AR9T9-F50HKFE'
            }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()['payment_status']

    
