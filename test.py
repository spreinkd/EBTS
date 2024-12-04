# Step 1: Obtain Access Token
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

headers = {
    "Accept": "application/json",
    "Accept-Language": "en-US",
    "Content-Type": "application/json",
}

response = requests.post(token_url, json=data, headers=headers)

# Check the response status and content
print(response.status_code)
print(response.text)
