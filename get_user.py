import requests
import json

api_token = "<your api token>"
domain = "<your okta domain>"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"SSWS {api_token}"
}

url = f"https://{domain}/api/v1/users/alex.jones@example.com"

response = requests.get(url=url, headers=headers)
print(response.status_code)
print(response.content)
