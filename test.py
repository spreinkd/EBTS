token_url = "https://wd2-impl-services1.workday.com/ccx/oauth2/wintrust3/token" 
# Step 1: Obtain Access Token
data = {
    "client_id": client_id,
    "client_secret": client_secret,
}

headers = {
    "Accept": "application/json",
}

response = requests.post(token_url, json=data, headers=headers)

# Check the response status and content
print(response.status_code)
print(response.text)
