import requests
import json

api_token = "<your api token>"
domain = "<your okta domain>"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"SSWS {api_token}"
}

url = f"https://{domain}/api/v1/users?activate=true"
body = {
    "profile": {
        "firstName": "alex",
        "lastName": "jones",
        "email": "alex.jones@example.com",
        "login": "alex.jones@example.com",
        "mobilePhone": "888-777-1234"
    },
    "credentials": {
        "password": {"value": "Str0ngp@s$word"}
    }
}


response = requests.post(url=url, headers=headers, data=json.dumps(body))
print(response.status_code)
print(response.content)
