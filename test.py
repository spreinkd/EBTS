import requests

# Get the token
auth_url = "https://<your-tenant>.workday.com/oauth2/token"
client_id = "your_client_id"
client_secret = "your_client_secret"
data = {"grant_type": "client_credentials"}

token_response = requests.post(auth_url, data=data, auth=(client_id, client_secret))
access_token = token_response.json().get("access_token")

# Use the token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

api_url = "https://<your-tenant>.workday.com/ccx/api/v1/employees"
response = requests.get(api_url, headers=headers)
print(response.json())
