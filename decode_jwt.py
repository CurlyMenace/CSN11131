#!/usr/bin/env python3

# CODE TAKEN FROM https://pythonsansar.com/creating-simple-json-web-token-jwt-in-python/

import jwt


SECRET_KEY = "CSN11131"

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZW5kZXIiOiJQYXRyeWsgUnliYSIsIm1lc3NhZ2UiOiJUaGlzIGlzIGEgdGVzdCBKV1QgbWVzc2FnZSIsImRhdGUiOiIyMDIyLTA1LTE1IDIzOjAxOjE3LjkzODAxMSJ9.0xMsYk8H1rjwQJc7aOknF7j_HZXRv9hNG77hIUP5TlA"

try:
    decoded_data = jwt.decode(jwt = token, key=SECRET_KEY, algorithms="HS256")
    print(decoded_data)
except Exception as e:
    message = f"Token is invalid --> {e}"
    print({"message": message})