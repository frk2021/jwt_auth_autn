from datetime import datetime, timedelta
from time import time, mktime
import jwt

dt = datetime.now() + timedelta(minutes=19)

headers = {
    "alg": "ES256",
    "kid": "default",
    "typ": "JWT",
}


payload = {
    "exp": 4685989700,
    "foo": "bar",
    "iat": 1532389700,
    "iss": "force0.coralworld.co ",
    "sub": "force0.coralworld.co",
}


with open("ec_private.pem", "rb") as fh:  # Add your file
    signing_key = fh.read()

gen_jwt = jwt.encode(payload, signing_key, algorithm="ES256", headers=headers)

print(f"[JWT] {gen_jwt}")
