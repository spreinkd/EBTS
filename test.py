try:
    # Fetch the token
    token_response = requests.post(auth_url, headers=headers, data=data, auth=(client_id, client_secret))
    
    # Check for HTTP errors
    token_response.raise_for_status()  # Raise error for HTTP codes >= 400
    
    # Parse the token
    access_token = token_response.json().get("access_token")
    
    if access_token:
        print("Access Token:", access_token)
    else:
        print("Failed to fetch token. Response:", token_response.json())

except requests.exceptions.RequestException as e:
    print("Error during token request:", str(e))
    # Print the response content for debugging
    print("Response Content:", token_response.text)
