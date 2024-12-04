import requests

# Get the token
auth_url = "https://qq3-impl-services1.rerre.com/ccx/oauth2/errrerwwww/token"
client_id = "dfgrrthtyhth" 
client_secret = "gergterergdgfg"
data = {"grant_type": "client_credentials"}

token_response = requests.post(auth_url, data=data, auth=(client_id, client_secret))
access_token = token_response.json().get("access_token")
print(access_token)
