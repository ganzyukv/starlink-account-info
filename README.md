# Starlink Account Info Retriever

Python console додаток для отримання інформації про Starlink акаунт.

## Структура

```
starlink-auth-v2/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── .env.example        # Configuration template
├── src/
│   ├── __init__.py
│   ├── auth.py         # OAuth2 authentication
│   ├── client.py       # API client
│   ├── mock.py         # Mock implementations
│   └── formatter.py    # Console output
└── README.md
```

## Швидкий старт

### Mock mode (для демонстрації)

```bash
python3 main.py --mock --email demo --password demo
```

### З реальним API

```bash
# Встановити залежності
pip3 install -r requirements.txt

# З credentials
python3 main.py --client-id "your_id" --client-secret "your_secret"

# З bearer token
python3 main.py --session-key "your_token"

# Через .env
cp .env.example .env
# Відредагувати .env
python3 main.py
```

## Команди

```bash
# Mock mode (demo дані, без реального API)
python3 main.py --mock

# З session key
python3 main.py --session-key "your_bearer_token"

# З client credentials
python3 main.py --client-id "your_id" --client-secret "your_secret"

# Синоніми
python3 main.py --email "your_id" --password "your_secret"

# Через .env
cp .env.example .env
python3 main.py

# Довідка
python3 main.py --help
```

## Параметри

- `--mock` - Mock mode (демо дані без реального API)
- `--session-key` - Bearer token (пропускає аутентифікацію)
- `--client-id`, `--email` - Service account client ID
- `--client-secret`, `--password` - Service account secret
- `--api-url` - API base URL (default: https://starlink.com)
- `--help` - Довідка

## Залежності

Обов'язкові:
- `requests` - для HTTP запитів
- `python-dotenv` - для .env файлів

```bash
pip3 install -r requirements.txt
```

## API Reference

- Authentication: https://starlink.readme.io/docs/authentication
  - Token: `POST /api/auth/connect/token` 
- Swagger UI: https://starlink.com/api/public/swagger/index.html?urls.primaryName=V2
- Endpoints:
  - Account: `GET /api/public/v2/account`
