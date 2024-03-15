import json

import requests


def initiate_session(phone_number, amount):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 2jqJmg3J4BkHysS10yp7ngatGxC8'
    }

    payload = {
        "BusinessShortCode": 174379,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwMzAzMDgyODE5",
        "Timestamp": "20240303082819",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": f"{amount}",
        "PartyA": 254708374149,
        "PartyB": 174379,
        "PhoneNumber": f"254{phone_number}",
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }

    # Convert payload to JSON string
    payload_json = json.dumps(payload)

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
                                headers=headers,
                                data=payload_json)
    print(response.text.encode('utf8'))
