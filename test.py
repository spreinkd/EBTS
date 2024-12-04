import requests
from requests.auth import HTTPBasicAuth

# Token endpoint URL
token_url = "https://example.com/oauth/token"

# Client credentials
client_id = "your_client_id"
client_secret = "your_client_secret"

# Headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Payload
payload = {
    "grant_type": "client_credentials",
    "scope": "read write",  # Adjust scope based on API documentation
}

# Send POST request (with Basic Auth if needed)
response = requests.post(token_url, data=payload, headers=headers, auth=HTTPBasicAuth(client_id, client_secret))

if response.status_code == 200:
    access_token = response.json().get("access_token")
    print("Access token:", access_token)
else:
    print("Failed to get access token:")
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
