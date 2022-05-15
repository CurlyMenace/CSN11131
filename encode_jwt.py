#!/usr/bin/env python3

# CODE TAKEN FROM https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/

import datetime
import jwt

SECRET_KEY = "CSN11131"

json_data = {
    "sender": "Patryk Ryba",
    "message": "This is a test JWT message",
    "date": str(datetime.datetime.now())
}

encoded_data = jwt.encode(payload=json_data, key=SECRET_KEY, algorithm="HS256")

print(encoded_data)