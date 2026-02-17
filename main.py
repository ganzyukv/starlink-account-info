#!/usr/bin/env python3
"""Starlink Account Info"""

import argparse
import os

from dotenv import load_dotenv
from src.client import StarlinkClient
from src.formatter import format_user_info

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Starlink account info fetcher")
    parser.add_argument("--token", type=str, help="Starlink.Com.Access.V1 cookie token")
    args = parser.parse_args()

    token = args.token or os.getenv("STARLINK_ACCESS_V1")

    if not token:
        raise RuntimeError("Token not found: pass it via --token or add STARLINK_ACCESS_V1 to .env")

    client = StarlinkClient(token)

    try:
        user = client.get_user_info()
        print(format_user_info(user))
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
