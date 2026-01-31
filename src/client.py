"""Starlink API client."""

import requests
from typing import Dict, Any


DEFAULT_API_URL = "https://starlink.com"


class StarlinkClient:
    """Client for interacting with Starlink API V2."""
    
    def __init__(self, session_key: str, api_url: str = DEFAULT_API_URL):
        if not session_key:
            raise ValueError("Session key is required")
        self.session_key = session_key
        self.api_url = api_url
    
    def get_account_info(self) -> Dict[str, Any]:
        """Retrieve account information from Starlink API."""
        url = f"{self.api_url}/api/public/v2/account"
        
        try:
            response = requests.get(
                url,
                headers={
                    'Authorization': f'Bearer {self.session_key}',
                    'Accept': 'application/json'
                },
                timeout=30
            )
            
            if response.status_code == 401:
                raise Exception("Invalid or expired bearer token")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
