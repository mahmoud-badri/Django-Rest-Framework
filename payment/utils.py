import requests

merchant_id = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2T1RZM09EUTNMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuODhLWUVKZnV3UFVoMElKVEY4a2FLUTRNMXF6MFRobHhLaG1ILVBlckljYmRxaEpRUUdTQm5lelJGN09ZTkUwM3hhLWVnOTlNZDF4Z2hjTDJRYUIzOXc="

def get_payment_token(merchant_id):
    headers = {"accept": "application/json", "content-type": "application/json"}
    body = {"api_key": merchant_id}
    response = requests.post(url=paymob_urls["authentication"], json=body)
    return response.json().get("token")


def get_order_id(amount):
    token = get_payment_token(merchant_id)
    body = {
        "auth_token": token,
        "delivery_needed": "false",
        "amount_cents": amount * 100,
        "currency": "EGP",
        "items": [],
    }
    response = requests.post(url=paymob_urls["get_order_id"], json=body).json()
    print("data", response.get("id"))
    return response.get("id")


def payment_key_request(user, amount):
    token = get_payment_token(merchant_id)
    order_id = get_order_id(amount)
    body = {
        "auth_token": token,
        "amount_cents": amount * 100,
        "expiration": 3600,
        "order_id": order_id,
        "billing_data": {
            "apartment": "NA",
            "email": str(user.email),
            "floor": "NA",
            "first_name": user.name,
            "street": "NA",
            "building": "NA",
            "phone_number": "20112345678",
            "shipping_method": "NA",
            "postal_code": "NA",
            "city": "NA",
            "country": "NA",
            "last_name": user.name,
            "state": "NA",
        },
        "currency": "EGP",
        "integration_id": 4545275,
        "lock_order_when_paid": "false",
    }
    response = requests.post(url=paymob_urls["paymentkey_request"], json=body).json()
    frameid = 834669
    print(response)
    cashier_url = paymob_urls["casher_url"].replace("{{frame_id}}", str(frameid))
    cashier_url = cashier_url.replace("{{token}}", response.get("token"))
    print(cashier_url)
    return cashier_url


paymob_urls = {
    "authentication": "https://accept.paymob.com/api/auth/tokens",
    "paymentkey_request": "https://accept.paymob.com/api/acceptance/payment_keys",
    "casher_url": "https://accept.paymobsolutions.com/api/acceptance/iframes/{{frame_id}}?payment_token={{token}}",
    "get_order_id": "https://accept.paymob.com/api/ecommerce/orders",
}