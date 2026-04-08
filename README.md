# Med World API

FastAPI project connected to local PostgreSQL, returning users and their accounts.

## Project structure

```text
med_world/
  app/
    api/routes.py
    core/config.py
    db/connection.py
    services/user_service.py
    main.py
  main.py
  .env.example
  requirements.txt
```

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

## Environment

Copy `.env.example` to `.env` and set your real values:

```env
APP_NAME=Med World API
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=bank
DB_USER=postgres
DB_PASSWORD=your_password_here
```

## Run

```bash
python -m uvicorn main:app --reload
```

## Endpoints

- `GET /` -> health message
- `GET /xyz` -> users with nested accounts
