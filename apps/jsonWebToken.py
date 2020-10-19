import jwt
import json

private_key = open('/Users/aniruddhanarendraraje/Documents/work/pocs/pythonBasics/apps/private.key', 'r', encoding='utf8')
private_key = private_key.read()

public_key = open('/Users/aniruddhanarendraraje/Documents/work/pocs/pythonBasics/apps/public.key', 'r', encoding='utf8')
public_key = public_key.read()

headers = {
    'iss': 'some iss',
    'aud': 'some aud',
    'sub': 'some sub',
    'exp': 7200,
    'alg': 'RS256'
}

encoded = jwt.encode({'some': 'payload'}, private_key, algorithm='RS256', headers=headers)
encoded = encoded.decode('utf-8')
print(encoded)
print("=================\n")

decoded_payload = jwt.decode(encoded, verify=False)
headers = jwt.get_unverified_header(encoded)
print(decoded_payload)
print(headers)
print("=================\n")

decoded = jwt.decode(encoded, "blabla", algorithms='RS256', verify=True)
print(decoded)