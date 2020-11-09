import hashlib
import base64
import json
import requests
from datetime import datetime
import calendar
import string
from random import *
import hmac

idempotency_key = 'aee984befae64'     # Unique for each 'Create Payment' request.

http_method = 'get'                   # Lower case.
base_url = 'https://sandboxapi.rapyd.net'
path = '/v1/data/countries' # Portion after the base URL.

# salt: randomly generated for each request.
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
salt = "".join(choice(allchar)for x in range(randint(min_char, max_char)))

# Current Unix time.
d = datetime.utcnow()
timestamp = calendar.timegm(d.utctimetuple())

access_key = '14294FE3A75919F6F030'   # The access key received from Rapyd.
secret_key = 'b8fc987280c81e3d08fc775ac3b77b589a029e66ee3a6fb0e962ed4d50d65f6f931eb8d80fd049b6'   # Never transmit the secret key by itself.

body = ''                        # JSON body goes here.

to_sign = http_method + path + salt + str(timestamp) + access_key + secret_key + body

h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)

signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

url = base_url + path

headers = {
    'access_key': access_key,
    'signature': signature,
    'salt': salt,
    'timestamp': str(timestamp),
    'Content-Type': "application\/json",
    'idempotency': idempotency_key
}

print(url)

r = requests.get(url, headers = headers)
print(r.text)