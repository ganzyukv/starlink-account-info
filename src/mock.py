"""Mock implementations for testing without real API."""

from typing import Dict, Any


class MockStarlinkClient:
    """Mock client for demonstration without real API calls."""

    def __init__(self, session_key: str, api_url: str = "https://starlink.com"):
        self.session_key = session_key
        self.api_url = api_url

    def get_account_info(self) -> Dict[str, Any]:
        return {
            "accountNumber": "ACC-DEMO-511274-31364-54",
            "regionCode": "US",
            "accountName": "Demo Starlink Account"
        }


def mock_authenticate(
    client_id: str,
    client_secret: str,
    api_url: str = "https://starlink.com"
) -> str:
    if client_id == "demo" and client_secret == "demo":
        return "mock-bearer-token-123"
    raise ValueError("Invalid credentials (use 'demo'/'demo' in mock mode)")
