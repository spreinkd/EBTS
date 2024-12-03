import requests

# Function to get an access token
def get_access_token(token_url, client_id, client_secret):
    """
    Retrieves an access token using client credentials.
    """
    try:
        response = requests.post(
            token_url,
            data={
                'grant_type': 'client_credentials',
                'client_id': client_id,
                'client_secret': client_secret,
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving access token: {e}")
        return None

# Function to fetch currency conversion rates
def get_currency_conversion_rates(api_url, access_token):
    """
    Calls the currency conversion rates API with the given access token.
    """
    try:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching currency conversion rates: {e}")
        return None

# Replace these values with your actual endpoint URLs and credentials
TOKEN_URL = "https://example.com/token"  # Token endpoint URL
API_URL = "https://example.com/get_currency_conversion_rates"  # API call URL
CLIENT_ID = "your_client_id"  # Client ID
CLIENT_SECRET = "your_client_secret"  # Client Secret

# Retrieve access token
access_token = get_access_token(TOKEN_URL, CLIENT_ID, CLIENT_SECRET)
if access_token:
    print("Access token retrieved successfully.")
    # Call the API
    conversion_data = get_currency_conversion_rates(API_URL, access_token)
    if conversion_data:
        print("Currency Conversion Rates:", conversion_data)
else:
    print("Failed to retrieve access token.")
