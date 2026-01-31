#!/usr/bin/env python3
"""Starlink Account Info Retriever - https://starlink.readme.io/docs/authentication"""

import sys
import os
import argparse
from dotenv import load_dotenv

from src.auth import authenticate, DEFAULT_API_URL
from src.client import StarlinkClient
from src.formatter import format_account_info
from src.mock import MockStarlinkClient, mock_authenticate


def main() -> None:
    # Завантажуємо змінні з файлу .env
    load_dotenv()
    
    # Створюємо парсер для аргументів командного рядка
    parser = argparse.ArgumentParser(
        description="Starlink Account Info Retriever",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --session-key "your_bearer_token"
  %(prog)s --email "client_id" --password "secret"
  %(prog)s --client-id "id" --client-secret "secret"
  %(prog)s --mock --email demo --password demo

Note: --email/--password are aliases for --client-id/--client-secret
        """
    )

    parser.add_argument('--session-key', dest='session_key', help='Bearer token')
    parser.add_argument('--client-id', '--email', dest='client_id', help='Client ID')
    parser.add_argument('--client-secret', '--password', dest='client_secret', help='Client secret')
    parser.add_argument('--api-url', default=DEFAULT_API_URL, help=f'API URL (default: {DEFAULT_API_URL})')
    parser.add_argument('--mock', action='store_true', help='Use mock mode (demo data, no real API)')

    args = parser.parse_args()
    
    if args.mock:
        print("\n\033[1;33m*** RUNNING IN MOCK MODE ***\033[0m\n")

    try:
        session_key = args.session_key or os.getenv('STARLINK_SESSION_KEY')
        client_id = args.client_id or os.getenv('STARLINK_CLIENT_ID')
        client_secret = args.client_secret or os.getenv('STARLINK_CLIENT_SECRET')
        
        if not session_key:
            if not client_id or not client_secret:
                print("Error: Provide --session-key or --client-id/--client-secret", file=sys.stderr)
                print("Or set STARLINK_SESSION_KEY or STARLINK_CLIENT_ID/STARLINK_CLIENT_SECRET in .env", file=sys.stderr)
                sys.exit(1)
            
            print("Authenticating...")
            if args.mock:
                session_key = mock_authenticate(client_id, client_secret, args.api_url)
            else:
                session_key = authenticate(client_id, client_secret, args.api_url)
            print("Authentication successful\n")
        
        if args.mock:
            client = MockStarlinkClient(session_key, args.api_url)
        else:
            client = StarlinkClient(session_key, args.api_url)
        
        account_info = client.get_account_info()
        output = format_account_info(account_info)
        print(output)
        
    except ValueError as e:
        print(f"\nValidation Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
