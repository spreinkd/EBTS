import requests

# Replace with your details
auth_url = "A"
token_url = "B" 
client_id = "C" 
client_secret = "D"

# Step 1: Obtain Access Token
data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
headers={
    "Accept": "application/json",
    "Accept-Language": "en-US",
    "Content-Type": "application/json",
}
response = requests.post( token_url,data=data,headers=headers)
response

<Response [400]>
