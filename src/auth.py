"""Authentication module for Starlink API."""

import requests

DEFAULT_API_URL = "https://starlink.com"


def authenticate(
    client_id: str,
    client_secret: str,
    api_url: str = DEFAULT_API_URL
) -> str:
    if not client_id or not client_secret:
        raise ValueError("Client ID and secret are required")
    
    token_url = f"{api_url}/api/auth/connect/token"
    
    try:
        response = requests.post(
            token_url,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data={
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'client_credentials'
            },
            timeout=10
        )
        
        response.raise_for_status()
        data = response.json()
        
        access_token = data.get('access_token')
        if not access_token:
            raise ValueError("Access token not received from API")
        
        return access_token
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Authentication failed: {str(e)}")
