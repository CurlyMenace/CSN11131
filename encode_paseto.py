#!/usr/bin/env python3

# CODE TAKEN FROM https://pypi.org/project/paseto/

import paseto
from paseto.keys.asymmetric_key import AsymmetricSecretKey
from paseto.protocols.v4 import ProtocolVersion4
my_key = AsymmetricSecretKey.generate(protocol=ProtocolVersion4)

# create a paseto token that expires in 5 minutes (300 seconds)
token = paseto.create(
    key=my_key,
    purpose='public',
    claims={'my claims': [1, 2, 3]},
    exp_seconds=300
)

parsed = paseto.parse(
    key=my_key,
    purpose='public',
    token=token,
)
print(token)
print(parsed)