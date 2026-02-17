# Starlink Account Info

Отримання інформації про акаунт Starlink напряму через cookie токен.

## Опис

Цей інструмент дозволяє отримати дані про ваш акаунт Starlink (ім’я, email, локаль тощо) використовуючи токен `Starlink.Com.Access.V1`, який зберігається у браузері після входу.

## Використання

### 1. Отримайте токен
- Увійдіть у акаунт Starlink у браузері.
- Відкрийте DevTools → Application → Cookies → `Starlink.Com.Access.V1`.
- Скопіюйте значення токена.

### 2. Встановити залежності
```bash
  pip3 install -r requirements.txt
```

### 3. Запуск із токеном напряму
```bash
  python3 main.py --token CfDJ8BrmZteN5jdLoWYoVZAk1aS...
```

### 4. Використання `.env`
- Створіть файл `.env` у корені проєкту: 

```bash
  cp .env.example .env
```
- Відредагувати .env
```env
  STARLINK_ACCESS_V1=ваш_реальний_токен
```

- Запустіть:
```bash
  python3 main.py
```

### 5. Поведінка при відсутності токена
- Якщо токен не передано через `--token` і не знайдено у `.env`, програма видасть помилку:
  ```
  RuntimeError: Token not found: pass it via --token or add STARLINK_ACCESS_V1 to .env
  ```

## Форматований вивід
Дані акаунта виводяться у зручному форматі через модуль `formatter`:

```
======================================================================
STARLINK ACCOUNT INFORMATION
======================================================================

Email: useremail@gmail.com
Email Verified: False
Family Name: {UserFamily}
Given Name: {UserName}
Locale: en-US
Name: {FullUserName}
Subject ID: 3ccbb1cc-9809-46ca-9fe1-0d1dea6bf520
Updated At: 1771319277
Is Support Agent: False
Is Spacex Employee: False
Enabled: False
Can Manage Clients: False
Roles: []
Employee Account Permissions: []
Permissions: []
======================================================================

```

## Структура проєкту
```
.
├── main.py
├── src
│   ├── __init__.py
│   ├── client.py
│   └── formatter.py
├── .env.example
└── README.md
```

## Залежності
- Python 3.9+
- [requests](https://pypi.org/project/requests/)
- python-dotenv [(pypi.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fpypi.org%2Fproject%2Fpython-dotenv%2F")
