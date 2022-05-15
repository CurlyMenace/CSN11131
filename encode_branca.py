#!/usr/bin/env python3

# CODE TAKEN FROM https://pypi.org/project/pybranca/
import json
import secrets
from branca import Branca

key = secrets.token_bytes(32)
branca = Branca(key)

string = json.dumps({
    "user" : "40228769@live.napier.ac.uk",
    "scope" : ["read", "write", "delete"]
})

token = branca.encode(string)
payload = branca.decode(token)

print(token)
print(payload)
          