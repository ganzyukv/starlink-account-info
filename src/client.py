"""Starlink API client."""

import os
from typing import Any, Dict

import requests


BASE_URL = os.getenv("STARLINK_BASE_URL", "https://starlink.com",)
ACCESS_COOKIE_NAME = "Starlink.Com.Access.V1"
DEFAULT_TIMEOUT = 10


class StarlinkClient:
    """Client for interacting with Starlink API"""

    def __init__(
        self,
        token: str,
        base_url: str = BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.cookies.set(ACCESS_COOKIE_NAME, token)

    def get_user_info(self) -> Dict[str, Any]:
        response = self.session.get(
            f"{self.base_url}/api/auth-rp/auth/user",
            timeout=self.timeout,
        )

        self._check_response(response)

        try:
            return response.json()
        except ValueError as exc:
            raise RuntimeError("Server returned non-JSON response.") from exc

    def _check_response(self, response: requests.Response) -> None:
        if response.status_code == 401:
            raise RuntimeError("Token is invalid or expired.")
        if response.status_code == 403:
            raise RuntimeError("Access forbidden.")
        if response.status_code >= 500:
            raise RuntimeError("Starlink server error.")

        response.raise_for_status()
