import requests

# Replace with your details
auth_url = "AUTHORIZATION_ENDPOINT_URL"
token_url = "TOKEN_ENDPOINT_URL"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Step 1: Obtain Access Token
response = requests.post(
    token_url,
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    },
)

if response.status_code == 200:
    token = response.json().get("access_token")
    print(f"Access Token: {token}")
else:
    print(f"Failed to retrieve token: {response.json()}")
    exit()
